# **Object Oriented Programming with JAVA**

# **Module: Inheritance: Inheritance Basics, Using super, Creating a Multilevel Hierarchy, Constructors**

Inheritance is a fundamental concept in Object Oriented Programming (OOP) that allows one class to inherit the properties and behavior of another class. In this section, we will explore the basics of inheritance in Java, including how to use the `super` keyword, create a multilevel hierarchy, and understand the role of constructors.

## **What is Inheritance?**

Inheritance is a mechanism that allows one class to inherit the properties and behavior of another class. The class that is being inherited from is called the parent or superclass, while the class that is doing the inheriting is called the child or subclass.

## **Types of Inheritance**

There are three types of inheritance in Java:

- **Single Inheritance**: A subclass can inherit from only one parent class.
- **Multiple Inheritance**: A subclass can inherit from multiple parent classes.
- **Multilevel Inheritance**: A subclass can inherit from a parent class that itself inherits from another parent class.
- **Hierarchical Inheritance**: A subclass can inherit from a parent class that is common to multiple subclasses.
- **Hybrid Inheritance**: A combination of multiple inheritance and multilevel inheritance.

## **Using the `super` Keyword**

The `super` keyword is used to access the members of the parent class from a subclass. It can be used in the constructor, method, and field declarations.

- **Constructor**: The `super` keyword is used to call the constructor of the parent class from a subclass constructor.
- **Method**: The `super` keyword is used to call a method of the parent class from a subclass method.
- **Field**: The `super` keyword is used to access a field of the parent class from a subclass field.

## **Example**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public Dog() {
        super();
        System.out.println("The dog is barking.");
    }
}
```

In this example, the `Dog` class inherits from the `Animal` class and overrides the `sound()` method. The `super()` keyword is used to call the constructor of the `Animal` class from the `Dog` class constructor.

## **Multilevel Hierarchy**

A multilevel hierarchy is a type of inheritance where a subclass inherits from a parent class that itself inherits from another parent class.

## **Example**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Mammal extends Animal {
    public void eat() {
        System.out.println("The mammal is eating.");
    }
}

public class Dog extends Mammal {
    public Dog() {
        super();
        System.out.println("The dog is barking.");
    }
}
```

In this example, the `Dog` class inherits from the `Mammal` class, which in turn inherits from the `Animal` class.

## **Constructors**

Constructors in Java are special methods that are used to initialize objects when they are created. A constructor can be used to call the constructor of the parent class using the `super` keyword.

## **Example**

```java
public class Animal {
    public Animal() {
        System.out.println("The animal is created.");
    }
}

public class Dog extends Animal {
    public Dog() {
        super();
        System.out.println("The dog is barking.");
    }
}
```

In this example, the `Dog` class constructor calls the `super()` constructor of the `Animal` class.

# **Executed, Method Overriding, Dynamic Method Dispatch, Using Abstract Classes, Using final with Inheritance, Local Variable Type Inference, and Inherita**

### **Executed**

- **Method Overriding**: Method overriding is a process where a subclass provides a different implementation of a method that is already available in its superclass. When a method is overridden, the method in the subclass has priority over the method in the superclass.
- **Dynamic Method Dispatch**: Dynamic method dispatch is a process where the compiler does not know which method to call at compile time. Instead, the runtime environment determines which method to call based on the type of the object being referred to.

### **Method Overriding**

Method overriding is a process where a subclass provides a different implementation of a method that is already available in its superclass.

## **Example**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("The dog is barking.");
    }
}
```

In this example, the `Dog` class overrides the `sound()` method of the `Animal` class.

### **Dynamic Method Dispatch**

Dynamic method dispatch is a process where the compiler does not know which method to call at compile time. Instead, the runtime environment determines which method to call based on the type of the object being referred to.

## **Example**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("The dog is barking.");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.sound();
    }
}
```

In this example, the `sound()` method is called dynamically based on the type of the object being referred to.

### **Using Abstract Classes**

Abstract classes are a type of class that cannot be instantiated on their own. They are used to provide a common implementation for a group of related classes.

## **Example**

```java
public abstract class Animal {
    public abstract void sound();
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("The dog is barking.");
    }
}

public class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("The cat is meowing.");
    }
}
```

In this example, the `Animal` class is an abstract class that provides a common implementation for the `Dog` and `Cat` classes.

### **Using final with Inheritance**

The `final` keyword is used to make a class, method, or variable immutable.

## **Example**

```java
public final class Animal {
    public final void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("The dog is barking.");
    }
}
```

In this example, the `Animal` class is declared as `final`, making it impossible for a subclass to provide a different implementation of the `sound()` method.

### **Local Variable Type Inference**

Local variable type inference is a feature of Java 10 and later versions that allows the compiler to infer the type of a local variable based on its assignment.

## **Example**

```java
public class Main {
    public static void main(String[] args) {
        var dog = new Dog();
        dog.sound();
    }
}
```

In this example, the type of the `dog` variable is inferred to be `Dog` based on its assignment.

### **Inherita**

The `inherita` keyword is not a valid keyword in Java. However, it is possible to achieve similar behavior by using inheritance.

## **Example**

```java
public class Animal {
    public void sound() {
        System.out.println("The animal makes a sound.");
    }
}

public class Dog extends Animal {
    public void sound() {
        System.out.println("The dog is barking.");
    }
}
```

In this example, the `Dog` class inherits the `sound()` method from the `Animal` class.

## **Further Reading**

- "Head First Design Patterns" by Kathy Sierra and Bert Bates
- "Java: A Beginner's Guide" by Herbert Schildt
- "Object-Oriented Programming in Java" by Elliotte Rusty Harold
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides
