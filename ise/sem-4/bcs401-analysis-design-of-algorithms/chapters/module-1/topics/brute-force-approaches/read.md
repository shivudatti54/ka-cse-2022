python
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i  # Key found at index i
    return -1         # Key not found