# Inheritance in Python

## Object Oriented Programming Python — BSc (Hons) Computer Science

---

## 1. Introduction

**Inheritance** is one of the four fundamental pillars of Object-Oriented Programming (OOP), alongside encapsulation, polymorphism, and abstraction. It represents an "is-a" relationship between classes and enables code reusability, extensibility, and logical hierarchical organization.

In the context of the Delhi University BSc (Hons) Computer Science curriculum (NEP 2024 UGCF), inheritance is a core concept that students must master to build robust, maintainable, and scalable software systems. This study material provides comprehensive coverage suitable for university-level instruction.

### Real-World Relevance

Consider a university management system:

- A base class `Person` stores common attributes like name, age, and email
- `Student` and `Professor` inherit from `Person`, gaining all its attributes
- `Student` can have additional attributes like `roll_number`, `course`, and `semester`
- `Professor` can have `employee_id`, `department`, and `specialization`

This hierarchical design eliminates code duplication and reflects real-world relationships accurately.

---

## 2. Fundamentals of Inheritance

### 2.1 What is Inheritance?

Inheritance allows a class (called the **child class** or **derived class**) to inherit attributes and methods from another class (called the **parent class** or **base class**). The child class can:

- Use all public attributes and methods of the parent class
- Override (redefine) inherited methods
- Add new attributes and methods specific to itself

### 2.2 Syntax

```python
class ParentClass:
    # Parent class attributes and methods
    pass

class ChildClass(ParentClass):
    # Child class inherits from ParentClass
    # Additional attributes and methods
    pass
```

### 2.3 Key Terminology

| Term | Definition |
|------|------------|
| **Base Class (Parent)** | The class whose properties are inherited |
| **Derived Class (Child)** | The class that inherits properties from another class |
| **Method Overriding** | Redefining a parent method in the child class |
| **super()** | Built-in function to access parent class methods |

### 2.4 Complete Example: Basic Inheritance

```python
# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"
    
    def start_engine(self):
        return "Engine started!"

# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # Call parent constructor using super()
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def display_info(self):
        # Override parent method
        return f"Car: {self.brand} {self.model} with {self.num_doors} doors"

# Create objects
vehicle = Vehicle("Generic", "Model X")
car = Car("Toyota", "Camry", 4)

print(vehicle.display_info())  # Output: Vehicle: Generic Model X
print(car.display_info())       # Output: Car: Toyota Camry with 4 doors
print(car.start_engine())      # Output: Engine started! (inherited)
```

---

## 3. Types of Inheritance

Python supports various types of inheritance, essential for the Delhi University examination pattern.

### 3.1 Single Inheritance

A child class inherits from one parent class.

```
    Parent
       |
     Child
```

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(f"{dog.name} says: {dog.speak()}")  # Output: Buddy says: Woof!
```

### 3.2 Multiple Inheritance

A child class inherits from more than one parent class.

```
  Parent1   Parent2
      \       /
       Child
```

```python
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimmable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimmable):
    def speak(self):
        return "Quack!"

duck = Duck()
print(duck.fly())     # Output: I can fly!
print(duck.swim())    # Output: I can swim!
print(duck.speak())   # Output: Quack!
```

**Important Note:** In multiple inheritance, the child class inherits methods from all parent classes. However, if both parent classes have a method with the same name, Python uses **Method Resolution Order (MRO)** to determine which method to call.

### 3.3 Multilevel Inheritance

A class inherits from a class that itself inherits from another class.

```
   Grandparent
       |
     Parent
       |
     Child
```

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        return self.name

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
    
    def display_employee(self):
        return f"{self.name}, ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
    
    def display_manager(self):
        return f"{self.name}, ID: {self.employee_id}, Dept: {self.department}"

manager = Manager("Alice", "MGR001", "Computer Science")
print(manager.display_name())      # Output: Alice (inherited from Person)
print(manager.display_employee())  # Output: Alice, ID: MGR001 (inherited from Employee)
print(manager.display_manager())   # Output: Alice, ID: MGR001, Dept: Computer Science
```

### 3.4 Hierarchical Inheritance

Multiple child classes inherit from a single parent class.

```
      Parent
    /   |   \
 Child1 Child2 Child3
```

