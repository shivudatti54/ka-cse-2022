# Symbolic Reasoning Under Uncertainty

## Introduction to Reasoning Under Uncertainty

In artificial intelligence, reasoning under uncertainty refers to the process of making decisions and drawing conclusions when available information is incomplete, unreliable, or ambiguous. Unlike classical logic which deals with absolute truths, real-world problems often involve elements of uncertainty that must be accounted for in intelligent systems. Symbolic reasoning under uncertainty extends traditional symbolic AI approaches (like predicate logic and rule-based systems) to handle uncertain information. This approach maintains the structured, knowledge-rich representation of symbolic systems while incorporating mechanisms to quantify and reason with uncertainty.

## Why Uncertainty Exists in AI Systems

Several factors contribute to uncertainty in AI:

1. **Incomplete information**: We rarely have all facts needed for certain conclusions
2. **Noisy data**: Sensor readings and measurements often contain errors
3. **Ambiguity**: The same evidence might support multiple conclusions
4. **Changing environments**: The world evolves, making previous knowledge less reliable
5. **Expert knowledge limitations**: Human experts often express knowledge with qualifications

## Key Concepts in Symbolic Reasoning Under Uncertainty

### Non-Monotonic Reasoning

Traditional logic is monotonic: adding new information never invalidates previous conclusions. Non-monotonic reasoning allows conclusions to be retracted when new evidence emerges.

```prolog
Initial Knowledge: Birds typically fly
Fact: Tweety is a bird
Conclusion: Tweety flies (default reasoning)
New Fact: Tweety is a penguin
Revised Conclusion: Tweety does not fly (exception)
```

**Example**: "Normally, birds fly, but penguins are exceptions." This allows drawing tentative conclusions that can be revised later.

### Default Reasoning

Default reasoning involves making assumptions about typical cases when specific information is lacking. It uses rules of the form: "If P is true, and it is consistent to assume Q, then conclude Q."

```prolog
Rule: If X is a bird, and it's consistent that X can fly, then assume X can fly.
Fact: Polly is a bird
Conclusion: Polly can fly (by default)
```

### Truth Maintenance Systems (TMS)

TMS are mechanisms that track dependencies between beliefs and maintain consistency when new information is added. There are two main types:

1. **Justification-based TMS**: Records reasons for beliefs
2. **Assumption-based TMS**: Manages beliefs based on assumptions

```prolog
Belief: Car starts (justified by: battery OK AND fuel adequate)
If new evidence shows battery is dead, the TMS retracts the belief
```

### Fuzzy Logic

Fuzzy logic handles uncertainty by allowing degrees of truth between completely true and completely false. Unlike binary logic (0 or 1), fuzzy logic uses values between 0 and 1.

```python
Concept: "Temperature is hot"
Binary: 0 (not hot) or 1 (hot)
Fuzzy: 0.0 (cold), 0.3 (warm), 0.7 (hot), 1.0 (very hot)
```

Fuzzy logic uses linguistic variables and membership functions to represent vague concepts.

## Major Approaches Compared

| Approach                | How it Handles Uncertainty            | Strengths                   | Limitations                 |
| ----------------------- | ------------------------------------- | --------------------------- | --------------------------- |
| **Non-Monotonic Logic** | Allows retracting conclusions         | Handles exceptions well     | Complex to implement        |
| **Default Reasoning**   | Makes assumptions about typical cases | Simple, intuitive           | Can lead to inconsistencies |
| **Fuzzy Logic**         | Uses degrees of truth                 | Handles vagueness naturally | May lose precision          |
| **Truth Maintenance**   | Manages belief dependencies           | Maintains consistency       | Computationally expensive   |

## Implementation Examples

### Default Reasoning Example

Let's represent the famous "birds fly" example with default logic:

```prolog
// Facts
bird(tweety).
penguin(tweety). // Added later

// Default rule
flies(X) :- bird(X), \+ abnormal(X).

// Exception rule
abnormal(X) :- penguin(X).
```

Initially, we conclude `flies(tweety)` because Tweety is a bird and we have no reason to believe he's abnormal. When we learn Tweety is a penguin, we derive `abnormal(tweety)` and retract the flying conclusion.

### Fuzzy Logic Example

Representing "comfortable temperature" using fuzzy logic:

```python
Membership functions:
Cold: μ(x) = {1 if x<15, (20-x)/5 if 15≤x≤20, 0 if x>20}
Warm: μ(x) = {(x-15)/5 if 15≤x≤20, 1 if 20≤x≤25, (30-x)/5 if 25≤x≤30}
Hot: μ(x) = {(x-25)/5 if 25≤x≤30, 1 if x>30}

At 22°C:
Cold: 0, Warm: 0.8, Hot: 0.0
```

We can create rules like: "If temperature is warm, then comfort level is high."

## Relationship to Other Uncertainty Methods

Symbolic reasoning under uncertainty differs from statistical approaches (covered in the next part of this module) in several ways:

| Aspect                   | Symbolic Reasoning         | Statistical Reasoning               |
| ------------------------ | -------------------------- | ----------------------------------- |
| **Representation**       | Rules, logic, symbols      | Probabilities, distributions        |
| **Knowledge Source**     | Expert knowledge, rules    | Data, observations                  |
| **Computation**          | Logical inference          | Mathematical calculations           |
| **Uncertainty Handling** | Non-monotonicity, defaults | Probabilities, confidence intervals |

Statistical reasoning (like Bayesian networks) quantifies uncertainty numerically, while symbolic approaches handle it through logical structures and exception mechanisms.

## Real-World Applications

1. **Expert Systems**: Medical diagnosis systems that handle exceptions to general rules
2. **Robotic Control**: Fuzzy logic controllers for smooth operation in varying conditions
3. **Natural Language Processing**: Handling ambiguous meanings and contextual exceptions
4. **Legal Reasoning**: Applying laws with exceptions and special cases

## Exam Tips

1. **Understand the difference** between symbolic and statistical approaches to uncertainty
2. **Memorize key characteristics** of each method (non-monotonicity, default reasoning, etc.)
3. **Practice with examples** - be able to apply each approach to simple scenarios
4. **Compare and contrast** the methods in terms of strengths and limitations
5. **Focus on applications** - understand which approach is suitable for different problem types
6. **Remember that symbolic methods** maintain the explainability of rule-based systems while handling uncertainty
