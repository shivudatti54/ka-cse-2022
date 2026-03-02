# Text Summarization and Generation

## Introduction
Text summarization and generation are fundamental tasks in Natural Language Processing (NLP) that involve condensing information (summarization) or creating new coherent text (generation). With the exponential growth of digital content, these techniques have become critical for applications ranging from news aggregation to AI-assisted writing tools.

Modern approaches leverage deep learning architectures like Transformer models, which have revolutionized the field through attention mechanisms. The research landscape includes extractive methods (selecting key sentences) and abstractive methods (generating novel phrases), with recent advances focusing on few-shot learning and ethical AI considerations.

For DU MSc CS students, understanding these techniques provides a foundation for research in information retrieval, dialogue systems, and AI safety. Current challenges include handling domain-specific jargon, maintaining factual consistency, and addressing hallucination in generated text.

## Key Concepts
1. **Extractive vs Abstractive Summarization**:
   - Extractive: Selects important sentences/phrases from source (e.g., TextRank algorithm)
   - Abstractive: Generates new sentences using NLG (e.g., BART, PEGASUS)

2. **Sequence-to-Sequence Architecture**:
   - Encoder-decoder framework with attention (Luong vs Bahdanau attention)
   - Handling long dependencies with transformer self-attention

3. **Evaluation Metrics**:
   - ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
   - BERTScore for semantic similarity
   - Human evaluation metrics (coherence, fluency)

4. **Controlled Generation**:
   - Temperature sampling for diversity control
   - Top-k and nucleus (top-p) sampling
   - Prompt engineering techniques

5. **Ethical Considerations**:
   - Bias propagation in training data
   - Detection of machine-generated text
   - Environmental impact of large models

## Examples

**Example 1: News Article Summarization**
*Problem*: Summarize a 500-word news article into 3 sentences using BERT-based extractive method.

*Solution*:
1. Preprocess text: sentence tokenization, remove stopwords
2. Compute sentence embeddings using BERT
3. Calculate cosine similarity between sentences
4. Apply TextRank algorithm to rank sentences
5. Select top 3 sentences with highest scores

**Example 2: Story Generation with GPT-3**
*Problem*: Generate a 100-word fantasy story starting with "The crystal forest glowed..."

*Solution*:
1. Set temperature=0.7 for creative diversity
2. Use prompt engineering: "Write a fantasy story in Tolkien's style:"
3. Implement nucleus sampling with top-p=0.9
4. Apply repetition penalty=1.2 to avoid loops
5. Post-process with grammar checker

## Exam Tips
1. Always differentiate between ROUGE-1 (unigram), ROUGE-L (longest sequence)
2. Understand transformer architecture components: self-attention, positional encoding
3. Be prepared to compare encoder-decoder vs decoder-only models
4. Know the ethical implications of text generation models
5. Practice calculating ROUGE scores manually
6. Study recent papers like PEGASUS (Google) and LED (Longformer-Encoder-Decoder)
7. Remember challenges in multilingual summarization

Length: 2500 words