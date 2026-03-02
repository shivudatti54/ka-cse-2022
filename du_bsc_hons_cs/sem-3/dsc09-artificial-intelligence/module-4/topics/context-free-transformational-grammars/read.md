# Context Free Transformational Grammars

## A Comprehensive Study Material for BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

### 1.1 What are Context-Free Transformational Grammars?

**Context-Free Transformational Grammars (CFTGs)** represent a powerful extension of classical Context-Free Grammars (CFGs) that incorporate **transformational rules** to capture systematic relationships between different sentence structures. Originally proposed by Noam Chomsky in the 1950s-1960s as part of his transformational-generative grammar framework, CFTGs have become fundamental to understanding how human language works and have found extensive applications in Artificial Intelligence, particularly in Natural Language Processing (NLP).

A **Context-Free Grammar** is a formal grammar where the left-hand side of each production rule consists of a single non-terminal symbol. While CFGs are excellent for describing the hierarchical structure of sentences through parse trees, they struggle to express relationships between different syntactic structures that share semantic content. This is where transformational grammars bridge the gap.

### 1.2 Real-World Relevance

Transformational grammars power many modern AI applications:

- **Machine Translation Systems**: Google Translate, DeepL, and other MT systems use transformational rules to map source language structures to target language structures
- **Speech Assistants**: Siri, Alexa, and Google Assistant use transformational grammars to parse and understand user commands
- **Text Generation**: AI writing assistants use transformational rules to rephrase and improve text
- **Information Extraction**: Extracting structured data from unstructured text
- **Question Answering Systems**: Transforming user queries into database queries

### 1.3 Delhi University Syllabus Context

This topic aligns with the **Artificial Intelligence** paper under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science, specifically covering formal grammar foundations, language processing, and AI applications. Students are expected to understand both theoretical foundations and practical implementations.

---

## 2. Theoretical Foundations

### 2.1 Context-Free Grammars (CFGs) - A Quick Review

A Context-Free Grammar G is defined as a 4-tuple:

```
G = (V, Σ, R, S)
```

Where:
- **V**: Finite set of non-terminal symbols (variables)
- **Σ**: Finite set of terminal symbols (alphabet)
- **R**: Finite set of production rules of the form A → α, where A ∈ V and α ∈ (V ∪ Σ)*
- **S**: Start symbol (S ∈ V)

**Example CFG for simple English sentences:**

```
S → NP VP
NP → Det N | NP PP
VP → V | V NP | VP PP
PP → P NP
Det → a | the
N → cat | dog | person
V → sees | likes | walks
P → in | with | on
```

This CFG can generate sentences like:
- "the cat sees a dog"
- "the person walks in the park"

### 2.2 The Need for Transformational Grammars

While CFGs can generate sentences, they cannot easily express:
1. **Paraphrase relationships**: "The cat was seen by the dog" and "The dog saw the cat" share meaning but have different structures
2. **Question formation**: The relationship between "She reads the book" and "Does she read the book?"
3. **Passive voice**: The relationship between active and passive constructions
4. **Sentence embedding**: "John believes [that Mary left]" vs. "John believes Mary left"

CFGs treat each sentence structure as independent. Transformational grammars capture the **systematic transformations** that relate these structures.

---

## 3. Context-Free Transformational Grammars: Formal Definition

### 3.1 Definition

A **Context-Free Transformational Grammar** is a 6-tuple:

```
T = (V, Σ, R, S, T_R, ⊢)
```

Where:
- **(V, Σ, R, S)**: A base Context-Free Grammar (as defined above)
- **T_R**: A finite set of **transformational rules**
- **⊢**: A relation defining the application of transformations

### 3.2 Components of a Transformational Grammar

#### The Base Grammar (Deep Structure)
The base CFG generates **deep structures** - abstract representations that capture the semantic content of sentences. These are sometimes called **kernel sentences** or **D-structures** in Chomskyan terminology.

#### Transformational Rules
Transformational rules are operations that map one structure to another. They are typically written as:

```
X → Y / A _ B / C _ D
```

Meaning: Transform X to Y when A precedes a position and B follows it, with context C before and D after.

Modern notation simplifies this to condition-action rules:
```
[Structure] → [Transformed Structure] [Conditions]
```

#### Surface Structure
The output after applying transformational rules is called the **surface structure** (S-structure), which is what we actually hear or read.

---

## 4. Types of Transformational Rules

### 4.1 Movement Transformations

Movement transformations relocate elements within a sentence structure.

#### 4.1.1 Wh-Movement (Question Formation)

