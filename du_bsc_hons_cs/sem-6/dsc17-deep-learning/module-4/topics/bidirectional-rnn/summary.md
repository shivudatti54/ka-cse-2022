# Bidirectional Recurrent Neural Networks (Bi-RNN) - Summary

## Key Definitions and Concepts

- **Bidirectional RNN**: A neural network architecture with two hidden layers processing input sequences in opposite directions—forward (left-to-right) and backward (right-to-left).

- **Forward Hidden State** ($\overrightarrow{h_t}$): Hidden representation computed by processing input from beginning to time step t.

- **Backward Hidden State** ($\overleftarrow{h_t}$): Hidden representation computed by processing input from end to time step t.

- **BiLSTM/BiGRU**: Bidirectional variants combining LSTM or GRU gating mechanisms with bidirectional processing.

## Important Formulas and Theorems

- Forward pass: $\overrightarrow{h_t} = \sigma(W_{f x} x_t + W_{f h} \overrightarrow{h_{t-1}} + b_f)$

- Backward pass: $\overleftarrow{h_t} = \sigma(W_{b x} x_t + W_{b h} \overleftarrow{h_{t+1}} + b_b)$

- Output: Concatenation of both hidden states: $y_t = [\overrightarrow{h_t}; \overleftarrow{h_t}]$

## Key Points

- Bi-RNN processes sequences in both directions simultaneously, providing complete contextual information at each time step.

- Output at each time step combines information from both past (forward) and future (backward) context.

- Two main variants: BiLSTM and BiGRU, combining bidirectional processing with gated memory mechanisms.

- Bi-RNN requires the entire input sequence before processing—unsuitable for real-time/streaming applications.

- Approximately doubles computational cost and memory compared to unidirectional RNNs.

- Essential architecture for sequence labeling tasks: NER, POS tagging, sentiment analysis.

- Training uses modified BPTT handling gradients from both temporal directions.

## Common Mistakes to Avoid

1. Confusing Bi-RNN with models that "predict the future"—Bi-RNN uses future input context, not predicts it.

2. Using Bi-RNN for online/streaming prediction where future data isn't available.

3. Assuming longer training time is always justified—use Bi-RNN only when bidirectional context genuinely improves performance.

4. Forgetting that backward layer processes from last timestep to first (reverse temporal order).

## Revision Tips

1. Draw the Bi-RNN architecture diagram—label forward/backward layers and show how outputs combine at each time step.

2. Memorize the three key scenarios: Use unidirectional for forecasting, Bi-RNN for sequence labeling when full sequence is available.

3. Review Keras/PyTorch implementation syntax: `Bidirectional(LSTM(...))` or `Bidirectional(GRU(...))`.

4. Practice explaining why "bank" needs bidirectional context in "I went to the bank to deposit money" versus "The river bank was eroded."

5. Compare computational costs: If a unidirectional RNN takes time T, Bi-RNN takes approximately 2T with double memory.