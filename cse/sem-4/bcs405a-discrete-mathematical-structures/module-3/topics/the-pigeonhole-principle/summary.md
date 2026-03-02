# The Pigeonhole Principle - Summary

## Key Definitions and Concepts

- **Simple Pigeonhole Principle:** If (n + 1) or more objects are placed into n boxes, then at least one box contains at least 2 objects.

- **Generalized Pigeonhole Principle:** If m objects are placed into n boxes, then at least one box contains at least ⌈m/n⌉ objects, where ⌈x⌉ is the ceiling function.

- **Box/Pigeonhole:** A category, set, or container used to group objects with a common property (colors, remainders, values, etc.)

- **Object:** Items being distributed into boxes (people, numbers, socks, etc.)

- **Injection:** A one-to-one function; if |A| > |B|, no function f: A → B can be injective.

## Important Formulas and Theorems

1. Simple form: (n + 1) objects → n boxes guarantees ≥2 in some box

2. Generalized form: m objects → n boxes guarantees ≥⌈m/n⌉ in some box

3. Minimum boxes needed: To guarantee k+1 objects in some box with m objects, we need n boxes where m > nk

4. For m objects and n boxes: minimum in largest box = ⌈m/n⌉, minimum in smallest box = ⌊m/n⌋

## Key Points

- The principle provides existence proofs without construction - it proves something exists but doesn't identify what

- Correctly identifying "boxes" (categories) and "objects" (items) is essential for problem-solving

- Remainder problems: n integers and m possible remainders guarantee two with same remainder when n > m

- The birthday problem: 366 people guarantee a shared birthday (ignoring leap years)

- The handshake theorem: In n people, two have same handshake count (0 to n-1 possible values)

- For handshake problem with n people: only n-1 possible handshake counts are possible, guaranteeing a repeat

- The principle is fundamental to understanding hash collisions in computer science

- Applications extend to graph theory (Ramsey numbers), combinatorics, and algorithm analysis

## Common Mistakes to Avoid

1. **Confusing the direction:** Remember more objects than boxes forces collision, not fewer

2. **Forgetting the ceiling function:** Using floor instead of ceiling in generalized form gives wrong minimum

3. **Incorrect box identification:** Choosing wrong categories for boxes is the most common error

4. **Ignoring edge cases:** With exact multiples (e.g., 6 objects into 3 boxes), exactly 2 per box is possible

5. **Over-applying:** The principle only guarantees existence, not specific identification of which box

## Revision Tips

1. Practice 3-5 problems daily focusing on different box/object interpretations

2. Memorize the formula ⌈m/n⌉ and understand when to apply simple vs. generalized form

3. For number theory problems, always consider remainders modulo n as boxes

4. Draw diagrams or create simple tables to visualize box distributions

5. Review previous year questions - pigeonhole principle appears frequently in exams
