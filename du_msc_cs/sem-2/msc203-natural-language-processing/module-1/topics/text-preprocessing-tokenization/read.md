# Text Preprocessing & Tokenization

## Introduction
Text preprocessing and tokenization form the foundation of Natural Language Processing (NLP) pipelines. In research-oriented NLP systems, raw text undergoes rigorous transformation to enable effective feature extraction for advanced tasks like transformer-based modeling, semantic analysis, and cross-lingual transfer learning. At DU's MSc CS program, understanding these preprocessing nuances is critical as real-world text data often contains multilingual content, social media noise, and domain-specific artifacts that challenge conventional approaches.

Modern NLP research emphasizes language-agnostic preprocessing strategies due to the rise of multilingual models like mBERT and XLM-R. Tokenization has evolved beyond simple whitespace splitting to subword units (e.g., BPE, WordPiece) that handle out-of-vocabulary words in transformer architectures. This module bridges classical linguistic approaches with cutting-edge neural text representation needs.

## Key Concepts
1. **Text Normalization**: 
   - Unicode normalization (NFC/NFD forms)
   - Case folding vs. lowercasing tradeoffs
   - Handling diacritics in Indic languages
   - Emoji/URL/mention normalization using regex patterns

2. **Tokenization Granularity**:
   - Word-level: Whitespace splitting with punctuation handling
   - Sentence segmentation using Punkt algorithm
   - Subword tokenization (BPE: Byte-Pair Encoding)
   - WordPiece (used in BERT) and SentencePiece (language-agnostic)

3. **Advanced Challenges**:
   - Code-mixed text processing (e.g., Hinglish)
   - Handling clitic contractions in Dravidian languages
   - Grapheme vs. morpheme-aware tokenization
   - Tokenization for transformer models (special [CLS], [SEP] tokens)

4. **Linguistic Processing**:
   - Stop word removal: Language-specific lists vs. TF-IDF based approaches
   - Stemming (Porter, Snowball) vs. Lemmatization (using WordNet/Morphological analyzers)
   - Compound word splitting (German, Scandinavian languages)

## Examples
**Example 1: Subword Tokenization**
Input: "unhappiness"
BPE Process:
1. Split into characters: u n h a p p i n e s s
2. Learn merges: p+p → pp, h+a → ha, etc.
3. Final tokens: "un", "happiness" (depending on merge operations)

**Example 2: Code-Mixed Text**
Input: "Kya baat hai! This pizza is lit 🔥"
Processing:
1. Normalize: lowercase, remove punctuation → "kya baat hai this pizza is lit fire"
2. Language identification: [HI, HI, HI, EN, EN, EN, EN, EMOJI]
3. Tokenize: ["kya", "baat", "hai", "this", "pizza", "is", "lit", "fire"]

**Example 3: Morphological Richness**
Input (Turkish): "çocuklarımızdansınız" (You are from our children)
Morpheme analysis: çocuk + lar + ımız + dan + sınız
Tokenization: ["çocuk", "lar", "ımız", "dan", "sınız"]

## Exam Tips
1. Always justify tokenization choices for specific NLP tasks (e.g., BPE for neural MT)
2. Understand Unicode normalization forms for handling Devanagari/Arabic scripts
3. Compare sentencepiece vs. WordPiece in terms of language independence
4. Discuss tradeoffs: Aggressive stemming vs. information loss in clinical text
5. Memorize key algorithms: Porter stemmer steps, BPE merge operations
6. Prepare examples of tokenization failures in social media text
7. Link preprocessing to downstream tasks: How improper tokenization affects BERT's attention patterns