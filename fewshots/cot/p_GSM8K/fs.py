FS_PROMPT = """Question: Sam works at the Widget Factory, assembling Widgets. He can assemble 1 widget every 10 minutes. Jack from the loading dock can help assemble widgets when he doesn't have anything else to do. When he helps, they put together 2 complete widgets every 15 minutes. Recently the factory hired Tony to help assemble widgets. Being new to the job, he doesn't work as fast as Sam or Jack. Yesterday Sam worked for 6 hours before he had to leave work early for a dentist appointment. Jack was able to help out for 4 hours before he had to go back to the loading dock to unload a new shipment of widget materials. Tony worked the entire 8-hour shift. At the end of the day, they had completed 68 widgets. How long does it take Tony to assemble a Widget, in minutes?
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