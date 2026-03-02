# Morphological Parsing

## Introduction to Morphology

Morphology is the branch of linguistics that studies the internal structure of words and the rules by which words are formed. In Natural Language Processing (NLP), **Morphological Parsing** is the process of analyzing a word to break it down into its constituent morphemes and determine its morphological structure. A morpheme is the smallest meaningful unit in a language. For example, the word "unhappiness" can be broken down into three morphemes: the prefix `un-` (meaning 'not'), the root `happy`, and the suffix `-ness` (meaning 'state of').

This process is crucial for NLP tasks because it helps in understanding the meaning and grammatical properties of words, which is foundational for syntactic analysis, machine translation, information retrieval, and more.

## Basic Concepts in Morphology

### Morphemes: The Building Blocks

Morphemes are categorized into two main types:

1.  **Stem/Root:** The core meaning-bearing unit of a word (e.g., `play` in `playing`, `replay`).
2.  **Affixes:** Morphemes that are attached to a stem. They are further subdivided:
    - **Prefix:** Added to the beginning of a stem (e.g., `re-` in `rewrite`).
    - **Suffix:** Added to the end of a stem (e.g., `-ed` in `walked`).
    - **Infix:** Inserted within a stem (common in some languages like Tagalog, but rare in English).
    - **Circumfix:** A combination of a prefix and a suffix that together signify a meaning (e.g., `ge-` + `-t` in German `gespielt` -> 'played').

### Types of Morphological Processes

- **Inflection:** Modifies a word to express different grammatical categories such as tense, case, voice, aspect, person, number, gender, and mood without changing its core meaning or part-of-speech. For example:
  - `walk` -> `walks`, `walked`, `walking` (verb inflection)
  - `cat` -> `cats` (noun inflection)
- **Derivation:** Creates a new word with a new meaning and often a change in the lexical category (part-of-speech). For example:
  - `teach` (verb) -> `teacher` (noun)
  - `happy` (adjective) -> `unhappy` (adjective) -> `unhappiness` (noun)

### Orthographic Rules

Spelling changes often occur when morphemes are combined. These must be handled by a morphological parser.

- **Epsilon Insertion:** Sometimes a letter is dropped. (e.g., `make` + `-ing` -> `making`, not `makeing`).
- **E-Deletion:** The silent 'e' at the end of a word is often dropped before a vowel-initial suffix (e.g., `make` + `-ed` -> `made`).
- **Y-Replacement:** A 'y' at the end of a word often changes to 'i' before certain suffixes (e.g., `city` -> `cities`, `happy` -> `happiness`).
- **Doubling:** The final consonant of a word is sometimes doubled (e.g., `run` -> `running`, `big` -> `bigger`).

## Finite-State Automata (FSA) for Morphology

Finite-State Automata (FSA), introduced in the previous section of the syllabus, are a fundamental computational model used for morphological parsing. They are excellent for representing regular languages and are well-suited for modeling the concatenative nature of morphology.

A simple FSA can be designed to recognize a set of words. For instance, an FSA for recognizing English regular plural nouns might have states representing the reading of the stem and then the plural suffix.

### Example: FSA for Simple English Nouns

Let's design an FSA to recognize words like `cat`, `cats`, `dog`, `dogs`, `fox`, `foxes`.

```
States: q0, q1, q2 (q0 is start, q2 is final)
Alphabet: c, a, t, d, o, g, f, x, s, e

Transitions:
q0 --c--> q1
q0 --d--> q1
q0 --f--> q1
q1 --a--> q2  // for 'ca'
q1 --o--> q2  // for 'do'
q1 --o--> q1? // Let's correct this. We need a better structure.

A more accurate representation would have states for each character.
A better approach is to use a FSA that accepts the stem, then an optional plural suffix.
```

A more abstract FSA for noun pluralization:

```
         +------------------------+
         |                        |
         v  s                     | e+s
Start -> [Stem] -- (if ends with s,x,z,ch,sh) --> [Add -es]
         | \
         |  \ (otherwise)
         |   \
         |    --> [Add -s]
         |
         (if ends with 'y' after consonant) -> [Replace y with ies]
```

This is a simplification; a real FSA would have many more paths and states.

## Finite-State Transducers (FSTs)

While an FSA can _recognize_ whether a word is valid, a **Finite-State Transducer (FST)** is a more powerful tool that can both recognize and _analyze/generate_ a word. An FST is essentially an FSA with an output tape. It reads a string of input symbols and writes a string of output symbols.

In morphological parsing, an FST can:

- **Analyze:** Take a surface form (e.g., `cats`) and output its lexical form + features (e.g., `cat +N +PL`).
- **Generate:** Take a lexical form + features (e.g., `cat +N +PL`) and output the surface form (e.e., `cats`).

### Structure of an FST

An FST transition is labeled as `input:output`. The symbol `ε` (epsilon) represents an empty string (no input or output).

### Example: FST for English Plural Nouns

Let's build a simple FST that maps lexical forms to surface forms for plural nouns.

