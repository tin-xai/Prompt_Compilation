"""
Main script for running LLM inference on datasets and saving results to CSV.
"""
import argparse
import json
import csv
import os
from pathlib import Path
from tqdm import tqdm
from datetime import datetime

# Import prompting techniques
from prompting_techniques.LtM import one_step_ltm, multi_step_ltm

# Import few-shot examples
from fewshots.LtM.p_GSM8K.one_step_fs import GSM8K_ONE_STEP_LTM
from fewshots.LtM.logical_deduction_seven_objects.one_step_fs import LOGICAL_DEDUCTION_ONE_STEP
from fewshots.LtM.logical_deduction_seven_objects.two_step_fs import (
    LOGICAL_DEDUCTION_DECOMPOSE, 
    LOGICAL_DEDUCTION_SOLVE
)
from fewshots.LtM.date.one_step_fs import DATE_UNDERSTANDING_ONE_STEP_LTM

# Import evaluation utilities
from utils.rule_based_eval import extract_answer_from_brackets, load_ground_truth


# Dataset configurations
DATASET_CONFIG = {
    "date": {
        "data_file": "data/date/test.jsonl",
        "fewshot_one_step": DATE_UNDERSTANDING_ONE_STEP_LTM,
        "id_field": "id",
        "question_field": "question",
        "answer_field": "answer",
    },
    "logical_deduction_seven_objects": {
        "data_file": "data/logical_deduction_seven_objects/test.json",
        "fewshot_one_step": LOGICAL_DEDUCTION_ONE_STEP,
        "fewshot_decompose": LOGICAL_DEDUCTION_DECOMPOSE,
        "fewshot_solve": LOGICAL_DEDUCTION_SOLVE,
        "id_field": "id",
        "question_field": "question",
        "answer_field": "answer",
    },
    "p_GSM8K": {
        "data_file": "data/p_GSM8K/r-gsm.jsonl",
        "fewshot_one_step": GSM8K_ONE_STEP_LTM,
        "id_field": "index",
        "question_field": "question",
        "answer_field": "answer",
    },
}

# Available models
AVAILABLE_MODELS = [
    "gemini-2.0-preview",
    
]


def load_dataset(dataset_name: str) -> list:
    """
    Load dataset from file.
    
    Args:
        dataset_name: Name of the dataset
        
    Returns:
        List of data items
    """
    config = DATASET_CONFIG[dataset_name]
    data_file = config["data_file"]
    
    data = []
    
    if data_file.endswith('.json'):
        with open(data_file, 'r') as f:
            data = json.load(f)
    elif data_file.endswith('.jsonl'):
        with open(data_file, 'r') as f:
            for line in f:
                data.append(json.loads(line.strip()))
    
    return data


def parse_ground_truth(answer, dataset_name: str) -> str:
    """
    Parse ground truth answer based on dataset format.
    
    Args:
        answer: Raw answer from dataset
        dataset_name: Name of the dataset
        
    Returns:
        Parsed ground truth string
    """
    if isinstance(answer, (int, float)):
        if float(answer) == int(answer):
            return str(int(answer))
        return str(answer)
    
    answer = str(answer)
    
    # Handle "#### answer" format (date dataset)
    if answer.startswith("####"):
        return answer.replace("####", "").strip()
    
    return answer.strip()


