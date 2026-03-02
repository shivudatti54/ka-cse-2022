Index:   0    1    2    3    4   (MAX=5)
Queue: [ A |  B |  C |    |    ]   // Initial state
         ^front      ^rear

After 2 dequeues (A and B are removed):
Queue: [    |    |  C |    |    ]
               ^front ^rear

Now, `rear` is at index 2, but we cannot insert a new element at index 0 or 1. The queue reports "Full" when `rear == MAX-1` (index 4), even though slots 0 and 1 are empty. This is **inefficient memory utilization**.