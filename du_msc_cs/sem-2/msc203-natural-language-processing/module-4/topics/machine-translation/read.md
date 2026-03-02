# Machine Translation

## Introduction
Machine Translation (MT) is the automated process of converting text from one natural language to another while preserving meaning. As a core task in Natural Language Processing, it bridges communication gaps in our globalized world and enables cross-lingual information access. Modern MT systems have evolved from rule-based approaches through statistical methods to today's neural architectures, achieving near-human performance in some domains.

The importance of MT extends beyond basic translation tasks. It underpins multilingual chatbots, real-time interpretation systems, and cross-lingual information retrieval. Current research focuses on low-resource languages, domain adaptation, and handling linguistic phenomena like morphology and syntax divergence. The University of Delhi's focus on computational linguistics makes this particularly relevant for MSc CS students working with India's multilingual context.

Recent breakthroughs like transformer architectures and zero-shot translation have revolutionized the field. However, challenges remain in handling language pairs with different syntactic structures (e.g., English-Hindi), preserving stylistic elements, and managing rare words. These challenges make MT an active research area with opportunities for theoretical contributions and practical implementations.

## Key Concepts
1. **Statistical Machine Translation (SMT)**: 
   - Based on noisy-channel model: P(target|source) ∝ P(source|target)P(target)
   - Phrase-based translation using parallel corpora
   - Challenges in reordering and alignment

2. **Neural Machine Translation (NMT)**:
   - Sequence-to-sequence models with encoder-decoder architecture
   - Attention mechanisms (Bahdanau, Transformer)
   - Subword tokenization (BPE, WordPiece)

3. **Evaluation Metrics**:
   - BLEU (n-gram precision with brevity penalty)
   - TER (edit distance-based)
   - METEOR (incorporating synonyms and stemming)

4. **Advanced Architectures**:
   - Transformer models with self-attention
   - Multilingual NMT using shared embeddings
   - Pretrained models (mBART, mT5)

5. **Linguistic Challenges**:
   - Morphological richness (e.g., Hindi verb conjugations)
   - Syntax divergence (SOV vs SVO structures)
   - Discourse-level coherence

## Examples

**Example 1: Phrase-Based SMT**
Problem: Translate "The cat sat on the mat" to Hindi using phrase table:
| Source Phrase | Target Phrase | Probability |
|---------------|---------------|-------------|
| the cat       | बिल्ली        | 0.8         |
| sat on        | पर बैठी       | 0.7         |

Solution:
1. Segment into phrases: [The cat] [sat on] [the mat]
2. Lookup translations: बिल्ली + पर बैठी + चटाई
3. Reorder for Hindi SOV structure: बिल्ली चटाई पर बैठी
4. Add determiners: बिल्ली चटाई पर बैठी (Hindi drops articles)

**Example 2: Attention in NMT**
Problem: Visualize attention weights for English-French translation of "Hello world → Bonjour le monde"

Steps:
1. Encoder processes source tokens
2. Decoder generates "Bonjour" while attending strongly to "Hello"
3. When generating "le", attention spreads between "world" and null
4. Final output shows diagonal attention pattern characteristic of aligned languages

**Example 3: BLEU Calculation**
Candidate: "the the the the the"
Reference: "The cat is on the mat"

Calculation:
1. Precision: 5/5 (unigram), 0/4 (bigram)
2. Brevity penalty: e^(1 - 5/6) ≈ 0.846
3. BLEU = 0.846 * exp(0.5*ln(5/5) + 0.5*ln(0/4)) = 0

## Exam Tips
1. Always compare SMT vs NMT architectures with specific technical differences
2. When drawing attention matrices, label axes clearly (encoder/decoder steps)
3. Memorize BLEU formula components: modified n-gram precision + brevity penalty
4. For Hindi-English examples, mention specific challenges like compound verbs
5. Discuss both automatic metrics and human evaluation trade-offs
6. Prepare transformer architecture diagram with self-attention blocks
7. Link MT challenges to India's linguistic diversity in answers

Length: 1500-3000 words, MSc CS (research-oriented) postgraduate level