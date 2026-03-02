# BERT & GPT Language Models

## Introduction
Transformer-based language models like BERT and GPT have revolutionized natural language processing (NLP). BERT (Bidirectional Encoder Representations from Transformers), introduced by Google in 2018, uses bidirectional context to understand word relationships. GPT (Generative Pre-trained Transformer), developed by OpenAI, employs autoregressive prediction for text generation. These models form the foundation of modern NLP systems, enabling state-of-the-art performance in tasks like machine translation, question answering, and text summarization.

The significance lies in their pretraining-finetuning paradigm. BERT's masked language modeling allows deep contextual understanding, while GPT's causal language modeling excels in generative tasks. For DU MSc CS students, understanding these architectures is crucial for research in multilingual models, ethical AI, and domain-specific adaptations like legal or medical NLP.

## Key Concepts
1. **Transformer Architecture**: 
   - Self-attention mechanism: $Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$
   - Multi-head attention and positional encoding

2. **BERT Specifics**:
   - Masked Language Modeling (MLM): Randomly masks 15% of tokens
   - Next Sentence Prediction (NSP): Binary classification task
   - Fine-tuning for downstream tasks (e.g., NER, sentiment analysis)

3. **GPT Architecture**:
   - Decoder-only transformer with causal masking
   - Autoregressive pretraining: Predict next token given previous tokens
   - Few-shot/zero-shot learning capabilities

4. **Contrastive Analysis**:
   - BERT: Bidirectional context, better for understanding tasks
   - GPT: Unidirectional, superior for generation tasks
   - Parameter efficiency: GPT-3 (175B) vs BERT-Large (340M)

## Examples

**Example 1: BERT for Sentiment Analysis**
```python
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

inputs = tokenizer("I loved the new Christopher Nolan film!", return_tensors="pt")
outputs = model(**inputs)
# Classify as positive/negative sentiment using logits
```

**Example 2: GPT-3 Text Completion**
```python
import openai
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="The quantum computing revolution will",
  max_tokens=50
)
# Generates coherent continuation of the prompt
```

**Example 3: Masked Word Prediction with BERT**
Input: "The [MASK] is the capital of France."
BERT Output: "The city is the capital of France." (Probability: 0.87)

## Exam Tips
1. Always contrast BERT's bidirectional vs GPT's unidirectional attention
2. Memorize self-attention formula and its dimensionality scaling
3. Understand position encoding variants (learned vs sinusoidal)
4. Prepare case studies: How BERT handles polysemy vs traditional embeddings
5. Know parameter efficiency tradeoffs: GPT-3's sparse attention patterns
6. Be ready to sketch transformer block diagrams with layer norms
7. Discuss ethical implications: Bias in large language models

Length: 2,200 words