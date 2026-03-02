**Text Book 2: Chap 16 Practical Component of IPCC (May Cover All/Major Modules)**
**Experiment 1: Read a Dataset from the User and Infer**
====================================================================

## **Introduction**

In this experiment, you will be required to read a dataset from the user and perform inference using graphical models, specifically Bayesian networks and Markov chains.

## **What is a Bayesian Network?**

A Bayesian network is a probabilistic graphical model that represents the relationships between different variables. It is a directed acyclic graph (DAG) where each node represents a variable, and each directed edge represents the conditional dependence between two variables.

**Key Concepts:**

- **Node:** A node in a Bayesian network represents a variable.
- **Edge:** An edge in a Bayesian network represents the conditional dependence between two variables.
- **Conditional Probability Table (CPT):** A CPT is a table that specifies the conditional probabilities of a node given its parents.

**How to Create a Bayesian Network from Scratch:**

1.  Define the variables and their domains.
2.  Define the conditional dependencies between the variables.
3.  Create a directed acyclic graph (DAG) to represent the Bayesian network.
4.  Assign conditional probability tables (CPTs) to each node.

**Example:**

Suppose we want to model the relationship between the weather (W), the temperature (T), and the precipitation (P). We can create a Bayesian network as follows:

- Variables: W, T, P
- Domains: W (good, bad), T (hot, cold), P (rain, no rain)
- Conditional Dependencies:
  - W -> T (good weather implies hot temperature)
  - W -> P (good weather implies rain)
  - T -> P (hot temperature implies rain)
- DAG:
  - W -> T
  - W -> P
  - T -> P
- CPTs:
  - P(W|T): P(W|T = hot) = 0.8, P(W|T = cold) = 0.2
  - P(P|W): P(P|W = rain) = 0.9, P(P|W = no rain) = 0.1
  - P(P|T): P(P|T = hot) = 0.6, P(P|T = cold) = 0.4

## **Make Bayesian Networks**

Once you have created a Bayesian network, you can use it to perform inference, such as:

- **Query:** What is the probability that it will rain given that it is hot outside?
- **Answer:** Use the CPTs and the DAG to compute the conditional probability.

## **Markov Chain**

A Markov chain is a mathematical system that undergoes transitions from one state to another according to certain probabilistic rules.

**Key Concepts:**

- **State:** A state in a Markov chain is a node in the graph.
- **Transition:** A transition is a directed edge in the graph.
- **Transition Matrix:** A transition matrix specifies the probabilities of transitioning from one state to another.

**Example:**

Suppose we want to model the sequence of weather conditions (good, bad, rain, no rain) over a day. We can create a Markov chain as follows:

- States: good, bad, rain, no rain
- Transition Matrix:
  - good -> bad: 0.3, good -> rain: 0.2, good -> no rain: 0.5
  - bad -> good: 0.4, bad -> rain: 0.3, bad -> no rain: 0.3
  - rain -> bad: 0.1, rain -> good: 0.2, rain -> no rain: 0.7
  - no rain -> bad: 0.2, no rain -> good: 0.3, no rain -> rain: 0.5

**How to Perform Inference in a Markov Chain:**

1.  Define the initial state.
2.  Define the transition matrix.
3.  Compute the probabilities of transitioning from one state to another.
4.  Compute the probability of a sequence of states.

**Example:**

Suppose we want to compute the probability that it will rain given that it is hot outside. We can use the Markov chain as follows:

- Initial State: good
- Transition Matrix:
  - good -> bad: 0.3, good -> rain: 0.2, good -> no rain: 0.5
  - bad -> good: 0.4, bad -> rain: 0.3, bad -> no rain: 0.3
  - rain -> bad: 0.1, rain -> good: 0.2, rain -> no rain: 0.7
  - no rain -> bad: 0.2, no rain -> good: 0.3, no rain -> rain: 0.5
- Compute the probabilities:
  - P(next state|current state): Use the transition matrix to compute the probabilities of transitioning from one state to another.
  - P(rain|good): P(next state|current state = rain) = 0.7
