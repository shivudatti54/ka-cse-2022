# Sample Space and Events

## Introduction

Probability theory forms the mathematical foundation for numerous computing applications, from algorithm analysis and machine learning to network protocols and cybersecurity. Before we can compute probabilities, we must first understand the framework upon which the entire theory is built: sample spaces and events.

When we talk about a "random experiment" in probability, we mean any process whose outcome cannot be predicted with certainty beforehand. In computing contexts, this could be the result of a random number generator, the time taken by a algorithm to execute, or the packet loss rate in a network transmission. The **sample space** represents the complete set of all possible outcomes of such an experiment, while **events** are subsets of this sample space that we are interested in analyzing.

Understanding sample spaces and events is crucial because every probability calculation ultimately boils down to measuring the "size" of an event relative to its sample space. This foundational concept appears repeatedly in DU examinations, and mastering it will give you the tools to tackle more complex probability problems involving conditional probability, Bayes' theorem, and random variables.

## Key Concepts

### 1. Random Experiment

A **random experiment** is a procedure that:
- Can be repeated under essentially the same conditions
- Has more than one possible outcome
- The outcome cannot be predicted with certainty before the experiment is performed

**Computing Examples:**
- Generating a random integer between 1 and 100 using a programming language's random function
- Measuring the execution time of a quantum algorithm
- Receiving a data packet and observing whether it arrives correctly or gets corrupted

### 2. Sample Space (S)

The **sample space** is the set of all possible outcomes of a random experiment. We denote it by S or Ω.

**Types of Sample Spaces:**

| Type | Description | Example |
|------|-------------|---------|
| Finite | Contains finite number of outcomes | S = {1, 2, 3, 4, 5, 6} for rolling a die |
| Countably Infinite | Outcomes can be put in one-to-one correspondence with natural numbers | S = {0, 1, 2, 3, ...} for number of failed login attempts |
| Uncountable (Continuous) | Contains an interval of real numbers | S = [0, 1] for execution time in milliseconds |

**Computing Example:** Consider a program that generates two random bits (0 or 1). The sample space is:
S = {(0,0), (0,1), (1,0), (1,1)}

This can also be written as S = {00, 01, 10, 11} with 4 equally likely outcomes.

### 3. Events

An **event** is a subset of the sample space. It may contain one outcome (simple event) or multiple outcomes (compound event). We typically denote events by capital letters like A, B, C.

**Simple Event:** An event containing exactly one outcome.
- Example: In the two-bits experiment, A = {(0,0)} represents both bits being 0

**Compound Event:** An event containing more than one outcome.
- Example: B = {(0,0), (0,1), (1,0)} represents "at least one bit is 0"

**Impossible Event:** The empty set ∅ (contains no outcomes)
**Certain Event:** The sample space itself S (contains all outcomes)

### 4. Operations on Events

Just like sets, events support several operations:

**Union (A ∪ B):** The event containing all outcomes in A or B or both.
- A ∪ B = {x : x ∈ A or x ∈ B}

**Intersection (A ∩ B):** The event containing outcomes common to both A and B.
- A ∩ B = {x : x ∈ A and x ∈ B}

