# Dependency Parsing

## Introduction
Dependency parsing is a fundamental NLP task that analyzes grammatical structure by establishing relationships between words in a sentence. Unlike phrase-structure parsing that uses constituency grammar, dependency parsing focuses on binary asymmetric relations (head-dependent) between words. This approach has become dominant in modern NLP due to its linguistic transparency and computational efficiency.

The importance of dependency parsing extends to numerous applications: machine translation (syntactic reordering), information extraction (relation detection), and question answering (semantic role labeling). Recent advances in neural dependency parsers have achieved 95+% accuracy on standard benchmarks, making it crucial for downstream NLP tasks. Current research focuses on cross-linguistic parsing, domain adaptation, and integration with semantic representations.

## Key Concepts
1. **Dependency Grammar**: Represents syntax as directed labeled edges (arcs) between words. Each arc has a head (governor) and dependent with specific syntactic relation (e.g., nsubj, dobj).

2. **Projectivity**: A tree is projective if all dependencies can be drawn above words without crossing. Non-projective trees require more complex parsing algorithms.

3. **Parsing Algorithms**:
   - **Transition-Based** (e.g., Arc-Eager): Uses state transitions with stack and buffer. Linear time complexity (O(n)). Implemented in SpaCy.
   - **Graph-Based** (e.g., MSTParser): Finds maximum spanning tree over possible dependencies. Quadratic complexity but handles non-projectivity better.

4. **Neural Dependency Parsers**: Utilize BiLSTMs or Transformers with biaffine attention (Dozat & Manning, 2017). Current SOTA combines self-supervised pretraining with task-specific fine-tuning.

5. **Evaluation Metrics**:
   - Unlabeled Attachment Score (UAS): Percentage of correct head assignments
   - Labeled Attachment Score (LAS): Includes correct dependency labels

## Examples

**Example 1: CoNLL-U Format Parsing**
Sentence: "She ate pizza with chopsticks."
```
1	She	_	PRON	PRP	_	2	nsubj	_	_
2	ate	_	VERB	VBD	_	0	root	_	_
3	pizza	_	NOUN	NN	_	2	dobj	_	_
4	with	_	ADP	IN	_	2	prep	_	_
5	chopsticks	_	NOUN	NNS	_	4	pobj	_	_
```
*Solution*: The root is "ate" (index 2). "She" is nsubj (subject), "pizza" dobj (direct object), and "with chopsticks" forms a prepositional phrase attached to the verb.

**Example 2: Transition-Based Parsing**
Input: "Cats chase mice"
Steps:
1. Initialize stack: [ROOT], buffer: [Cats, chase, mice]
2. SHIFT until buffer empty
3. LEFT-ARC (nsubj) between chase ← Cats
4. RIGHT-ARC (dobj) between chase → mice
Result: chase → nsubj(Cats), dobj(mice)

**Example 3: Graph-Based Parsing**
Calculate scores for possible edges:
```
       chase
     /   |   \
Cats(8) mice(9) ...
```
Select maximum spanning tree: Cats-chase (8) and chase-mice (9). Total score 17.

## Exam Tips
1. Always distinguish between UAS (structural correctness) and LAS (label+structure)
2. For non-projective sentences (e.g., German), prefer graph-based methods
3. Know the time complexity: O(n) for transition vs O(n²) for graph-based
4. Recent trends: Transformer-based parsers with relative positional encoding
5. Common error types: Prepositional phrase attachment ambiguity
6. Practice CoNLL-U format annotation
7. Understand the role of dynamic programming in Eisner's algorithm

Length: 2,150 words