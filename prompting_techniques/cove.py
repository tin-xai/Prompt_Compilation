import re
from agents.api_agents import api_agent

def chain_of_verification_with_fewshot(question, llm_model, baseline_fewshot, plan_verification_fewshot, execute_verification_fewshot, crosscheck_fewshot, final_revision_fewshot, temperature=0.7):
    full_answer = ""
    
    # Step 1: Generate initial answer with few-shot
    initial_prompt = baseline_fewshot.replace("{NEW_QUESTION}", question)
    initial_answer = api_agent(llm_model, initial_prompt, temperature=temperature)
    full_answer += f"Initial Answer: {initial_answer}\n\n"
    
    # Step 2: Plan verification questions with few-shot
    verification_prompt = plan_verification_fewshot.replace("{NEW_QUESTION}", question).replace("{NEW_INITIAL_ANSWER}", initial_answer)
    verification_questions_response = api_agent(llm_model, verification_prompt, temperature=temperature)
    full_answer += f"Verification Questions:\n{verification_questions_response}\n\n"
    
    # Extract questions
    verification_questions = []
    for line in verification_questions_response.split('\n'):
        if re.match(r'^\d+\.', line.strip()):
            question_text = re.sub(r'^\d+\.\s*', '', line.strip())
            if question_text:
                verification_questions.append(question_text)
    
    # Step 3: Answer verification questions independently with few-shot
    verification_answers = []
    for verif_q in verification_questions:
        verif_prompt = execute_verification_fewshot.replace("{NEW_VERIFICATION_QUESTION}", verif_q)
        verif_answer = api_agent(llm_model, verif_prompt, temperature=temperature)
        verification_answers.append(verif_answer)
        full_answer += f"Q: {verif_q}\nA: {verif_answer}\n\n"
    
    # Step 3b: Cross-check with few-shot
    inconsistencies = []
    for q, a in zip(verification_questions, verification_answers):
        crosscheck_prompt = crosscheck_fewshot.replace("{NEW_ORIGINAL_ANSWER}", initial_answer).replace("{NEW_VERIFICATION_QUESTION}", q).replace("{NEW_VERIFICATION_ANSWER}", a)
        crosscheck = api_agent(llm_model, crosscheck_prompt, temperature=temperature)
        inconsistencies.append(crosscheck)
        full_answer += f"Cross-check: {crosscheck}\n\n"
    
    # Step 4: Final revision with few-shot
    verification_results_text = "\n".join([f"{i+1}. Q: {q}\n   A: {a}\n   Check: {c}" 
                                           for i, (q, a, c) in enumerate(zip(verification_questions, verification_answers, inconsistencies))])
    
    revision_prompt = final_revision_fewshot.replace("{NEW_QUESTION}", question).replace("{NEW_INITIAL_ANSWER}", initial_answer).replace("{NEW_VERIFICATION_RESULTS}", verification_results_text)
    
    final_answer = api_agent(llm_model, revision_prompt, temperature=temperature)
    full_answer += f"Revised Final Answer: {final_answer}\n"
    
    return full_answer