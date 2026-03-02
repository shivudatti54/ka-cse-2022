# Natural Language Processing (NLP) Basics

## 1. Introduction to Natural Language Processing

Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) and computational linguistics concerned with enabling computers to understand, interpret, and generate human language in a valuable way. The ultimate goal of NLP is to break down the barrier of human-computer interaction, allowing machines to process and "make sense" of the vast amounts of natural language data available.

### 1.1. Challenges in NLP

The challenge of NLP lies in the inherent ambiguity and complexity of human language. For example, the word "bank" can mean a financial institution or the side of a river. Resolving this ambiguity requires context, which is a non-trivial task for a machine.

## 2. The NLP Pipeline: From Raw Text to Understanding

Most NLP tasks follow a standard pipeline of processing steps to transform raw, unstructured text into a structured form that a machine can analyze.

```
Raw Text -> Tokenization -> Stop Word Removal -> Stemming/Lemmatization -> POS Tagging -> Parsing -> Feature Extraction -> ML/NLP Model -> Output
```

### 2.1. Tokenization

This is the first step, where a stream of text is broken down into smaller units called tokens. These tokens are usually words, numbers, or punctuation marks.

- **Example:** The sentence "I don't like NLP." might be tokenized into: `['I', 'do', "n't", 'like', 'NLP', '.']`
- **Challenges:** Handling contractions (e.g., "don't" vs. "do not") and compound words (e.g., "New York") can be complex.

### 2.2. Stop Word Removal

Stop words are common words that appear frequently but often carry less meaningful information (e.g., "the", "is", "at", "which"). Removing them helps reduce the dataset's dimensionality and focuses processing on more important words.

- **Example:** "The quick brown fox jumps over the lazy dog" becomes "quick brown fox jumps lazy dog".

### 2.3. Stemming and Lemmatization

These are text normalization techniques that reduce words to their base or root form.

- **Stemming:** A crude heuristic process that chops off the ends of words to achieve this goal. It often creates non-real words.
- Example: "jumps", "jumping", "jumped" -> `jump`
- Example: "running", "runner", "ran" -> `run`
- **Lemmatization:** A more sophisticated process that uses a vocabulary and morphological analysis to return the base or dictionary form of a word, known as the lemma.
- Example: "better" -> `good` (Stemming would return `better`)
- Example: "was" -> `be`

**Table: Stemming vs. Lemmatization**

| Feature      | Stemming                      | Lemmatization                            |
| :----------- | :---------------------------- | :--------------------------------------- |
| **Method**   | Rule-based, heuristic         | Dictionary-based, morphological analysis |
| **Output**   | Stem (may not be a real word) | Lemma (always a real word)               |
| **Speed**    | Fast                          | Slower                                   |
| **Accuracy** | Less accurate                 | More accurate                            |
| **Context**  | Does not consider context     | Can consider part-of-speech              |

### 2.4. Part-of-Speech (POS) Tagging

This involves assigning a grammatical category (noun, verb, adjective, etc.) to each token in a sentence. This is crucial for understanding the grammatical structure and meaning.

- **Example:** "The/DT quick/JJ brown/JJ fox/NN jumps/VBZ over/IN the/DT lazy/JJ dog/NN ./." (DT=Determiner, JJ=Adjective, NN=Noun, VBZ=Verb, IN=Preposition)

## 3. Syntactic and Semantic Analysis

### 3.1. Syntactic Analysis (Parsing)

This step involves analyzing the grammatical structure of a sentence to establish relationships between words. It creates a parse tree that represents the sentence's structure.

**Example Parse Tree for "The cat sat on the mat":**

```
S
/ | \
NP VP .
/ | | \
DT NN V PP
| | | | \
The cat sat on NP
/ | \
DT NN
the mat
```

(S = Sentence, NP = Noun Phrase, VP = Verb Phrase, PP = Prepositional Phrase)

### 3.2. Semantic Analysis

This is the task of extracting the literal, dictionary meaning from text. It goes beyond grammar to understand the meaning of words and how they combine to form sentence meaning. This involves tasks like:

- **Word Sense Disambiguation (WSD):** Determining which sense of a word is used in a sentence (e.g., "bank" as a financial institution vs. a river bank).
- **Named Entity Recognition (NER):** Identifying and classifying named entities into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, etc.
- **Example:** "**Barack Obama** [PERSON] was born in **Hawaii** [LOCATION]."

## 4. Key NLP Tasks and Applications

NLP is not a single technology but a suite of technologies powering many modern applications.

**Table: Common NLP Tasks**

| Task                            | Description                                                                                        | Example Application                                 |
| :------------------------------ | :------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| **Sentiment Analysis**          | Determining the emotional tone or opinion (positive, negative, neutral) behind a body of text.     | Analyzing product reviews, social media monitoring. |
| **Machine Translation**         | Automatically translating text from one language to another.                                       | Google Translate, DeepL.                            |
| **Text Summarization**          | Producing a concise and fluent summary while preserving key information.                           | Summarizing news articles, legal documents.         |
| **Chatbots & Dialogue Systems** | Systems that can converse with a human in natural language.                                        | Customer service bots, Siri, Alexa.                 |
| **Information Retrieval**       | Finding material (usually documents) of an unstructured nature that satisfies an information need. | Web search engines (Google, Bing).                  |
| **Question Answering**          | Automatically answering questions posed by humans in a natural language.                           | IBM Watson, Amazon Alexa.                           |

## 5. Representing Words: From Bag-of-Words to Word Embeddings

For a machine to process text, words must be converted into numerical vectors. This is called word representation.

### 5.1. Bag-of-Words (BoW)

This is a simple and common method where a text is represented as a "bag" (multiset) of its words, disregarding grammar and word order but keeping multiplicity. Each document is a vector in a high-dimensional space, where each dimension represents a word from the vocabulary.

- **Limitation:** Loses all information about word order and context.

### 5.2. Word Embeddings (e.g., Word2Vec)

This is a more advanced technique where words are mapped to vectors of real numbers in a continuous vector space. The key idea is that semantically similar words are mapped to nearby points in this vector space.

- **Example:** In a well-trained embedding space, the vectors for `King - Man + Woman ≈ Queen`.
- **Advantage:** Captures semantic and syntactic relationships between words.

## 6. Exam Tips

1. **Understand the Pipeline:** Memorize the order of the NLP pipeline (Tokenization -> ... -> Parsing). Be able to explain what each step does and why it's important.
2. **Differentiate Stemming/Lemmatization:** Be prepared to explain the difference with clear examples. Remember that lemmatization is more accurate but requires more computational power.
3. **Interpret POS Tags:** You don't need to memorize every tag, but understand common ones like NN (noun), VB (verb), JJ (adjective). You should be able to interpret a tagged sentence.
4. **Know the Applications:** Link key NLP tasks (Sentiment Analysis, NER, Machine Translation) to their real-world applications. This is a common question.
5. **Contrast Representations:** Understand why Bag-of-Words is a simplistic model and how Word Embeddings offer a superior representation by capturing meaning.
