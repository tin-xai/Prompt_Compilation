baseline_fewshot = """Question: Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?
Answer: Sam completes a widget every 10 minutes. 
When Jack helps they finish 2 in 15 minutes. Sam has finished 1 widget and has begun working on another one, and Jack finishes the second one at 15 minutes. So it takes Jack 15 minutes to complete a widget.
Sam worked for 6 hours yesterday, so he was able to complete 6 hours * 60 minutes per hour / 10 minutes per widget = 36 widgets.
Jack worked for 4 hours, so he was able to complete 4 hours * 60 minutes per hour / 15 minutes per widget = 16 widgets.
Sam, Jack, and Tony were able to complete 68 widgets together. So of those, Tony personally completed 68 widgets - 36 widgets - 16 widgets = 16 widgets.
It took Tony 8 hours to complete those 16 widgets, so he takes 8 hours * 60 minutes per hour / 16 widgets = 8*60/16=30 minutes per widget.
The answer is {30}.

Question: For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?
Answer: There are 144/12 = 12 sets of 12 cans that the family collected. So, the family would receive $0.50 x 12 = $6 for the cans. There are 20/5 = 4 sets of 5 kilograms of newspapers that the family collected. So, the family would receive $1.50 x 4 = $6 for the newspapers. Therefore, the family would receive a total of $6 + $6 = $12.
The answer is {12}.

Question: {NEW_QUESTION}
Answer:"""

plan_verification_fewshot = """Question: Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?

Initial Answer: Sam completes a widget every 10 minutes. When Jack helps they finish 2 in 15 minutes. Sam has finished 1 widget and has begun working on another one, and Jack finishes the second one at 15 minutes. So it takes Jack 15 minutes to complete a widget. Sam worked for 6 hours yesterday, so he was able to complete 6 hours * 60 minutes per hour / 10 minutes per widget = 36 widgets. Jack worked for 4 hours, so he was able to complete 4 hours * 60 minutes per hour / 15 minutes per widget = 16 widgets. Sam, Jack, and Tony were able to complete 68 widgets together. So of those, Tony personally completed 68 widgets - 36 widgets - 16 widgets = 16 widgets. It took Tony 8 hours to complete those 16 widgets, so he takes 8 hours * 60 minutes per hour / 16 widgets = 8*60/16=30 minutes per widget. The answer is {30}.

Verification Questions:
1. How many widgets can Sam complete in 6 hours if he completes 1 widget every 10 minutes?
2. How many widgets can Jack complete in 4 hours if he completes 1 widget every 15 minutes?
3. If Sam completed 36 widgets and Jack completed 16 widgets, and the total was 68 widgets, how many widgets did Tony complete?
4. If Tony worked for 8 hours and completed 16 widgets, how many minutes does it take Tony to complete one widget?

Question: For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?

Initial Answer: There are 144/12 = 12 sets of 12 cans that the family collected. So, the family would receive $0.50 x 12 = $6 for the cans. There are 20/5 = 4 sets of 5 kilograms of newspapers that the family collected. So, the family would receive $1.50 x 4 = $6 for the newspapers. Therefore, the family would receive a total of $6 + $6 = $12. The answer is {12}.

Verification Questions:
1. How many sets of 12 cans are in 144 cans?
2. If you get $0.50 for every 12 cans, how much money do you get for 12 sets?
3. How many sets of 5 kilograms are in 20 kilograms of newspapers?
4. If you get $1.50 for every 5 kilograms, how much money do you get for 4 sets?
5. What is $6 plus $6?

Question: A man is trying to maximize the amount of money he saves each month. In particular, he is trying to decide between two different apartments. The first apartment costs $800 per month in rent and will cost an additional $260 per month in utilities. The second apartment costs $900 per month and will cost an additional $200 per month in utilities. The first apartment is slightly further from the man's work, and the man would have to drive 31 miles per day to get to work. The second apartment is closer, and the man would only have to drive 21 miles to get to work. According to the IRS, each mile a person drives has an average cost of 58 cents. If the man must drive to work 20 days each month, what is the difference between the total monthly costs of these two apartments after factoring in utility and driving-related costs (to the nearest whole dollar)?

Initial Answer: The mileage cost for the first apartment will be 31*20*0.58 = $359.60. This makes the total monthly cost of the first apartment 359.60 + 800 + 260 = $1419.60. Similarly, the mileage cost for the second apartment will be 21*20*0.58 = $243.60. Thus, the total monthly cost of the second apartment is 243.60 + 900 + 200 = 1343.60. Therefore, the difference in total monthly costs is 1419.60 - 1343.60 = $76. The answer is {76}.

Verification Questions:
1. What is 31 miles times 20 days times $0.58 per mile?
2. What is $800 plus $260 plus $359.60?
3. What is 21 miles times 20 days times $0.58 per mile?
4. What is $900 plus $200 plus $243.60?
5. What is $1419.60 minus $1343.60?

Question: {NEW_QUESTION}

Initial Answer: {NEW_INITIAL_ANSWER}

Verification Questions:"""

