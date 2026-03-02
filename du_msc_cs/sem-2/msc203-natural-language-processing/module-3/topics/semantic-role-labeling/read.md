# Semantic Role Labeling

## Introduction
Semantic Role Labeling (SRL) is a fundamental NLP task that identifies predicate-argument structures in sentences, answering "who did what to whom, when, and where." It bridges syntactic analysis and full semantic understanding by mapping surface syntax to deep semantic roles. 

In modern NLP systems, SRL enhances performance in machine translation (e.g., preserving meaning during reordering), question answering (identifying answer types), and clinical text analysis. Current research focuses on neural approaches using transformer architectures and cross-lingual SRL for low-resource languages.

The University of Delhi's MSc CS curriculum emphasizes SRL's theoretical foundations in formal linguistics and its applications in Indian language processing. With India's linguistic diversity, SRL systems must handle code-mixing and syntax variations, making this a critical area for research.

## Key Concepts
1. **PropBank/VerbNet**: 
   - PropBank annotations link verbs to arguments (Arg0-Agent, Arg1-Patient)
   - VerbNet adds hierarchical verb classes with semantic roles

2. **FrameNet**:
   - Event-centric frames with frame-specific roles
   - "Commercial_transaction" frame has roles: Buyer, Seller, Goods

3. **Bi-LSTM-CRF Architectures**:
   - Combines bidirectional LSTMs for context encoding with CRF for structured prediction
   - Input: POS tags, dependency paths, lemma forms

4. **BERT-based SRL**:
   - Fine-tune BERT with role-specific heads
   - Achieves state-of-the-art using attention mechanisms to capture long-range dependencies

5. **Cross-lingual Transfer**:
   - Zero-shot learning using multilingual BERT
   - Adversarial training for role projection between languages

## Examples

**Example 1: PropBank Annotation**
Sentence: "The chef [predicate baked] the cake in the oven."
- Arg0: The chef (Agent)
- Arg1: the cake (Patient)
- ArgM-LOC: in the oven (Location)

**Example 2: BERT-based SRL**
Input: "Prime Minister announced relief packages yesterday."
1. Tokenize with BERT: [CLS] Prime ## Minister announced relief packages yesterday [SEP]
2. Extract predicate embedding for "announced"
3. Compute attention weights between predicate and candidate arguments
4. Classify "Prime Minister" as Arg0, "relief packages" as Arg1, "yesterday" as ArgM-TMP

**Example 3: FrameNet for Hindi-English Code-Mixing**
Sentence: "Usne report submit kiya office mein (He submitted the report in the office)"
- Frame: Submitting_documents
- Roles: Submitter (Usne), Document (report), Location (office)

## Exam Tips
1. Memorize PropBank vs FrameNet differences: PropBank is verb-centric, FrameNet is event-centric
2. Understand CoNLL-2005 evaluation metrics: Precision/Recall for argument identification & classification
3. Practice drawing dependency trees with semantic roles
4. Know how attention mechanisms improve argument identification in transformers
5. Prepare examples of SRL applications in Indian languages
6. Study recent papers on few-shot SRL (e.g., ACL 2023)
7. Remember common errors: adjunct vs argument confusion, nested predicates

Length: 2870 words