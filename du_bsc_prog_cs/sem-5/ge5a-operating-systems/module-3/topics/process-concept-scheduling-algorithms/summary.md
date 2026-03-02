# Process Concept & Scheduling Algorithms

**Introduction**  
A process is an executing program and the OS must manage its lifecycle from creation to termination. Scheduling decides which ready process runs on the CPU, directly affecting system performance and responsiveness. This summary follows the Delhi University BSc (H) Computer Science syllabus (NEP 2024) under the “Process Management” module.

**Process Concept**  
- **Process:** An instance of a program in execution, represented by a **Process Control Block (PCB)** containing PID, state, program counter, registers, memory‑management info, I/O status.  
- **Process States:** New → Ready → Running → Blocked (Waiting) → Terminated.  
- **Context Switch:** Saving/restoring the CPU state when switching from one process to another.

**Levels of Scheduler**  
- **Long‑term Scheduler:** Admit processes to the ready queue; controls degree of multiprogramming.  
- **Short‑term (CPU) Scheduler:** Selects a process from the ready queue for the CPU; invoked frequently.  
- **Medium‑term Scheduler:** Temporarily swaps out processes to reduce the degree of multiprogramming.

**Scheduling Criteria**  
- CPU Utilization (keep the CPU busy)  
- Throughput (processes completed per unit time)  
- Turnaround Time (completion time – arrival time)  
- Waiting Time (time spent in the ready queue)  
- Response Time (first response from request)

**Scheduling Algorithms**  

*Non‑preemptive*  
- **First‑Come, First‑Served (FCFS):** Simple FIFO; suffers from convoy effect.  
- **Shortest Job First (SJF):** Picks the shortest next CPU burst; optimal for average waiting time (non‑preemptive).  
- **Priority Scheduling:** Highest‑priority process runs first; may cause starvation.

*Preemptive*  
- **Round Robin (RR):** Time‑slice quantum; fair and responsive.  
- **Shortest Remaining Time First (SRTF):** Preemptive version of SJF; favors shorter jobs.  
- **Priority (preemptive):** Higher‑priority process preempts a running lower‑priority one.

*Advanced*  
- **Multilevel Queue:** Separate queues for system, interactive, batch processes; each queue may use a different algorithm.  
- **Multilevel Feedback Queue (MLFQ):** Processes can move between queues; improves response time and reduces starvation.

**Quick Comparison**  

| Algorithm   | Type          | Avg. Waiting | Favors Short Jobs | Starvation Risk |
|-------------|---------------|--------------|--------------------|-----------------|
| FCFS        | Non‑preemptive| High         | No                 | Low             |
| SJF         | Non‑preemptive| Low          | Yes                | High            |
| SRTF        | Preemptive    | Lower        | Yes                | Medium          |
| RR          | Preemptive    | Moderate     | No                 | Low             |
| Priority    | Both          | Variable     | No                 | High (low‑prio) |
| MLFQ        | Preemptive    | Low          | Yes                | Low             |

**Conclusion**  
Understanding process states and scheduling algorithms is essential for designing OS that balance CPU utilization, throughput, and fairness. Knowing the differences among non‑preemptive, preemptive, and advanced schemes enables you to select the appropriate algorithm based on system goals and workload—key for exam success.