execute_verification_fewshot = """Question: How many widgets can Sam complete in 6 hours if he completes 1 widget every 10 minutes?
Answer: 6 hours = 6 * 60 = 360 minutes. If Sam completes 1 widget every 10 minutes, then in 360 minutes he completes 360 / 10 = 36 widgets.

Question: How many widgets can Jack complete in 4 hours if he completes 1 widget every 15 minutes?
Answer: 4 hours = 4 * 60 = 240 minutes. If Jack completes 1 widget every 15 minutes, then in 240 minutes he completes 240 / 15 = 16 widgets.

Question: If Sam completed 36 widgets and Jack completed 16 widgets, and the total was 68 widgets, how many widgets did Tony complete?
Answer: Tony completed 68 - 36 - 16 = 16 widgets.

Question: If Tony worked for 8 hours and completed 16 widgets, how many minutes does it take Tony to complete one widget?
Answer: 8 hours = 8 * 60 = 480 minutes. 480 minutes / 16 widgets = 30 minutes per widget.

Question: How many sets of 12 cans are in 144 cans?
Answer: 144 / 12 = 12 sets.

Question: If you get $0.50 for every 12 cans, how much money do you get for 12 sets?
Answer: $0.50 * 12 = $6.

Question: What is 31 miles times 20 days times $0.58 per mile?
Answer: 31 * 20 * 0.58 = 620 * 0.58 = $359.60.

Question: What is $800 plus $260 plus $359.60?
Answer: 800 + 260 + 359.60 = $1419.60.

Question: {NEW_VERIFICATION_QUESTION}
Answer:"""

crosscheck_fewshot = """Original Answer: Sam completes a widget every 10 minutes. When Jack helps they finish 2 in 15 minutes. Sam has finished 1 widget and has begun working on another one, and Jack finishes the second one at 15 minutes. So it takes Jack 15 minutes to complete a widget. Sam worked for 6 hours yesterday, so he was able to complete 6 hours * 60 minutes per hour / 10 minutes per widget = 36 widgets. Jack worked for 4 hours, so he was able to complete 4 hours * 60 minutes per hour / 15 minutes per widget = 16 widgets. Sam, Jack, and Tony were able to complete 68 widgets together. So of those, Tony personally completed 68 widgets - 36 widgets - 16 widgets = 16 widgets. It took Tony 8 hours to complete those 16 widgets, so he takes 8 hours * 60 minutes per hour / 16 widgets = 8*60/16=30 minutes per widget. The answer is {30}.

Verification Question: How many widgets can Sam complete in 6 hours if he completes 1 widget every 10 minutes?
Verification Answer: 6 hours = 6 * 60 = 360 minutes. If Sam completes 1 widget every 10 minutes, then in 360 minutes he completes 360 / 10 = 36 widgets.

Analysis: Consistent. The original answer states Sam completed 36 widgets in 6 hours, and the verification confirms this calculation is correct.

Original Answer: Sam completes a widget every 10 minutes. When Jack helps they finish 2 in 15 minutes. Sam has finished 1 widget and has begun working on another one, and Jack finishes the second one at 15 minutes. So it takes Jack 15 minutes to complete a widget. Sam worked for 6 hours yesterday, so he was able to complete 6 hours * 60 minutes per hour / 10 minutes per widget = 36 widgets. Jack worked for 4 hours, so he was able to complete 4 hours * 60 minutes per hour / 15 minutes per widget = 16 widgets. Sam, Jack, and Tony were able to complete 68 widgets together. So of those, Tony personally completed 68 widgets - 36 widgets - 16 widgets = 16 widgets. It took Tony 8 hours to complete those 16 widgets, so he takes 8 hours * 60 minutes per hour / 16 widgets = 8*60/16=30 minutes per widget. The answer is {30}.

Verification Question: If Tony worked for 8 hours and completed 16 widgets, how many minutes does it take Tony to complete one widget?
Verification Answer: 8 hours = 8 * 60 = 480 minutes. 480 minutes / 16 widgets = 30 minutes per widget.

Analysis: Consistent. The original answer calculated Tony takes 30 minutes per widget, and the verification confirms this is correct: 480 / 16 = 30.

Original Answer: There are 144/12 = 12 sets of 12 cans that the family collected. So, the family would receive $0.50 x 12 = $6 for the cans. There are 20/5 = 4 sets of 5 kilograms of newspapers that the family collected. So, the family would receive $1.50 x 4 = $6 for the newspapers. Therefore, the family would receive a total of $6 + $6 = $12. The answer is {12}.

Verification Question: What is $6 plus $6?
Verification Answer: $6 + $6 = $12.

Analysis: Consistent. The original answer states the total is $12, and the verification confirms that $6 + $6 = $12.

Original Answer: {NEW_ORIGINAL_ANSWER}

Verification Question: {NEW_VERIFICATION_QUESTION}
Verification Answer: {NEW_VERIFICATION_ANSWER}

Analysis:"""

