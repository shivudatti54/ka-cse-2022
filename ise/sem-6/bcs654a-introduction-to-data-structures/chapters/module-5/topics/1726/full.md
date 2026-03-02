# **17.2.6 Insertion Sort**

## **Introduction**

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. Each subsequent element from the unsorted region is inserted into the sorted region in its correct position.

## **History**

Insertion sort has been known since the late 19th century. It was first described by George Boole in 1847, and later by Van Mandeleert in 1885. However, it was not widely used until the 1950s, when it was used in the United States Army's data processing system.

## **How Insertion Sort Works**

Here is a step-by-step explanation of how insertion sort works:

1.  Start with the first element of the array, which is already sorted.
2.  Take the next element from the unsorted region and compare it with the elements in the sorted region.
3.  If the element is smaller than the first element in the sorted region, insert it into the sorted region.
4.  Otherwise, shift the elements in the sorted region to the right until you find the correct position for the element.
5.  Insert the element into the correct position in the sorted region.
6.  Repeat steps 2-5 until the entire array is sorted.

## **Algorithm**

Here is a simple implementation of insertion sort in Python:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
```

## **Time Complexity**

The time complexity of insertion sort is O(n^2) in the worst case, where n is the number of elements in the array. However, if the input is already sorted or nearly sorted, the time complexity can be O(n).

## **Space Complexity**

The space complexity of insertion sort is O(1), because a single additional memory space is required to store the key variable.

## **Advantages**

1.  **Stability**: Insertion sort is a stable sorting algorithm, which means that it preserves the order of equal elements.
2.  **Simple implementation**: Insertion sort has a simple implementation and is easy to understand.
3.  **Adaptability**: Insertion sort can be used to sort partially sorted or nearly sorted data.

## **Disadvantages**

1.  **High time complexity**: Insertion sort has a high time complexity, especially for large datasets.
2.  **Not suitable for large datasets**: Insertion sort is not suitable for large datasets because its time complexity increases quadratically with the size of the input.

## **Applications**

Insertion sort is commonly used in:

1.  **Small datasets**: Insertion sort is suitable for small datasets because its time complexity is relatively low.
2.  **Nearly sorted data**: Insertion sort can be used to sort nearly sorted data because its time complexity is relatively low in this case.
3.  **Stability**: Insertion sort is used in applications where stability is required.

## **Case Studies**

1.  **Sorting a list of students**: Suppose we have a list of students with their names and ages. We want to sort the list by age. We can use insertion sort to sort the list.
2.  **Sorting a list of numbers**: Suppose we have a list of numbers and we want to sort them in ascending order. We can use insertion sort to sort the list.

## **Example Use Cases**

1.  **Sorting a list of names**: Suppose we have a list of names and we want to sort them alphabetically. We can use insertion sort to sort the list.
2.  **Sorting a list of numbers**: Suppose we have a list of numbers and we want to sort them in ascending order. We can use insertion sort to sort the list.

## **Code Examples**

### Python

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
print("Sorted array:", insertion_sort(arr))
```

### Java

```java
public class InsertionSort {
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i-1;
            while (j >= 0 && key < arr[j]) {
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Original array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        insertionSort(arr);
        System.out.println("Sorted array: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
```

## **Further Reading**

1.  **"Introduction to Algorithms"** by Thomas H. Cormen
2.  **"The Algorithm Design Manual"** by Steven S. Skiena
3.  **"Sorting Algorithms"** by Thomas H. Cormen
4.  **"Introduction to Data Structures and Algorithms"** by Mark Allen Weiss

## **Conclusion**

Insertion sort is a simple sorting algorithm that works by dividing the input into a sorted and an unsorted region. It is a stable sorting algorithm that can be used to sort partially sorted or nearly sorted data. However, it has a high time complexity and is not suitable for large datasets. Despite its limitations, insertion sort is commonly used in small datasets and applications where stability is required.
