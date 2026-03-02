# Agents and Environment

## Introduction

Agents and Environment is a foundational concept in Artificial Intelligence that forms the basis for understanding how intelligent systems interact with the world around them. The agent paradigm provides a unified framework for designing and analyzing AI systems, from simple automated systems to complex autonomous robots.

In the context of 's Artificial Intelligence syllabus, this topic serves as the building block for understanding all subsequent AI techniques. An **agent** is any entity that perceives its environment through sensors and acts upon that environment through actuators. This simple yet powerful abstraction allows us to model a wide variety of systems, including thermostat controllers, chess-playing programs, autonomous vehicles, and even human beings.

The study of agents and environments is crucial because it defines the problem space for AI. By clearly specifying what an agent can perceive and what actions it can perform, we establish the boundaries within which intelligent behavior must be achieved. This framework helps AI practitioners make informed decisions about agent architecture, environment characteristics, and appropriate algorithms for different scenarios.

## Key Concepts

### Agent Definition

An **intelligent agent** is a computer program or system that:

- **Perceives** its environment through sensors
- **Reasons** about the perceived information
- **Acts** upon the environment through actuators
- **Learns** from past experiences to improve performance

The relationship between agent and environment is cyclical: the agent takes actions that change the environment, which in turn produces new percepts that the agent must respond to.

### Agent Function and Agent Program

The **agent function** is a mathematical mapping from percept histories to actions. It represents the ideal behavior of an agent - what the agent _should_ do for every possible percept sequence. This function is often called the **agent program**.

The agent function is an abstract description, while the **agent program** is a concrete implementation. For a given agent, we can represent:

```
Agent Function: f: P* → A
where P* is the set of all possible percept sequences
 A is the set of all possible actions
```

### Rationality and Performance Measures

A **rational agent** is one that selects actions that maximize its expected performance measure, given the percept sequence and the agent's built-in knowledge. Rationality depends on:

1. **Performance Measure**: The criteria that define success (e.g., points scored in a game, distance traveled, money saved)
2. **Percept Sequence**: What the agent has perceived so far
3. **Prior Knowledge**: What the agent knows about the environment initially
4. **Available Actions**: What actions the agent can perform
5. **Learning Capabilities**: The agent's ability to improve its performance

**Important**: Rationality is about _expected_ performance, not guaranteed success. A rational agent may sometimes make mistakes if its knowledge is incomplete.

### PEAS Description

To properly specify a task environment, we use the **PEAS** framework:

- **P**erformance Measure: The criterion for evaluating agent behavior
- **E**nvironment: The setting in which the agent operates
- **A**ctuators: The means by which the agent affects the environment
- **S**ensors: The means by which the agent perceives the environment

**Example - Autonomous Driving Agent:**

- Performance Measure: Safety, destination reached, time taken, comfort, legal compliance
- Environment: Roads, traffic, pedestrians, weather conditions
- Actuators: Steering wheel, accelerator, brake, signals, horn
- Sensors: Cameras, LIDAR, radar, GPS, speedometer

### Environment Types

Environments can be classified based on several properties:

1. **Fully Observable vs. Partially Observable**: Can the agent perceive the complete state of the environment at each point in time?

- Fully observable: Chess with visible board
- Partially observable: Poker (cards hidden), real-world driving

2. **Deterministic vs. Stochastic**: Is the next state completely determined by the current state and action?

- Deterministic: Mathematical puzzles, chess
- Stochastic: Weather prediction, medical diagnosis

3. **Episodic vs. Sequential**: Does each episode depend on previous episodes?

- Episodic: Classification tasks, spam detection
- Sequential: Game playing, navigation

4. **Static vs. Dynamic**: Does the environment change while the agent is thinking?

- Static: Crossword puzzles
- Dynamic: Real-time strategy games, driving

5. **Discrete vs. Continuous**: Are there clearly defined states and actions?

- Discrete: Chess board positions
- Continuous: Robot arm movement, temperature control

6. **Single-agent vs. Multi-agent**: Are other agents present?

- Single-agent: Puzzle solving
- Multi-agent: Poker, autonomous vehicles

### Agent Types/Architectures

**1. Simple Reflex Agent**

