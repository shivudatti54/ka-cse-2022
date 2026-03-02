# Representation Revisited

## Introduction

Knowledge representation is one of the fundamental pillars of artificial intelligence, serving as the bridge between human understanding and machine computation. In our exploration of AI, we have examined various representation schemes, from simple propositional logic to more expressive first-order logic. This topic revisits the concept of representation, examining why certain representation languages are better suited for particular problem domains and how the choice of representation affects reasoning efficiency.

The study of representation is not merely academic; it has profound practical implications for building intelligent systems. When we represent knowledge about the world, we are making commitments about what entities exist, what relationships matter, and what operations we can perform. These commitments determine what our AI systems can learn, reason about, and ultimately accomplish. A well-chosen representation can make complex problems tractable, while a poor choice can render seemingly simple problems unsolvable.

This revisit becomes particularly important when we consider the spectrum from propositional logic to first-order logic. Propositional logic, while computationally tractable, lacks the expressive power to handle generic statements about objects and relationships. First-order logic addresses these limitations but brings computational complexity. Understanding when and how to use each representation is crucial for any AI practitioner.

## Key Concepts

### Properties of Good Representations

A good knowledge representation should possess several critical properties. **Expressivity** refers to the ability to represent the full range of knowledge needed for a domain—a representation that cannot express necessary truths is fundamentally inadequate. **Computational tractability** ensures that reasoning with the representation can be performed within reasonable time bounds; a perfectly expressive representation that requires exponential time is often impractical. **Ease of acquisition** considers how knowledge gets into the system—whether through manual encoding, learning from data, or combination approaches.

Additional properties include **clarity**, where the representation has clean semantics making reasoning about correctness possible; **modularity**, allowing pieces of knowledge to be added, removed, or modified independently; and **perspicuity**, enabling humans to understand what the system knows and how it reasons. These properties often conflict in practice, requiring careful trade-offs based on application requirements.

### The Representation Spectrum

Knowledge representation exists on a spectrum of expressivity. At the lowest level, we have **ground atomic facts**, simple statements about specific objects that can be directly stored in a knowledge base. Above this, **propositional logic** allows combination of facts using logical connectives (AND, OR, NOT, IMPLIES), enabling representation of general rules but still treating each object as a separate case. **First-order logic** extends this further by introducing quantifiers (for all, there exists) and predicates that can range over objects, dramatically increasing expressive power.

Beyond first-order logic, we encounter **description logics** that provide a tractable subset of first-order logic with well-defined reasoning procedures; **frame-based representations** that organize knowledge into hierarchical structures with slots and inheritance; **semantic networks** that represent knowledge as graphs of nodes and edges; and **ontologies** that provide shared vocabularies for domains. Each step up this spectrum increases expressivity while potentially decreasing computational tractability.

### Procedural Versus Declarative Representation

An important distinction in knowledge representation is between **procedural knowledge** (knowing how to do something) and **declarative knowledge** (knowing that something is true). Procedural representation encodes knowledge as programs or procedures that manipulate data; the knowledge is embedded in the algorithm itself. Declarative representation encodes knowledge as statements in a formal language that can be interpreted by a separate reasoning engine.

Modern AI systems typically favor declarative representations for several reasons. Declarative knowledge is easier to verify, debug, and modify without understanding the entire system. It enables separate development of the knowledge base and reasoning mechanisms. However, purely declarative systems can suffer from inefficiency that procedural representations avoid. The optimal approach often combines both, using declarative representations for domain knowledge while allowing procedural attachments for efficiency-critical operations.

### Representation and Reasoning Are Inseparable

A fundamental insight in knowledge representation is that representation and reasoning cannot be separated. The choice of representation determines what reasoning algorithms are applicable, and different representations make different reasoning tasks easy or hard. This relationship is formalized in the **representation theorem** of knowledge representation: for any representation language, there exists a corresponding reasoning formalism, and the complexity characteristics of the language directly impact the complexity of reasoning.

