# Textbook 2: Ch

## INTRODUCTION TO DATA STRUCTURES

### Module: Arrays: Introduction, One-Dimensional Arrays, Two-Dimensional Arrays, Initializing Two-Dimensional Arrays

## 1. Introduction to Data Structures

Data structures are the fundamental building blocks of computer science. They enable us to organize, store, and manage data efficiently. In this module, we will explore the basics of arrays, which are a type of data structure that stores a collection of elements of the same data type in contiguous memory locations.

## 2. What is an Array?

An array is a data structure that stores a collection of elements of the same data type in contiguous memory locations. Each element in the array is identified by an index or subscript, which allows us to access and manipulate individual elements.

### Diagram: Array Structure

```
  +---------------+
  |  Array Name  |
  +---------------+
  |  Index  |  Element  |
  +---------------+
  |  0       |  e1     |
  |  1       |  e2     |
  |  2       |  e3     |
  |  ...     |  ...    |
  |  n-1     |  en-1   |
  +---------------+
```

## 3. Characteristics of Arrays

Arrays have several characteristics that make them useful for data storage and manipulation:

- **Fixed Size**: Arrays have a fixed size, which is determined at the time of creation.
- **Homogeneous Elements**: All elements in an array must be of the same data type.
- **Contiguous Memory**: Elements in an array are stored in contiguous memory locations, which makes them efficient to access.

## 4. Types of Arrays

There are two main types of arrays:

- **One-Dimensional Arrays**: Arrays that store elements of the same data type in a single dimension.
- **Two-Dimensional Arrays**: Arrays that store elements of the same data type in multiple dimensions.

### Example: One-Dimensional Array

```c
int numbers[5] = {1, 2, 3, 4, 5};
```

This declares a one-dimensional array `numbers` with 5 elements, initialized with the values 1, 2, 3, 4, and 5.

## 5. Initializing Arrays

Arrays can be initialized using the following methods:

- **Direct Initialization**: Elements are assigned values directly when the array is declared.
- **Array Initialization**: Elements are assigned values using a separate initialization statement.

### Example: Direct Initialization

```c
int numbers[5] = {1, 2, 3, 4, 5};
```

### Example: Array Initialization

```c
int numbers[5];
numbers[0] = 1;
numbers[1] = 2;
numbers[2] = 3;
numbers[3] = 4;
numbers[4] = 5;
```

## 6. Accessing and Manipulating Array Elements

Array elements can be accessed and manipulated using their index or subscript. The index starts from 0, and the last valid index is `n-1`, where `n` is the number of elements in the array.

### Example: Accessing Array Elements

```c
int numbers[5] = {1, 2, 3, 4, 5};
int element = numbers[2]; // Access the 3rd element
```

## 7. Two-Dimensional Arrays

Two-dimensional arrays are arrays of arrays. Each inner array has its own set of elements.

### Example: Two-Dimensional Array

```c
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

This declares a two-dimensional array `matrix` with 2 rows and 3 columns, initialized with the values 1, 2, 3, 4, 5, and 6.

## 8. Multidimensional Arrays

Multidimensional arrays are arrays of arrays of arrays. Each inner array has its own set of elements.

### Example: Multidimensional Array

```c
int array[2][2][2] = {
    {
        {1, 2},
        {3, 4}
    },
    {
        {5, 6},
        {7, 8}
    }
};
```

This declares a multidimensional array `array` with 2 rows, 2 columns, and 2 sub-arrays, initialized with the values 1, 2, 3, 4, 5, 6, 7, and 8.

## 9. Applications of Arrays

Arrays have many applications in computer science and real-world problems:

- **Database Management**: Arrays are used to store and manage large amounts of data in databases.
- **Graphics and Game Development**: Arrays are used to store and manipulate graphics data, such as pixels and vertices.
- **Machine Learning**: Arrays are used to store and manipulate large datasets in machine learning algorithms.

## 10. Further Reading

- "Data Structures and Algorithms in Python" by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
- "Introduction to Algorithms" by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein
- "Mathematics for Computer Science" by Michael Sipser

The end.
