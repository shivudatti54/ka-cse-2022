# Learning Objectives

After studying this topic, you should be able to:

1. Define global state in the context of distributed systems and explain its components (local state and channel state)

2. Distinguish between consistent and inconsistent global states with appropriate examples

3. Explain the happened-before relation and its role in defining consistent cuts

4. Describe the Chandy-Lamport snapshot algorithm including its assumptions, steps, and correctness properties

5. Analyze why FIFO channel properties are necessary for the snapshot algorithm to work correctly

6. Interpret the lattice of global states and explain its significance in reasoning about distributed computations

7. Apply global state concepts to practical problems such as termination detection and checkpointing

8. Evaluate whether a given global state representation is consistent or inconsistent