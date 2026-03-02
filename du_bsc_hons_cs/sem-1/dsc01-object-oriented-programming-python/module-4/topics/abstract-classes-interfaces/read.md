# Abstract Classes and Interfaces in Python

## Introduction

Object-Oriented Programming (OOP) is a fundamental concept in software development, and abstract classes and interfaces are crucial components of OOP. In Python, abstract classes and interfaces help define a blueprint for objects that share common characteristics and behaviors. Abstract classes provide a way to define a class that cannot be instantiated on its own and is meant to be inherited by other classes. Interfaces, on the other hand, define a contract that must be implemented by any class that implements it.

In this topic, we will explore the concept of abstract classes and interfaces in Python, their importance, and how to use them effectively in our programs.

## Key Concepts

### Abstract Classes

An abstract class in Python is a class that cannot be instantiated on its own and is meant to be inherited by other classes. Abstract classes are defined using the `abc` (Abstract Base Classes) module in Python. To define an abstract class, we use the `ABC` class from the `abc` module and decorate the methods that must be implemented by the subclass using the `@abstractmethod` decorator.

Here's an example of an abstract class:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
```
In this example, the `Shape` class is an abstract class that defines two abstract methods: `area` and `perimeter`. Any class that inherits from `Shape` must implement these two methods.

### Interfaces

Interfaces in Python are not explicitly defined as they are in languages like Java or C#. However, we can achieve the same functionality using abstract classes. An interface is essentially a contract that specifies a set of methods that must be implemented by any class that implements it.

To define an interface in Python, we can use an abstract class with only abstract methods. Here's an example:
```python
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass
```
In this example, the `Printable` class is an interface that defines a single abstract method: `print`. Any class that implements `Printable` must implement the `print` method.

## Examples

### Example 1: Implementing an Abstract Class

Let's create a class `Circle` that inherits from the `Shape` abstract class:
```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
```
In this example, the `Circle` class implements the `area` and `perimeter` methods, which are required by the `Shape` abstract class.

### Example 2: Implementing an Interface

Let's create a class `Document` that implements the `Printable` interface:
```python
class Document(Printable):
    def __init__(self, text):
        self.text = text

    def print(self):
        print(self.text)
```
In this example, the `Document` class implements the `print` method, which is required by the `Printable` interface.

## Exam Tips

1. Abstract classes are used to define a blueprint for objects that share common characteristics and behaviors.
2. Interfaces define a contract that must be implemented by any class that implements it.
3. Abstract classes can have both abstract and concrete methods.
4. Interfaces can only have abstract methods.
5. A class can inherit from multiple abstract classes, but it can only implement one interface.
6. When implementing an abstract class or interface, make sure to implement all the required methods.
7. Use abstract classes and interfaces to promote code reuse and modularity.