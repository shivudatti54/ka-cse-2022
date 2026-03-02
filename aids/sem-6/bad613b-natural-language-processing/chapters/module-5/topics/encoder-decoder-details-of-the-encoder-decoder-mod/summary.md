# **Encoder-Decoder Model Revision Notes**

## **I. Introduction**

- Encoder-Decoder model is a fundamental architecture in sequence-to-sequence models
- Used for machine translation (MT) tasks

## **II. Details of the Encoder-Decoder Model**

- **Architecture:**
  - Encoder: takes input sequence and generates a continuous representation (context vector)
  - Decoder: generates output sequence based on context vector
- **Key Components:**
  - Encoder layers (e.g. LSTM, GRU)
  - Decoder layers (e.g. LSTM, GRU)
  - Attention mechanism (optional)
- **Training Objective:**
  - Maximizing likelihood of the output sequence given the input sequence

## **III. Translating in Low-Resource Situations**

- **Low-Resource Languages:**
  - Languages with limited training data (e.g. minority languages, languages with limited online presence)
- **Handling Low-Resource Languages:**
  - Using pre-trained models as starting points
  - Fine-tuning models on limited data
  - Using data augmentation techniques

## **IV. MT Evaluation**

- **Evaluation Metrics:**
  - BLEU score (a measure of similarity between predicted and reference translations)
  - METE score (a measure of fluency and coherence)
- **Other Evaluation Metrics:**
  - ROUGE score (a measure of overlapping n-grams between predicted and reference translations)

## **V. Bias and Ethical Issues**

- **Bias in MT Models:**
  - Language bias: models may favor certain languages over others
  - Cultural bias: models may reflect cultural biases in the training data
- **Mitigating Bias:**
  - Data augmentation techniques
  - Regularization techniques (e.g. dropout, weight decay)
  - Human evaluation and feedback

## **VI. Important Formulas and Definitions**

- **BLEU Score:**
  - BLEU = (sum of n-gram precisions) / (max n-gram precision)
- **ROUGE Score:**
  - ROUGE = (sum of overlapping n-grams) / (max overlapping n-grams)
- **Attention Mechanism:**
  - Attention = αt = softmax(At)
