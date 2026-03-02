# Artificial Intelligence

## Introduction

Artificial Intelligence (AI) represents one of the most transformative technological developments in the history of computing. At its core, AI is the branch of computer science that aims to create systems capable of performing tasks that typically require human intelligence. These tasks encompass a wide range of cognitive functions including learning, reasoning, problem-solving, perception, language understanding, and decision-making. The field sits at the intersection of computer science, mathematics, psychology, linguistics, neuroscience, and philosophy, making it inherently interdisciplinary.

The relevance of AI in today's world cannot be overstated. From virtual assistants like Siri and Alexa to autonomous vehicles, from medical diagnosis systems to financial trading algorithms, AI has permeated virtually every aspect of modern life. For students of Computer Science at the University of Delhi, understanding AI is no longer optional but essential. The module you are studying, which covers uncertain knowledge and reasoning, probability, and expert systems, forms the theoretical foundation upon which modern AI systems are built. This chapter on Artificial Intelligence serves as the gateway to understanding how machines can be programmed to exhibit intelligent behavior, particularly in environments characterized by uncertainty and incomplete information.

The study of AI is particularly relevant in the context of the Wumpus World problem, which you will encounter later in this module. The Wumpus World represents a classic AI problem environment where an agent must navigate through uncertainty—uncertainty about the contents of adjacent squares, uncertainty about the outcomes of its actions, and uncertainty about how to interpret sensory information. This chapter establishes the fundamental concepts that enable an AI agent to function effectively in such challenging environments.

## Key Concepts

### Definition and Scope of Artificial Intelligence

Artificial Intelligence can be defined as the study and design of intelligent agents, where an intelligent agent is a system that perceives its environment and takes actions that maximize its chances of success. This definition, proposed by researchers like Stuart Russell and Peter Norvig, emphasizes the agent-oriented perspective that dominates modern AI research.

The scope of AI encompasses several subfields and techniques. Machine Learning (ML) enables systems to learn from experience and improve performance without being explicitly programmed. Deep Learning, a subset of machine learning using artificial neural networks with multiple layers, has achieved remarkable success in image recognition, natural language processing, and speech recognition. Natural Language Processing (NLP) focuses on enabling computers to understand, interpret, and generate human language. Robotics combines AI with mechanical engineering to create machines that can interact with the physical world.

### Approaches to AI: Thinking versus Acting

One of the fundamental distinctions in AI research revolves around two key questions: Should AI systems think like humans or act like humans? And should they think rationally or act rationally? These questions give rise to four primary approaches.

The Turing Test approach, proposed by Alan Turing in 1950, focuses on acting like a human. A system passes the Turing Test if a human interrogator, after asking questions in natural language, cannot determine whether the responses come from a human or a machine. This approach emphasizes observable behavior rather than internal mechanisms. Systems designed to pass the Turing Test must possess capabilities in natural language processing, knowledge representation, automated reasoning, and machine learning.

The Cognitive Modeling approach focuses on thinking like a human. This involves creating computational models based on theories of human cognition, drawing from cognitive psychology and neuroscience. The goal is to simulate human thought processes, not just replicate their outputs. Examples include production systems, which model human problem-solving through condition-action rules, and connectionist models that simulate neural processing.

The Laws of Rationality approach focuses on thinking rationally. Rational agents should make correct inferences and reach logical conclusions. This approach draws heavily from logic, probability theory, and decision theory. Logic-based AI assumes that optimal thinking can be achieved through formal reasoning systems. However, this approach faces challenges in dealing with uncertainty and computational complexity.

The Rational Agent approach focuses on acting rationally. A rational agent is one that acts to achieve the best expected outcome, given its knowledge about the environment. This is the most general approach and the one adopted in modern AI research. It encompasses various techniques including search algorithms, probabilistic reasoning, and machine learning. The rational agent approach is particularly relevant to the Wumpus World problem, where the agent must act under uncertainty to achieve its goals.

### Components of an AI System

An AI system typically consists of several interconnected components that work together to exhibit intelligent behavior.

The perception subsystem enables the AI system to gather information about its environment. In the Wumpus World, this corresponds to the sensors that detect breeze, stench, glitter, and other percepts. Perception can involve various input modalities including cameras, microphones, sensors, and textual data.

The knowledge representation subsystem stores and organizes information that the AI system uses to understand its environment and make decisions. Knowledge can be represented using various formalisms including logic, semantic networks, frames, production rules, and probabilistic models. The choice of representation significantly impacts the system's reasoning capabilities.

The reasoning subsystem processes stored knowledge to draw conclusions, make predictions, and solve problems. Reasoning can be deductive (drawing specific conclusions from general principles), inductive (generalizing from examples), or abductive (inferring the most likely explanations for observations). In uncertain environments, probabilistic reasoning becomes essential.

The learning subsystem enables the system to improve its performance over time through experience. Learning can be supervised (learning from labeled examples), unsupervised (finding patterns in unlabeled data), or reinforcement (learning from rewards and punishments received for actions).

The action subsystem translates decisions into actual behavior or outputs. In the Wumpus World, actions include moving forward, turning left or right, and grabbing or shooting. Rational agents select actions that maximize expected utility.

### Types of AI Environments

AI systems operate in various types of environments that differ in their properties and the challenges they present.

Fully observable environments are those where the agent can perceive the complete state of the environment at each point in time. Chess is an example of a fully observable environment. Partially observable environments, like the Wumpus World, require the agent to reason about unobserved aspects based on limited perceptions.

