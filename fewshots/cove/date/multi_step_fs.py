baseline_fewshot = """Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
Answer: If 2015 is coming in 36 hours, then it is coming in 2 days.
2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014.
So one week from today will be 01/06/2015.
The answer is {01/05/2015}.

Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
Answer: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday.
Today is the first monday, would be six days later.
So today is 01/07/2019.
The answer is {01/07/2019}.

Question: {NEW_QUESTION}
Answer:"""

plan_verification_fewshot = """Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

Initial Answer: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/06/2015. The answer is {01/05/2015}.

Verification Questions:
1. If 2015 is coming in 36 hours, what is today's date?
2. What date is 7 days after 12/30/2014?
3. Is 01/05/2015 the same as 01/06/2015?

Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

Initial Answer: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019. The answer is {01/07/2019}.

Verification Questions:
1. If January 1st, 2019 is a Tuesday, what day of the week is January 7th, 2019?
2. How many days after Tuesday is the first Monday?
3. What is the date of the first Monday after January 1st, 2019?

Question: {NEW_QUESTION}

Initial Answer: {NEW_INITIAL_ANSWER}

Verification Questions:"""

execute_verification_fewshot = """Question: If 2015 is coming in 36 hours, what is today's date?
Answer: 36 hours is 1.5 days. 1.5 days before 01/01/2015 is 12/30/2014 at noon. So today is 12/30/2014.

Question: If January 1st, 2019 is a Tuesday, what day of the week is January 7th, 2019?
Answer: January 7th is 6 days after January 1st. Tuesday + 6 days = Monday. So January 7th, 2019 is a Monday.

Question: How many days after Tuesday is the first Monday?
Answer: The days after Tuesday are: Wednesday (1), Thursday (2), Friday (3), Saturday (4), Sunday (5), Monday (6). So the first Monday is 6 days after Tuesday.

Question: {NEW_VERIFICATION_QUESTION}
Answer:"""

crosscheck_fewshot = """Original Answer: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/06/2015. The answer is {01/05/2015}.

Verification Question: What date is 7 days after 12/30/2014?
Verification Answer: 7 days after 12/30/2014 is 01/06/2015.

Analysis: The original answer states "one week from today will be 01/06/2015" but then gives the final answer as {01/05/2015}. The verification confirms that 7 days after 12/30/2014 is 01/06/2015. This is an inconsistency - the final answer should be 01/06/2015, not 01/05/2015.

Original Answer: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019. The answer is {01/07/2019}.

Verification Question: How many days after Tuesday is the first Monday?
Verification Answer: The first Monday is 6 days after Tuesday.

Analysis: Consistent. The original answer correctly identifies that the first Monday is 6 days after Tuesday (01/01/2019), which would be 01/07/2019.

Original Answer: {NEW_ORIGINAL_ANSWER}

Verification Question: {NEW_VERIFICATION_QUESTION}
Verification Answer: {NEW_VERIFICATION_ANSWER}

Analysis:"""

final_revision_fewshot = """Original Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?

Initial Answer: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/06/2015. The answer is {01/05/2015}.

Verification Results:
1. Q: If 2015 is coming in 36 hours, what is today's date?
   A: Today is 12/30/2014.
   Check: Consistent
2. Q: What date is 7 days after 12/30/2014?
   A: 7 days after 12/30/2014 is 01/06/2015.
   Check: Inconsistency - original answer says 01/06/2015 in reasoning but final answer is {01/05/2015}

Revised Final Answer: If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So one week from today will be 01/06/2015. The answer is {01/06/2015}.

Original Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?

Initial Answer: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first monday, would be six days later. So today is 01/07/2019. The answer is {01/07/2019}.

Verification Results:
1. Q: If January 1st, 2019 is a Tuesday, what day of the week is January 7th, 2019?
   A: January 7th, 2019 is a Monday.
   Check: Consistent
2. Q: How many days after Tuesday is the first Monday?
   A: 6 days after Tuesday.
   Check: Consistent

Revised Final Answer: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday. Today is the first Monday, which is 6 days later. So today is 01/07/2019. The answer is {01/07/2019}.

---

Original Question: {NEW_QUESTION}

Initial Answer: {NEW_INITIAL_ANSWER}

Verification Results:
{NEW_VERIFICATION_RESULTS}

Revised Final Answer:"""