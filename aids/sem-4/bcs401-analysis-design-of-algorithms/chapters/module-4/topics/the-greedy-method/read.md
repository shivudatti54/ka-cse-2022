pseudo code
GreedyActivitySelector(s, f): // s[]->start, f[]->finish
    n = s.length
    A = {a1} // Select the first activity
    k = 1    // last selected activity index
    for i = 2 to n:
        if s[i] >= f[k]:
            A = A U {ai}
            k = i
    return A