Deterministic environments are those where the outcome of any action is completely determined by the current state and the action itself. Stochastic environments involve uncertainty in outcomes, where actions may have multiple possible results with associated probabilities.

Static environments remain unchanged while the agent is deliberating, while dynamic environments can change during the agent's decision-making process. Discrete environments have a finite number of distinct states and actions, while continuous environments involve infinite possibilities.

Single-agent environments involve only one intelligent entity, while multi-agent environments involve multiple AI systems that may cooperate or compete. Game playing represents a classic multi-agent environment where agents must consider the actions and strategies of opponents.

### Expert Systems

Expert systems represent a major application area of AI that is directly relevant to this module. An expert system is a computer program that encodes and applies expert knowledge to solve complex problems in a specific domain. Unlike general-purpose AI systems, expert systems are designed for narrow domains where human expertise is well-defined and can be articulated.

The architecture of an expert system typically includes a knowledge base containing domain knowledge, an inference engine that applies reasoning mechanisms to the knowledge base, a working memory that stores current facts and hypotheses, and user interface components that facilitate interaction with users.

Knowledge acquisition is the process of extracting knowledge from human experts and encoding it in a form that the system can use. This is often considered a bottleneck in expert system development due to the difficulty of articulating tacit knowledge. Knowledge representation formalisms used in expert systems include production rules (if-then statements), semantic networks, and frames.

Expert system shells are software tools that provide a ready-made framework for building expert systems without requiring programming from scratch. These shells include the inference engine and user interface, allowing developers to focus on encoding domain-specific knowledge.

## Examples

### Example 1: Wumpus World Agent

Consider the Wumpus World environment, a classic AI problem that demonstrates many key concepts. The agent starts in room [1,1], facing right. It perceives a breeze (B) from [1,2] or [2,1], but no stench, meaning no Wumpus is adjacent. From the initial position, the agent must reason about the contents of adjacent rooms.

The agent's knowledge base initially contains: "Starting at [1,1], breeze implies pit in [1,2] or [2,1]". Since there is no stench at [1,1], we know the Wumpus is not in [1,2] or [2,1]. After exploring and finding a pit at [2,1], the agent can conclude [1,2] is safe to visit. This demonstrates logical reasoning under uncertainty.

A rational agent in the Wumpus World uses probabilistic reasoning when multiple explanations are possible. If the agent detects both breeze and stench in a room, it must reason about the probabilities of pit and Wumpus placements in adjacent rooms. Bayes' rule, which you will study later in this module, enables the agent to update its beliefs based on new evidence.

### Example 2: Medical Diagnosis Expert System

A medical diagnosis expert system encodes knowledge from physicians to assist in diagnosing diseases. The knowledge base might contain rules such as: "IF patient has fever AND patient has cough AND patient has chest pain THEN patient might have pneumonia (probability: 0.7)".

The inference engine applies these rules to patient symptoms. If a patient presents with fever, cough, and chest pain, the system generates pneumonia as a hypothesis. Additional tests can be requested to confirm or rule out this hypothesis. The system uses uncertain reasoning, recognizing that symptoms rarely provide definitive diagnoses.

Explanation facilities allow the system to explain its reasoning to users. For instance, the system might explain: "I diagnosed pneumonia because the patient has fever, cough, and chest pain. In my knowledge base, 70% of patients with these symptoms have pneumonia."

### Example 3: Search-Based Problem Solving

A vacuum cleaner robot operating in a 2-room environment demonstrates search-based AI. The robot's goal is to clean both rooms. The state space includes which rooms are clean or dirty. The robot starts in one room and can move between rooms or suck dirt from the current room.

Using a simple search algorithm like breadth-first search, the robot explores states systematically: from initial state (Room A dirty, Room B dirty), it tries actions in sequence until both rooms are clean. This demonstrates how AI converts problem-solving into state space search, a fundamental technique applicable across many domains.

## Exam Tips

1. UNDERSTAND THE DIFFERENCE BETWEEN THE FOUR AI APPROACHES: Be clear about the distinction between thinking like a human versus thinking rationally, and acting like a human versus acting rationally. The rational agent approach is most relevant to modern AI and links directly to the Wumpus World problem.

2. KNOW THE COMPONENTS OF AN AI SYSTEM: Ensure you can identify and explain perception, knowledge representation, reasoning, learning, and action subsystems with examples.

3. EXPERT SYSTEMS ARE APPLICATION-FOCUSED: Remember that expert systems apply AI techniques to specific domains. Know the architecture components: knowledge base, inference engine, working memory, and user interface. Understand knowledge acquisition as a bottleneck process.

4. UNCERTAINTY IS CENTRAL TO THIS MODULE: The Wumpus World exemplifies AI under uncertainty. Study how agents handle partial observability, non-deterministic outcomes, and sequential decisions.

5. DIFFERENTIATE BETWEEN ENVIRONMENT TYPES: Know the distinctions between fully observable and partially observable, deterministic and stochastic, static and dynamic, discrete and continuous environments. Apply these to examples.

6. RELATE TO OTHER MODULE TOPICS: This AI chapter connects directly to probability, Bayes' rule, and expert systems. Expect questions that integrate concepts across topics in Module 5.

7. PRACTICE WITH THE WUMPUS WORLD: Many exam questions use the Wumpus World to test understanding of AI concepts. Ensure you can trace through agent reasoning and explain how percepts inform actions.