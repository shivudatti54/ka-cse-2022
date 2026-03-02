# **An Overview of C++: What is Object-Oriented Programming? Introducing C++ Classes**

## **Module: 5 Hours**

## **Topic: An Overview of C++: What is Object-Oriented Programming? Introducing C++ Classes**

### Overview of Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of objects and classes. It provides a way to organize and structure code in a more efficient and effective manner.

#### Key Concepts of OOP

- **Encapsulation**: The concept of bundling data and methods that operate on that data into a single unit, called a class or object.
- **Abstraction**: The practice of exposing only the necessary information to the outside world while hiding the implementation details.
- **Inheritance**: The ability of one class to inherit the properties and behavior of another class.
- **Polymorphism**: The ability of an object to take on multiple forms, depending on the context in which it is used.

### Introduction to C++ Classes

In C++, a class is a blueprint for creating objects. It defines the properties and behavior of an object, including its data members (variables) and member functions (methods).

#### Defining a C++ Class

A C++ class is defined using the `class` keyword followed by the class name. The class name is typically capitalized and can be followed by a colon (:).

```cpp
class ClassName {
    // Data members
    type variableName;
    // Member functions
    returnType functionName();
};
```

#### Key Components of a C++ Class

- **Data Members**: Variables that are part of the class definition.
- **Member Functions**: Functions that belong to the class and can operate on the data members.
- **Constructors**: Special member functions that are called when an object is created.
- **Destructor**: Special member function that is called when an object is destroyed.

### Example of a C++ Class

```cpp
class Car {
    private:
        string color;
        int speed;

    public:
        Car(string c, int s) {
            color = c;
            speed = s;
        }

        void accelerate(int amount) {
            speed += amount;
        }

        void brake(int amount) {
            speed -= amount;
        }

        string getColor() {
            return color;
        }

        int getSpeed() {
            return speed;
        }
};
```

### Creating Objects from a C++ Class

To create objects from a C++ class, you use the `class_name` keyword followed by parentheses containing the required initializations.

```cpp
Car myCar("Red", 0);
```

### Accessing and Modifying Data Members

You can access and modify data members using the dot notation.

```cpp
myCar.accelerate(10);
myCar.brake(5);
```

This will increment the speed of the car by 10 and then decrement it by 5.

### Inheritance in C++

Inheritance is a fundamental concept in OOP that allows one class to inherit the properties and behavior of another class.

#### Example of Inheritance

```cpp
class Animal {
    public:
        void eat() {
            cout << "Eating..." << endl;
        }
};

class Dog : public Animal {
    public:
        void bark() {
            cout << "Barking..." << endl;
        }
};
```

In this example, the `Dog` class inherits the `eat()` method from the `Animal` class and adds its own `bark()` method.

### Conclusion

In this module, we have covered the basics of object-oriented programming and introduced C++ classes. We have seen how to define a C++ class, create objects from a class, and access and modify data members. We have also touched upon the concept of inheritance in C++. With this knowledge, you can start building object-oriented programs in C++.
