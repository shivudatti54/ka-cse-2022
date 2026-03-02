# Intelligent Agents and Environment Structure

## Introduction
In Artificial Intelligence, an **intelligent agent** is a computational entity that perceives its environment through sensors and acts upon it via actuators. The study of agents and their environments is fundamental to understanding AI systems, as per the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science. This summary covers key concepts for exam revision.

## Key Concepts

### 1. Intelligent Agent Definition
- An agent is a system that makes decisions based on **percepts** (sensory inputs) to achieve **goals**.
- The **agent function** maps percept sequences to actions, implemented via an **agent program**.

### 2. Agent Structure
- **Sensors**: Perceive environment (e.g., cameras, microphones).
- **Actuators**: Execute actions (e.g., motors, speakers).
- **Performance Measure**: Evaluates agent's success (e.g., score, efficiency).
- **PEAS Framework**: Performance, Environment, Actuators, Sensors—used to specify agent tasks.

### 3. Types of Intelligent Agents
- **Simple Reflex Agents**: Act on current percept using condition-action rules; limited to fully observable, deterministic environments.
- **Model-Based Reflex Agents**: Maintain internal state (model of world) to handle partial observability.
- **Goal-Based Agents**: Use goal information to plan actions; more flexible than reflex agents.
- **Utility-Based Agents**: Optimize a utility function to maximize satisfaction; handle trade-offs.
- **Learning Agents**: Improve performance over time through feedback (reinforcement learning); include a learning element, performance element, and critic.

### 4. Environment Structure
- **Observable vs. Partially Observable**: Fully accessible environments provide complete percept information.
- **Deterministic vs. Stochastic**: Deterministic environments have predictable outcomes; stochastic ones involve uncertainty.
- **Episodic vs. Sequential**: Episodic environments have independent episodes; sequential actions affect future states.
- **Static vs. Dynamic**: Dynamic environments change over time; static environments remain constant during agent reasoning.
- **Discrete vs. Continuous**: Discrete environments have finite states/actions; continuous ones involve continuous variables.
- **Single-Agent vs. Multi-Agent**: Multi-agent environments involve interactions with other agents (competition or cooperation).

### 5. Rationality
- A rational agent chooses actions to maximize its performance measure based on percept history and available knowledge.
- Rationality depends on the environment, capabilities, and goals.

## Conclusion
Understanding intelligent agents and their environment structures is crucial for designing AI systems. Focus on the types of agents, PEAS, and environment properties for exams. Practice mapping real-world scenarios to agent types and environment classifications. Refer to Delhi University syllabus modules for detailed study.