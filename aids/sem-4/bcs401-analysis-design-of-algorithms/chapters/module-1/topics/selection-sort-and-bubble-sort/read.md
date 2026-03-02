for i from 0 to n-2:
    min_index = i
    for j from i+1 to n-1:
        if array[j] < array[min_index]:
            min_index = j
    swap array[i] and array[min_index]