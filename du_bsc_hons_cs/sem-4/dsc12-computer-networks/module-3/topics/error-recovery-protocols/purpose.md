# Learning Objectives

After studying this topic, you should be able to:

1. Explain the fundamental need for error recovery protocols in computer networks and describe how ARQ mechanisms work.

2. Analyze the Stop-and-Wait ARQ protocol including its operation, sequence number usage, timeout mechanism, and performance limitations.

3. Implement and evaluate the Go-Back-N ARQ protocol, understanding the sliding window concept, cumulative acknowledgments, and retransmission strategy.

4. Compare and contrast Selective Repeat ARQ with Go-Back-N, explaining why selective retransmission improves throughput in high-delay networks.

5. Calculate channel utilization for Stop-and-Wait protocols and determine the minimum sequence number bits required for different window sizes in Go-Back-N and Selective Repeat.

6. Identify scenarios where each protocol is appropriate based on network characteristics such as error rate, propagation delay, and link bandwidth.

7. Analyze protocol behavior in edge cases including lost acknowledgments, duplicate frames, and frame reordering.