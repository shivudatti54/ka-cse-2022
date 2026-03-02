**Subject: Introduction to Artificial Intelligence (18CS71)**
**Module 5: A Modern Approach**

### Introduction to A Modern Approach

The field of Artificial Intelligence is vast and has evolved through various paradigms. "A Modern Approach" refers to the influential textbook *Artificial Intelligence: A Modern Approach* (AIMA) by Stuart Russell and Peter Norvig. This text has become a cornerstone for AI education worldwide, including at . It provides a unified, structured framework for understanding AI, moving beyond a collection of isolated techniques. This module introduces the core structure and philosophy of this modern approach, which organizes the vast field of AI around the concept of rational agents.

---

### Core Concepts Explained

#### 1. The Intelligent Agent

The central concept in the modern approach is the **Agent**. An agent is anything that can perceive its environment through **sensors** and act upon that environment through **actuators**. This is a powerful abstraction that applies to everything from a simple thermostat to a sophisticated humanoid robot.

*   **Percept:** A single unit of sensory input (e.g., a pixel, a temperature reading, a sound wave).
*   **Percept Sequence:** The complete history of everything the agent has perceived so far.
*   **Action:** The output of the agent that affects the environment.

The job of AI is to design the **agent function**, which maps any given percept sequence to an action. The physical machinery that runs this function is the **agent program**.

#### 2. The PEAS Description

To specify the task environment for an agent clearly, we use the **PEAS** framework:

*   **P**erformance: How do we measure the agent's success? (e.g., profit, accuracy, speed).
*   **E**nvironment: What world does the agent operate in?
*   **A**ctuators: What can the agent *do*? (e.g., move, turn, speak, print).
*   **S**ensors: What can the agent *perceive*? (e.g., camera, GPS, keyboard input).

**Example: Self-Driving Car**
*   **Performance:** Safety, journey time, fuel efficiency, traffic law compliance.
*   **Environment:** Roads, other vehicles, pedestrians, weather conditions.
*   **Actuators:** Steering wheel, accelerator, brake, turn signals, display screen.
*   **Sensors:** Cameras, LIDAR, radar, GPS, odometer.

#### 3. Types of Agents

A key insight is that not all agents are created equal. The modern approach categorizes agents based on their internal design, which dictates their capability and intelligence.

1.  **Simple Reflex Agents:** These act based on the current percept only, using condition-action rules (e.g., `IF car-in-front-is-braking THEN apply-brake`). They are simple but fail in partially observable environments.
2.  **Model-Based Reflex Agents:** These maintain an internal **state** that depends on the percept history, effectively building a model of the world they cannot fully see. This state helps them handle partial observability.
3.  **Goal-Based Agents:** These agents have a goal (a desired state of the world) and consider the future consequences of their actions. They use **search** and **planning** techniques to find a sequence of actions that will achieve their goal.
4.  **Utility-Based Agents:** When there are multiple goals or conflicting ways to achieve a goal, a utility function (which measures the "happiness" of the agent) is used to choose the best possible action. This is the most general and powerful type of agent.

#### 4. Types of Environments

The nature of the environment plays a crucial role in determining the appropriate agent design. Environments can be characterized along several dimensions:

*   **Fully vs. Partially Observable:** Can the agent see the complete state of the environment?
*   **Deterministic vs. Stochastic:** Is the next state completely determined by the current state and action? (Or is there uncertainty?)
*   **Episodic vs. Sequential:** Is each action an independent "episode," or do previous actions affect future ones?
*   **Static vs. Dynamic:** Does the environment change while the agent is deliberating?
*   **Discrete vs. Continuous:** Are the percepts, states, time, and actions distinct and finite?

Understanding these properties helps an AI engineer select the right algorithms and agent architecture for the problem.

---

### Key Points & Summary

*   **Agent-Centric View:** The modern approach organizes AI around the concept of a **rational agent**—one that acts to achieve the best expected outcome.
*   **Unified Framework:** It provides a structured way to think about all AI problems, from simple to complex, using the common language of agents, environments, sensors, and actuators.
*   **PEAS Specification:** A critical first step in designing any AI system is to formally define its Performance, Environment, Actuators, and Sensors.
*   **Spectrum of Agents:** Agent designs range from simple reflex-based systems to advanced utility-based systems that reason about the future. The choice depends on the complexity of the environment and the task.
*   **Environment Properties:** The characteristics of the environment (observable, deterministic, etc.) are fundamental constraints that dictate which AI techniques will be effective.

This agent-based framework is not just theoretical; it is the practical foundation upon which modern AI systems like autonomous vehicles, recommendation systems, and game-playing agents are built and understood.