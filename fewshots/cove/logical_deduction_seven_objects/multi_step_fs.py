baseline_fewshot = """Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were seven golfers: Ana, Eve, Ada, Dan, Rob, Amy, and Joe. Dan finished third. Ana finished above Ada. Amy finished last. Dan finished below Rob. Eve finished below Ada. Rob finished below Joe. Options: (A) Ana finished third (B) Eve finished third (C) Ada finished third (D) Dan finished third (E) Rob finished third (F) Amy finished third (G) Joe finished third
Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a robin, an owl, a quail, a falcon, a hummingbird, a cardinal, and a crow. The hummingbird is to the left of the falcon. The crow is to the right of the cardinal. The cardinal is the second from the right. The quail is the third from the right. The falcon is to the left of the robin. The owl is the second from the left. Options: (A) The robin is the fourth from the left (B) The owl is the fourth from the left (C) The quail is the fourth from the left (D) The falcon is the fourth from the left (E) The hummingbird is the fourth from the left (F) The cardinal is the fourth from the left (G) The crow is the fourth from the left
Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6 (since there are 7 positions total). 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon: The falcon must be in a position to the right of the hummingbird. 6. The falcon is to the left of the robin: This means the falcon must be in a position to the left of the robin. Now, we can summarize the positions we have so far: 2: Owl 5: Quail 6: Cardinal 7: Crow. Since the owl is in position 2, the only available positions left for the hummingbird, falcon, and robin are 1, 3, and 4. Now, we can answer the question, the robin is in position 4. The answer is {A}.

Question: {NEW_QUESTION}
Answer:"""

plan_verification_fewshot = """Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. In a golf tournament, there were seven golfers: Ana, Eve, Ada, Dan, Rob, Amy, and Joe. Dan finished third. Ana finished above Ada. Amy finished last. Dan finished below Rob. Eve finished below Ada. Rob finished below Joe. Options: (A) Ana finished third (B) Eve finished third (C) Ada finished third (D) Dan finished third (E) Rob finished third (F) Amy finished third (G) Joe finished third

Initial Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Verification Questions:
1. Does the problem statement directly say that Dan finished third?
2. Are there any other golfers who could have finished third based on the constraints?
3. Is Dan's third-place finish consistent with "Dan finished below Rob" and "Rob finished below Joe"?

Question: The following paragraphs each describe a set of seven objects arranged in a fixed order. The statements are logically consistent within each paragraph. On a branch, there are seven birds: a robin, an owl, a quail, a falcon, a hummingbird, a cardinal, and a crow. The hummingbird is to the left of the falcon. The crow is to the right of the cardinal. The cardinal is the second from the right. The quail is the third from the right. The falcon is to the left of the robin. The owl is the second from the left. Options: (A) The robin is the fourth from the left (B) The owl is the fourth from the left (C) The quail is the fourth from the left (D) The falcon is the fourth from the left (E) The hummingbird is the fourth from the left (F) The cardinal is the fourth from the left (G) The crow is the fourth from the left

Initial Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6 (since there are 7 positions total). 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon: The falcon must be in a position to the right of the hummingbird. 6. The falcon is to the left of the robin: This means the falcon must be in a position to the left of the robin. Now, we can summarize the positions we have so far: 2: Owl 5: Quail 6: Cardinal 7: Crow. Since the owl is in position 2, the only available positions left for the hummingbird, falcon, and robin are 1, 3, and 4. Now, we can answer the question, the robin is in position 4. The answer is {A}.

Verification Questions:
1. If the cardinal is the second from the right in a list of 7, what position number is that?
2. If the quail is the third from the right, what position number is that?
3. If the cardinal is in position 6 and the crow is to the right of the cardinal, what position is the crow in?
4. What positions are left unfilled after placing owl (2), quail (5), cardinal (6), and crow (7)?
5. Given that hummingbird is left of falcon, and falcon is left of robin, and positions 1, 3, 4 are available, which bird goes in position 4?

Question: In a golf tournament, there were seven golfers: Eli, Eve, Mel, Joe, Mya, Rob, and Ada. Ada finished above Mya. Eli finished below Joe. Eli finished above Eve. Ada finished second-to-last. Mel finished third. Rob finished fourth. Options: (A) Eli finished third-to-last (B) Eve finished third-to-last (C) Mel finished third-to-last (D) Joe finished third-to-last (E) Mya finished third-to-last (F) Rob finished third-to-last (G) Ada finished third-to-last

Initial Answer: To determine the correct answer, let's analyze the provided facts: 1. Ada finished second-to-last: This means Ada is in 6th place. 2. Mel finished third: Mel is in 3rd place. 3. Rob finished fourth: Rob is in 4th place. 4. Ada finished above Mya: Since Ada is in 6th place, Mya must be in 7th place (last). 5. Eli finished below Joe: This means Joe is ranked higher than Eli. 6. Eli finished above Eve: This means Eve is ranked lower than Eli. Now, we can summarize the rankings based on the above facts: 1: Joe (since he is above Eli). 2: Eli (since he is above Eve). 3: Mel (given) 4: Rob (given). 5: Eve (since she is below Eli). 6: Ada (given as second-to-last). 7: Mya (last). Now, we need to find who finished third-to-last. The third-to-last position is 5th place. From our rankings, Eve finished in 5th place. The answer is {B}.

Verification Questions:
1. If Ada finished second-to-last in a tournament of 7, what position is that?
2. If Ada is in 6th place and Ada finished above Mya, what position is Mya in?
3. What is the third-to-last position in a tournament of 7 golfers?
4. Given the fixed positions (Mel=3rd, Rob=4th, Ada=6th, Mya=7th), and the constraints (Eli below Joe, Eli above Eve), what are the possible positions for Joe, Eli, and Eve?
5. If positions 1, 2, and 5 are available for Joe, Eli, and Eve, and Joe > Eli > Eve, who is in position 5?

Question: {NEW_QUESTION}

Initial Answer: {NEW_INITIAL_ANSWER}

Verification Questions:"""

