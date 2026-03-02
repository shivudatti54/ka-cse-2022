# **Multiple-Processor Scheduling RevisionNotes**

## **Chapter 3: Scheduling Algorithms for Multiple Processors**

- **3.1: First-Come-First-Served (FCFS) Scheduling**
  - Suitable for multiple processors: No
  - Advantages: Simple to implement, fair scheduling
  - Disadvantages: Inefficient use of processors, no priority scheduling
- **3.2: Shortest Job First (SJF) Scheduling**
  - Suitable for multiple processors: No
  - Advantages: Efficient use of processors, minimal wait time
  - Disadvantages: May lead to starvation, no priority scheduling
- **3.3: Priority Scheduling (PS)**
  - Suitable for multiple processors: Yes
  - Advantages: Fair scheduling, efficient use of processors
  - Disadvantages: Complex implementation, priority ordering
- **3.4: Round Robin (RR) Scheduling**
  - Suitable for multiple processors: Yes
  - Advantages: Fair scheduling, efficient use of processors
  - Disadvantages: Short burst time, priority ordering

## **Chapter 4: Scheduling Algorithms for Multiple Processors**

- **4.1: Multilevel Feedback Queue (MFQ) Scheduling**
  - Suitable for multiple processors: Yes
  - Advantages: Efficient use of processors, minimal wait time
  - Disadvantages: Complex implementation, priority ordering
- **4.2: Earliest Deadline First (EDF) Scheduling**
  - Suitable for multiple processors: Yes
  - Advantages: Fair scheduling, efficient use of processors
  - Disadvantages: Priority ordering, complex implementation
- **4.3: Rate Monotonic Scheduling (RMS)**
  - Suitable for multiple processors: Yes
  - Advantages: Fair scheduling, efficient use of processors
  - Disadvantages: Priority ordering, complex implementation
- **4.4: Deadlock Prevention Techniques**
  - Banker's algorithm
  - Eden's algorithm
  - Safety intervals

## **Chapter 5: Scheduling Algorithms for Real-Time Systems**

- **5.1: Rate Monotonic Scheduling (RMS)**
  - Suitable for real-time systems: Yes
  - Advantages: Fair scheduling, efficient use of processors
  - Disadvantages: Priority ordering, complex implementation
- **5.2: Earliest Deadline First (EDF) Scheduling**
  - Suitable for real-time systems: Yes
  - Advantages: Fair scheduling, efficient use of processors
  - Disadvantages: Priority ordering, complex implementation
- **5.3: Fixed Priority Scheduling**
  - Suitable for real-time systems: Yes
  - Advantages: Simple to implement, fair scheduling
  - Disadvantages: Priority ordering, may lead to starvation
- **5.4: Priority Inheritance**
  - Suitable for real-time systems: Yes
  - Advantages: Efficient use of processors, minimal wait time
  - Disadvantages: Priority ordering, complex implementation

## **Important Formulas and Definitions**

- **Turnaround time**: Time taken by a process to complete its execution
- **Waiting time**: Time a process spends waiting in the ready queue
- **Burst time**: Time a process occupies the processor
- **Response time**: Time taken by the system to respond to a request
- **Average time**: Average time a process spends in the ready queue
- **Priority ordering**: Ordering processes based on their priority
