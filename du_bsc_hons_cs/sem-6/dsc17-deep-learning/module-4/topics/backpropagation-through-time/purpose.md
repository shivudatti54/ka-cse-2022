# Learning Objectives

After studying this topic, you should be able to:

1. Explain the concept of temporal unrolling in RNNs and how it transforms recurrent computation into an equivalent feedforward structure.

2. Describe the complete BPTT algorithm, including the forward pass through time, gradient computation at each time step, and weight updates.

3. Analyze the vanishing and exploding gradient problems in BPTT, identifying their root causes and consequences for training RNNs.

4. Derive and compute gradients through time using the chain rule, demonstrating understanding of how errors propagate backwards through the sequence.

5. Compare full BPTT with truncated BPTT, explaining the trade-offs between computational efficiency and gradient quality.

6. Implement the BPTT algorithm for a simple RNN, including forward pass, backward pass, and weight updates.

7. Evaluate why standard RNNs struggle with long sequences and explain how gating mechanisms in LSTMs and GRUs address BPTT's limitations.