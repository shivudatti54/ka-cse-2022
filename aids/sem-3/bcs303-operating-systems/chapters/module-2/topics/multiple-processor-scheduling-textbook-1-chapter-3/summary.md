# **Multiple-Processor Scheduling Revision Notes**

## **Chapter 3: Fixed-Priority Scheduling**

- **Fixed-Priority Scheduling (FPS)**: A scheduling algorithm where each process is assigned a priority level and executed accordingly.
- **Priority Ceiling Scheduling (PCS)**: An extension of FPS where the priority of each process is adjusted dynamically based on the highest priority process in the ready queue.
- **Earliest Deadline First (EDF) Scheduling**: A real-time scheduling algorithm that assigns the shortest available time slice to the process with the earliest deadline.

## **Chapter 4: Rate Monotonic Scheduling (RMS)**

- **Rate Monoticonic Scheduling (RMS)**: A scheduling algorithm that assigns a time slice to each process based on its priority, which is determined by its period and deadline.
- **Period and Deadline**: The period is the time between two consecutive occurrences of a process, while the deadline is the time by which a process must be completed.

## **Chapter 5: Multilevel Feedback Queue (MLFQ) Scheduling**

- **Multilevel Feedback Queue (MLFQ) Scheduling**: A scheduling algorithm that divides the ready queue into multiple queues based on the priority of processes.
- **Feedback**: The time slice assigned to a process is based on the feedback from the output buffer of the process.

**Important Formulas and Definitions:**

- **Priority Ceiling**: The maximum priority that a process can be assigned, which is the maximum priority of the processes in the ready queue.
- **Rate Monotonic Scheduling Formula**: `T = (P_i) * (1 / (1 - (1 / D_i)))`, where `T` is the time slice, `P_i` is the period of process `i`, and `D_i` is the deadline of process `i`.
- **Multilevel Feedback Queue Formula**: `T = (1 / (1 - (1 / D_i))) / (1 + (1 / (D_i - T)))`, where `T` is the time slice, `D_i` is the deadline of process `i`, and `i` is the index of the process.
