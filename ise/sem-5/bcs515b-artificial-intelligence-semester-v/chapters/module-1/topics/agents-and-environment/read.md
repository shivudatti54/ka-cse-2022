# Agents and Environment in Artificial Intelligence

## 1. Introduction to Agents

In Artificial Intelligence, an **agent** is anything that can be perceived as acting intelligently. More formally, an agent is an entity that perceives its **environment** through **sensors** and acts upon that environment through **actuators**.

This agent-environment interaction is the fundamental concept around which AI is built. Think of a human agent: eyes, ears, and other organs act as sensors; hands, legs, and mouth act as actuators. Similarly, a robotic agent might have cameras and infrared sensors, with motors and grippers as actuators. A software agent perceives its environment through keystrokes, file contents, and network packets, acting by displaying output, sending data, or writing files.

```
      [Sensors]  ->  [Percepts]
                    /
    Environment <- -> Agent
                    \
      [Actuators] <- [Actions]
```

_Figure 1: The Agent-Environment Interaction Loop_

## 2. The PEAS Framework

To define an agent's task clearly, we use the **PEAS** framework: Performance measure, Environment, Actuators, Sensors.

- **Performance Measure**: The objective criterion for success. How we determine if the agent is doing well.
- **Environment**: The external context in which the agent operates.
- **Actuators**: The means by which the agent acts on the environment.
- **Sensors**: The means by which the agent perceives the environment.

**Example: A Self-Driving Car**

| PEAS Component  | Description                                                                   |
| :-------------- | :---------------------------------------------------------------------------- |
| **P**erformance | Safety, destination reached quickly, legal driving, comfort, fuel efficiency. |
| **E**nvironment | Roads, other vehicles, pedestrians, traffic signs, weather conditions.        |
| **A**ctuators   | Steering wheel, accelerator, brake, turn signals, display screen.             |
| **S**ensors     | Cameras, LiDAR, radar, GPS, odometer, accelerometer.                          |

## 3. The Concept of Rationality

A **rational agent** is one that does the "right thing" given what it knows and what it has perceived. More technically, for each possible percept sequence, a rational agent should select an action that is expected to maximize its **performance measure**, based on the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

Rationality depends on four key factors:

1.  The performance measure that defines the criterion of success.
2.  The agent's prior knowledge of the environment.
3.  The actions that the agent can perform.
4.  The agent's complete percept sequence to date.

Rationality is not the same as omniscience (knowing the actual outcome of an action) or clairvoyance (knowing the future). A rational agent can make decisions based on incomplete information and might take an action that fails by bad luck, as long as the _expected_ outcome was the best possible.

## 4. The Nature of Environments: Task Environments

The problems faced by agents are defined by their **task environment**. Specifying the task environment is essentially defining the problem the agent is meant to solve. We can classify environments along several key dimensions.

### 4.1. Properties of Task Environments

1.  **Fully Observable vs. Partially Observable**
    - **Fully Observable**: The agent's sensors give it complete access to the relevant state of the environment at each point in time (e.g., a crossword puzzle).
    - **Partially Observable**: The agent lacks full awareness of the environment state (e.g., a poker game with hidden cards, a self-driving car with blind spots). Most real-world environments are partially observable.

2.  **Single Agent vs. Multi-Agent**
    - **Single Agent**: An environment containing only one agent (e.g., solving a crossword puzzle alone).
    - **Multi-Agent**: An environment containing other agents who may be competitive or cooperative (e.g., chess, driving alongside other cars). The presence of other agents introduces strategic complexity.

3.  **Deterministic vs. Stochastic**
    - **Deterministic**: The next state of the environment is completely determined by the current state and the action executed by the agent (e.g., a game of chess where the rules are fixed).
    - **Stochastic**: The next state has an element of randomness or uncertainty; it is not completely predictable (e.g., rolling dice in a board game, the behavior of other drivers).

4.  **Episodic vs. Sequential**
    - **Episodic**: The agent's experience is divided into atomic "episodes." In each episode, the agent perceives and then performs a single action. The choice of action in one episode does not depend on previous episodes (e.g., an image classification agent).
    - **Sequential**: The current decision affects future decisions. The agent must plan ahead and consider long-term consequences (e.g., playing chess, navigating a maze).

5.  **Static vs. Dynamic**
    - **Static**: The environment does not change while the agent is deliberating (thinking) (e.g., a crossword puzzle).
    - **Dynamic**: The environment can change while the agent is deliberating, forcing it to act continuously (e.g., driving a taxi—the world changes while you decide your next move).

