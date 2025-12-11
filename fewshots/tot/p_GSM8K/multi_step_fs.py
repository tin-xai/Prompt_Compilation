# Standard CoT Prompt (Used for final path generation or baseline)
gsm8k_cot = """Answer the following math problem.

Question: Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?
Answer: Sam completes a widget every 10 minutes. When Jack helps they finish 2 in 15 minutes. Sam has finished 1 widget and has begun working on another one, and Jack finishes the second one at 15 minutes. So it takes Jack 15 minutes to complete a widget. Sam worked for 6 hours yesterday, so he was able to complete 6 hours * 60 minutes per hour / 10 minutes per widget = 36 widgets. Jack worked for 4 hours, so he was able to complete 4 hours * 60 minutes per hour / 15 minutes per widget = 16 widgets. Sam, Jack, and Tony were able to complete 68 widgets together. So of those, Tony personally completed 68 widgets - 36 widgets - 16 widgets = 16 widgets. It took Tony 8 hours to complete those 16 widgets, so he takes 8 hours * 60 minutes per hour / 16 widgets = 8*60/16=30 minutes per widget. The answer is {30}.

Question: For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?
Answer: There are 144/12 = 12 sets of 12 cans that the family collected. So, the family would receive $0.50 x 12 = $6 for the cans. There are 20/5 = 4 sets of 5 kilograms of newspapers that the family collected. So, the family would receive $1.50 x 4 = $6 for the newspapers. Therefore, the family would receive a total of $6 + $6 = $12. The answer is {12}.

Question: {input}
Answer:"""

# Propose Prompt (Used to generate candidate next steps)
gsm8k_propose = """Input: Sam works at the Widget Factory... (Sam: 1/10min. Jack+Sam: 2/15min. Tony: New. Sam works 6h, Jack 4h, Tony 8h. Total: 68. Find Tony's rate.)
Possible next steps:
Approach 1: Calculate Sam's individual production first. He works 6 hours at 10 mins/widget.
Approach 2: Determine Jack's production rate. If Sam+Jack = 2 in 15 mins, deduce Jack's speed.
Approach 3: Convert all time units to minutes (6h -> 360m, 4h -> 240m, 8h -> 480m) to standardize calculations.

Input: For every 12 cans you recycle, you receive $0.50, and for every 5 kilograms of newspapers, you receive $1.50. If your family collected 144 cans and 20 kilograms of newspapers, how much money would you receive?
Possible next steps:
Approach 1: Calculate the revenue from cans first. Find how many sets of 12 are in 144.
Approach 2: Calculate the revenue from newspapers first. Find how many sets of 5kg are in 20kg.
Approach 3: Set up an equation for Total Money = (Cans / 12 * 0.50) + (News / 5 * 1.50).

Input: {input}
Possible next steps:"""

# Value Prompt (Used to evaluate if a step is correct)
gsm8k_value = """Evaluate if the calculation step is correct (sure/likely/impossible)

Question: Sam works at the Widget Factory... (Sam: 1/10min. Jack+Sam: 2/15min. Tony: New. Sam works 6h, Jack 4h, Tony 8h. Total: 68. Find Tony's rate.)
Step: Sam works 6 hours. 6 hours = 360 minutes. 360 / 10 = 36 widgets.
Judge: sure

Question: Sam works at the Widget Factory...
Step: Jack worked 4 hours. 4 hours = 240 minutes. Since they make 2 widgets in 15 mins, Jack makes 240 / 15 * 2 = 32 widgets.
Judge: impossible (This ignores that the 2/15 rate includes Sam. Jack is slower individually).

Question: For every 12 cans you recycle, you receive $0.50... 144 cans, 20kg news.
Step: Cans revenue: 144 / 12 = 12 sets. 12 * $0.50 = $6.00.
Judge: sure

Question: For every 12 cans you recycle, you receive $0.50... 144 cans, 20kg news.
Step: Newspaper revenue: 20kg * $1.50 = $30.00.
Judge: impossible (Price is per 5kg, not per 1kg. Must divide 20 by 5 first).

Question: {input}
Step: {step}
Judge:"""