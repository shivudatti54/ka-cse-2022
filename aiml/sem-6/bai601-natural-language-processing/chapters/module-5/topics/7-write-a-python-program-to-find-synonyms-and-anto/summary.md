# **Revision Notes: Finding Synonyms and Antonyms of "Active" using WordNet**

## **Introduction**

- Natural Language Processing (NLP) module
- Focus on Machine Translation: Language Divergences and Typology
- Topic 7: Write a Python program to find synonyms and antonyms of the word "active" using WordNet

## **Key Points**

- **WordNet**: a lexical database of English words
- **Synonyms**: words with similar meanings
- **Antonyms**: words with opposite meanings
- **Python program**: to find synonyms and antonyms of the word "active" using WordNet

## **WordNet API**

- `wn.synsets('active')`: returns a list of synsets (sets of synonyms) for the word "active"
- `wn.lemmas('active')`: returns a list of lemmas (base forms of words) for the word "active"

## **Finding Synonyms**

- Use `wn.synsets('active')` to get a list of synsets
- Use `wn.lemmas('active')` to get a list of lemmas
- Use `wn.synsets('active')[0].lemmas()` to get a list of synonyms

## **Finding Antonyms**

- Use `wn.synsets('active')` to get a list of synsets
- Use `wn.synsets('active')[0].antonyms()` to get a list of antonyms

**Python Code**

```python
import nltk
from nltk.corpus import wordnet

# Load the WordNet corpus
nltk.download('wordnet')

# Define a function to find synonyms
def find_synonyms(word):
    synsets = wordnet.synsets(word)
    lemmas = synsets[0].lemmas()
    synonyms = [lemma.name() for lemma in lemmas if lemma.antonyms()]
    return synonyms

# Define a function to find antonyms
def find_antonyms(word):
    synsets = wordnet.synsets(word)
    antonyms = synsets[0].antonyms()
    return [antonym.name() for antonym in antonyms]

# Find synonyms and antonyms of the word "active"
synonyms = find_synonyms('active')
antonyms = find_antonyms('active')

print("Synonyms:", synonyms)
print("Antonyms:", antonyms)
```

**Note**: Make sure to install the necessary libraries and download the WordNet corpus before running the code.
