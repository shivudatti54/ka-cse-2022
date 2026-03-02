# Textbook 1: Ch

## INTRODUCTION TO DATA STRUCTURES

### Arrays: Introduction, One-Dimensional Arrays, Two-Dimensional Arrays

#### Introduction to Arrays

=====================================================

An array is a collection of elements of the same data type stored in contiguous memory locations. Arrays provide efficient means of storing and accessing large amounts of data.

#### Characteristics of Arrays

---

- **Homogeneous**: All elements in an array are of the same data type.
- **Ordered**: Elements in an array are arranged in a specific order.
- **Fixed Size**: Arrays have a fixed size that cannot be changed during runtime.

#### Types of Arrays

---

### One-Dimensional Arrays

---

A one-dimensional array is an array that stores elements in a single row or column. Each element is identified by an index that corresponds to its position in the array.

#### One-Dimensional Array Declaration

---

```cpp
int arr[5]; // declares a one-dimensional array of 5 integers
```

#### One-Dimensional Array Indexing

---

```cpp
#include <iostream>

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    std::cout << "Element at index 0: " << arr[0] << std::endl;
    std::cout << "Element at index 1: " << arr[1] << std::endl;
    std::cout << "Element at index 4: " << arr[4] << std::endl;

    return 0;
}
```

### Two-Dimensional Arrays

---

A two-dimensional array is an array that stores elements in multiple rows and columns. Each element is identified by two indices that correspond to its position in the array.

#### Two-Dimensional Array Declaration

---

```cpp
int arr[2][3]; // declares a two-dimensional array of 2x3 integers
```

#### Two-Dimensional Array Indexing

---

```cpp
#include <iostream>

int main() {
    int arr[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    std::cout << "Element at row 0, column 0: " << arr[0][0] << std::endl;
    std::cout << "Element at row 1, column 1: " << arr[1][1] << std::endl;
    std::cout << "Element at row 0, column 2: " << arr[0][2] << std::endl;

    return 0;
}
```

#### Initializing Two-Dimensional Arrays

---

```cpp
#include <iostream>

int main() {
    int arr[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // initialize elements using the comma operator
    arr[0][0] = arr[0][1] = arr[0][2] = 1;
    arr[1][0] = arr[1][1] = arr[1][2] = 2;

    std::cout << "Element at row 0, column 0: " << arr[0][0] << std::endl;
    std::cout << "Element at row 1, column 1: " << arr[1][1] << std::endl;

    return 0;
}
```

#### Initializing Two-Dimensional Arrays using Arrays of Arrays

---

```cpp
#include <iostream>

int main() {
    int arr[2][3] = {
        {1, 2, 3},
        {4, 5, 6}
    };

    // initialize elements using arrays of arrays
    int temp[3] = {1, 2, 3};
    arr[0][0] = arr[0][1] = arr[0][2] = temp[0];
    arr[0][0] = arr[0][1] = arr[0][2] = temp[1];
    arr[0][0] = arr[0][1] = arr[0][2] = temp[2];

    int temp2[3] = {4, 5, 6};
    arr[1][0] = arr[1][1] = arr[1][2] = temp2[0];
    arr[1][0] = arr[1][1] = arr[1][2] = temp2[1];
    arr[1][0] = arr[1][1] = arr[1][2] = temp2[2];

    std::cout << "Element at row 0, column 0: " << arr[0][0] << std::endl;
    std::cout << "Element at row 1, column 1: " << arr[1][1] << std::endl;

    return 0;
}
```

#### Key Concepts

---

- Arrays provide efficient means of storing and accessing large amounts of data.
- Arrays have a fixed size that cannot be changed during runtime.
- One-dimensional arrays store elements in a single row or column.
- Two-dimensional arrays store elements in multiple rows and columns.
- Arrays can be initialized using the comma operator, arrays of arrays, and explicit initialization.
