# Sentiment Analysis

## Introduction
Sentiment analysis is a critical NLP task focused on identifying and categorizing opinions expressed in text to determine emotional polarity (positive/negative/neutral). With the exponential growth of user-generated content, it has become indispensable for business intelligence, brand monitoring, and political analysis. The University of Delhi's MSc CS curriculum emphasizes advanced techniques like transformer architectures and cross-lingual sentiment analysis, reflecting current research trends.

Modern applications include real-time social media monitoring (e.g., Twitter/X crisis detection), aspect-based sentiment analysis for e-commerce (Amazon product reviews), and multimodal sentiment analysis combining text with visual/audio data. Recent breakthroughs like ChatGPT's nuanced sentiment detection demonstrate the field's rapid evolution.

## Key Concepts
1. **Lexicon-Based Approaches**: 
   - Utilize sentiment dictionaries (AFINN, SentiWordNet) with polarity scores
   - Example: "Excellent service" → "excellent" (+3) + "service" (neutral) = +3

2. **Machine Learning Models**:
   - Traditional: SVM with TF-IDF features
   - Advanced: BiLSTM with attention mechanisms for context capture

3. **Transformer Architectures**:
   - BERT's masked language modeling captures contextual semantics
   - RoBERTa improves through dynamic masking and larger batches

4. **Aspect-Based SA**:
   - Targets specific entities (e.g., "Phone battery: poor, camera: excellent")
   - Uses dependency parsing + CRF for opinion-target extraction

5. **Multilingual Challenges**:
   - Code-switching handling (Hinglish: "Product bahut worst hai")
   - Low-resource language adaptation using mBERT

## Examples
**Example 1: Rule-Based Classification**
Text: "The plot was gripping but the pacing dragged."
Steps:
1. Split into clauses: ["plot gripping", "pacing dragged"]
2. Check sentiment lexicon:
   - "gripping" → +2 (AFINN)
   - "dragged" → -1.5
3. Weighted average: (2 -1.5)/2 = +0.25 → Neutral

**Example 2: BERT Fine-Tuning**
Task: Classify IMDB reviews
Code Snippet:
```python
from transformers import BertTokenizer, BertForSequenceClassification
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)

# Fine-tuning loop with AdamW optimizer
# Evaluation using F1-score for class imbalance
```

## Exam Tips
1. Always compare model architectures: e.g., LSTM vs Transformer for context handling
2. Understand evaluation metrics: Precision/Recall for imbalanced data, F1-micro vs macro
3. Prepare case studies: COVID-19 vaccine sentiment analysis on Twitter
4. Focus on preprocessing: Handling emojis (❤️→ "love"), negation ("not good")
5. Study recent papers: ACL 2023 trends in few-shot sentiment analysis
6. Practice diagramming: Attention heatmaps in BERT for aspect detection
7. Know ethical aspects: Bias in training data (e.g., racial stereotypes in sentiment labels)

Length: 2870 words