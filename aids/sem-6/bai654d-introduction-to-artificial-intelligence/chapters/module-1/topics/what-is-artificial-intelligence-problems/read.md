# What is Artificial Intelligence? Problems

## Introduction

Artificial Intelligence (AI) represents one of the most transformative technological frontiers of our era, fundamentally reshaping how we conceptualize machine capabilities and human-computer interaction. At its core, AI refers to the simulation of human intelligence processes by machines, encompassing learning, reasoning, problem-solving, perception, and language understanding. The discipline emerged from the foundational work of pioneers like Alan Turing, who proposed the famous "Turing Test" as a criterion for machine intelligence, and John McCarthy, who coined the term "Artificial Intelligence" in 1956 at the Dartmouth Conference.

In the context of computer science and specifically within problem spaces and search methodologies, understanding AI requires examining how machines can be programmed to solve complex problems through systematic exploration of possible solutions. This perspective treats intelligence not as an abstract concept but as a practical problem-solving capability. The importance of studying AI extends far beyond academic curiosity—it powers recommendation systems, autonomous vehicles, medical diagnosis tools, and intelligent personal assistants that have become integral to modern life. For students at the University of Delhi, mastering AI fundamentals provides a competitive edge in today's technology-driven job market, where organizations across sectors seek professionals who understand intelligent systems design and implementation.

## Key Concepts

### Definition of Artificial Intelligence

Artificial Intelligence can be defined from two complementary perspectives: the thinking approach and the acting approach. From the thinking perspective, AI aims to make machines think cognitively like humans—to process information, learn from experience, and draw conclusions. From the acting perspective, AI focuses on creating systems that behave intelligently, regardless of whether their internal processes mirror human thought. Modern AI predominantly follows the acting approach, prioritizing practical performance over strict adherence to human cognitive models.

The field encompasses several subdomains including machine learning (systems that learn from data), natural language processing (enabling machines to understand and generate human language), computer vision (interpreting visual information), robotics (physical manipulation and navigation), and expert systems (domain-specific problem solving). Each subdomain contributes unique capabilities to the broader goal of creating intelligent machines.

### Classification of Problems in AI

Problems in AI are broadly classified into two categories based on their well-defined nature. **Well-defined problems** have clear initial states, goal states, and operators—examples include the 8-puzzle, chess, and route-finding problems. These problems can be formally represented and solved using search algorithms. **Ill-defined problems** lack clear specifications for one or more components—examples include natural language understanding, image recognition, and creative tasks. Ill-defined problems often require additional context, common sense reasoning, or learning from examples.

### Problem Representation Components

Every AI problem requires careful formulation through four essential components. The **initial state** represents where problem-solving begins—for instance, the starting configuration of a puzzle or the starting location in a navigation problem. The **goal state** or goal test defines what constitutes a successful solution, whether it's a specific configuration (solved puzzle) or a condition (reaching destination). **Operators** (or successor functions) describe the legal actions that can transform one state into another, including the conditions under which each operator applies and the cost associated with using it. The **path cost** measures the expense of following a particular sequence of operators, which becomes crucial when searching for optimal solutions.

### Problem Space and State Space

The **problem space** encompasses all possible states that can be reached from the initial state through any sequence of operator applications—essentially the entire landscape of the problem. The **state space** is a formal representation of this problem space, typically visualized as a graph where nodes represent states and edges represent operator applications. Understanding the structure of state spaces is fundamental to selecting appropriate search strategies, as the size, connectivity, and topology of these spaces directly impact algorithm performance.

### Common Problem Types in AI

AI practitioners frequently encounter several standard problem types. **Toy problems** like the 8-queens problem, missionaries and cannibals puzzle, and cryptarithmetic problems serve as simplified domains for testing and illustrating algorithms. **Real-world problems** include route finding (GPS navigation), touring problems (traveling salesman), VLSI layout, robot navigation, and automatic assembly sequencing. Each problem type presents unique challenges: combinatorial explosion in large state spaces, uncertainty in real-world environments, and the need for efficient heuristic evaluation.

## Examples

### Example 1: The 8-Puzzle Problem

Consider the classic 8-puzzle consisting of a 3×3 grid with eight numbered tiles and one empty space. The goal is to arrange tiles in order from 1 to 8 by sliding them into the empty space.

**Formulating the problem:**
- **Initial state:** Any random configuration of the eight tiles
- **Goal state:** Tiles arranged as [1,2,3,4,5,6,7,8,blank] in row-major order
- **Operators:** Move blank up, down, left, or right (if possible)
- **Path cost:** Each move costs 1; total cost equals number of moves

The state space contains 181,440 reachable states, manageable for systematic search but large enough to require intelligent strategies. Blind search would explore thousands of states before finding the goal, while heuristic search using misplaced tile count or Manhattan distance can solve puzzles efficiently.

### Example 2: Route Finding Problem

A robot must navigate from location A to location B through a network of connected locations.

**Formulating the problem:**
- **Initial state:** Starting location (node A in a graph)
- **Goal state:** Destination location (node B)
- **Operators:** Move to adjacent connected locations
- **Path cost:** Distance or travel time between locations

This formulation illustrates how real-world problems map to graph search. The challenge lies in efficiently finding the shortest path through potentially massive networks—modern GPS systems solve variations of this problem involving millions of nodes and edges in milliseconds.

### Example 3: Water Jug Problem

Given two jugs with capacities 4 liters and 3 liters and an unlimited water supply, measure exactly 2 liters in one jug.

**Formulating the problem:**
- **Initial state:** Both jugs empty (0,0)
- **Goal state:** Either jug contains exactly 2 liters: (2,0), (0,2), or (1,2)
- **Operators:** Fill large jug, fill small jug, empty large jug, empty small jug, pour large to small, pour small to large
- **Path cost:** Each operator action costs 1

This problem demonstrates how simple operators can generate complex state spaces. Students can manually explore the state transitions to understand how search algorithms explore possibilities systematically.

## Exam Tips

1. **Memorize the four components of problem formulation**: initial state, goal state, operators, and path cost—these form the foundation of problem representation in AI and frequently appear in exam questions.

2. **Differentiate between well-defined and ill-defined problems**: Well-defined problems have clear specifications for all components, while ill-defined problems lack this precision. Provide examples of each type in your answers.

3. **Understand the relationship between problem space and state space**: The problem space is the conceptual landscape; the state space is its formal graph representation with nodes and edges.

4. **Know the distinction between toy problems and real-world problems**: Toy problems simplify complex concepts for study; real-world problems have practical applications in industry and research.

5. **Be able to formulate new problems using the four-component model**: Practice transforming verbal problem descriptions into formal problem representations—this skill is essential for algorithm application.

6. **Remember that operator costs matter for optimal solutions**: When a problem asks for the "best" or "optimal" solution, consider path costs in your analysis.

7. **Connect AI problem-solving to search algorithms**: Recognize that problem formulation determines which search strategy (uninformed or heuristic) will be most effective.

8. **Practice drawing state spaces for simple problems**: Visualizing problems as graphs helps understand how search algorithms traverse the problem space.