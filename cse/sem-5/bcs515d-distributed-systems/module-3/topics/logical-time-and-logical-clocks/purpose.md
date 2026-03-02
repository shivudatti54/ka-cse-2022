# Learning Objectives

After studying this topic, you should be able to:

1. Explain the limitations of physical clocks in distributed systems and why logical time is necessary.

2. Define and apply the happened-before relation (→) to determine causal ordering between events.

3. Implement and trace Lamport logical clocks, including the clock update rules for local events, message sending, and message receiving.

4. Differentiate between Lamport logical clocks and vector clocks, explaining the advantages of vector clocks in detecting causality.

5. Apply vector clock operations to track causal relationships and identify concurrent events in distributed scenarios.

6. Explain how logical clocks are used in practical distributed system applications like mutual exclusion, checkpointing, and replicated data management.

7. Analyze event ordering scenarios and determine whether events are causally related or concurrent using appropriate clock mechanisms.

8. Evaluate trade-offs between different logical clock approaches in terms of complexity, space requirements, and causal tracking capability.
