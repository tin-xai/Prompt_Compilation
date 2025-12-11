INIT_PROMPT = """Question: Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?
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

"""

SELF_CRITIQUE_PROMPT = """Question: A man is trying to maximize the amount of money he saves each month. In particular, he is trying to decide between two different apartments. The first apartment costs $800 per month in rent and will cost an additional $260 per month in utilities. The second apartment costs $900 per month and will cost an additional $200 per month in utilities. The first apartment is slightly further from the man's work, and the man would have to drive 31 miles per day to get to work. The second apartment is closer, and the man would only have to drive 21 miles to get to work. According to the IRS, each mile a person drives has an average cost of 58 cents. If the man must drive to work 20 days each month, what is the difference between the total monthly costs of these two apartments after factoring in utility and driving-related costs (to the nearest whole dollar)?
Answer: The mileage cost for the first apartment will be 31*20*0.58 = $359.60
This makes the total monthly cost of the first apartment 359.60 + 800 + 260 = $1419.60
Similarly, the mileage cost for the second apartment will be 21*20*0.58 = $243.60
Thus, the total monthly cost of the second apartment is 243.60 + 900 + 200 = 1343.60
Therefore, the difference in total monthly costs is 1419.60 - 1343.60 = $76
The answer is {76}.

Let's check the reasoning step by step:
Step 1: "The mileage cost for the first apartment will be 31*20*0.58 = $359.60" ✓ Correct (31 miles * 20 days * $0.58 = $359.60)
Step 2: "total monthly cost of the first apartment 359.60 + 800 + 260 = $1419.60" ✓ Correct
Step 3: "mileage cost for the second apartment will be 21*20*0.58 = $243.60" ✓ Correct (21 miles * 20 days * $0.58 = $243.60)
Step 4: "total monthly cost of the second apartment is 243.60 + 900 + 200 = 1343.60" ✓ Correct
Step 5: "difference in total monthly costs is 1419.60 - 1343.60 = $76" ✓ Correct
Overall quality: 10/10 (perfect calculation and reasoning)
Should this answer be refined further? No

Question: A curry house sells curries that have varying levels of spice. Recently, a lot of the customers have been ordering very mild curries and the chefs have been having to throw away some wasted ingredients. To reduce cost and food wastage, the curry house starts monitoring how many ingredients are actually being used and changes their spending accordingly. The curry house needs 3 peppers for very spicy curries, 2 peppers for spicy curries, and only 1 pepper for mild curries. After adjusting their purchasing, the curry house now buys the exact amount of peppers they need. Previously, the curry house was buying enough peppers for 30 very spicy curries, 30 spicy curries, and 10 mild curries. They now buy enough peppers for 15 spicy curries and 90 mild curries. They no longer sell very spicy curries. How many fewer peppers does the curry house now buy?
Answer: The curry house previously bought 3 peppers per very spicy curry * 30 very spicy curries = 90 peppers for very spicy curries.
They also bought 2 peppers per spicy curry * 30 spicy curries = 60 peppers for spicy curries.
They also bought 1 pepper per mild curry * 10 mild curries = 10 peppers for mild curries.
So they were previously buying 90 + 60 + 10 = 160 peppers.
They now buy 2 peppers per spicy curry * 15 spicy curries = 30 peppers for spicy curries.
They also now buy 1 pepper per mild curry * 90 mild curries = 90 peppers for mild curries.
So they now buy 30 + 90 = 120 peppers.
This is a difference of 160 peppers bought originally - 120 peppers bought now = 40 peppers.
The answer is {40}.

Let's check the reasoning step by step:
Step 1: "3 peppers per very spicy curry * 30 very spicy curries = 90 peppers" ✓ Correct
Step 2: "2 peppers per spicy curry * 30 spicy curries = 60 peppers" ✓ Correct
Step 3: "1 pepper per mild curry * 10 mild curries = 10 peppers" ✓ Correct
Step 4: "previously buying 90 + 60 + 10 = 160 peppers" ✓ Correct
Step 5: "2 peppers per spicy curry * 15 spicy curries = 30 peppers" ✓ Correct
Step 6: "1 pepper per mild curry * 90 mild curries = 90 peppers" ✓ Correct
Step 7: "now buy 30 + 90 = 120 peppers" ✓ Correct
Step 8: "difference of 160 - 120 = 40 peppers" ✓ Correct
Overall quality: 10/10 (all calculations are correct and well-organized)
Should this answer be refined further? No

"""

