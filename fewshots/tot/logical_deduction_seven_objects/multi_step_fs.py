# Standard CoT Prompt (Used for final path generation)
logic_cot = """Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were seven golfers: Ana, Eve, Ada, Dan, Rob, Amy, and Joe. Dan finished third. Ana finished above Ada. Amy finished last. Dan finished below Rob. Eve finished below Ada. Rob finished below Joe. Options: (A) Ana finished third (B) Eve finished third (C) Ada finished third (D) Dan finished third (E) Rob finished third (F) Amy finished third (G) Joe finished third
Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a robin, an owl, a quail, a falcon, a hummingbird, a cardinal, and a crow. The hummingbird is to the left of the falcon. The crow is to the right of the cardinal. The cardinal is the second from the right. The quail is the third from the right. The falcon is to the left of the robin. The owl is the second from the left. Options: (A) The robin is the fourth from the left (B) The owl is the fourth from the left (C) The quail is the fourth from the left (D) The falcon is the fourth from the left (E) The hummingbird is the fourth from the left (F) The cardinal is the fourth from the left (G) The crow is the fourth from the left
Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6. 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon, and the falcon is to the left of the robin. Available spots are 1, 3, 4. This order fits as Hummingbird(1), Falcon(3), Robin(4). The robin is in position 4. The answer is {A}.

Question: {input}
Answer:"""

# Propose Prompt (Used to generate candidate next steps)
logic_propose = """Input: On a branch, there are seven birds... The hummingbird is to the left of the falcon. The crow is to the right of the cardinal. The cardinal is the second from the right. The quail is the third from the right. The falcon is to the left of the robin. The owl is the second from the left.
Possible next steps:
Deduction 1: Identify absolute positions first. "Cardinal is second from right" -> Pos 6. "Owl is second from left" -> Pos 2.
Deduction 2: Identify relative positions. "Hummingbird < Falcon" and "Falcon < Robin" creates a chain: Hummingbird < Falcon < Robin.
Deduction 3: Analyze the "Right side" cluster. Cardinal is 6. Crow is right of Cardinal -> Crow is 7. Quail is 3rd from right -> Quail is 5.

Input: In a golf tournament... Dan finished third. Ana finished above Ada. Amy finished last. Dan finished below Rob. Eve finished below Ada. Rob finished below Joe.
Possible next steps:
Deduction 1: Pinpoint the explicit rank provided. "Dan finished third" means Dan = 3.
Deduction 2: Identify the last place. "Amy finished last" means Amy = 7.
Deduction 3: Analyze the top ranks. Rob finished below Joe (Joe < Rob). Dan (3) finished below Rob (Rob < 3). This implies Joe is 1 and Rob is 2.

Input: {input}
Possible next steps:"""

# Value Prompt (Used to evaluate if a step is correct)
logic_value = """Evaluate if the deduction step fits the constraints (sure/likely/impossible)

Question: On a branch... Cardinal is 2nd from right. Owl is 2nd from left.
Step: The Owl is in position 2.
Judge: sure

Question: On a branch... Cardinal is 2nd from right.
Step: The Cardinal is in position 2.
Judge: impossible (2nd from right is position 6, not 2).

Question: In a golf tournament... Dan finished third... Rob finished below Joe.
Step: Joe finished in 4th place.
Judge: impossible (Dan is 3rd. If Rob is below Joe, and Dan is below Rob, Joe must be higher than 3rd, likely 1st or 2nd).

Question: In a golf tournament... Amy finished last.
Step: Amy is in position 7.
Judge: sure

Question: {input}
Step: {step}
Judge:"""