from fewshots.self_refine.date.multi_step_fs import REFINE_PROMPT


INIT_PROMPT = """Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were seven golfers: Ana, Eve, Ada, Dan, Rob, Amy, and Joe. Dan finished third. Ana finished above Ada. Amy finished last. Dan finished below Rob. Eve finished below Ada. Rob finished below Joe. Options: (A) Ana finished third (B) Eve finished third (C) Ada finished third (D) Dan finished third (E) Rob finished third (F) Amy finished third (G) Joe finished third
Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. A fruit stand sells seven fruits: kiwis, plums, mangoes, watermelons, pears, peaches, and oranges. The pears are the third-cheapest. The kiwis are the second-most expensive. The pears are more expensive than the plums. The oranges are less expensive than the kiwis. The mangoes are the third-most expensive. The peaches are the second-cheapest. Options: (A) The kiwis are the second-cheapest (B) The plums are the second-cheapest (C) The mangoes are the second-cheapest (D) The watermelons are the second-cheapest (E) The pears are the second-cheapest (F) The peaches are the second-cheapest (G) The oranges are the second-cheapest
Answer: The question asks which fruit is the second-cheapest. According to the information provided, the peaches are the second-cheapest. The answer is {F}.

"""

SELF_CRITIQUE_PROMPT = """Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a bus, a motorcycle, a hatchback, a station wagon, a minivan, a truck, and a limousine. The station wagon is the fourth-newest. The motorcycle is newer than the truck. The station wagon is older than the hatchback. The minivan is newer than the hatchback. The bus is newer than the minivan. The truck is newer than the limousine. Options: (A) The bus is the third-oldest (B) The motorcycle is the third-oldest (C) The hatchback is the third-oldest (D) The station wagon is the third-oldest (E) The minivan is the third-oldest (F) The truck is the third-oldest (G) The limousine is the third-oldest
Answer: To determine which vehicle is the third-oldest, we need to analyze the given facts: 1. The station wagon is the fourth-newest: This means there are three vehicles that are newer than the station wagon. 2. The motorcycle is newer than the truck: This indicates that the motorcycle is not the oldest and is positioned above the truck in terms of age. 3. The station wagon is older than the hatchback: This means the hatchback is newer than the station wagon. 4. The minivan is newer than the hatchback: This places the minivan above the hatchback in terms of age. 5. The bus is newer than the minivan: This means the bus is the newest among the minivan and the hatchback. 6. The truck is newer than the limousine: This indicates that the limousine is older than the truck. Now, let's summarize the order based on the information: - Since the station wagon is the fourth-newest, we can denote the order as follows: - 1st: Bus (newest) - 2nd: Minivan (newer than hatchback) - 3rd: Motorcycle (newer than truck) - 4th: Station Wagon (given) - 5th: Hatchback (older than station wagon) - 6th: Truck (newer than limousine) - 7th: Limousine (oldest) From this arrangement, we can see that the third-oldest vehicle is the motorcycle. The answer is {B}.

Let's check the reasoning step by step:
Step 1: Identified "station wagon is fourth-newest" correctly ✓
Step 2: Listed all relationships between vehicles ✓ Correct
Step 3: Attempted to build order from newest to oldest
Step 4: Claimed order is: Bus(1st), Minivan(2nd), Motorcycle(3rd), Station Wagon(4th), Hatchback(5th), Truck(6th), Limousine(7th)
Let me verify this order against all constraints:
- Station wagon is 4th-newest? Yes ✓
- Motorcycle newer than truck? Motorcycle is 3rd, truck is 6th. Yes ✓
- Station wagon older than hatchback? Station wagon is 4th, hatchback is 5th. Wait - 4th-newest means newer, not older! ✗ ERROR!
- This violates the constraint "station wagon is older than hatchback"
The positions need to be recalculated more carefully considering all constraints.
Overall quality: 5/10 (logical approach but incorrect final ordering)
Should this answer be refined further? Yes

Question: On a branch, there are seven birds: a robin, an owl, a quail, a falcon, a hummingbird, a cardinal, and a crow. The hummingbird is to the left of the falcon. The crow is to the right of the cardinal. The cardinal is the second from the right. The quail is the third from the right. The falcon is to the left of the robin. The owl is the second from the left. Options: (A) The robin is the fourth from the left (B) The owl is the fourth from the left (C) The quail is the fourth from the left (D) The falcon is the fourth from the left (E) The hummingbird is the fourth from the left (F) The cardinal is the fourth from the left (G) The crow is the fourth from the left
Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6 (since there are 7 positions total). 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon: The falcon must be in a position to the right of the hummingbird. 6. The falcon is to the left of the robin: This means the falcon must be in a position to the left of the robin.
Now, we can summarize the positions we have so far: 2: Owl 5: Quail 6: Cardinal 7: Crow. Since the owl is in position 2, the only available positions left for the hummingbird, falcon, and robin are 1, 3, and 4.  Now, we can answer the question, the robin is in position 4. The answer is {A}.

Let's check the reasoning step by step:
Step 1: "cardinal is position 6" ✓ Correct (second from right in 7 positions = position 6)
Step 2: "quail is position 5" ✓ Correct (third from right = position 5)
Step 3: "crow is position 7" ✓ Correct (to the right of cardinal at position 6)
Step 4: "owl is position 2" ✓ Correct (second from left = position 2)
Step 5: Fixed positions are 2: Owl, 5: Quail, 6: Cardinal, 7: Crow ✓
Step 6: Remaining positions are 1, 3, 4 for hummingbird, falcon, robin ✓
Step 7: Need to place these three based on: hummingbird < falcon < robin
Step 8: Conclusion "robin is in position 4" - but this wasn't fully justified!
The answer doesn't show WHY robin is at position 4. We need to verify:
If hummingbird < falcon < robin, and positions are 1,3,4, then: hummingbird=1, falcon=3, robin=4 ✓
This satisfies all constraints, but the working should show this verification.
Overall quality: 8/10 (correct answer but incomplete justification for final step)
Should this answer be refined further? Yes

"""