execute_verification_fewshot = """Question: Does the problem statement directly say that Dan finished third?
Answer: Yes, the problem explicitly states "Dan finished third."

Question: Are there any other golfers who could have finished third based on the constraints?
Answer: No, since the problem explicitly states "Dan finished third," no other golfer can finish third. The constraints must be consistent with Dan being in third place.

Question: Is Dan's third-place finish consistent with "Dan finished below Rob" and "Rob finished below Joe"?
Answer: Yes. If Dan is in 3rd place and Dan finished below Rob, then Rob must be in 1st or 2nd place. If Rob finished below Joe, then Joe must be in 1st place. This means Joe=1st, Rob=2nd, Dan=3rd, which is consistent.

Question: If the cardinal is the second from the right in a list of 7, what position number is that?
Answer: Second from the right means counting from the right: position 7 is first from right, position 6 is second from right. So the cardinal is in position 6.

Question: If the quail is the third from the right, what position number is that?
Answer: Third from the right means: position 7 is first, position 6 is second, position 5 is third from the right. So the quail is in position 5.

Question: If the cardinal is in position 6 and the crow is to the right of the cardinal, what position is the crow in?
Answer: To the right means higher position number. The only position to the right of position 6 in a list of 7 is position 7. So the crow is in position 7.

Question: What positions are left unfilled after placing owl (2), quail (5), cardinal (6), and crow (7)?
Answer: Positions filled: 2, 5, 6, 7. Total positions: 1, 2, 3, 4, 5, 6, 7. Unfilled positions: 1, 3, 4.

Question: Given that hummingbird is left of falcon, and falcon is left of robin, and positions 1, 3, 4 are available, which bird goes in position 4?
Answer: If hummingbird < falcon < robin, and we have positions 1, 3, 4, then the order must be: hummingbird=1, falcon=3, robin=4. Therefore, robin is in position 4.

Question: If Ada finished second-to-last in a tournament of 7, what position is that?
Answer: Second-to-last in a tournament of 7 means 6th place (7th is last, 6th is second-to-last).

Question: If Ada is in 6th place and Ada finished above Mya, what position is Mya in?
Answer: If Ada is in 6th place and finished above Mya, then Mya must be in a lower position (higher number). The only position below 6th in a tournament of 7 is 7th place. So Mya is in 7th place.

Question: What is the third-to-last position in a tournament of 7 golfers?
Answer: In a tournament of 7: 7th is last, 6th is second-to-last, 5th is third-to-last. So 5th place is third-to-last.

Question: Given the fixed positions (Mel=3rd, Rob=4th, Ada=6th, Mya=7th), and the constraints (Eli below Joe, Eli above Eve), what are the possible positions for Joe, Eli, and Eve?
Answer: Fixed positions: 3, 4, 6, 7. Available positions: 1, 2, 5. Constraints: Joe > Eli > Eve (in ranking, lower number = better). So Joe must be 1st, Eli must be 2nd, and Eve must be 5th.

Question: If positions 1, 2, and 5 are available for Joe, Eli, and Eve, and Joe > Eli > Eve, who is in position 5?
Answer: Joe > Eli > Eve means Joe has the best ranking (lowest position number). So Joe=1st, Eli=2nd, Eve=5th. Eve is in position 5.

Question: {NEW_VERIFICATION_QUESTION}
Answer:"""