```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def describe(self):
        return f"A {self.color} shape"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

circle = Circle("Red", 5)
rectangle = Rectangle("Blue", 4, 6)
triangle = Triangle("Green", 3, 4)

print(circle.describe(), "Area:", round(circle.area(), 2))
print(rectangle.describe(), "Area:", rectangle.area())
print(triangle.describe(), "Area:", triangle.area())
```

### 3.5 Hybrid Inheritance

A combination of two or more types of inheritance.

```
      Parent
     /      \
  Child1  Child2
     \      /
      Child3
```

```python
class University:
    def __init__(self, name):
        self.name = name
    
    def get_university_name(self):
        return f"University: {self.name}"

class Department(University):
    def __init__(self, name, dept_name):
        super().__init__(name)
        self.dept_name = dept_name
    
    def get_department(self):
        return f"Department: {self.dept_name}"

class Faculty(University):
    def __init__(self, name, faculty_name):
        super().__init__(name)
        self.faculty_name = faculty_name
    
    def get_faculty(self):
        return f"Faculty: {self.faculty_name}"

class Course(Department, Faculty):
    def __init__(self, uni_name, dept_name, faculty_name, course_name):
        Department.__init__(self, uni_name, dept_name)
        Faculty.__init__(self, uni_name, faculty_name)
        self.course_name = course_name
    
    def get_course_info(self):
        return f"Course: {self.course_name}\n{self.get_university_name()}\n{self.get_department()}\n{self.get_faculty()}"

course = Course("Delhi University", "Computer Science", "Science", "BSc Hons CS")
print(course.get_course_info())
```

---

## 4. Method Resolution Order (MRO)

MRO determines the order in which base classes are searched when executing a method. It is crucial in multiple inheritance scenarios.

### 4.1 How MRO Works

Python uses the **C3 Linearization** algorithm. You can view the MRO of any class using:

```python
ClassName.mro()
# or
ClassName.__mro__
```

### 4.2 Example Demonstrating MRO

```python
class A:
    def show(self):
        return "Method from class A"

class B(A):
    def show(self):
        return "Method from class B"

class C(A):
    def show(self):
        return "Method from class C"

class D(B, C):  # Inherits from B and C
    pass

# Check MRO
print("MRO of class D:", [cls.__name__ for cls in D.mro()])

# Method resolution
d = D()
print(d.show())  # Output: Method from class B
```

**Output:**
```
MRO of class D: ['D', 'B', 'C', 'A', 'object']
Method from class B
```

The method `show()` from class `B` is called because `B` appears before `C` in the MRO.

### 4.3 Diamond Problem

The diamond problem occurs in multiple inheritance when a class inherits from two classes that both inherit from a common base class.

```
       A
      / \
     B   C
      \ /
       D
```

```python
class A:
    def process(self):
        return "Processing in A"

class B(A):
    def process(self):
        return "Processing in B"

class C(A):
    def process(self):
        return "Processing in C"

class D(B, C):
    pass

d = D()
print(d.process())  # Uses MRO: D -> B -> C -> A
print("MRO:", [cls.__name__ for cls in D.mro()])
```

**Output:**
```
Processing in B
MRO: ['D', 'B', 'C', 'A', 'object']
```

---

## 5. Advanced Topics

### 5.1 Abstract Base Classes (ABC)

Abstract base classes define a blueprint for other classes. They can have abstract methods (methods without implementation) that must be implemented by derived classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def area(self):
        pass  # No implementation - must be overridden
    
    def describe(self):
        return f"A {self.color} shape with area {self.area()}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Cannot instantiate abstract class
# shape = Shape("Red")  # TypeError: Can't instantiate abstract class Shape

circle = Circle("Blue", 5)
rectangle = Rectangle("Green", 4, 6)

print(circle.describe())       # Output: A Blue shape with area 78.53975
print(rectangle.describe())    # Output: A Green shape with area 24
```

### 5.2 isinstance() and issubclass()

These built-in functions are essential for runtime type checking.

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

# isinstance() - checks if object is instance of class
print(isinstance(dog, Dog))        # True
print(isinstance(dog, Animal))     # True (Dog inherits from Animal)
print(isinstance(dog, Cat))        # False

# issubclass() - checks if class is subclass of another
print(issubclass(Dog, Animal))     # True
print(issubclass(Cat, Animal))     # True
print(issubclass(Animal, object))  # True
print(issubclass(Dog, Cat))        # False
```

