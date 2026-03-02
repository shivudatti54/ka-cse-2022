# **Python Programming for Data Science**

## **Module: 6 hr**

## **Topic: Chapter 3 and Chapter 4**

## **Chapter 3: Data Types and Operators**

### 3.1 Numeric Data Types

---

In Python, there are two main numeric data types: `int` and `float`.

- `int`: Whole numbers, either positive, negative, or zero.
- `float`: Decimals or fractions.

```python
# int data type
x = 10  # integer
y = 20  # integer

# float data type
a = 10.5  # float
b = 20.8  # float

print(type(x))  # Output: <class 'int'>
print(type(a))  # Output: <class 'float'>
```

### 3.2 String Data Type

---

`str` is the string data type in Python. It is enclosed in single quotes or double quotes.

```python
# string data type
name = 'John Doe'  # string
age = "30 years old"  # string

print(name)  # Output: John Doe
print(age)  # Output: 30 years old
```

### 3.3 Boolean Data Type

---

`bool` is the boolean data type in Python. It is used to represent true or false values.

```python
# boolean data type
is_admin = True  # boolean
is_active = False  # boolean

print(type(is_admin))  # Output: <class 'bool'>
print(type(is_active))  # Output: <class 'bool'>
```

### 3.4 List Data Type

---

A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists.

```python
# list data type
fruits = ['apple', 'banana', 'cherry']  # list
numbers = [1, 2, 3, 4, 5]  # list

print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

### 3.5 Tuple Data Type

---

A tuple is an immutable collection of items that can be of any data type.

```python
# tuple data type
colors = ('red', 'green', 'blue')  # tuple
students = (1, 2, 3, 4, 5)  # tuple

print(colors)  # Output: ('red', 'green', 'blue')
print(students)  # Output: (1, 2, 3, 4, 5)
```

### 3.6 Dictionary Data Type

---

A dictionary is an unordered collection of key-value pairs.

```python
# dictionary data type
person = {'name': 'John Doe', 'age': 30, 'city': 'New York'}  # dictionary
phone_numbers = {'home': '123-456-7890', 'office': '098-765-4321'}  # dictionary

print(person)  # Output: {'name': 'John Doe', 'age': 30, 'city': 'New York'}
print(phone_numbers)  # Output: {'home': '123-456-7890', 'office': '098-765-4321'}
```

### 3.7 Set Data Type

---

A set is an unordered collection of unique items.

```python
# set data type
numbers = {1, 2, 3, 4, 5}  # set
fruits = {'apple', 'banana', 'cherry'}  # set

print(numbers)  # Output: {1, 2, 3, 4, 5}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}
```

### 3.8 Operators

---

Python supports various operators for performing arithmetic, comparison, logical, and assignment operations.

#### 3.8.1 Arithmetic Operators

---

```python
# arithmetic operators
a = 10
b = 5

print(a + b)  # Output: 15
print(a - b)  # Output: 5
print(a \* b)  # Output: 50
print(a / b)  # Output: 2.0
```

#### 3.8.2 Comparison Operators

---

```python
# comparison operators
x = 10
y = 5

print(x > y)  # Output: True
print(x == y)  # Output: False
print(x != y)  # Output: True
```

#### 3.8.3 Logical Operators

---

```python
# logical operators
a = True
b = False

print(a and b)  # Output: False
print(a or b)  # Output: True
print(not a)  # Output: False
```

#### 3.8.4 Assignment Operators

---

```python
# assignment operators
a = 10
b = a + 5

print(b)  # Output: 15
```

## **Chapter 4: Control Structures**

### 4.1 If-Else Statements

---

```python
# if-else statements
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

### 4.2 For Loops

---

```python
# for loops
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
```

### 4.3 While Loops

---

```python
# while loops
i = 0

while i < 5:
    print(i)
    i += 1
```

### 4.4 Break and Continue Statements

---

```python
# break and continue statements
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)
```

### 4.5 Functions

---

```python
# functions
def greet(name):
    print("Hello, " + name)

greet("John Doe")
```

### 4.6 Modules

---

```python
# modules
import math

print(math.pi)  # Output: 3.14159265359
```
