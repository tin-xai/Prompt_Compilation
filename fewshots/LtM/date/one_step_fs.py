ONE_STEP_PROMPT = """Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
A: Let's break down this problem:
1. What is today's date?
2. What is the date one week from today?

1. If 2015 is coming in 36 hours, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014.
2. One week from today is 7 days after 12/30/2014, which is 01/06/2015.

The answer is {01/06/2015}.

Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
A: Let's break down this problem:
1. What day of the week was 01/01/2019?
2. What is today's date?

1. The first day of 2019 was Tuesday, so 01/01/2019 was a Tuesday.
2. Today is the first Monday of 2019. The first Monday would be 6 days after Tuesday (the 1st), so today is 01/07/2019.

The answer is {01/07/2019}.
"""