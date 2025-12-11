HOT_FS_PROMPT = """Question: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
Reformatted Question: <fact1>2015</fact1> is coming in <fact2>36 hours</fact2>. What is the date <fact3>one week from today</fact3> in MM/DD/YYYY?
Answer: If <fact1>2015</fact1> is coming in <fact2>36 hours</fact2>, then it is coming in 2 days. 2 days before 01/01/2015 is 12/30/2014, so today is 12/30/2014. So <fact3>one week from today</fact3> will be 01/06/2015. The answer is {01/05/2015}.

Question: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
Reformatted Question: The first day of <fact1>2019</fact1> is a <fact2>Tuesday</fact2>, and today is the first <fact3>Monday</fact3> of <fact1>2019</fact1>. What is the date today in MM/DD/YYYY?
Answer: If the <fact2>first day of 2019 was Tuesday</fact2>, then 01/01/2019 was a <fact2>Tuesday</fact2>. Today is the <fact3>first Monday</fact3>, which would be six days later. So today is 01/07/2019. The answer is {01/07/2019}.
"""