This interdependency means that selecting a representation requires considering the entire reasoning pipeline. A representation that makes learning easy might make inference hard, or vice versa. The practical art of knowledge engineering involves navigating these trade-offs based on the specific requirements of the application.

### Frame Problem and Situational Calculus

A classic challenge in knowledge representation is the **frame problem**: how to represent what does not change when actions are performed, without explicitly stating all the things that remain the same. In formal terms, we need axioms that characterize the effects of actions (successor state axioms) while implicitly preserving everything else.

The **situation calculus**, developed by John McCarthy, provides one solution to this problem. It represents the world as a series of situations resulting from actions, with situation variables representing points in time. Fluents are predicates that vary between situations, and axioms specify how actions affect fluents. While theoretically sound, practical applications often require additional mechanisms to handle the combinatorial explosion of possible situations.

## Examples

### Example 1: Representing Family Relationships

Consider representing family relationships. In **propositional logic**, we would need separate propositions for each family: `father(john, bob)`, `mother(susan, bob)`, `father(john, alice)`, and so on. This requires 2n propositions for n child-parent relationships and becomes unwieldy for large families.

In **first-order logic**, we can write general rules:
```
∀x,y: parent(x,y) → child(y,x)
∀x,y: father(x,y) → parent(x,y)
∀x,y: mother(x,y) → parent(x,y)
∀x,y: parent(x,y) ∧ male(x) → father(x,y)
```

This compact representation handles any family size with the same three axioms. The trade-off is that first-order inference is more complex than propositional inference, though specialized reasoners handle many common cases efficiently through unification and forward chaining.

### Example 2: Robot Navigation Domain

A robot navigating a grid world requires representation of locations, obstacles, and paths. Using **propositional logic**, we might represent each cell's state: `clear(cell_1_1)`, `obstacle(cell_2_3)`, `at(robot, cell_1_1)`. Movement requires updating many propositions explicitly.

Using **first-order logic with situation calculus**:
```
∀s: at(robot, l, s) ∧ adjacent(l, l') → at(robot, l', do(move(l,l'), s))
∀s: clear(l) → at(robot, l, do(move(l',l), s)) → at(robot, l, s)
```

This compactly represents movement for any configuration. The frame axioms (second line) use successor state axioms to specify what changes, avoiding the frame problem. This representation supports planning algorithms that can find paths in arbitrary grid configurations.

### Example 3: University Course Representation

Representing information about university courses illustrates representation choice:

**Propositional approach** (verbose):
```
cs101_credits(3)
cs101_prereq(cs100)
cs101_semester(fall)
math201_credits(4)
math201_prereq(math101)
```

**First-order approach** (compact):
```
∀x: course(x) ∧ cs(x) → credits(x, 3)
∀x: course(x) ∧ math(x) → credits(x, 4)
∀x,y: prereq(x,y) → requires(x,y)
∀x: course(x) → hasCredits(x) ∧ hasSemester(x)
```

The first-order version scales to hundreds of courses with a fixed number of axioms. It also supports queries like "Find all 4-credit courses" that are trivial in first-order logic but require enumeration in propositional form.

## Exam Tips

1. **Know the trade-offs**: Be prepared to explain why one representation might be preferred over another in specific scenarios. Understand the expressivity versus tractability trade-off.

2. **Distinguish propositional from first-order**: Clearly articulate the key differences—propositional logic lacks quantifiers and object variables, making it unable to concisely express general rules about objects.

3. **Remember the frame problem**: Understand what the frame problem is and at least one approach to solving it (successor state axioms in situation calculus).

4. **Link to inference**: Connect representation choices to inference methods. Forward chaining works well with rule-based representations; unification is essential for first-order logic inference.

5. **Ontologies matter**: Understand that ontologies provide shared vocabularies enabling interoperability and logical inference across knowledge bases.

6. **Procedural vs declarative**: Be able to explain when each is appropriate and how modern systems often combine both approaches.

7. **Real-world applications**: Connect abstract representation concepts to practical applications like expert systems, semantic web, and natural language understanding.