### 5.3 Using super() Effectively

The `super()` function provides access to parent class methods and is essential for proper initialization in inheritance hierarchies.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)  # Call parent constructor
        self.roll_no = roll_no
        self.course = course
    
    def display(self):
        # Call parent display and extend
        return f"{super().display()}, Roll No: {self.roll_no}, Course: {self.course}"

student = Student("Rahul", 20, "CS/2024/001", "BSc Hons CS")
print(student.display())
```

**Output:**
```
Name: Rahul, Age: 20, Roll No: CS/2024/001, Course: BSc Hons CS
```

---

## 6. Comprehensive Practical Example

### University Management System

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Person(ABC):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    @abstractmethod
    def get_role(self):
        pass
    
    def display_info(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nRole: {self.get_role()}"

# Derived classes
class Student(Person):
    def __init__(self, name, email, phone, roll_no, semester, course):
        super().__init__(name, email, phone)
        self.roll_no = roll_no
        self.semester = semester
        self.course = course
        self.grades = {}
    
    def get_role(self):
        return "Student"
    
    def add_grade(self, subject, grade):
        self.grades[subject] = grade
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nRoll No: {self.roll_no}\nSemester: {self.semester}\nCourse: {self.course}\nGrades: {self.grades}"

class Professor(Person):
    def __init__(self, name, email, phone, emp_id, department, specialization):
        super().__init__(name, email, phone)
        self.emp_id = emp_id
        self.department = department
        self.specialization = specialization
        self.courses_taught = []
    
    def get_role(self):
        return "Professor"
    
    def assign_course(self, course):
        self.courses_taught.append(course)
    
    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nEmployee ID: {self.emp_id}\nDepartment: {self.department}\nSpecialization: {self.specialization}\nCourses: {self.courses_taught}"

# Staff class for hierarchical inheritance
class Staff(Person):
    def __init__(self, name, email, phone, emp_id, designation):
        super().__init__(name, email, phone)
        self.emp_id = emp_id
        self.designation = designation
    
    def get_role(self):
        return "Staff"

# Test the system
student = Student("Amit Kumar", "amit@du.ac.in", "9876543210", "CS/2024/001", 3, "BSc Hons CS")
student.add_grade("Python Programming", "A")
student.add_grade("Data Structures", "A-")

professor = Professor("Dr. Sarah Khan", "sarah@du.ac.in", "9876543211", "PROF/001", "Computer Science", "Machine Learning")
professor.assign_course("Machine Learning")
professor.assign_course("Deep Learning")

staff = Staff("Mr. Rajesh Kumar", "rajesh@du.ac.in", "9876543212", "STF/001", "Administrative Officer")

print("=" * 50)
print("STUDENT INFORMATION")
print("=" * 50)
print(student.display_info())

print("\n" + "=" * 50)
print("PROFESSOR INFORMATION")
print("=" * 50)
print(professor.display_info())

print("\n" + "=" * 50)
print("STAFF INFORMATION")
print("=" * 50)
print(staff.display_info())

# Type checking
print("\n" + "=" * 50)
print("TYPE CHECKING")
print("=" * 50)
print(f"Is student a Person? {isinstance(student, Person)}")
print(f"Is professor a Student? {isinstance(professor, Student)}")
print(f"Is Professor subclass of Person? {issubclass(Professor, Person)}")
```

---

## 7. Key Takeaways

1. **Inheritance Fundamentals**: Inheritance establishes an "is-a" relationship, enabling code reusability through parent-child class relationships.

2. **Types of Inheritance**: Python supports single, multiple, multilevel, hierarchical, and hybrid inheritance, each suitable for different design scenarios.

3. **Method Resolution Order (MRO)**: In multiple inheritance, MRO determines the sequence of base class method lookup using Python's C3 Linearization algorithm.

4. **Abstract Base Classes**: Use the `abc` module to create abstract classes that enforce method implementation in derived classes.

5. **Type Checking**: `isinstance()` and `issubclass()` are essential for runtime polymorphism and type validation.

6. **super() Function**: Always use `super()` to properly call parent class methods and maintain the inheritance chain.

