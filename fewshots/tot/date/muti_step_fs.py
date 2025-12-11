# 2-shot
date_cot = '''Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
A: If 2015 is coming in 36 hours, then it is 36 hours before Jan 1, 2015. 36 hours is 1.5 days. 1.5 days before Jan 1 is Dec 30, 2014. One week from Dec 30 is Jan 6, 2015. Answer: {01/06/2015}

Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
A: If the first day of 2019 was Tuesday, Jan 1, then the first Monday would be 6 days later. Jan 1 + 6 days = Jan 7. Answer: {01/07/2019}


Q: {input}
A:
'''

# 1-shot
date_propose = '''Input: Today is the last day of the first quarter of 2013. What is the date 24 hours later in MM/DD/YYYY?
Possible next steps:
Thought 1: Identify the last day of the first quarter (Jan, Feb, Mar). It is March 31.
Thought 2: Determine the number of days in the first quarter of 2013 (non-leap year).
Thought 3: Calculate the date 24 hours (1 day) after the current date.

Input: {input}
Possible next steps:
'''

# 2-shot
date_value = '''Evaluate if the date calculation step is valid (sure/impossible)

Q: Today is the last day of Feb 2015.
Step: Today is Feb 29, 2015.
Judge: impossible (2015 is not a leap year)

Q: Today is Aug 31. What is tomorrow?
Step: Tomorrow is Sep 1.
Judge: sure

Q: {input}
Step: {step}
Judge:'''