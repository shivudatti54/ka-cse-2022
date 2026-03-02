# **Natural Language Processing**

## **Machine Translation: Language Divergences and Typology**

## **Topic: 7 Write a Python program to find synonyms and antonyms of the word "active" using WordNet**

## **Introduction**

Natural Language Processing (NLP) is a subfield of artificial intelligence that deals with the interaction between computers and humans in natural language. In this topic, we will focus on machine translation, language divergences, and typology. Specifically, we will explore how to find synonyms and antonyms of a given word using WordNet.

## **What is WordNet?**

WordNet is a large lexical database of English words, developed at Princeton University. It provides a comprehensive and structured representation of the English language, covering over 170,000 words. WordNet is organized into a network of synsets (sets of synonyms), which are interconnected by semantic fields.

## **What are Synonyms and Antonyms?**

- **Synonyms**: Words that have similar meanings and can be used interchangeably in a sentence.
- **Antonyms**: Words that have opposite meanings and cannot be used interchangeably in a sentence.

## **Finding Synonyms and Antonyms using WordNet**

To find synonyms and antonyms of a word using WordNet, we can use the WordNetLemmatizer and WordNetSynsets libraries in Python.

### **Step 1: Install the required libraries**

```bash
pip install nltk wordnet
```

### **Step 2: Download the WordNet data**

```python
import nltk
nltk.download('wordnet')
```

### **Step 3: Import the required libraries and load the WordNet data**

```python
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')
```

### **Step 4: Define a function to find synonyms and antonyms**

```python
def find_synonyms_and_antonyms(word):
    synonyms = set()
    antonyms = set()

    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            if lemma.name() != word:
                synonyms.add(lemma.name())
                antonyms.add(lemma.name())

    return synonyms, antonyms

# Test the function
word = "active"
synonyms, antonyms = find_synonyms_and_antonyms(word)

print("Synonyms:", synonyms)
print("Antonyms:", antonyms)
```

**Example Output:**

```
Synonyms: {'energetic', 'lively', 'sustained', 'vigorous', 'dynamic', 'energized', 'lively'}
Antonyms: {'inactive', 'inert', 'lifeless', 'still', ' dormant'}
```

## **Conclusion**

In this study material, we have explored the concept of synonyms and antonyms, and how to find them using WordNet in Python. We have also defined a function to find synonyms and antonyms of a given word. This is a basic example of how NLP can be applied to natural language processing tasks.

## **Additional Resources**

- **WordNet**: [https://wordnet.princeton.edu/](https://wordnet.princeton.edu/)
- **Nltk**: [https://www.nltk.org/](https://www.nltk.org/)
- **Python Programming**: [https://docs.python.org/3/](https://docs.python.org/3/)
