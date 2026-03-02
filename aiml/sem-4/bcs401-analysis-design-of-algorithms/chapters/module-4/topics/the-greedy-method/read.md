python
# Pseudocode for Activity Selection
def activity_selector(s, f): # s[start], f[finish]
    n = len(s)
    A = [1]  # Select the first activity
    k = 0    # index of last selected activity

    for m in range(1, n):
        if s[m] >= f[k]:  # if activity m starts after activity k finishes
            A.append(m+1) # add it (using 1-based indexing)
            k = m         # update the last selected activity
    return A