**Transform**: Declarative → Interrogative

```
Rule: Wh-Movement
Input:  [CP C [TP Subject T [VP V Object]]]
Output: [CP Wh-word [TP t Subject T [VP V t Object]]]
```

**Example**:
- Deep: "She reads the book"
- Surface: "What does she read?"

```python
# Simplified Wh-Movement Transformation in Python

class TransformRule:
    def __init__(self, name, input_pattern, output_transform):
        self.name = name
        self.input_pattern = input_pattern
        self.output_transform = output_transform
    
    def apply(self, tree):
        """Apply transformation to a parse tree"""
        if self.matches(tree):
            return self.transform(tree)
        return tree
    
    def matches(self, tree):
        return tree.type == self.input_pattern
    
    def transform(self, tree):
        # Move wh-word to front, add auxiliary inversion
        pass

class WhMovement(TransformRule):
    def __init__(self):
        super().__init__(
            "Wh-Movement",
            "declarative",
            self.wh_transform
        )
    
    def wh_transform(self, tree):
        """
        Transform: S → Wh-question
        Input:  [S [NP She] [VP reads [NP the book]]]
        Output: [Q [NP What] [Aux does] [NP she] [VP read t]]
        """
        # Extract wh-phrase from object position
        wh_phrase = tree.find_noun_phrase_in_vp()
        
        # Create question structure with movement
        question = QuestionTree()
        question.add_wh_element(wh_phrase)
        question.add_auxiliary("does")
        question.add_subject(tree.get_subject())
        question.add_verb_phrase(tree.get_verb_phrase_without_object())
        question.add_trace(wh_phrase)  #留下 trace
        
        return question

# Demonstration
def demo_wh_movement():
    # Parse tree for "She reads the book"
    declarative = Tree("S")
    declarative.add_child(Tree("NP", [Tree("She")]))
    vp = Tree("VP")
    vp.add_child(Tree("V", ["reads"]))
    vp.add_child(Tree("NP", [Tree("the"), Tree("book")]))
    declarative.add_child(vp)
    
    print("Input (Deep Structure):")
    print(declarative)
    
    # Apply Wh-Movement
    transformer = WhMovement()
    question = transformer.apply(declarative)
    
    print("\nOutput (Surface Structure):")
    print("What does she read?")

demo_wh_movement()
```

#### 4.1.2 Passive Transformation

**Transform**: Active → Passive

```
Rule: Passive
Input:  [VP V [NP Object]]
Output: [VP was V [PP by [NP Subject]]]
```

**Example**:
- Deep: "The dog saw the cat"
- Surface: "The cat was seen by the dog"

```python
class PassiveTransformation(TransformRule):
    """
    Implements Passive Voice Transformation
    Deep Structure: [NP1] [VP V NP2]
    Surface Structure: [NP2] [VP was V by NP1]
    """
    
    def __init__(self):
        super().__init__("Passive", "active", self.make_passive)
    
    def make_passive(self, tree):
        """
        Transform active voice to passive voice
        
        Input:  [S [NP The dog] [VP saw [NP the cat]]]
        Output: [S [NP The cat] [VP was seen by [NP the dog]]]
        """
        # Extract subject and object
        subject = tree.get_child("NP")  # The dog
        verb_phrase = tree.get_child("VP")
        verb = verb_phrase.get_verb()   # saw
        direct_object = verb_phrase.get_object()  # the cat
        
        # Create passive structure
        passive = Tree("S")
        
        # Move object to subject position
        passive.add_child(Tree("NP", direct_object.leaves))
        
        # Create new VP with "be" + past participle
        new_vp = Tree("VP")
        new_vp.add_child(Tree("Aux", ["was"]))
        new_vp.add_child(Tree("V", [self.to_past_participle(verb)]))
        
        # Add "by" phrase with original subject
        pp = Tree("PP")
        pp.add_child(Tree("P", ["by"]))
        pp.add_child(Tree("NP", subject.leaves))
        new_vp.add_child(pp)
        
        passive.add_child(new_vp)
        return passive
    
    def to_past_participle(self, verb):
        """Convert verb to past participle"""
        # Simple demonstration - real implementation needs irregular verbs
        irregular = {
            'saw': 'seen',
            'ate': 'eaten',
            'wrote': 'written',
            'broke': 'broken'
        }
        return irregular.get(verb, verb + "ed")

# Demonstration
def demo_passive_transformation():
    # Input: "The dog saw the cat"
    active = Tree("S")
    active.add_child(Tree("NP", ["The", "dog"]))
    vp = Tree("VP")
    vp.add_child(Tree("V", ["saw"]))
    vp.add_child(Tree("NP", ["the", "cat"]))
    active.add_child(vp)
    
    print("Input (Active Voice):")
    print("The dog saw the cat")
    
    transformer = PassiveTransformation()
    passive = transformer.apply(active)
    
    print("\nOutput (Passive Voice):")
    print("The cat was seen by the dog")
    print("\nParse Tree:")
    print(passive)

demo_passive_transformation()
```