6.  **Discrete vs. Continuous**
    - **Discrete**: The environment has a finite number of distinct states, percepts, and actions (e.g., a game of tic-tac-toe).
    - **Continuous**: The state, percepts, or actions vary smoothly over a range (e.g., driving a car, where speed and steering angle are continuous).

7.  **Known vs. Unknown**
    - **Known**: The outcomes for all actions are given (the "laws of physics" of the environment are known to the agent).
    - **Unknown**: The agent does not know how the environment works and must learn it through experience.

The simplest environment is Fully Observable, Deterministic, Episodic, and Static. Real-world problems often fall on the more complex end of these spectra: Partially Observable, Stochastic, Sequential, Dynamic, and Continuous.

## 5. The Structure of Agents: Agent Programs

The agent's architecture is the physical or computational infrastructure (the computer, sensors, actuators). The **agent program** is the function that implements the mapping from percept sequences to actions. This program runs on the agent architecture.

```
Percept Sequence -> [Agent Program] -> Action
```

_Figure 2: The Agent Program_

We can design different types of agents based on their internal structure and complexity.

### 5.1. Simple Reflex Agents

These are the simplest agents. They act based on the _current percept_, ignoring the percept history. They use condition-action rules: `if percept then action`.

```
      [Sensors] -> [Condition-Action Rules] -> [Actuators]
```

_Figure 3: Simple Reflex Agent_

- **Pros**: Simple, fast.
- **Cons**: Limited intelligence; cannot operate in partially observable environments. They have no memory.

### 5.2. Model-Based Reflex Agents

These agents maintain an internal **state** that depends on the percept history, effectively allowing them to handle partially observable environments. The internal state is updated based on how the agent thinks the world works (a **model** of the world).

```
      [Sensors] -> [Update Internal State] -> [State] -> [Condition-Action Rules] -> [Actuators]
                         ^
                         |
                  [Model of World]
```

_Figure 4: Model-Based Reflex Agent_

- **Pros**: Can operate in partially observable environments.
- **Cons**: Still reactive; doesn't explicitly consider the future.

### 5.3. Goal-Based Agents

These agents have an internal state and a **goal**. They act not just based on the current state but also consider which actions will help them achieve their goal. This requires searching and planning.

```
      [Sensors] -> [Update State] -> [State] -> [Goals] -> [Decide Action] -> [Actuators]
                         ^                           |
                         |                    [Search/Planning]
                  [Model of World]
```

_Figure 5: Goal-Based Agent_

- **Pros**: More flexible than reflex agents; can make decisions that are good in the long term.
- **Cons**: Decision-making can be computationally expensive.

### 5.4. Utility-Based Agents

Goals are often binary (achieved/not achieved). A **utility function** maps a state (or sequence of states) to a real number, representing the agent's degree of happiness or satisfaction. A utility-based agent acts to maximize its expected utility.

```
      [Sensors] -> [Update State] -> [State] -> [Utility] -> [Decide Action] -> [Actuators]
                         ^                           |
                         |                    [Optimization]
                  [Model of World]
```

_Figure 6: Utility-Based Agent_

- **Pros**: Can compare different goal states and choose the best one. Can handle trade-offs (e.g., speed vs. safety).
- **Cons**: Most complex; requires a well-defined utility function.

### 5.5. Learning Agents

A learning agent can improve its performance over time. It has a **performance element** (which is responsible for selecting actions, like the agents above) and a **learning element** (which is responsible for making improvements). The learning element uses feedback from a **critic** and suggestions from a **problem generator**.

```
[Performance Element] -> [Actuators] -> [Environment] -> [Sensors]
      ^                       |                             |
      |                [Critic] -> [Feedback]               |
      |                       |                             |
[Learning Element] <-> [Knowledge] <-----------------------/
      ^
      |
[Problem Generator] -> [Exploratory Actions]
```

_Figure 7: Learning Agent_

## 6. Exam Tips

- **PEAS is Key**: Always start analyzing an agent by defining its PEAS. This clarifies the problem.
- **Environment Classification**: Be prepared to classify a given task environment using the seven properties (Observable, Multi-agent, etc.). Real-world is often Partially Observable, Stochastic, Sequential, Dynamic.
- **Rationality vs. Perfection**: Remember that a rational agent maximizes _expected_ performance, not guaranteed success. Luck is a factor.
- **Agent Types**: Understand the progression from Simple Reflex to Learning Agents. Know which type is suited for which kind of environment.
- **Utility over Goals**: For complex decisions where there are multiple "good" outcomes, a utility-based agent is necessary to choose the _best_ one.
- **Draw the Diagrams**: Practice drawing the agent-environment interaction loop and the internal structures of the different agent types. A clear diagram can often explain a concept faster than words.
