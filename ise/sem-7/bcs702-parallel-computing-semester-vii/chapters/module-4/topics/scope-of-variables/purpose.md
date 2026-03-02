# Learning Objectives
After studying this topic, you should be able to:
1.  Define and distinguish between shared and private variable scope in the context of OpenMP.
2.  Predict the default data-sharing attribute of a variable based on its declaration context and the OpenMP construct it is used in.
3.  Correctly apply the `private`, `firstprivate`, `lastprivate`, `shared`, and `default` clauses to control variable scope.
4.  Implement the `reduction` clause to correctly and efficiently perform collective operations like sum or max across multiple threads.
5.  Identify potential race conditions in OpenMP code caused by improper variable scoping and propose solutions to fix them.
6.  Explain the purpose and benefit of using `default(none)` to enforce explicit variable scoping.