crosscheck_fewshot = """Original Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Verification Question: Does the problem statement directly say that Dan finished third?
Verification Answer: Yes, the problem explicitly states "Dan finished third."

Analysis: Consistent. The original answer correctly identifies that Dan finished third is explicitly stated in the problem.

Original Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Verification Question: Is Dan's third-place finish consistent with "Dan finished below Rob" and "Rob finished below Joe"?
Verification Answer: Yes. If Dan is in 3rd place and Dan finished below Rob, then Rob must be in 1st or 2nd place. If Rob finished below Joe, then Joe must be in 1st place. This means Joe=1st, Rob=2nd, Dan=3rd, which is consistent.

Analysis: Consistent. The original answer's conclusion that Dan finished third is supported by the constraint verification.

Original Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6 (since there are 7 positions total). 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon: The falcon must be in a position to the right of the hummingbird. 6. The falcon is to the left of the robin: This means the falcon must be in a position to the left of the robin. Now, we can summarize the positions we have so far: 2: Owl 5: Quail 6: Cardinal 7: Crow. Since the owl is in position 2, the only available positions left for the hummingbird, falcon, and robin are 1, 3, and 4. Now, we can answer the question, the robin is in position 4. The answer is {A}.

Verification Question: If the cardinal is the second from the right in a list of 7, what position number is that?
Verification Answer: Second from the right means counting from the right: position 7 is first from right, position 6 is second from right. So the cardinal is in position 6.

Analysis: Consistent. The original answer correctly converts "second from the right" to position 6.

Original Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6 (since there are 7 positions total). 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon: The falcon must be in a position to the right of the hummingbird. 6. The falcon is to the left of the robin: This means the falcon must be in a position to the left of the robin. Now, we can summarize the positions we have so far: 2: Owl 5: Quail 6: Cardinal 7: Crow. Since the owl is in position 2, the only available positions left for the hummingbird, falcon, and robin are 1, 3, and 4. Now, we can answer the question, the robin is in position 4. The answer is {A}.

Verification Question: Given that hummingbird is left of falcon, and falcon is left of robin, and positions 1, 3, 4 are available, which bird goes in position 4?
Verification Answer: If hummingbird < falcon < robin, and we have positions 1, 3, 4, then the order must be: hummingbird=1, falcon=3, robin=4. Therefore, robin is in position 4.

Analysis: Consistent. The verification confirms that robin is in position 4, matching the original answer.

Original Answer: To determine the correct answer, let's analyze the provided facts: 1. Ada finished second-to-last: This means Ada is in 6th place. 2. Mel finished third: Mel is in 3rd place. 3. Rob finished fourth: Rob is in 4th place. 4. Ada finished above Mya: Since Ada is in 6th place, Mya must be in 7th place (last). 5. Eli finished below Joe: This means Joe is ranked higher than Eli. 6. Eli finished above Eve: This means Eve is ranked lower than Eli. Now, we can summarize the rankings based on the above facts: 1: Joe (since he is above Eli). 2: Eli (since he is above Eve). 3: Mel (given) 4: Rob (given). 5: Eve (since she is below Eli). 6: Ada (given as second-to-last). 7: Mya (last). Now, we need to find who finished third-to-last. The third-to-last position is 5th place. From our rankings, Eve finished in 5th place. The answer is {B}.

Verification Question: What is the third-to-last position in a tournament of 7 golfers?
Verification Answer: In a tournament of 7: 7th is last, 6th is second-to-last, 5th is third-to-last. So 5th place is third-to-last.

Analysis: Consistent. The original answer correctly identifies that third-to-last is 5th place.

Original Answer: To determine the correct answer, let's analyze the provided facts: 1. Ada finished second-to-last: This means Ada is in 6th place. 2. Mel finished third: Mel is in 3rd place. 3. Rob finished fourth: Rob is in 4th place. 4. Ada finished above Mya: Since Ada is in 6th place, Mya must be in 7th place (last). 5. Eli finished below Joe: This means Joe is ranked higher than Eli. 6. Eli finished above Eve: This means Eve is ranked lower than Eli. Now, we can summarize the rankings based on the above facts: 1: Joe (since he is above Eli). 2: Eli (since he is above Eve). 3: Mel (given) 4: Rob (given). 5: Eve (since she is below Eli). 6: Ada (given as second-to-last). 7: Mya (last). Now, we need to find who finished third-to-last. The third-to-last position is 5th place. From our rankings, Eve finished in 5th place. The answer is {B}.

Verification Question: If positions 1, 2, and 5 are available for Joe, Eli, and Eve, and Joe > Eli > Eve, who is in position 5?
Verification Answer: Joe > Eli > Eve means Joe has the best ranking (lowest position number). So Joe=1st, Eli=2nd, Eve=5th. Eve is in position 5.

Analysis: Consistent. The verification confirms Eve is in 5th place (third-to-last), which matches the original answer {B}.

Original Answer: {NEW_ORIGINAL_ANSWER}

Verification Question: {NEW_VERIFICATION_QUESTION}
Verification Answer: {NEW_VERIFICATION_ANSWER}

Analysis:"""