REFINE_PROMPT = """Question: On a branch, there are seven birds: a hummingbird, a cardinal, a blue jay, an owl, a raven, a quail, and a robin. The hummingbird is to the left of the quail. The robin is to the left of the cardinal. The blue jay is the leftmost. The cardinal is the fourth from the left. The raven is the third from the right. The owl is the third from the left. Options: (A) The hummingbird is the second from the right (B) The cardinal is the second from the right (C) The blue jay is the second from the right (D) The owl is the second from the right (E) The raven is the second from the right (F) The quail is the second from the right (G) The robin is the second from the right
Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The blue jay is the leftmost: This means the blue jay is in position 1. 2. The cardinal is the fourth from the left: Therefore, the cardinal is in position 4. 3. The raven is the third from the right: Since there are seven birds, the raven is in position 5 (7 - 3 + 1 = 5). 4. The owl is the third from the left: This places the owl in position 3. 5. The hummingbird is to the left of the quail: Since the hummingbird must be to the left of the quail, and the only remaining positions are 2 and 6, the hummingbird must be in position 2 and the quail in position 6. 6. The robin is to the left of the cardinal: The only remaining position for the robin is 7, which is to the left of the cardinal in position 4. Now, we can summarize the positions: 1. Blue Jay 2. Hummingbird 3. Owl 4. Cardinal 5. Raven 6. Quail 7. Robin Now, we can answer the question regarding which bird is the second from the right. The second from the right is position 6, which is occupied by the quail. The answer is {F}.

Feedback: The logic is mostly sound, but there's an error in step 6. The robin cannot be in position 7 and also be "to the left of the cardinal" at position 4, since position 7 is to the RIGHT of position 4. Need to reconsider the placement of robin.
Overall quality: 6/10
Should this answer be refined further? Yes

Refined Answer:
Answer: Let's systematically place each bird using the constraints:
1. Blue jay is leftmost → Position 1
2. Cardinal is fourth from left → Position 4
3. Raven is third from right → Position 5 (since 7 - 3 + 1 = 5)
4. Owl is third from left → Position 3

Current layout: 1:Blue Jay, 3:Owl, 4:Cardinal, 5:Raven

Remaining positions: 2, 6, 7 for hummingbird, quail, and robin

5. Robin is to the left of cardinal (position 4) → Robin must be in position 2 (only available position left of 4)
6. Hummingbird is to the left of quail → With positions 6 and 7 remaining, this constraint cannot be satisfied since both are to the RIGHT of cardinal.

Wait, let me reconsider. Robin must be in position 2. That leaves positions 6 and 7 for hummingbird and quail.
Since hummingbird is to the left of quail, hummingbird must be in position 6 and quail in position 7.

Final layout: 1:Blue Jay, 2:Robin, 3:Owl, 4:Cardinal, 5:Raven, 6:Hummingbird, 7:Quail

The second from the right is position 6, which is the hummingbird.
The answer is {A}.

Question: In a golf tournament, there were seven golfers: Eli, Eve, Mel, Joe, Mya, Rob, and Ada. Ada finished above Mya. Eli finished below Joe. Eli finished above Eve. Ada finished second-to-last. Mel finished third. Rob finished fourth. Options: (A) Eli finished third-to-last (B) Eve finished third-to-last (C) Mel finished third-to-last (D) Joe finished third-to-last (E) Mya finished third-to-last (F) Rob finished third-to-last (G) Ada finished third-to-last
Answer: To determine the correct answer, let's analyze the provided facts: 1. Ada finished second-to-last: This means Ada is in 6th place. 2. Mel finished third: Mel is in 3rd place. 3. Rob finished fourth: Rob is in 4th place. 4. Ada finished above Mya: Since Ada is in 6th place, Mya must be in 7th place (last). 5. Eli finished below Joe: This means Joe is ranked higher than Eli. 6. Eli finished above Eve: This means Eve is ranked lower than Eli. Now, we can summarize the rankings based on the above facts: 1: Joe (since he is above Eli). 2: Eli (since he is above Eve). 3: Mel (given) 4: Rob (given). 5: Eve (since she is below Eli). 6: Ada (given as second-to-last). 7: Mya (last). Now, we need to find who finished third-to-last. The third-to-last position is 5th place. From our rankings, Eve finished in 5th place. The answer is {B}.

Feedback: The placement logic has issues. If Joe is 1st and Eli is 2nd, then Eli would be above Eve. But we need to verify all positions are consistent. With Mel at 3rd and Rob at 4th already fixed, positions 1, 2, and 5 need to accommodate Joe, Eli, and Eve such that Joe > Eli > Eve. Let's check: 1:Joe, 2:Eli would make Eli 2nd, not below Joe properly since we need more golfers between them potentially.
Overall quality: 7/10
Should this answer be refined further? Yes

Refined Answer:
Answer: Let's place the golfers step by step:

Fixed positions from explicit statements:
- Position 3: Mel (given)
- Position 4: Rob (given)
- Position 6: Ada (second-to-last)
- Position 7: Mya (last, since Ada finished above Mya)

Remaining positions: 1, 2, 5 for Joe, Eli, and Eve

Constraints for these three:
- Eli finished below Joe (Joe > Eli, meaning Joe has better/lower position number)
- Eli finished above Eve (Eli > Eve, meaning Eli has better/lower position number)
- Therefore: Joe > Eli > Eve

With positions 1, 2, 5 available:
- Position 1: Joe
- Position 2: Eli
- Position 5: Eve

Final ranking: 1:Joe, 2:Eli, 3:Mel, 4:Rob, 5:Eve, 6:Ada, 7:Mya

Third-to-last is position 5, which is Eve.
The answer is {B}.

"""