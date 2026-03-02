python
# Simplified Python example for profiling a sorting algorithm
import time
import random

def test_sorting_algorithm(algorithm):
    input_sizes = [100, 1000, 5000, 10000]
    for size in input_sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        start_time = time.time()
        algorithm(test_data)  # Run the algorithm on the data
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Input Size: {size}, Time taken: {elapsed_time:.6f} seconds")