- Acts only on the current percept
- Uses condition-action rules
- Works only in fully observable environments
- Example: Thermostat controlling temperature

**2. Model-Based Reflex Agent**

- Maintains internal state representing unobserved aspects
- Uses a model of how the world works
- Can handle partially observable environments
- Example: Vacuum cleaner with dirt sensor memory

**3. Goal-Based Agent**

- Considers future consequences of actions
- Has a goal or set of goals to achieve
- Uses search and planning algorithms
- Example: GPS navigation system

**4. Utility-Based Agent**

- Considers not just goals but quality of outcomes
- Has a utility function to compare different states
- Can handle trade-offs between multiple objectives
- Example: Autonomous vehicle balancing speed vs. safety

**5. Learning Agent**

- Can improve performance over time through learning
- Has four components: learning element, performance element, critic, and problem generator
- Adapts to new environments and situations
- Example: AlphaGo learning from playing games

## Examples

### Example 1: Vacuum Cleaner Agent

**Problem**: Design an agent to clean a two-room environment.

**PEAS Description:**

- Performance Measure: Amount of dirt cleaned in time T
- Environment: Two rooms (A and B), possibly with dirt
- Actuators: Move left/right, suck dirt
- Sensors: Dirt detector, location sensor

**Agent Program (Simple Reflex):**

```
function REFLEX-VACUUM-AGENT([location, status]) returns action
 if status = Dirty then return Suck
 else if location = A then return Right
 else if location = B then return Left
```

**Analysis**: This is a simple reflex agent that works in a fully observable, deterministic, episodic environment. It doesn't use any internal state or model.

### Example 2: Chess-Playing Agent

**Problem**: Design an agent to play chess.

**PEAS Description:**

- Performance Measure: Win/Lose/Draw, points scored
- Environment: Chess board with all pieces visible
- Actuators: Move a piece according to chess rules
- Sensors: Visual input of the board

**Environment Properties:**

- Fully observable (chess board is visible)
- Deterministic (moves have predictable effects)
- Sequential (history matters)
- Static (environment doesn't change during thinking)
- Discrete (finite states and moves)
- Multi-agent (opponent present)

**Agent Type**: Goal-based with utility function (minimax algorithm with alpha-beta pruning)

### Example 3: Medical Diagnosis Agent

**Problem**: Design an agent to diagnose patient conditions.

**PEAS Description:**

- Performance Measure: Accurate diagnosis, patient recovery, treatment cost
- Environment: Patient records, symptoms, test results
- Actuators: Order tests, prescribe treatments, refer to specialists
- Sensors: Patient history, examination results, test reports

**Environment Properties:**

- Partially observable (not all symptoms visible, underlying disease hidden)
- Stochastic (patients may respond unpredictably)
- Sequential (treatment affects future states)
- Dynamic (patient condition changes over time)
- Continuous (symptoms can take any value)
- Multi-agent (doctor, patient, specialists)

**Agent Type**: Utility-based, combining probability (Bayesian networks) with utility theory

## Exam Tips

1. **Remember PEAS**: Always describe any agent using Performance measure, Environment, Actuators, and Sensors - this is a favorite exam question.

2. **Know all environment properties**: Fully/Partially observable, Deterministic/Stochastic, Episodic/Sequential, Static/Dynamic, Discrete/Continuous, Single/Multi-agent.

3. **Differentiate agent types**: Simple reflex (no state), Model-based (internal state), Goal-based (future consideration), Utility-based (prefers better outcomes), Learning (improves over time).

4. **Rationality ≠ Omniscience**: A rational agent makes the best decision given its percepts and knowledge - it cannot predict the future perfectly.

5. **Environment determines agent complexity**: Simple environments allow simple agents; complex environments require sophisticated architectures.

6. **Fully observable environments can use simple reflex**: When the agent can see everything, condition-action rules work well.

7. **Partial observability requires internal state**: Agents need memory to track what they cannot currently perceive.

8. **Real-world applications**: Understand how concepts apply to autonomous vehicles, chatbots, robotics, and game-playing systems.

9. **Agent program vs Agent function**: The function is the specification (what to do), the program is the implementation (how to do it).

10. **PEAS is essential for problem definition**: Before designing any AI solution, always define PEAS to clarify the task.