**Lexicon:** `reg-noun -> cat, dog, fox ...` (We'll assume a simple stem)

**Architecture:** We can cascade FSTs. First, a transducer spells the stem. Then, a separate transducer handles the morphological rules.

**Orthographic Rule FST (for adding -s):**
This FST must handle the spelling rules.

- Input: stem + `^s#`
- Output: surface form

For example, for `fox`:

- Input: `f o x ^ s #`
- Output: `f o x e s`

The FST would have states and transitions to check the final character of the stem and insert an `e` if needed.

```
States: q0 (start), q1, q2 (final)
# is an end-of-word marker.
^ indicates a morpheme boundary.

Example transitions for the 'insert e' rule:
q0 -- x:ε --> q1   // read 'x', output nothing yet, move to state q1.
q1 -- ^:ε --> q1   // read morpheme boundary, output nothing.
q1 -- s:e --> q2   // read 's', output 'e' first, then 's'.
q2 -- #:# --> q2   // read end-of-word, output end-of-word.

For a word like 'dog':
q0 -- d:d --> q0
q0 -- o:o --> q0
q0 -- g:g --> q0
q0 -- ^:ε --> q0
q0 -- s:s --> q2   // simply output 's'
q2 -- #:# --> q2
```

This is a highly simplified view. Real-world FSTs like those used in the Xerox tools are vastly more complex and powerful.

## The Role of Lexicon

A morphological parser is not complete without a **lexicon**—a database of all the stems (roots) and affixes of a language, along with their linguistic information (e.g., part-of-speech, gender). The parser consults the lexicon to validate stems and determine which affixes can legally attach to them.

For example, the lexicon entry for `play` would indicate it is a verb. The parser can then use this to know that `-ed` (past tense) and `-ing` (progressive) are valid inflectional suffixes, while `-ness` (which usually attaches to adjectives) is not.

## Morphological Parsing in Indian Languages

Indian languages, such as Hindi, Tamil, and Bengali, are highly inflectional and morphologically rich. They often exhibit **agglutinative** morphology, where words are formed by joining multiple morphemes together in a linear sequence, each contributing a distinct meaning.

**Challenges:**

- **High Morpheme-to-Word Ratio:** A single word can convey what takes multiple words in English.
  - Example (Hindi): "किताबें" (`kitaab` + `e` + `ṃ`) -> "books" (plural + definite marker).
- **Sandhi:** Phonological changes at morpheme boundaries are very common and complex.
- **Free Word Order:** The rich morphology often conveys grammatical relations, making word order more flexible than in English.

The **Paninian Framework**, mentioned in the syllabus, is a grammar model based on the ancient Indian linguist Panini. It is highly suitable for modeling Indian languages due to its sophisticated handling of morphology and morpho-phonemics (Sandhi). Morphological parsers for Indian languages often leverage this framework or are inspired by its principles.

## Applications of Morphological Parsing

1.  **Information Retrieval (IR):** Morphological parsing is the basis for **stemming** and **lemmatization**. Reducing words to their base form ("running", "runs" -> "run") improves recall by matching documents containing different inflections of a search term.
2.  **Machine Translation:** Correctly identifying the tense, number, and gender of a word in the source language is essential for generating the correct grammatical form in the target language.
3.  **Speech Processing:** Understanding morphology helps in predicting likely word sequences and generating correct pronunciations.
4.  **Spelling Error Detection and Correction:** A morphological parser can identify if a potentially misspelled word is a valid inflection of a known root.
5.  **Text-to-Speech Synthesis:** The parser determines the correct pronunciation of affixes and stems in context.

## Comparison: Stemming vs. Lemmatization vs. Full Morphological Parsing

| Feature            | Stemming                            | Lemmatization                | Full Morphological Parsing                  |
| :----------------- | :---------------------------------- | :--------------------------- | :------------------------------------------ |
| **Output**         | Crude stem (may not be a real word) | Base dictionary form (lemma) | Lemma + Full grammatical features           |
| **Awareness**      | Pattern-based, no context           | Uses vocabulary & morphology | Uses lexicon, morphology, and often context |
| **Complexity**     | Simple, fast (e.g., Porter Stemmer) | More complex, slower         | Most complex, slowest                       |
| **Example Input**  | "running"                           | "running"                    | "running"                                   |
| **Example Output** | "run"                               | "run" (verb)                 | "run +V +PresPart" or "run +V +Gerund"      |
| **Use Case**       | Quick-and-dirty IR                  | Accurate IR, Text Analysis   | Deep NLP, MT, Grammar Checking              |

## Exam Tips

- **Understand the Core Definitions:** Be able to define and distinguish between morpheme, stem, affix, inflection, and derivation. These are classic short answer questions.
- **Draw FSAs/FSTs:** Practice drawing simple Finite-State Automata and Transducers for given morphological rules (e.g., English past tense `-ed`). Label your states and transitions clearly.
- **Explain with Examples:** When asked to explain a concept like "orthographic rules," always provide clear examples (e.g., `make` + `ing` = `making`).
- **Compare and Contrast:** Be prepared to write a paragraph comparing stemming, lemmatization, and full parsing in terms of their goals, methods, and applications.
- **Think About Indian Languages:** Relate the topic back to the challenges of processing morphologically rich languages like Hindi. Mention the Paninian framework as a relevant solution.
- **Know the Applications:** Link morphological parsing to other parts of the syllabus (IR, MT, Text Classification). This shows a integrated understanding of NLP.
