import re
from agents.api_agents import api_agent

def multi_step_self_refine(
    llm_model, 
    question, 
    p_gen,       # Initial generation prompt (few-shot examples)
    p_fb,        # Feedback prompt (few-shot examples)
    p_refine,    # Refine prompt (few-shot examples)
    temperature=1.0, 
    max_iterations=3
):
    """
    Multi-step Self-Refine prompting following the SELF-REFINE paper.
    
    Args:
        llm_model: The language model to use
        question: The question to answer
        p_gen: Few-shot prompt for initial generation (p_gen in paper)
        p_fb: Few-shot prompt for feedback generation (p_fb in paper)
        p_refine: Few-shot prompt for refinement (p_refine in paper)
        temperature: Sampling temperature
        max_iterations: Maximum number of refinement iterations
    
    Returns:
        full_answer: Complete trace of the refinement process
    """
    
    full_answer = ""
    history = []  # Keep full history as in the paper
    
    # Step 1: Generate initial answer (INIT) using p_gen
    initial_prompt = f"""{p_gen}Question: {question}
Answer:"""

    current_answer = api_agent(llm_model, initial_prompt, temperature=temperature)
    full_answer += f"Initial Answer:\n{current_answer}\n\n"
    
    if current_answer is None:
        return None
    
    # Iterative refinement loop (FEEDBACK + REFINE)
    for iteration in range(max_iterations):
        # Step 2: Self-critique with stopping indicator (FEEDBACK) using p_fb
        critique_prompt = f"""{p_fb}Question: {question}
Answer: {current_answer}

# Let's check the reasoning step by step:"""

        critique = api_agent(llm_model, critique_prompt, temperature=temperature)
        full_answer += f"Critique {iteration + 1}:\n{critique}\n\n"
        
        if critique is None:
            return full_answer
        
        history.append(('answer', current_answer))
        history.append(('critique', critique))
        
        # Check for stopping condition (simplified)
        critique_lower = critique.lower()
        if ("should this answer be refined further? no" in critique_lower or 
            "should this answer be refined further: no" in critique_lower or
            "no further refinement" in critique_lower or
            "quality: 10/10" in critique_lower):
            full_answer += "Stopping: Model indicates no further refinement needed.\n"
            break
        
        # Step 3: Refine based on critique (REFINE) using p_refine
        refine_prompt = f"""{p_refine}Question: {question}
Answer: {current_answer}

Feedback: {critique}

# Improved answer:
Answer:"""

        refined_answer = api_agent(llm_model, refine_prompt, temperature=temperature)
        full_answer += f"Refined Answer {iteration + 1}:\n{refined_answer}\n\n"
        
        if refined_answer is None:
            return full_answer
        
        current_answer = refined_answer
    
    # Extract final answer in required format
    final_prompt = f"""Based on all the refinements, provide your final answer.

Enclose your ultimate answer in curly brackets {{}}.

Final Answer:"""
    
    final_answer = api_agent(llm_model, final_prompt, temperature=temperature)
    full_answer += f"Final Answer:\n{final_answer}\n"
    
    return full_answer