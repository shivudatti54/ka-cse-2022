# Module 2: Representing Knowledge Using Rules

## Introduction

In Artificial Intelligence, solving a problem requires knowledge about the world. This knowledge must be represented in a way that is both efficient for storage and effective for computational reasoning. One of the most intuitive and historically significant methods for this is **Rule-Based Knowledge Representation**. This approach uses "If-Then" conditional statements to encode knowledge, mirroring human decision-making processes. It forms the backbone of many early expert systems and remains highly relevant today in areas like business logic engines and automation.

## Core Concepts

### 1. What is a Rule?

A rule is a conditional statement that expresses a logical relationship between pieces of knowledge. It typically consists of two parts:

- **Antecedent (IF part):** This is the condition or the premise. It is a conjunction (logical AND) of one or more facts or patterns.
- **Consequent (THEN part):** This is the action or the conclusion that is inferred or executed if the antecedent is satisfied. It can be a new fact, an action, or a recommendation.

**Syntax:** `IF <condition(s)> THEN <action/conclusion>`

### 2. Rule-Based Systems (RBS)

A collection of such rules forms a **Rule-Based System**, also known as a **Production System**. The core components of an RBS are:

- **Rule Base (Knowledge Base):** This is the set of all rules that encapsulate the expert knowledge for a specific domain.
- **Working Memory (Fact Base):** A global database that contains the known facts, initial data, and inferred facts about the current problem or state of the world.
- **Inference Engine:** This is the "brain" of the system. It compares the facts in the Working Memory against the conditions (antecedents) of the rules in the Rule Base. It determines which rules are applicable and executes them.

### 3. The Inference Process

The inference engine operates in a **recognize-act cycle**:

1. **Match:** Check the conditions of all rules against the current facts in the working memory. Rules whose conditions are satisfied are triggered and become candidates for execution. This set of candidate rules is called the **conflict set**.
2. **Conflict Resolution:** If multiple rules are triggered, the inference engine uses a **conflict resolution strategy** (e.g., priority, most specific rule, most recent fact) to select exactly one rule to fire.
3. **Act (Fire):** Execute the consequent (THEN part) of the selected rule. This usually means adding a new fact to the working memory or performing an external action.
4. The cycle repeats until no more rules are triggered or a termination condition is met.

### 4. Forward vs. Backward Chaining

The inference engine can operate in two primary modes:

- **Forward Chaining (Data-Driven Reasoning):** Starts with the available data in the working memory. It uses the rules to derive new data until a desired goal is reached. It's like "What conclusions can I draw from this data?"
- _Example: Medical diagnosis systems._ Start with symptoms (data) to infer a disease (goal).
- **Backward Chaining (Goal-Driven Reasoning):** Starts with a hypothesized goal (e.g., a possible conclusion). The system then checks what rules would prove that goal and recursively checks if the conditions of those rules are true. It's like "What do I need to prove this goal?"
- _Example: Proving a theorem._ Start with the theorem (goal) and work backwards to see if it can be supported by known axioms (facts).

## Example: A Simple Animal Identification System

Let's define a small rule base:

**Rule Base:**

1. IF animal has fur THEN it is a mammal
2. IF animal gives milk THEN it is a mammal
3. IF animal has feathers THEN it is a bird
4. IF it is a mammal AND it eats meat THEN it is a carnivore
5. IF it is a carnivore AND it has tawny color AND it has dark spots THEN it is a cheetah
6. IF it is a carnivore AND it has tawny color AND it has black stripes THEN it is a tiger

**Working Memory (Initial Facts):** `animal has fur, eats meat, has tawny color, has dark spots`

**Inference Process (Forward Chaining):**

1. Fact `has fur` matches Rule 1. Fire Rule 1: **Add `it is a mammal`** to working memory.
2. Working Memory is now: `[has fur, eats meat, tawny color, dark spots, is a mammal]`
3. `is a mammal` and `eats meat` match Rule 4. Fire Rule 4: **Add `it is a carnivore`**.
4. Working Memory is now: `[... , is a carnivore]`
5. `is a carnivore`, `has tawny color`, and `has dark spots` match Rule 5. Fire Rule 5: **Conclude `it is a cheetah`**.

## Comparison of Forward and Backward Chaining

|                     | Forward Chaining  | Backward Chaining |
| ------------------- | ----------------- | ----------------- |
| **Start Point**     | Available data    | Hypothesized goal |
| **Reasoning Style** | Data-driven       | Goal-driven       |
| **Example**         | Medical diagnosis | Proving a theorem |

## Key Points & Summary

- **Intuitive and Modular:** Rules are a natural way to represent human expertise. They are modular—new knowledge can be added by simply inserting a new rule without necessarily altering existing ones.
- **Separation of Knowledge and Control:** The rule base (knowledge) is kept separate from the inference engine (control), making the system easier to maintain and update.
- **Inefficiency for Large Sets:** Inference can become slow with a very large number of rules, as the engine must check all rules in each cycle.
- **Conflict Resolution is Crucial:** Well-defined strategies are needed to handle situations where multiple rules are triggered simultaneously.
- **Foundation for Expert Systems:** This paradigm was fundamental to the development of Expert Systems in the 1970s and 1980s, which aimed to capture and automate the decision-making of human experts.
- **Modern Relevance:** The core concept of "If-Then" logic is ubiquitous, found in business rules engines (e.g., Drools), automation tools, and smart home applications.

## Exam Tips

- Understand the structure of a rule and how it is used in a rule-based system.
- Be able to explain the recognize-act cycle of the inference engine.
- Know the difference between forward and backward chaining, and when each is used.
- Understand the importance of conflict resolution strategies in rule-based systems.

## Key Takeaways

- Rule-based systems are a powerful way to represent human expertise and make decisions based on that expertise.
- The inference engine is the "brain" of the system, and its recognize-act cycle is key to understanding how the system works.
- Forward and backward chaining are two different modes of reasoning used in rule-based systems, each with its own strengths and weaknesses.
- Conflict resolution strategies are crucial in rule-based systems, as they help to ensure that the system makes the correct decision in situations where multiple rules are triggered simultaneously.
