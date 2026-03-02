# Using a Friend Function in C++

## Introduction

In object-oriented programming, encapsulation is one of the fundamental pillars that restricts direct access to an object's data members. However, there are situations where certain functions or classes need privileged access to private members of another class. C++ provides the `friend` keyword to achieve this balance between data hiding and operational flexibility. A friend function is a non-member function that has special access to the private and protected members of a class in which it is declared as a friend.

The concept of friend functions was introduced in C++ to handle scenarios where two classes need to share data or when operators require access to private members of both classes. Unlike member functions, friend functions do not belong to the class's scope and are called like regular functions. However, they enjoy the same privileges as member functions when it comes to accessing private and protected data. This makes friend functions particularly useful for operator overloading, stream extraction and insertion operators, and implementing binary operations between objects of different classes.

## Key Concepts

### Declaration of Friend Function

A friend function is declared inside a class using the `friend` keyword. This declaration can be placed in either the public, private, or protected section of the class, though conventionally it is placed in the public section. The function definition is separate from the class and does not use the `friend` keyword again.

```cpp
class Rectangle {
private:
 int length;
 int breadth;

public:
 Rectangle(int l, int b) {
 length = l;
 breadth = b;
 }

 // Friend function declaration
 friend int calculateArea(Rectangle r);
};

// Friend function definition
int calculateArea(Rectangle r) {
 return r.length * r.breadth; // Accessing private members
}
```

### Characteristics of Friend Functions

1. **Not a Member Function**: A friend function is not part of any class, so it cannot be called using the dot (.) or arrow (->) operators on objects.

2. **Has Object as Parameter**: The friend function must take at least one object of the class as a parameter to access its private members.

3. **Cannot Access 'this' Pointer**: Since friend functions are not members, they do not have access to the `this` pointer of the class.

4. **Can be Declared in Multiple Classes**: A single function can be a friend of multiple classes, allowing it to access private members of all those classes.

5. **Cannot be Used for Virtual Functions**: Friend functions cannot be declared as virtual, and they do not participate in polymorphism.

### Friend Function for Binary Operator Overloading

Friend functions are particularly useful for overloading binary operators when the left operand is not an object of the class or when symmetric treatment of both operands is required.

```cpp
class Complex {
private:
 int real;
 int imag;

public:
 Complex(int r = 0, int i = 0) {
 real = r;
 imag = i;
 }

 // Friend function for addition
 friend Complex operator+(Complex c1, Complex c2);

 void display() {
 cout << real << " + " << imag << "i" << endl;
 }
};

Complex operator+(Complex c1, Complex c2) {
 Complex temp;
 temp.real = c1.real + c2.real;
 temp.imag = c1.imag + c2.imag;
 return temp;
}

int main() {
 Complex c1(3, 4), c2(5, 6), c3;
 c3 = c1 + c2; // Calls operator+(c1, c2)
 c3.display(); // Output: 8 + 10i
 return 0;
}
```

### Friend Classes

A friend class is a class whose all member functions are friend functions of another class. All member functions of the friend class can access private and protected members of the class that granted friendship.

```cpp
class B; // Forward declaration

class A {
private:
 int dataA;

public:
 A() { dataA = 10; }

 // Declaring B as friend class
 friend class B;
};

class B {
public:
 void display(A obj) {
 cout << "Data from A: " << obj.dataA << endl;
 }

 void modify(A &obj, int val) {
 obj.dataA = val;
 }
};

int main() {
 A objA;
 B objB;
 objB.display(objA); // Output: Data from A: 10
 objB.modify(objA, 50);
 objB.display(objA); // Output: Data from A: 50
 return 0;
}
```

### Friend Function with Default Arguments

Friend functions cannot have default arguments that depend on the class members, but they can have regular default arguments in their parameter list.

## Examples

### Example 1: Comparing Objects of Two Different Classes

Write a program to compare two boxes and find the larger one using a friend function.

```cpp
class Box {
private:
 int width;
 int height;

public:
 Box(int w, int h) {
 width = w;
 height = h;
 }

 int area() {
 return width * height;
 }

 // Declare comparison function as friend
 friend bool isGreater(Box b1, Box b2);
};

bool isGreater(Box b1, Box b2) {
 int area1 = b1.width * b1.height;
 int area2 = b2.width * b2.height;
 return area1 > area2;
}

int main() {
 Box b1(5, 4);
 Box b2(3, 6);

 cout << "Box1 Area: " << b1.area() << endl;
 cout << "Box2 Area: " << b2.area() << endl;

 if (isGreater(b1, b2))
 cout << "Box1 is larger" << endl;
 else
 cout << "Box2 is larger" << endl;

 return 0;
}
```

**Output:**

```
Box1 Area: 20
Box2 Area: 18
Box1 is larger
```

### Example 2: Overloading Stream Operators

Using friend functions to overload insertion (<<) and extraction (>>) operators.

```cpp
class Time {
private:
 int hours;
 int minutes;

public:
 Time(int h = 0, int m = 0) {
 hours = h;
 minutes = m;
 }

 // Friend function declarations for stream operators
 friend ostream& operator<<(ostream& out, Time t);
 friend istream& operator>>(istream& in, Time& t);
};

ostream& operator<<(ostream& out, Time t) {
 out << t.hours << " hours " << t.minutes << " minutes";
 return out;
}

istream& operator>>(istream& in, Time& t) {
 cout << "Enter hours: ";
 in >> t.hours;
 cout << "Enter minutes: ";
 in >> t.minutes;
 return in;
}

int main() {
 Time t1(5, 30), t2;

 cout << "Time1: " << t1 << endl;

 cout << "Enter Time2:" << endl;
 cin >> t2;
 cout << "Time2: " << t2 << endl;

 return 0;
}
```

### Example 3: Swapping Private Data Between Two Objects

```cpp
class Sample {
private:
 int value;

public:
 Sample(int v = 0) {
 value = v;
 }

 void display() {
 cout << "Value: " << value << endl;
 }

 // Friend function declaration
 friend void swap(Sample& s1, Sample& s2);
};

void swap(Sample& s1, Sample& s2) {
 int temp = s1.value;
 s1.value = s2.value;
 s2.value = temp;
}

int main() {
 Sample obj1(10), obj2(20);

 cout << "Before swap:" << endl;
 obj1.display(); // Value: 10
 obj2.display(); // Value: 20

 swap(obj1, obj2);

 cout << "After swap:" << endl;
 obj1.display(); // Value: 20
 obj2.display(); // Value: 10

 return 0;
}
```

## Exam Tips

1. **Remember Syntax**: The `friend` keyword must be used only in the function declaration inside the class, not in the definition outside the class.

2. **Distinguish from Member Functions**: Friend functions are not called with object name and dot operator; they take objects as explicit parameters.

3. **Friend Classes vs Friend Functions**: A friend class gives all member functions access, while a friend function gives only that specific function access.

4. **Common Applications**: Be prepared to write programs using friend functions for operator overloading, stream operators, and cross-class data access.

5. **Prefer Member Functions**: When both member functions and friend functions can solve the problem, prefer member functions for better encapsulation.

6. **Forward Declaration**: When using friend functions across classes, remember to use forward declaration for the class that is not defined yet.

7. **Non-Member Nature**: Remember that friend functions do not have a `this` pointer and cannot be virtual, though they can access all private members of the class.