7. **Design Principles**: Inheritance should be used to model genuine "is-a" relationships; prefer composition over inheritance when appropriate.

---

## 8. Assessment Section

### 8.1 Multiple Choice Questions (MCQs)

**Q1.** What is the output of the following code?

```python
class A:
    def process(self):
        return "A"

class B(A):
    def process(self):
        return "B"

class C(A):
    def process(self):
        return "C"

class D(B, C):
    pass

obj = D()
print(obj.process())
```
- a) A
- b) B
- c) C
- d) Error

**Q2.** Which function is used to call the parent class constructor in Python?
- a) parent()
- b) super()
- c) parent_init()
- d) base()

**Q3.** In Python, which keyword is used to define an abstract method?
- a) abstract
- b) @abstractmethod
- c) abstractmethod
- d) virtual

**Q4.** What does `issubclass(Student, Person)` return if `Student` inherits from `Person`?
- a) False
- b) True
- c) Error
- d) None

**Q5.** In a multilevel inheritance chain `A → B → C`, which class's method is called first when looking for a method in an instance of C?
- a) A
- b) B
- c) C
- d) object

**Q6.** Which type of inheritance is depicted below?
```
     Parent
   /   |   \
Child1 Child2 Child3
```
- a) Multiple Inheritance
- b) Hierarchical Inheritance
- c) Multilevel Inheritance
- d) Hybrid Inheritance

**Q7.** What is the MRO for class `D(B, C)` where both B and C inherit from A?
- a) D, B, C, A
- b) D, B, A, C
- c) D, B, C, A, object
- d) D, C, B, A

**Q8.** Which function displays the Method Resolution Order of a class?
- a) ClassName.mro()
- b) ClassName.get_mro()
- c) ClassName.show_mro()
- d) ClassName.__mro__

### 8.2 Flashcards

| Term | Description |
|------|-------------|
| **Inheritance** | OOP concept enabling a class to inherit attributes and methods from another class |
| **Parent Class** | The base class whose properties are inherited (also called superclass) |
| **Child Class** | The derived class that inherits properties (also called subclass) |
| **Method Overriding** | Redefining a parent class method in the child class with same signature |
| **MRO (Method Resolution Order)** | The order in which Python searches for a method in inheritance hierarchy |
| **super()** | Built-in function to call parent class methods and constructors |
| **Abstract Base Class** | A class that cannot be instantiated and may contain abstract methods |
| **Multiple Inheritance** | When a class inherits from more than one parent class |
| **isinstance()** | Checks if an object is an instance of a class or its subclasses |
| **issubclass()** | Checks if a class is a subclass of another class |

### 8.3 Short Answer Questions

1. Explain the difference between `isinstance()` and `issubclass()` with examples.

2. What is the "Diamond Problem" in multiple inheritance, and how does Python solve it?

3. Why can't we instantiate an abstract class in Python? Explain with an example.

4. Differentiate between single inheritance and multiple inheritance with code examples.

5. Explain the role of `super().__init__()` in child class constructors.

### 8.4 Coding Questions

**Question 1:** Write a Python program demonstrating multilevel inheritance with a university scenario: `Person` → `Employee` → `Teacher`. Each class should have appropriate attributes and methods.

**Question 2:** Create an abstract class `BankAccount` with abstract methods `deposit()` and `withdraw()`. Create two derived classes `SavingsAccount` and `CurrentAccount` that implement these methods.

**Question 3:** Given the following code, predict the output and draw the inheritance diagram:

```python
class X:
    def show(self):
        return "X"

class Y(X):
    def show(self):
        return "Y"

class Z(X):
    def show(self):
        return "Z"

class W(Y, Z):
    pass

obj = W()
print(obj.show())
print("MRO:", [c.__name__ for c in W.mro()])
```

**Question 4:** Create a hybrid inheritance system for a hospital management system with `Person` (base), `Doctor` and `Patient` (inheriting from Person), and `MedicalRecord` that inherits from both Doctor and Patient.

---

## References

- Python Software Foundation. (2024). Python 3.x Documentation.
- Delhi University BSc (Hons) Computer Science Syllabus - NEP 2024 UGCF
- "Fluent Python" by Luciano Ramalho - Advanced Python OOP concepts

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University as per the NEP 2024 UGCF curriculum.*