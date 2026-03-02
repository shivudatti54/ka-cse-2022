# Learning Objectives
After studying this topic, you should be able to:
1.  Define what an execution plan is and explain its role in the query processing pipeline.
2.  Describe the function of common physical operators (e.g., Seq Scan, Index Scan, Nested Loops Join, Hash Join, Sort).
3.  Interpret a simple textual execution plan, identifying the flow of data from leaf nodes to the root.
4.  Analyze an execution plan to hypothesize why a specific operator was chosen (e.g., scan vs. index, type of join).
5.  Propose a database optimization (e.g., adding an index, updating statistics) based on the analysis of a given execution plan.
6.  Explain how outdated statistics can lead to suboptimal execution plan selection.