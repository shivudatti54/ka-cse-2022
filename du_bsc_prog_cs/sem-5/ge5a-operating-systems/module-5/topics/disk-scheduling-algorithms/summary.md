# Disk Scheduling Algorithms - Summary

## Key Definitions and Concepts

- **Seek Time**: Time taken for the disk arm to move to the correct cylinder/track
- **Rotational Delay**: Time waiting for the correct sector to rotate under the head
- **Track**: Concentric circle on a disk surface
- **Cylinder**: All tracks with the same radius across multiple platters
- **Starvation**: Problem where certain requests never get serviced due to persistent nearby requests

## Important Formulas and Theorems

- **Average Seek Time** = Total Head Movement / Number of Requests
- **Total Head Movement** = Sum of absolute differences between consecutive head positions
- For FCFS: Order = Order of arrival
- For SSTF: Next = Request closest to current head position
- For SCAN: Serves all requests in one direction, then reverses
- For C-SCAN: Serves all in one direction, jumps back to start, serves remaining
- LOOK: Like SCAN but only goes to last request in each direction
- C-LOOK: Like C-SCAN but only goes to last request

## Key Points

- FCFS is simplest but has worst performance; SSTF improves but risks starvation
- SCAN (elevator algorithm) provides good performance with predictable head movement
- C-SCAN provides uniform wait times but may have slightly higher average seek time
- LOOK and C-LOOK are practical implementations that avoid unnecessary travel to disk edges
- SSTF can cause starvation; all FCFS variants are starvation-free
- SCAN-family algorithms provide more uniform service times than SSTF
- Average seek time is the most commonly evaluated metric in exams

## Common Mistakes to Include

- Forgetting to include initial head position in calculations
- Not specifying head direction for SCAN/C-SCAN variants
- Assuming SSTF is optimal (it's only locally optimal)
- Confusing SCAN with C-SCAN—SCAN reverses direction, C-SCAN jumps back

## Revision Tips

1. Practice numerical problems with different request sequences and initial head positions
2. Memorize the order of servicing for each algorithm given the same input
3. Focus on understanding why SCAN outperforms FCFS—examine the pattern of head movement
4. Remember: In modern systems, operating systems often use deadline-based scheduling or combine multiple approaches