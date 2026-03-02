# Network Flow, Max Flow, and Min Cut - Summary

## Key Definitions and Concepts

* Flow network: A directed graph with capacities on the edges.
* Flow: A function that assigns a non-negative value to each edge.
* Cut: A partition of the vertices into two sets.
* Max flow problem: Find the maximum possible flow from the source to the sink.
* Min cut problem: Find the minimum set of edges that, when removed, will disconnect the source from the sink.

## Important Formulas and Theorems

* Max-flow min-cut theorem: The maximum flow is equal to the minimum cut capacity.
* Ford-Fulkerson algorithm: A algorithm for solving the max flow problem.
* Edmonds-Karp algorithm: An implementation of the Ford-Fulkerson algorithm using BFS.

## Key Points

* The max flow problem and the min cut problem are dual problems.
* The Ford-Fulkerson algorithm and the Edmonds-Karp algorithm are used to solve these problems.
* The maximum flow is equal to the minimum cut capacity.
* The minimum cut is the set of edges that, when removed, will disconnect the source from the sink.
* The time complexity of the Ford-Fulkerson algorithm is O(E^2) and the Edmonds-Karp algorithm is O(VE^2).
* These concepts have numerous applications in computer networks, transportation systems, and logistics.

## Common Mistakes to Avoid

* Not understanding the definitions of flow network, flow, and cut.
* Not knowing the key concepts of the max flow problem and the min cut problem.
* Not being familiar with the Ford-Fulkerson algorithm and the Edmonds-Karp algorithm.
* Not practicing solving max flow and min cut problems.

## Revision Tips

* Review the definitions of flow network, flow, and cut.
* Practice solving max flow and min cut problems using the Ford-Fulkerson algorithm and the Edmonds-Karp algorithm.
* Understand the relationship between the max flow problem and the min cut problem.
* Review the time complexity of the Ford-Fulkerson algorithm and the Edmonds-Karp algorithm.