# **INTRODUCTION TO DATA STRUCTURES**

## **Arrays: Introduction**

Arrays are a fundamental data structure in computer science that store a collection of elements of the same data type in a single variable. Arrays are useful for storing and manipulating data that requires access to its elements in a specific order.

### Definition

An array is a rectangular table of elements of the same data type stored in contiguous memory locations. Each element is identified by an index or subscript that specifies its position in the array.

### Characteristics

- Arrays are homogeneous, meaning that all elements in the array must be of the same data type.
- Arrays are stored in contiguous memory locations, making them efficient for storage and access.
- Arrays can be used to store and manipulate large amounts of data.

### Types of Arrays

There are two main types of arrays:

- **One-Dimensional Arrays**: Arrays that store elements in a single row or column.
- **Two-Dimensional Arrays**: Arrays that store elements in multiple rows and columns.

### Advantages of Arrays

- Arrays are efficient for storing and accessing large amounts of data.
- Arrays can be used to implement other data structures, such as lists and matrices.

### Example

```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    printf("Array elements: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Output

```
Array elements: 1 2 3 4 5
```

## **2.1 - One-Dimensional Arrays**

One-dimensional arrays are arrays that store elements in a single row or column. They are the most basic type of array and are used to store a collection of elements of the same data type.

### Declaration

The declaration of a one-dimensional array is as follows:

```c
type arrName[indexSize];
```

### Example

```c
#include <stdio.h>

int main() {
    int arr[5];
    printf("Array elements: ");
    for (int i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Output

```
Array elements: 1 2 3 4 5
```

## **2.2 - Initializing Two-Dimensional Arrays**

Two-dimensional arrays are arrays that store elements in multiple rows and columns. They are used to implement matrices, which are used to solve systems of linear equations and other mathematical problems.

### Declaration

The declaration of a two-dimensional array is as follows:

```c
type arrName[rowSize][columnSize];
```

### Example

```c
#include <stdio.h>

int main() {
    int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf("Array elements: ");
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### Output

```
Array elements: 1 2 3
4 5 6
```

## **2.3 - Accessing and Updating Array Elements**

Arrays can be accessed and updated using their indices. The syntax for accessing and updating an array element is as follows:

```c
arrIndex = value;
value = arrIndex;
```

### Example

```c
#include <stdio.h>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    int arrIndex;
    int value;

    printf("Enter an index: ");
    scanf("%d", &arrIndex);

    printf("Enter a value: ");
    scanf("%d", &value);

    arr[arrIndex] = value;

    printf("Updated array elements: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Output

```
Enter an index: 2
Enter a value: 10
Updated array elements: 1 2 10 4 5
```