def run_inference(
    dataset_name: str,
    model_name: str,
    prompting_method: str = "one_step",
    temperature: float = 0.7,
    limit: int = None,
    output_dir: str = "results"
):
    """
    Run inference on a dataset and save results to CSV.
    
    Args:
        dataset_name: Name of the dataset to run on
        model_name: Name of the LLM model to use
        prompting_method: "one_step" or "two_step" (for LtM)
        temperature: Temperature for LLM generation
        limit: Optional limit on number of samples to process
        output_dir: Directory to save results
    """
    # Load dataset
    print(f"Loading dataset: {dataset_name}")
    data = load_dataset(dataset_name)
    config = DATASET_CONFIG[dataset_name]
    
    if limit:
        data = data[:limit]
    
    print(f"Loaded {len(data)} samples")
    
    # Get few-shot examples
    fewshot_one_step = config.get("fewshot_one_step", "")
    fewshot_decompose = config.get("fewshot_decompose", "")
    fewshot_solve = config.get("fewshot_solve", "")
    
    # Prepare output
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(
        output_dir, 
        f"{dataset_name}_{model_name}_{prompting_method}_{timestamp}.csv"
    )
    
    # Results storage
    results = []
    
    # Run inference
    print(f"Running inference with model: {model_name}")
    print(f"Prompting method: {prompting_method}")
    print(f"Output file: {output_file}")
    
    for item in tqdm(data, desc="Processing"):
        item_id = item[config["id_field"]]
        question = item[config["question_field"]]
        gt_raw = item[config["answer_field"]]
        gt = parse_ground_truth(gt_raw, dataset_name)
        
        # Run LLM
        try:
            if prompting_method == "one_step":
                response = one_step_ltm(
                    model_name, 
                    question, 
                    examples=fewshot_one_step,
                    temperature=temperature
                )
            elif prompting_method == "two_step":
                response = multi_step_ltm(
                    model_name,
                    question,
                    decompose_examples=fewshot_decompose,
                    solve_examples=fewshot_solve,
                    temperature=temperature
                )
            else:
                raise ValueError(f"Unknown prompting method: {prompting_method}")
        except Exception as e:
            print(f"Error processing item {item_id}: {e}")
            response = None
        
        # Handle None response
        if response is None:
            response = ""
        
        # Store result
        results.append({
            "id": item_id,
            "question": question,
            "answer": response,
            "GT": gt
        })
    
    # Save to CSV
    print(f"Saving results to {output_file}")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "question", "answer", "GT"])
        writer.writeheader()
        writer.writerows(results)
    
    # Calculate and print accuracy
    correct = 0
    extraction_failures = 0
    
    for result in results:
        extracted = extract_answer_from_brackets(result["answer"])
        if extracted is None:
            extraction_failures += 1
        else:
            # Normalize for comparison
            extracted_norm = extracted.strip().upper() if len(extracted) == 1 else extracted.strip()
            gt_norm = result["GT"].strip().upper() if len(result["GT"]) == 1 else result["GT"].strip()
            
            # Try numeric comparison
            try:
                if float(extracted_norm.replace(',', '')) == float(gt_norm.replace(',', '')):
                    correct += 1
                    continue
            except ValueError:
                pass
            
            # String comparison
            if extracted_norm == gt_norm or extracted_norm.lower() == gt_norm.lower():
                correct += 1
    
    total = len(results)
    accuracy = correct / total if total > 0 else 0.0
    
    print(f"\n{'='*50}")
    print(f"Results Summary")
    print(f"{'='*50}")
    print(f"Total samples: {total}")
    print(f"Correct: {correct}")
    print(f"Accuracy: {accuracy:.2%}")
    print(f"Extraction failures: {extraction_failures}")
    print(f"Results saved to: {output_file}")
    
    return results, accuracy


def main():
    parser = argparse.ArgumentParser(
        description="Run LLM inference on datasets and save results to CSV"
    )
    
    parser.add_argument(
        "--dataset",
        type=str,
        required=True,
        choices=list(DATASET_CONFIG.keys()),
        help="Dataset to run inference on"
    )
    
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help=f"LLM model to use. Available: {', '.join(AVAILABLE_MODELS)}"
    )
    
    parser.add_argument(
        "--method",
        type=str,
        default="one_step",
        choices=["one_step", "two_step"],
        help="Prompting method (default: one_step)"
    )
    
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Temperature for LLM generation (default: 0.7)"
    )
    
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of samples to process (default: all)"
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default="results",
        help="Directory to save results (default: results)"
    )
    
    args = parser.parse_args()
    
    # Run inference
    run_inference(
        dataset_name=args.dataset,
        model_name=args.model,
        prompting_method=args.method,
        temperature=args.temperature,
        limit=args.limit,
        output_dir=args.output_dir
    )


if __name__ == "__main__":
    main()

# Run on date dataset with gemini
# python main.py --dataset date --model gemini-1.5-flash

# # Run on GSM8K with llama (limit to 10 samples for testing)
# python main.py --dataset p_GSM8K --model llama_sambanova_70b --limit 10

# # Use two-step prompting method
# python main.py --dataset logical_deduction_seven_objects --model gemini-2.0-flash --method two_step