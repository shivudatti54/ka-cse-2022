# Learning Objectives
After studying this topic, you should be able to:
1.  Define the term "loop-carried dependency" and distinguish it from within-iteration dependencies.
2.  Identify and classify the three main types of loop-carried dependencies (flow, anti-, output) in a given code snippet.
3.  Correctly determine whether a given `for` loop can be parallelized with OpenMP based on its dependency structure.
4.  Apply the OpenMP `reduction` clause to correctly parallelize loops that perform associative and commutative operations (e.g., sum, product).
5.  Explain why using synchronization constructs (`critical`, `atomic`) inside a parallel loop often leads to poor performance.
6.  Describe at least one strategy (other than reduction) for handling or overcoming loop-carried dependencies.