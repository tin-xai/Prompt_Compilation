LOGICAL_DEDUCTION_DECOMPOSE = """Q: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In an antique car show, there are seven vehicles: a bus, a motorcycle, a hatchback, a station wagon, a minivan, a truck, and a limousine. The station wagon is the fourth-newest. The motorcycle is newer than the truck. The station wagon is older than the hatchback. The minivan is newer than the hatchback. The bus is newer than the minivan. The truck is newer than the limousine. Which vehicle is the third-oldest?
A: To answer "Which vehicle is the third-oldest?", we need to know: "What is the complete ordering of vehicles from newest to oldest?"

Q: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a hummingbird, a cardinal, a blue jay, an owl, a raven, a quail, and a robin. The hummingbird is to the left of the quail. The robin is to the left of the cardinal. The blue jay is the leftmost. The cardinal is the fourth from the left. The raven is the third from the right. The owl is the third from the left. Which bird is the second from the right?
A: To answer "Which bird is the second from the right?", we need to know: "What are the fixed positions?", "What are the positions of the remaining birds?"

"""

LOGICAL_DEDUCTION_SOLVE = """In an antique car show, there are seven vehicles: a bus, a motorcycle, a hatchback, a station wagon, a minivan, a truck, and a limousine. The station wagon is the fourth-newest. The motorcycle is newer than the truck. The station wagon is older than the hatchback. The minivan is newer than the hatchback. The bus is newer than the minivan. The truck is newer than the limousine.

Q: What is the complete ordering of vehicles from newest to oldest?
A: Let me work through the constraints:
- Station wagon is 4th-newest (position 4)
- Station wagon is older than hatchback → hatchback is positions 1-3
- Minivan is newer than hatchback → minivan is also positions 1-3
- Bus is newer than minivan → bus must be position 1, 2, or 3
- Motorcycle is newer than truck
- Truck is newer than limousine

Since bus > minivan > hatchback, and all are newer than station wagon (position 4):
Position 1 (newest): Bus
Position 2: Minivan
Position 3: Motorcycle (must be here, newer than truck)
Position 4: Station wagon
Position 5: Hatchback
Position 6: Truck
Position 7 (oldest): Limousine

The answer is this ordering.

Q: Which vehicle is the third-oldest?
A: From the ordering above, the third-oldest is position 5, which is the hatchback. However, looking at the options and re-checking: position 5 from newest = position 3 from oldest. That's the motorcycle. The answer is {B}.

On a branch, there are seven birds: a hummingbird, a cardinal, a blue jay, an owl, a raven, a quail, and a robin. The hummingbird is to the left of the quail. The robin is to the left of the cardinal. The blue jay is the leftmost. The cardinal is the fourth from the left. The raven is the third from the right. The owl is the third from the left.

Q: What are the fixed positions?
A: From the facts:
- Blue jay is leftmost: position 1
- Cardinal is fourth from left: position 4
- Raven is third from right: position 5 (since 7 - 3 + 1 = 5)
- Owl is third from left: position 3

Q: What are the positions of the remaining birds?
A: Remaining birds: hummingbird, quail, robin
Remaining positions: 2, 6, 7
Constraints:
- Hummingbird is left of quail
- Robin is left of cardinal (position 4)

Since robin must be left of cardinal (position 4), and positions 1 and 3 are taken, robin cannot satisfy this unless there's an error. Let me reconsider: "left of cardinal" likely means robin is in position 2, 6, or 7 but position 7 is rightmost. 

Actually, the robin must be in position 2, 6, or 7. Given robin < cardinal (position 4), robin must be in position 2.
Hummingbird < quail, so hummingbird in position 6, quail in position 7? But let me verify...

Position 2: Robin (only option left of cardinal)
Positions 6, 7: hummingbird and quail (hummingbird < quail)
Position 6: Quail, Position 7: Robin? No, robin is position 2.

Final: Position 2: Hummingbird, Position 6: Quail, Position 7: Robin

Q: Which bird is the second from the right?
A: Second from right is position 6, which is the quail. The answer is {F}.

A fruit stand sells seven fruits: kiwis, plums, mangoes, watermelons, pears, peaches, and oranges. The pears are the third-cheapest. The kiwis are the second-most expensive. The pears are more expensive than the plums. The oranges are less expensive than the kiwis. The mangoes are the third-most expensive. The peaches are the second-cheapest.

Q: Is the answer explicitly stated in the facts?
A: Yes, "The peaches are the second-cheapest" is directly stated. The answer is {F}."""