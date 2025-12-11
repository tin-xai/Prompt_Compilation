import re
from agents.api_agents import api_agent

import re
# from api_utils import api_agent  <-- Assuming this is where your agent lives

def adaptive_tree_of_thoughts(question, dataset_type, llm_model, fs_prompts, temperature=1.0):
    """
    Adapts ToT depth/breadth based on dataset characteristics.
    
    Args:
        question (str): The input problem.
        dataset_type (str): "date_understanding", "p_GSM8K", or "logical_deduction_seven_objects".
        llm_model (str): The model name (e.g. "gpt-4").
        fs_prompts (dict): Dictionary containing the few-shot strings. 
                           Expected keys: 'cot', 'propose', 'value'.
        temperature (float): Generation temperature.
    """
    
    # 1. Configure Search Parameters based on dataset
    if dataset_type == "date_understanding":
        max_depth = 1
        beam_width = 2
        needs_evaluation = False
        
    elif dataset_type == "p_GSM8K":
        max_depth = 2
        beam_width = 3
        needs_evaluation = True
        
    elif dataset_type == "logical_deduction_seven_objects":
        max_depth = 4
        beam_width = 3
        needs_evaluation = True
    else:
        # Default configuration
        max_depth = 3
        beam_width = 3
        needs_evaluation = True
    
    full_answer = ""
    states = [{"thoughts": [], "text": question}]
    
    # 2. Main Search Loop (BFS)
    for depth in range(max_depth):
        full_answer += f"\n=== Depth {depth} ===\n"
        new_states = []
        
        for state in states:
            current_context = state["text"]
            reasoning_history = "\n".join(state["thoughts"])
            
            # --- GENERATION PHASE ---
            # Format the 'propose' prompt based on dataset requirements
            if dataset_type == "logical_deduction_seven_objects":
                # Logic prompts require 'current_state' param
                current_ordering = reasoning_history if reasoning_history else "None"
                generate_prompt = fs_prompts['propose'].format(
                    input=current_context, 
                    current_state=current_ordering
                )
            elif dataset_type == "p_GSM8K":
                # GSM8K includes history in the input field if it exists
                combined_input = current_context
                if reasoning_history:
                    combined_input += f"\nPrevious steps: {reasoning_history}"
                generate_prompt = fs_prompts['propose'].format(input=combined_input)
            else:
                # Standard (Date/Default)
                generate_prompt = fs_prompts['propose'].format(input=current_context)

            # Call API
            thoughts_response = api_agent(llm_model, generate_prompt, temperature=temperature)
            if not thoughts_response:
                continue
            
            # Extract thoughts using Regex or String processing
            thoughts = []
            if dataset_type == "date_understanding":
                # Date usually returns a single direct line
                thoughts = [thoughts_response.strip()]
            else:
                # Math/Logic uses "Approach X:" or "Deduction X:" format
                for line in thoughts_response.split('\n'):
                    match = re.match(r'^(?:Approach|Deduction|Thought)\s*\d+[:\.]\s*(.+)', line.strip())
                    if match:
                        thoughts.append(match.group(1))
            
            # --- EVALUATION PHASE ---
            for thought in thoughts:
                if needs_evaluation:
                    eval_clean = "uncertain" # Default fallback
                    
                    if dataset_type in ["p_GSM8K", "logical_deduction_seven_objects"]:
                        eval_prompt = fs_prompts['value'].format(
                            input=state["text"], 
                            step=thought
                        )
                        evaluation = api_agent(llm_model, eval_prompt, temperature=0)
                        if evaluation:
                            eval_clean = evaluation.strip().lower()
                    
                    full_answer += f"Thought: {thought}\nEval: {eval_clean}\n"
                    
                    # Filtering Logic: Keep if correct/valid/sure/uncertain
                    if any(x in eval_clean for x in ["correct", "valid", "sure", "likely"]):
                        new_state = {
                            "thoughts": state["thoughts"] + [thought],
                            "text": state["text"],
                            "eval": eval_clean
                        }
                        new_states.append(new_state)
                else:
                    # No evaluation needed (e.g. Date Understanding)
                    new_state = {
                        "thoughts": state["thoughts"] + [thought],
                        "text": state["text"]
                    }
                    new_states.append(new_state)
        
        if not new_states:
            break
        
        # Prune (Beam Search)
        if needs_evaluation:
            # Sort by confidence (prioritizing explicit 'sure'/'correct' over 'likely')
            new_states.sort(key=lambda s: 0 if "sure" in s.get("eval", "") or "correct" in s.get("eval", "") else 1)
        
        states = new_states[:beam_width]
        full_answer += f"Keeping {len(states)} states for next depth.\n"
    
    # --- SOLVE PHASE (Final Answer) ---
    final_answers = []
    for state in states:
        reasoning_str = "\n".join(state['thoughts'])
        
        # Prepare context for the final Chain-of-Thought prompt
        if dataset_type == "date_understanding":
            # Date usually just wants the input
            trace_input = state['text'] 
        else:
            # Others benefit from seeing the trace
            trace_input = f"{question}\nTrace:\n{reasoning_str}"

        solve_prompt = fs_prompts['cot'].format(input=trace_input)
        
        answer = api_agent(llm_model, solve_prompt, temperature=temperature)
        if answer:
            final_answers.append(answer)
            full_answer += f"\nPath answer: {answer}\n"
    
    if not final_answers:
        return None
    
    # Vote (Self-Consistency) if we have multiple answers
    if len(final_answers) > 1:
        # Simple majority voting or LLM-based voting could go here.
        # Using LLM-based voting as per original design:
        candidates = chr(10).join([f"{i+1}. {ans}" for i, ans in enumerate(final_answers)])
        vote_prompt = f"""{question}\n\nCandidate answers:\n{candidates}\n\nWhich answer is most accurate? Respond with just the number."""
        
        vote = api_agent(llm_model, vote_prompt, temperature=0)
        full_answer += f"\nVote Result: {vote}\n"
    
    return full_answer

# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    # Mocking the imports from your external files
    # from gsm8k.fs import cot_prompt, propose_prompt, value_prompt
    
    # Create the dictionary as it would appear after importing
    my_gsm8k_prompts = {
        "cot": """Answer the following math problem.\nQ: {input}\nAnswer:""",
        "propose": """Input: {input}\nPossible next steps:\n""",
        "value": """Evaluate if correct (sure/impossible)\nQ: {input}\nStep: {step}\nJudge:"""
    }

    q = "Sam works at the Widget Factory... (etc)"
    
    # Pass the dictionary into the function
    result = adaptive_tree_of_thoughts(
        question=q,
        dataset_type="p_GSM8K", 
        llm_model="gpt-4", 
        fs_prompts=my_gsm8k_prompts
    )
    
    print(result)