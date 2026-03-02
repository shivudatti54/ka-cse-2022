python # Pseudocode for Insertion Sort (Decrease-by-1)
def insertionSort(A):
for i from 1 to n-1: # Start with the 2nd element (index 1)
v = A[i] # v is the element to be inserted
j = i - 1 # Find the correct position for v in the sorted subarray A[0..i-1]
while j >= 0 and A[j] > v:
A[j+1] = A[j] # Shift larger elements to the right
j = j - 1
A[j+1] = v # Insert v into its correct position
