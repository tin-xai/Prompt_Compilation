import re
import sys
sys.path.append("../")
from agents.api_agents import api_agent

def multi_step_ltm(llm_model, question, decompose_examples="", solve_examples="", temperature=1.0):
    """
    Multi-step Least-to-Most prompting (Two-stage)
    Step 1: Decompose the question into sub-questions
    Step 2: Solve each sub-question iteratively
    Step 3: Combine answers for final response
    """
    
    # Step 1: Decompose with few-shot examples
    decompose_prompt = f"""{decompose_examples}

Q: {question}
A: To answer the question "{question}", we need to know:"""

    full_answer = ""
    decomposition = api_agent(llm_model, decompose_prompt, temperature=temperature)
    full_answer += f"Decomposition: {decomposition}\n\n"
    
    if decomposition is None:
        return None
        
    # Extract sub-questions from decomposition
    sub_questions = []
    for line in decomposition.split('\n'):
        # Match patterns like "1.", '"sub-question"', or bullet points
        match = re.search(r'["\']([^"\']+)["\']', line)
        if match:
            sub_questions.append(match.group(1))
        elif re.match(r'^\d+\.', line.strip()):
            sub_question = re.sub(r'^\d+\.\s*', '', line.strip())
            if sub_question:
                sub_questions.append(sub_question.strip('"\''))
    
    if not sub_questions:
        return None
    
    # Step 2: Solve each sub-question iteratively with context
    sub_answers = []
    context = f"{question}\n\n"
    
    for i, sub_q in enumerate(sub_questions):
        # Build context with previous Q&A pairs
        if i > 0:
            context += f"Q: {sub_questions[i-1]}\nA: {sub_answers[i-1]}\n\n"
        
        solve_prompt = f"""{solve_examples}

{context}Q: {sub_q}
A:"""
        
        sub_answer = api_agent(llm_model, solve_prompt, temperature=temperature)
        if sub_answer is None:
            return None
        sub_answers.append(sub_answer)
        full_answer += f"Q: {sub_q}\nA: {sub_answer}\n\n"
    
    # The last answer should contain the final answer
    # Extract answer in curly brackets if present
    return full_answer

def one_step_ltm(llm_model, question, examples="", temperature=1.0):
    """
    One-step Least-to-Most prompting (Merged decomposition + solving)
    Used for GSM8K-style problems where decomposition is straightforward
    """
    # Few-shot examples should show decomposition + solving together
    prompt = f"""{examples}

Q: {question}
A: Let's break down this problem:"""
    
    # Get decomposition + initial solving
    response = api_agent(llm_model, prompt, temperature=temperature)
    # The last answer should contain the final answer
    # Extract answer in curly brackets if present
    return response