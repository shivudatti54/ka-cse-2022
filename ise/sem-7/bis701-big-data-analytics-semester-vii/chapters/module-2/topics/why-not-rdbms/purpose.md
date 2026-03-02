### Learning Purpose: Why not RDBMS?

**1. Importance:**
This topic is crucial as it establishes the fundamental limitations of traditional Relational Database Management Systems (RDBMS) in handling modern big data. Understanding these constraints is the first step toward justifying and adopting specialized big data technologies like Hadoop and NoSQL databases, which are designed for volume, velocity, and variety.

**2. What Students Will Learn:**
Students will learn to identify the specific technical and architectural shortcomings of RDBMS—such as lack of horizontal scalability, rigid schema, difficulty managing unstructured data, and high costs—that make them unsuitable for big data scenarios. They will analyze the CAP theorem and how RDBMS prioritizes consistency over availability and partition tolerance.

**3. Connection to Other Concepts:**
This knowledge directly connects to subsequent modules on distributed file systems (HDFS), NoSQL databases (Cassandra, MongoDB), and distributed processing frameworks (MapReduce, Spark). It provides the critical "why" behind the entire big data ecosystem, forming a foundational contrast against which new solutions are understood.

**4. Real-World Applications:**
This is applied when organizations must choose a database technology. For example, an RDBMS is perfect for transactional banking systems, but a social media platform analyzing petabytes of unstructured user data for trends would require a horizontally scalable NoSQL solution to avoid performance bottlenecks and inflexibility.