**Complement (A' or Aᶜ):** The event containing all outcomes in S that are not in A.
- A' = {x ∈ S : x ∉ A}

**Difference (A - B):** The event containing outcomes in A but not in B.
- A - B = {x : x ∈ A and x ∉ B}

### 5. Mutually Exclusive Events

Two events A and B are **mutually exclusive** (or disjoint) if they cannot occur simultaneously:
A ∩ B = ∅

**Example:** In rolling a die, A = {1, 3, 5} (odd numbers) and B = {2, 4, 6} (even numbers) are mutually exclusive because you cannot get both an odd and even number in a single roll.

### 6. Exhaustive Events

Events A₁, A₂, ..., Aₙ are **exhaustive** if their union covers the entire sample space:
A₁ ∪ A₂ ∪ ... ∪ Aₙ = S

### 7. Equally Likely Outcomes

A sample space has **equally likely outcomes** if each outcome has the same probability of occurring. In such cases:
P(each outcome) = 1/|S|

where |S| denotes the number of outcomes in S.

## Examples

### Example 1: Network Packet Transmission

A network interface card sends data packets. Each packet has a 20% chance of being corrupted during transmission. Consider the experiment of sending 3 packets.

**Solution:**

**Step 1: Define the sample space**
Each packet can be either Success (S) or Corrupted (C). The sample space contains 2³ = 8 outcomes:
S = {SSS, SSC, SCS, CSS, SCC, CSC, CCS, CCC}

**Step 2: Define events**
Let A = "exactly 1 packet is corrupted"
A = {SCC, CSC, CCS} — 3 outcomes

Let B = "at least 2 packets are corrupted"
B = {CCS, CSC, SCC, CCC} — 4 outcomes

Let C = "no packet is corrupted"
C = {SSS} — 1 outcome

**Step 3: Calculate probabilities (assuming equally likely)**
Since outcomes are equally likely and each has probability (0.8)³ × (0.2)⁰ = 0.512 for success pattern or (0.8)² × (0.2)¹ = 0.128 for exactly one failure, we can compute:

P(A) = 3 × 0.128 = 0.384
P(B) = 3 × 0.128 + 1 × 0.008 = 0.392
P(C) = 0.512

### Example 2: Algorithm Performance

An algorithm's execution time (in milliseconds) follows a uniform distribution on the interval [5, 15]. Let:
- Event A: Execution time is less than 8 ms
- Event B: Execution time is between 10 and 12 ms

**Solution:**

The sample space is continuous: S = [5, 15]

**Event A:** A = [5, 8)
Length of A = 8 - 5 = 3
P(A) = Length of A / Length of S = 3/10 = 0.3

**Event B:** B = [10, 12]
Length of B = 12 - 10 = 2
P(B) = 2/10 = 0.2

**Event A ∩ B:** Since A = [5, 8) and B = [10, 12], they are mutually exclusive.
P(A ∩ B) = 0

**Event A ∪ B:** P(A ∪ B) = P(A) + P(B) - P(A ∩ B) = 0.3 + 0.2 - 0 = 0.5

### Example 3: Database Query Results

A database query returns records with probabilities: 60% match condition X, 45% match condition Y, and 25% match both. For 1000 records:

**Solution:**

Let A = "matches condition X", B = "matches condition Y"
|A| = 600, |B| = 450, |A ∩ B| = 250

**Sample space:** S has 1000 outcomes

**Find P(A ∪ B):**
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
= 0.60 + 0.45 - 0.25 = 0.80

So 800 records match at least one condition.

**Find P(A' ∩ B):**
P(A' ∩ B) = P(B) - P(A ∩ B) = 0.45 - 0.25 = 0.20
= 200 records match Y but not X

## Exam Tips

1. **Always define the sample space first**: Before solving any probability problem, clearly write down the sample space S. This prevents errors and shows your methodology to examiners.

2. **Use set notation properly**: Remember that events are sets. Use proper symbols (∈, ⊂, ∪, ∩) in your answers, not words alone.

3. **Check for equally likely outcomes**: The formula P(A) = |A|/|S| only applies when outcomes are equally likely. For weighted probabilities, use the multiplication rule.

4. **Apply De Morgan's Laws**: For complements of unions and intersections:
   - (A ∪ B)' = A' ∩ B'
   - (A ∩ B)' = A' ∪ B'

5. **Draw Venn diagrams**: For problems involving two or three events, a Venn diagram helps visualize unions, intersections, and complements clearly.

6. **Distinguish between "at least" and "exactly"**: In counting problems, "at least one" often means the complement of "none." For example, P(at least one corrupted) = 1 - P(none corrupted).

7. **For continuous sample spaces**: When S = [a, b] is an interval, probability is proportional to interval length. P(A) = (length of A) / (length of S).

8. **Verify your answers**: Check that probabilities lie between 0 and 1, and that mutually exclusive events have P(A ∪ B) = P(A) + P(B).