final_revision_fewshot = """Original Question: In a golf tournament, there were seven golfers: Ana, Eve, Ada, Dan, Rob, Amy, and Joe. Dan finished third. Ana finished above Ada. Amy finished last. Dan finished below Rob. Eve finished below Ada. Rob finished below Joe. Options: (A) Ana finished third (B) Eve finished third (C) Ada finished third (D) Dan finished third (E) Rob finished third (F) Amy finished third (G) Joe finished third

Initial Answer: In the golf tournament, Dan finished third is explicitly stated, so the answer is {D}.

Verification Results:
1. Q: Does the problem statement directly say that Dan finished third?
   A: Yes, the problem explicitly states "Dan finished third."
   Check: Consistent
2. Q: Are there any other golfers who could have finished third based on the constraints?
   A: No, the problem explicitly states Dan finished third.
   Check: Consistent
3. Q: Is Dan's third-place finish consistent with "Dan finished below Rob" and "Rob finished below Joe"?
   A: Yes. Joe=1st, Rob=2nd, Dan=3rd is consistent.
   Check: Consistent

Revised Final Answer: The problem explicitly states "Dan finished third." This is consistent with all the given constraints (Dan finished below Rob, Rob finished below Joe). The answer is {D}.

---

Original Question: On a branch, there are seven birds: a robin, an owl, a quail, a falcon, a hummingbird, a cardinal, and a crow. The hummingbird is to the left of the falcon. The crow is to the right of the cardinal. The cardinal is the second from the right. The quail is the third from the right. The falcon is to the left of the robin. The owl is the second from the left. Options: (A) The robin is the fourth from the left (B) The owl is the fourth from the left (C) The quail is the fourth from the left (D) The falcon is the fourth from the left (E) The hummingbird is the fourth from the left (F) The cardinal is the fourth from the left (G) The crow is the fourth from the left

Initial Answer: To determine the positions of the birds, we can analyze the given facts step by step: 1. The cardinal is the second from the right: This means the cardinal is in position 6 (since there are 7 positions total). 2. The quail is the third from the right: Since the cardinal is in position 6, the quail must be in position 5. 3. The crow is to the right of the cardinal: Since the cardinal is in position 6, the crow must be in position 7. 4. The owl is the second from the left: This means the owl is in position 2. 5. The hummingbird is to the left of the falcon: The falcon must be in a position to the right of the hummingbird. 6. The falcon is to the left of the robin: This means the falcon must be in a position to the left of the robin. Now, we can summarize the positions we have so far: 2: Owl 5: Quail 6: Cardinal 7: Crow. Since the owl is in position 2, the only available positions left for the hummingbird, falcon, and robin are 1, 3, and 4. Now, we can answer the question, the robin is in position 4. The answer is {A}.

Verification Results:
1. Q: If the cardinal is the second from the right in a list of 7, what position number is that?
   A: Position 6
   Check: Consistent
2. Q: If the quail is the third from the right, what position number is that?
   A: Position 5
   Check: Consistent
3. Q: If the cardinal is in position 6 and the crow is to the right of the cardinal, what position is the crow in?
   A: Position 7
   Check: Consistent
4. Q: What positions are left unfilled after placing owl (2), quail (5), cardinal (6), and crow (7)?
   A: Positions 1, 3, 4
   Check: Consistent
5. Q: Given that hummingbird is left of falcon, and falcon is left of robin, and positions 1, 3, 4 are available, which bird goes in position 4?
   A: Robin is in position 4
   Check: Consistent

Revised Final Answer: Based on the constraints: cardinal (position 6), quail (position 5), crow (position 7), owl (position 2). The remaining positions 1, 3, 4 must be filled by hummingbird, falcon, and robin. Since hummingbird < falcon < robin, they occupy positions 1, 3, and 4 respectively. Therefore, robin is the fourth from the left. The answer is {A}.

---

Original Question: In a golf tournament, there were seven golfers: Eli, Eve, Mel, Joe, Mya, Rob, and Ada. Ada finished above Mya. Eli finished below Joe. Eli finished above Eve. Ada finished second-to-last. Mel finished third. Rob finished fourth. Options: (A) Eli finished third-to-last (B) Eve finished third-to-last (C) Mel finished third-to-last (D) Joe finished third-to-last (E) Mya finished third-to-last (F) Rob finished third-to-last (G) Ada finished third-to-last

Initial Answer: To determine the correct answer, let's analyze the provided facts: 1. Ada finished second-to-last: This means Ada is in 6th place. 2. Mel finished third: Mel is in 3rd place. 3. Rob finished fourth: Rob is in 4th place. 4. Ada finished above Mya: Since Ada is in 6th place, Mya must be in 7th place (last). 5. Eli finished below Joe: This means Joe is ranked higher than Eli. 6. Eli finished above Eve: This means Eve is ranked lower than Eli. Now, we can summarize the rankings based on the above facts: 1: Joe (since he is above Eli). 2: Eli (since he is above Eve). 3: Mel (given) 4: Rob (given). 5: Eve (since she is below Eli). 6: Ada (given as second-to-last). 7: Mya (last). Now, we need to find who finished third-to-last. The third-to-last position is 5th place. From our rankings, Eve finished in 5th place. The answer is {B}.

Verification Results:
1. Q: If Ada finished second-to-last in a tournament of 7, what position is that?
   A: 6th place
   Check: Consistent
2. Q: If Ada is in 6th place and Ada finished above Mya, what position is Mya in?
   A: 7th place
   Check: Consistent
3. Q: What is the third-to-last position in a tournament of 7 golfers?
   A: 5th place
   Check: Consistent
4. Q: Given the fixed positions (Mel=3rd, Rob=4th, Ada=6th, Mya=7th), and the constraints (Eli below Joe, Eli above Eve), what are the possible positions for Joe, Eli, and Eve?
   A: Joe=1st, Eli=2nd, Eve=5th
   Check: Consistent
5. Q: If positions 1, 2, and 5 are available for Joe, Eli, and Eve, and Joe > Eli > Eve, who is in position 5?
   A: Eve is in position 5
   Check: Consistent

Revised Final Answer: Fixed positions: Mel=3rd, Rob=4th, Ada=6th (second-to-last), Mya=7th (last). Constraints: Joe > Eli > Eve. This gives us: Joe=1st, Eli=2nd, Eve=5th. Third-to-last in a tournament of 7 is 5th place. Therefore, Eve finished third-to-last. The answer is {B}.

---

Original Question: {NEW_QUESTION}

Initial Answer: {NEW_INITIAL_ANSWER}

Verification Results:
{NEW_VERIFICATION_RESULTS}

Revised Final Answer:"""