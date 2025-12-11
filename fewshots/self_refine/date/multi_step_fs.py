# Generate initial answer to date reasoning problems

INIT_PROMPT = """Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
Answer: If 2015 is coming in 36 hours, then it is coming in 2 days.
2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014.
So one week from today will be 01/06/2015.
The answer is {01/06/2015}.

Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
Answer: If the first day of 2019 was Tuesday, then 01/01/2019 was a Tuesday.
Today is the first monday, would be six days later.
So today is 01/07/2019.
The answer is {01/07/2019}.

"""

# Critically evaluate the reasoning for date calculation problems
SELF_CRITIQUE_PROMPT = """
Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
Answer: If 2015 is coming in 36 hours, then it is coming in 2 days.
2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014.
So one week from today will be 01/06/2015.
The answer is {01/06/2015}.

Let's check the reasoning step by step:
Step 1: "2015 is coming in 36 hours" → "coming in 2 days" ✓ Correct (36 hours = 1.5 days ≈ 2 days)
Step 2: "2 days before 01/01/2015 is 12/30/2014" ✓ Correct
Step 3: "one week from today will be 01/06/2015" ✗ ERROR!
12/30/2014 + 7 days = 01/06/2015, but this crosses into the new year.
Let me verify: 12/30 + 1 day = 12/31, 12/31 + 1 day = 01/01, 01/01 + 5 days = 01/06
Actually, the calculation is correct! No errors found.

Question: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?
Answer: One day after 06/01/1943 is 06/02/1943, so today is 06/02/1943.
10 days before today is 05/23/1943.
The answer is {05/23/1943}.

Let's check the reasoning step by step:
Step 1: "One day after 06/01/1943 is 06/02/1943" ✓ Correct
Step 2: "10 days before today is 05/23/1943" ✗ ERROR!
06/02 - 10 days: Going back 10 days from June 2nd.
06/02 - 2 days = 05/31, then 05/31 - 8 days = 05/23
Wait, let me recalculate: 06/02 - 10 = May (31 days), so 06/02 - 10 = 05/(02+31-10) = 05/23 ✓ Actually correct!
The reasoning is correct.

"""

# Improve the answer based on identified issues
REFINE_PROMPT = """
Question: Jane was born on the last day of February in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
Answer: The last day of February is the 28th, so Jane was born on 02/28/2001.
Today is her 16-year old birthday, so today is 02/28/2017.
So yesterday was 02/27/2017.
The answer is {02/27/2017}.

Feedback: The reasoning is correct, though could mention leap year consideration for February.

Refined Answer: The last day of February depends on whether it's a leap year. 
2001 was not a leap year, so February had 28 days, making the last day 02/28/2001.
Jane was born on 02/28/2001.
Today is her 16-year-old birthday, which is 16 years later: 2001 + 16 = 2017.
So today is 02/28/2017.
Yesterday was one day before today, which is 02/27/2017.
The answer is {02/27/2017}.

Question: Yesterday was April 30, 2021. What is the date tomorrow in MM/DD/YYYY?
Answer: Yesterday was 04/30/2021.
Tomorrow is two days after yesterday, so tomorrow is 05/02/2021.
The answer is {05/02/2021}.

Feedback: The calculation "Tomorrow is two days after yesterday" is correct, but the reasoning could be clearer by explicitly stating what today is.

Refined Answer: Yesterday was 04/30/2021.
Today is one day after yesterday, so today is 05/01/2021.
Tomorrow is one day after today, so tomorrow is 05/02/2021.
The answer is {05/02/2021}.

"""