### 4.2 Substitution Transformations

Substitution transformations replace one element with another while maintaining grammaticality.

#### 4.2.1 Auxiliary Replacement

```
Rule: Auxiliary Insertion/Deletion
Transform: Question formation requires auxiliary movement
```

#### 4.2.2 Pronoun Replacement

```
Rule: Pronominalization
Input:  [NP John] and [NP John]
Output: [NP John] and [NP he]
```

### 4.3 Deletion and Insertion Transformations

#### 4.3.1 Imperative Formation

```
Rule: Imperative
Input:  [TP you [VP go]]
Output: [ImpP go]
```

#### 4.3.2 Complementizer Deletion

```
Rule: That-Deletion
Input:  [CP that [TP he left]]
Output: [CP he left]
```

Example:
- "I believe that he is honest" → "I believe he is honest"

### 4.4 Identity Transformations (Null Operations)

Some transformations don't change structure but verify constraints:
- **Constraints on Movement**: Specific rules about what can move where
- **Bounding Theory**: Limits on how far elements can move
- **Case Theory**: Ensures nouns appear in appropriate positions

---

## 5. Formal Properties of Transformational Rules

### 5.1 Structure Preservation

Transformations should preserve the **linguistic content** while changing structure:

1. **θ-role preservation**: The thematic roles (agent, patient, theme, etc.) remain constant
2. **Argument structure**: The number and type of arguments remains the same
3. **Semantic content**: The meaning (apart from focus/presupposition) is preserved

### 5.2 The Projection Principle

Transformations cannot delete or add required elements:
- All transformations apply to complete structures
- Lexical items must have their θ-roles satisfied

### 5.3 Conditions on Transformations

1. **Subjacency**: Movement cannot cross more than one bounding node (typically IP, NP)
2. **Left Branch Condition**: Cannot extract from within a left-branching node
3. **Specified Subject Condition**: Cannot extract from a subject position under certain conditions

---

## 6. Applications in Artificial Intelligence

### 6.1 Natural Language Processing

#### 6.1.1 Syntactic Parsing

Transformational grammars help parsers generate multiple possible structures:

```python
class TransformationalParser:
    """
    Parser that uses transformational grammar for sentence analysis
    """
    
    def __init__(self, base_grammar, transformations):
        self.grammar = base_grammar
        self.transformations = transformations
    
    def parse(self, sentence):
        # Step 1: Generate deep structure
        deep_structure = self.grammar.generate(sentence)
        
        # Step 2: Apply transformations in order
        surface_structure = deep_structure
        for transform in self.transformations:
            surface_structure = transform.apply(surface_structure)
        
        return {
            'deep': deep_structure,
            'surface': surface_structure,
            'transformations_applied': self.get_trace()
        }

# Usage
grammar = CFG.from_rules(sentence_grammar_rules)
transformations = [
    WhMovement(),
    PassiveTransformation(),
    ComplementizerDeletion()
]
parser = TransformationalParser(grammar, transformations)
result = parse("What was seen by the dog")
```

#### 6.1.2 Sentence Generation

For text generation, transformations can produce varied output:

```python
class GrammaticalVarietyGenerator:
    """
    Generate multiple surface forms from a single deep structure
    """
    
    def __init__(self):
        self.transformations = {
            'passive': PassiveTransformation(),
            'question': WhMovement(),
            'negative': NegationTransformation(),
            'imperative': ImperativeTransformation()
        }
    
    def generate_varieties(self, deep_structure):
        """
        Input: Deep structure [The dog see the cat]
        Output: Multiple surface structures showing grammatical variety
        """
        varieties = {}
        
        # Original (active declarative)
        varieties['active_declarative'] = deep_structure
        
        # Passive
        varieties['passive'] = self.transformations['passive'].apply(deep_structure)
        
        # Question (wh)
        varieties['wh_question'] = self.transformations['question'].apply(deep_structure)
        
        # Yes/No question (requires auxiliary insertion)
        varieties['yes_no_question'] = self.transformations['aux_inversion'].apply(deep_structure)
        
        return varieties

# Demonstration
generator = GrammaticalVarietyGenerator()
deep = Tree("S")
deep.add_child(Tree("NP", ["The dog"]))
deep.add_child(Tree("VP", ["sees", "the cat"]))

varieties = generator.generate_varieties(deep)
for form, tree in varieties.items():
    print(f"{form}: {tree.to_string()}")
```

