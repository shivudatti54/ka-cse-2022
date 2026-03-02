Initial:       [1] -> [2] -> [3] -> NULL
               c
prev = NULL

Step 1:        [1] -> [2] -> [3] -> NULL
               c      nxt
               (nxt = c.next)

Step 2:        [1]    [2] -> [3] -> NULL
               c      nxt
               (c.next = prev=NULL)

Step 3:        [1]    [2] -> [3] -> NULL
               p      c
               (prev = c, c = nxt)