REFINE_PROMPT = """Question: At the beginning of the day, Principal Kumar instructed Harold to raise the flag up the flagpole. The flagpole is 60 feet long, and when fully raised, the flag sits on the very top of the flagpole. Later that morning, Vice-principal Zizi instructed Harold to lower the flag to half-mast. So, Harold lowered the flag halfway down the pole. Later, Principal Kumar told Harold to raise the flag to the top of the pole once again, and Harold did just that. At the end of the day, Vice-principal Zizi instructed Harold to completely lower the flag, take it off of the pole, and put it away for the evening. Over the course of the day, how far, in feet, had the flag moved up and down the pole?
Answer: Half of the distance up the flagpole is 60/2 = 30 feet.
Thus, Harold moved the flag 60 up + 30 down + 30 up + 60 down = 180 feet.
The answer is {180}.

Feedback: The calculation appears correct, but the explanation could be clearer about tracking each movement step by step.
Overall quality: 8/10
Should this answer be refined further? Yes

Refined Answer:
Answer: Let's track each movement of the flag:
1. Morning: Harold raises the flag to the top = 60 feet up
2. Later morning: Harold lowers the flag to half-mast (middle of pole) = 30 feet down (from 60 to 30)
3. Later: Harold raises the flag back to the top = 30 feet up (from 30 to 60)
4. End of day: Harold completely lowers the flag = 60 feet down (from 60 to 0)
Total distance: 60 + 30 + 30 + 60 = 180 feet.
The answer is {180}.

Question: Jo-Bob hopped into the hot air balloon, released the anchor rope, and pulled on the lift chain, which ignited the flame and provided the warm air that caused the balloon to rise. When the lift chain was pulled, the balloon would rise at a rate of 50 feet per minute. But when the chain was not being pulled, the balloon would slowly descend at a rate of 10 feet per minute. During his balloon ride, he pulled the chain for 15 minutes, then released the rope for 10 minutes, then pulled the chain for another 15 minutes, and finally released the chain and allowed the balloon to slowly descend back to the earth. During his balloon ride, what was the highest elevation reached by the balloon?
Answer: The first 15-minute chain pull caused the balloon to rise 50*15=750 feet.
Releasing the chain for 10 minutes caused the balloon to descend 10*10=100 feet.
The second 15-minute chain pull caused the balloon to rise another 50*15=750 feet.
Thus, at the end of the second chain pull, when the balloon was at its highest elevation, the balloon had risen to an elevation of 750-100+750=1400 feet above the earth's surface.
The answer is {1400}.

Feedback: The calculations are correct, but it would be clearer to show the cumulative elevation after each phase rather than just the final calculation.
Overall quality: 8/10
Should this answer be refined further? Yes

Refined Answer:
Answer: Let's track the balloon's elevation after each phase:
Phase 1: First chain pull for 15 minutes: 50 feet/minute * 15 minutes = 750 feet
Elevation after phase 1: 750 feet
Phase 2: Release for 10 minutes: 10 feet/minute * 10 minutes = 100 feet descent
Elevation after phase 2: 750 - 100 = 650 feet
Phase 3: Second chain pull for 15 minutes: 50 feet/minute * 15 minutes = 750 feet rise
Elevation after phase 3: 650 + 750 = 1400 feet
This is the highest elevation reached, as the balloon descends after this point.
The answer is {1400}.

"""