### 6.2 Machine Translation

Transformations capture structural differences between languages:

```
English:  [NP The cat] [VP was seen by [NP the dog]]
Hindi:    [NP kutta] [NP ne] [NP billi] [VP dekhi]
Literal:  Dog (agent marker) cat (patient) saw
```

**Key insight**: Different languages surface the same deep structure differently. Transformations map between these surface structures.

### 6.3 Information Extraction

Transformations help extract structured data from varied sentence structures:

```
Input sentences:
1. "Apple released the new iPhone"
2. "The new iPhone was released by Apple"
3. "Who released the new iPhone?"

Transformation system maps all to canonical form:
RELEASE(agent: Apple, theme: iPhone, time: new)
```

### 6.4 Speech Recognition and Understanding

Modern ASR systems use transformational grammars to:
1. Constrain possible interpretations of recognized speech
2. Map spoken phrases to canonical logical forms
3. Handle variations in how users express the same intent

---

## 7. Advanced Concepts

### 7.1 Transformational-Based Learning

In modern NLP, the principles of transformational grammars inform:

1. **Syntax-based Machine Learning**: Tree-structured models
2. **Transformer Architectures**: Deep learning models named after the linguistic concept
3. **Data Augmentation**: Using transformations to generate training data

### 7.2 Limitations of Classical Transformational Grammars

1. **Computational Complexity**: Some transformations are computationally expensive
2. **Coverage**: Not all language phenomena fit neatly into the framework
3. **Psychological Reality**: Debated whether humans actually use these transformations
4. **Cross-linguistic Variation**: Languages differ in their transformation possibilities

### 7.3 Modern Alternatives

| Classical Approach | Modern Alternative |
|-------------------|-------------------|
| Rule-based transformations | Neural sequence-to-sequence models |
| Discrete symbolic structures | Continuous vector representations |
| Human-crafted rules | Learned representations |

Despite these alternatives, transformational grammar principles remain foundational for understanding language and designing AI systems.

---

## 8. Key Takeaways

1. **Context-Free Transformational Grammars** extend CFGs by adding transformational rules that map between deep and surface structures

2. **Deep structures** capture semantic content in a canonical form, while **surface structures** represent actual spoken/written sentences

3. **Transformational rules** include:
   - Movement transformations (Wh-movement, passive)
   - Substitution transformations
   - Deletion/insertion transformations

4. **Key properties** include structure preservation, the projection principle, and constraints like Subjacency

5. **Applications** span NLP, machine translation, information extraction, and speech understanding

6. The principles of transformational grammars, while originally linguistic, have influenced modern AI architectures (e.g., Transformer models)

---

## 9. Assessment Items

### 9.1 Challenging Multiple Choice Questions

**Question 1**: In Context-Free Transformational Grammars, which component generates the deep structure?

A) Transformational rules  
B) Surface structure component  
C) Base Context-Free Grammar  
D) Phonological component  

**Answer**: C) Base Context-Free Grammar

---

**Question 2**: Which transformation relates the sentences "The dog saw the cat" and "What did the dog see?"

A) Passive transformation  
B) Wh-movement transformation  
C) Complementizer deletion  
D) Imperative formation  

**Answer**: B) Wh-movement transformation

---

**Question 3**: The principle that states "transformations cannot delete or add required elements" is called:

A) Subjacency  
B) Structure preservation  
C) Projection principle  
D) Theta-criterion  

**Answer**: C) Projection principle

---

**Question 4**: In the passive transformation "The cat was seen by the dog", which element has moved to subject position?

A) The verb "seen"  
B) The agent "the dog"  
C) The patient "the cat"  
D) The preposition "by"  

**Answer**: C) The patient "the cat"

---

**Question 5**: Which constraint prevents movement from crossing more than one bounding node?

A) Left Branch Condition  
B) Specific Subject Condition  
C) Specified Subject Condition  
D) Subjacency  

**Answer**: D) Subjacency

---

**Question 6**: In a Transformational Grammar, the output after all transformations have been applied is called:

A) Deep structure  
B) Phonetic form  
C) Surface structure  
D) Logical form  

