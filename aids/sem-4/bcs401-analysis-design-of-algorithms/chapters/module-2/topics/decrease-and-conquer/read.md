python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:        # Decrease-by-one and conquer
        return n * factorial(n-1)