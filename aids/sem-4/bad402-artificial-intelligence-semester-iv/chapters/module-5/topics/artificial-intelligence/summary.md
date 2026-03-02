# Artificial Intelligence - Summary

## Key Definitions and Concepts

- ARTIFICIAL INTELLIGENCE: The study and design of intelligent agents—systems that perceive their environment and take actions to maximize success.

- INTELLIGENT AGENT: A system that uses sensors to perceive the environment and actuators to act upon it, with the goal of achieving optimal outcomes.

- EXPERT SYSTEM: A computer program that encodes expert knowledge to solve complex problems in specific domains, featuring knowledge base, inference engine, working memory, and user interface.

- KNOWLEDGE ACQUISITION: The process of extracting knowledge from human experts and encoding it for machine use—a major bottleneck in expert system development.

- PARTIALLY OBSERVABLE ENVIRONMENT: An environment where the agent cannot perceive the complete state, requiring reasoning about unobserved aspects (e.g., Wumpus World).

## Important Formulas and Theorems

- RATIONAL AGENT DEFINITION: A rational agent selects actions that maximize the expected utility, given its percept history and built-in knowledge.

- TURING TEST: A test where a human interrogator, through natural language questions, cannot distinguish between human and machine responses—focuses on observable behavior rather than internal mechanisms.

## Key Points

1. Four approaches to AI exist: thinking humanly (cognitive modeling), acting humanly (Turing test), thinking rationally (logic-based), and acting rationally (rational agent approach).

2. The rational agent approach is most general and relevant to modern AI, encompassing search, probabilistic reasoning, and machine learning techniques.

3. AI systems consist of five components: perception (sensors), knowledge representation (storage), reasoning (inference), learning (improvement), and action (actuators).

4. Environment properties determine AI challenges: partial observability requires belief states, stochastic outcomes need probability, dynamic environments demand quick decisions.

5. Expert systems apply encoded human expertise to narrow domains, using production rules, semantic networks, or frames for knowledge representation.

6. The Wumpus World is a classic partially observable, stochastic, sequential decision problem that demonstrates AI under uncertainty.

7. Knowledge acquisition is difficult because experts often cannot articulate tacit knowledge and rules they use unconsciously.

8. Expert system shells provide ready-made frameworks including inference engines, allowing developers to focus on domain knowledge.

## Common Mistakes to Avoid

1. CONFUSING "THINKING" WITH "ACTING": A common error is mixing up approaches that focus on internal reasoning versus observable behavior. Think (cognitive modeling) versus Act (Turing Test) are fundamentally different perspectives.

2. OVERLOOKING UNCERTAINTY: Many students forget that real-world AI must handle incomplete information. The Wumpus World specifically tests uncertainty handling, a key theme of this module.

3. IGNORING THE CONNECTION BETWEEN TOPICS: AI does not exist in isolation. Expect exam questions that connect AI concepts to Bayes' rule, probability, and expert systems covered elsewhere in Module 5.

4. EQUATING AI WITH MACHINE LEARNING: While machine learning is important, AI encompasses search, knowledge representation, reasoning, planning, and perception—broader than just learning algorithms.

## Revision Tips

1. CREATE A COMPARISON CHART: Tabulate the four AI approaches with examples, advantages, and limitations. This clarifies distinctions that exams frequently test.

2. PRACTICE WUMPUS WORLD TRACES: Work through several Wumpus World scenarios, identifying percepts, updating beliefs, and selecting actions. This integrates multiple module concepts.

3. BUILD EXPERT SYSTEM MENTAL MODEL: When studying expert systems, imagine building one for a familiar domain (e.g., diagnosing flu). This grounds abstract concepts in concrete understanding.

4. REVISIT PROBABILITY FOUNDATIONS: Since this module connects AI to uncertain reasoning, ensure you are comfortable with probability concepts before the exam.