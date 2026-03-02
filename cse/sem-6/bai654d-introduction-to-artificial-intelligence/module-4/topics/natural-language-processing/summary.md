# Natural Language Processing

## Overview

Natural Language Processing (NLP) enables computers to understand, interpret, and generate human language by breaking down the inherent ambiguity and complexity through a pipeline of processing steps. NLP transforms raw text into structured forms that machines can analyze for tasks like translation, sentiment analysis, and question answering.

## Key Points

- **Tokenization**: Breaking text into smaller units (tokens) like words, numbers, and punctuation marks
- **Stop Word Removal**: Eliminating common words with less meaningful information (the, is, at) to reduce dimensionality
- **Stemming**: Crude heuristic process chopping word endings to get root form (may create non-words)
- **Lemmatization**: Sophisticated process using vocabulary and morphology to return dictionary base form (lemma)
- **POS Tagging**: Assigning grammatical categories (noun, verb, adjective) to each token
- **Syntactic Parsing**: Analyzing grammatical structure to create parse trees showing word relationships
- **Semantic Analysis**: Extracting literal meaning through word sense disambiguation and named entity recognition
- **Word Embeddings**: Advanced representation mapping words to continuous vector spaces capturing semantic relationships

## Important Concepts

- NLP pipeline: Tokenization → Stop Word Removal → Stemming/Lemmatization → POS Tagging → Parsing → Feature Extraction → ML Model
- Lemmatization is more accurate but slower than stemming (better→good vs better→better)
- Bag-of-Words loses word order information while Word Embeddings capture semantic similarity (King - Man + Woman ≈ Queen)
- Key applications: sentiment analysis, machine translation, text summarization, chatbots, question answering

## Notes

- Memorize the NLP pipeline order and be able to explain each step's purpose
- Differentiate stemming versus lemmatization with clear examples
- Understand common POS tags: NN (noun), VB (verb), JJ (adjective)
- Link NLP tasks to real-world applications like Google Translate, sentiment analysis on reviews
- Contrast Bag-of-Words simplicity with Word Embeddings' superior semantic representation