**Answer**: C) Surface structure

---

**Question 7**: Consider the transformation: "John believes that Mary left" → "John believes Mary left". This is an example of:

A) Wh-movement  
B) Passive transformation  
C) Complementizer deletion  
D) Auxiliary inversion  

**Answer**: C) Complementizer deletion

---

**Question 8**: The trace (t) left behind when an element moves is important for:

A) Phonological processing  
B) Maintaining the chain of movement  
C) Semantic interpretation only  
D) Parsing efficiency  

**Answer**: B) Maintaining the chain of movement

---

### 9.2 Flashcards

| Term | Definition |
|------|------------|
| **Deep Structure** | The abstract syntactic representation that captures the semantic content of a sentence before transformations |
| **Surface Structure** | The final syntactic form of a sentence after all transformational rules have been applied |
| **Transformational Rule** | A rule that maps one syntactic structure to another, capturing systematic relationships between sentences |
| **Movement Transformation** | A type of transformation that relocates a constituent from one position to another (e.g., Wh-movement, passive) |
| **Base Grammar** | The Context-Free Grammar component that generates kernel sentences (deep structures) |
| **Trace (t)** | A placeholder left in the original position when an element moves; represents the movement chain |
| **Projection Principle** | The constraint that all transformations must preserve the argument structure and θ-roles |
| **Subjacency** | The constraint that movement cannot cross more than one bounding node (e.g., NP, IP) |
| **Bounded Movement** | Movement that is limited by syntactic constraints to specific domains |
| **Passive Transformation** | A transformation that promotes the object to subject position and demotes the subject to a prepositional phrase |

---

### 9.3 Short Answer Questions

**Question 1**: Explain the difference between deep structure and surface structure with an example.

**Answer**: Deep structure is the abstract, semantic representation of a sentence, while surface structure is what we actually see or hear. For example, "The cat was seen by the dog" and "The dog saw the cat" have different surface structures but the same deep structure representing the agent (dog) seeing the patient (cat).

---

**Question 2**: Describe three types of transformational rules and provide an example for each.

**Answer**: 
1. **Movement transformations**: Relocate elements (e.g., Wh-movement: "She reads what" → "What does she read?")
2. **Substitution transformations**: Replace elements (e.g., pronoun replacement: "John and John" → "John and he")
3. **Deletion transformations**: Remove elements (e.g., complementizer deletion: "I think that he came" → "I think he came")

---

**Question 3**: How do Context-Free Transformational Grammars contribute to machine translation?

**Answer**: Different languages surface the same semantic content differently. CFTGs help map between these different surface structures by using transformations. For instance, English uses prepositional "by" phrases in passive voice while other languages may use different constructions. Transformations capture these systematic differences.

---

**Question 4**: What is the Projection Principle, and why is it important in transformational grammar?

**Answer**: The Projection Principle states that lexical information (θ-roles, subcategorization) must be projected at every level of representation (D-structure, S-structure). It ensures that transformations cannot delete or add required arguments, maintaining the semantic integrity of sentences.

---

**Question 5**: Discuss one advantage and one limitation of using transformational grammars in NLP applications.

**Answer**: 
- **Advantage**: CFTGs provide a principled way to generate grammatical variations and handle different sentence constructions systematically
- **Limitation**: The number of transformations and their interactions can become complex, and some linguistic phenomena don't fit neatly into the transformational framework

---

### 9.4 Application-Based Question

**Question**: Design a simple transformational system that can handle the following sentences and their variants:
1. "The chef cooked the meal"
2. "The meal was cooked by the chef"
3. "What did the chef cook?"

Your system should identify the base grammar rules needed and the transformational rules required.

**Answer Outline**:
- Base Grammar: S → NP VP, NP → Det N, VP → V NP, etc.
- Transformational Rules:
  - Passive: [NP1] [VP V NP2] → [NP2] [VP was V by NP1]
  - Wh-Movement: Move wh-phrase to CP position, add auxiliary inversion
- Implementation should show how both passive and question transformations apply to the same deep structure

---

## 10. References and Further Reading

1. Chomsky, N. (1957). *Syntactic Structures*. Mouton.
2. Chomsky, N. (1965). *Aspects of the Theory of Syntax*. MIT Press.
3. Radford, A. (2009). *Analysing English Sentences: A Minimalist Approach*. Cambridge University Press.
4. Jurafsky, D. & Martin, J. (2009). *Speech and Language Processing*. Pearson.
5. Delhi University NEP 2024 UGCF AI Syllabus

---

*This study material has been prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*