final_revision_fewshot = """Original Question: Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?

Initial Answer: Sam completes a widget every 10 minutes. When Jack helps they finish 2 in 15 minutes. Sam has finished 1 widget and has begun working on another one, and Jack finishes the second one at 15 minutes. So it takes Jack 15 minutes to complete a widget. Sam worked for 6 hours yesterday, so he was able to complete 6 hours * 60 minutes per hour / 10 minutes per widget = 36 widgets. Jack worked for 4 hours, so he was able to complete 4 hours * 60 minutes per hour / 15 minutes per widget = 16 widgets. Sam, Jack, and Tony were able to complete 68 widgets together. So of those, Tony personally completed 68 widgets - 36 widgets - 16 widgets = 16 widgets. It took Tony 8 hours to complete those 16 widgets, so he takes 8 hours * 60 minutes per hour / 16 widgets = 8*60/16=30 minutes per widget. The answer is {30}.

Verification Results:
1. Q: How many widgets can Sam complete in 6 hours if he completes 1 widget every 10 minutes?
   A: 36 widgets
   Check: Consistent
2. Q: How many widgets can Jack complete in 4 hours if he completes 1 widget every 15 minutes?
   A: 16 widgets
   Check: Consistent
3. Q: If Sam completed 36 widgets and Jack completed 16 widgets, and the total was 68 widgets, how many widgets did Tony complete?
   A: 16 widgets
   Check: Consistent
4. Q: If Tony worked for 8 hours and completed 16 widgets, how many minutes does it take Tony to complete one widget?
   A: 30 minutes per widget
   Check: Consistent

Revised Final Answer: Sam completes a widget every 10 minutes. When Jack helps they finish 2 in 15 minutes, so it takes Jack 15 minutes to complete a widget. Sam worked for 6 hours, completing 36 widgets. Jack worked for 4 hours, completing 16 widgets. Together they completed 68 widgets, so Tony completed 68 - 36 - 16 = 16 widgets. Tony worked for 8 hours (480 minutes) to complete 16 widgets, so he takes 480/16 = 30 minutes per widget. The answer is {30}.

---

Original Question: For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?

Initial Answer: There are 144/12 = 12 sets of 12 cans that the family collected. So, the family would receive $0.50 x 12 = $6 for the cans. There are 20/5 = 4 sets of 5 kilograms of newspapers that the family collected. So, the family would receive $1.50 x 4 = $6 for the newspapers. Therefore, the family would receive a total of $6 + $6 = $12. The answer is {12}.

Verification Results:
1. Q: How many sets of 12 cans are in 144 cans?
   A: 12 sets
   Check: Consistent
2. Q: If you get $0.50 for every 12 cans, how much money do you get for 12 sets?
   A: $6
   Check: Consistent
3. Q: How many sets of 5 kilograms are in 20 kilograms of newspapers?
   A: 4 sets
   Check: Consistent
4. Q: If you get $1.50 for every 5 kilograms, how much money do you get for 4 sets?
   A: $6
   Check: Consistent
5. Q: What is $6 plus $6?
   A: $12
   Check: Consistent

Revised Final Answer: The family collected 144 cans, which is 144/12 = 12 sets of 12 cans. At $0.50 per set, they receive $0.50 x 12 = $6 for cans. The family collected 20 kilograms of newspapers, which is 20/5 = 4 sets of 5 kilograms. At $1.50 per set, they receive $1.50 x 4 = $6 for newspapers. The total is $6 + $6 = $12. The answer is {12}.

---

Original Question: {NEW_QUESTION}

Initial Answer: {NEW_INITIAL_ANSWER}

Verification Results:
{NEW_VERIFICATION_RESULTS}

Revised Final Answer:"""