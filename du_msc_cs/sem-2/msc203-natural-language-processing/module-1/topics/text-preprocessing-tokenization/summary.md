# Text Preprocessing and Tokenization - Summary

## Key Definitions and Concepts

- **Token**: A discrete unit of text extracted during the tokenization process; can be a word, subword, character, or sentence
- **Tokenization**: The process of segmenting text into tokens, forming the first step in most NLP pipelines
- **Word Tokenization**: Splitting text into words based on whitespace and punctuation boundaries
- **Subword Tokenization**: Decomposing words into meaningful subword units (morphemes) to handle OOV words; includes BPE, WordPiece, and Unigram methods
- **Text Normalization**: Transforming text to a standard form through case folding, accent removal, stemming, or lemmatization

## Important Formulas and Concepts

- **BPE Merge Operations**: Iteratively merges most frequent adjacent character pairs in training corpus to build vocabulary
- **Maximum Matching**: Greedy algorithm segmenting text into longest dictionary matches (FMM: left-to-right, BMM: right-to-left)
- **Vocabulary Size Trade-off**: Larger vocabularies → better representation but more parameters; smaller vocabularies → better generalization but longer sequences

## Key Points

1. Tokenization is the foundational step in NLP; quality of tokenization directly impacts downstream task performance
2. English tokenization is relatively straightforward; challenge increases for morphologically rich and space-delimited languages
3. Subword tokenization (BPE, WordPiece) solves the OOV problem inherent in word-level tokenization
4. Text normalization must be chosen based on task requirements—stemming is aggressive while lemmatization preserves semantic meaning
5. Regular expressions provide fine-grained control for complex tokenization patterns
6. Modern transformer models use pre-trained subword tokenizers (e.g., BERT uses WordPiece, GPT uses BPE)
7. Chinese and Japanese require word segmentation rather than simple boundary detection
8. Noisy text from social media requires specialized tokenization approaches
9. Sentence tokenization faces challenges from abbreviations and ellipsis
10. Tokenization choices affect sequence length, memory usage, and computational efficiency

## Common Mistakes to Avoid

- Treating all tokenizers as equivalent—they differ significantly in handling edge cases
- Applying case normalization universally when sentiment or named entity information matters
- Using stemming when lemmatization would preserve needed semantic information
- Ignoring language-specific tokenization requirements
- Overlooking the impact of tokenization on downstream model performance

## Revision Tips

1. Practice implementing different tokenization approaches on sample texts to understand their outputs
2. Memorize the differences between stemming algorithms (Porter, Snowball) and lemmatization approaches
3. Review how tokenization integrates with modern language models in the Hugging Face ecosystem
4. Solve previous year DU examination questions on tokenization to understand exam patterns
5. Study the impact of tokenization choices on specific NLP tasks like POS tagging and NER