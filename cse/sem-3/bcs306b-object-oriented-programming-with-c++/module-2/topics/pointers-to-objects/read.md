# Pointers to Objects in C++

## Introduction

Pointers to objects represent one of the most powerful and essential concepts in C++ object-oriented programming. In the world of C++, pointers serve as fundamental tools for memory management, dynamic object creation, and efficient function parameter passing. When combined with the object-oriented paradigm, pointers become even more significant as they enable polymorphic behavior, dynamic binding, and efficient memory utilization.

In C++, objects are typically stored in memory with specific addresses, and pointers allow us to store those addresses and manipulate objects indirectly. This indirect access provides tremendous flexibility in programming, enabling developers to create complex data structures like linked lists, trees, and graphs. Moreover, pointers to objects form the backbone of many C++ standard library containers and algorithms.

Understanding pointers to objects is crucial for any C++ programmer because it bridges the gap between traditional procedural programming and object-oriented programming. This knowledge becomes particularly important when studying advanced topics such as virtual functions, inheritance, and dynamic polymorphism. In the university's BCS306B curriculum, this topic serves as a foundation for understanding how C++ implements runtime polymorphism through virtual tables and pointer manipulation.

## Key Concepts

### Declaration and Initialization of Pointers to Objects

A pointer to an object is declared similar to any other pointer, but the data type is a class name instead of a primitive type. The syntax for declaring a pointer to an object is:

```cpp
ClassName* pointerName;
```

For example, if we have a class named `Student`, we can declare a pointer to Student objects as:

```cpp
Student* ptr;
```

Before using a pointer to an object, it must be initialized to point to a valid object or allocated memory. There are three primary ways to initialize pointers to objects:

1. **Assigning the address of an existing object:**

```cpp
Student s1;
Student* ptr = &s1;
```

2. **Dynamic memory allocation using new:**

```cpp
Student* ptr = new Student;
```

3. **Assigning one pointer to another:**

```cpp
Student* ptr1 = new Student;
Student* ptr2 = ptr1;
```

### Accessing Members Using Arrow Operator (->)

Once a pointer to an object is initialized, we need a way to access its members (attributes and member functions). The arrow operator (`->`) is specifically designed for this purpose. It combines dereferencing and member access into a single operation.

The syntax is:

```cpp
pointer->memberName
```

Consider the following class:

```cpp
class Rectangle {
private:
 int length;
 int breadth;
public:
 void setDimensions(int l, int b) {
 length = l;
 breadth = b;
 }
 int area() {
 return length * breadth;
 }
};
```

To access members through a pointer:

```cpp
Rectangle rect;
Rectangle* ptr = &rect;
ptr->setDimensions(10, 5); // Calls setDimensions() on the object
cout << ptr->area(); // Calls area() and prints 50
```

It's important to note that we cannot use the dot operator (.) with pointers directly. Attempting to do so will result in a compilation error. The alternative would be to dereference the pointer first and then use the dot operator:

```cpp
(*ptr).setDimensions(10, 5); // Equivalent to ptr->setDimensions(10, 5)
```

However, the arrow operator is preferred due to its readability and conciseness.

### Dynamic Memory Allocation for Objects

Dynamic memory allocation for objects works similarly to primitive types but involves constructors and destructors. When using the `new` operator with objects, the constructor is automatically called, and when using `delete`, the destructor is invoked.

```cpp
class BankAccount {
private:
 int accountNumber;
 double balance;
public:
 BankAccount(int accNo, double bal) {
 accountNumber = accNo;
 balance = bal;
 }
 ~BankAccount() {
 cout << "Destructor called for account " << accountNumber << endl;
 }
 void display() {
 cout << "Account: " << accountNumber << ", Balance: " << balance << endl;
 }
};

int main() {
 BankAccount* acc = new BankAccount(1001, 5000.00);
 acc->display();
 delete acc; // Destructor is called here
 return 0;
}
```

When allocating an array of objects dynamically, the syntax differs slightly:

```cpp
BankAccount* accounts = new BankAccount[10]; // Array of 10 objects
// Access elements
accounts[0].display(); // or accounts->display()
delete[] accounts; // Must use delete[] for arrays
```

### The this Pointer

Every non-static member function in C++ has access to a special pointer called `this`. This pointer points to the object for which the member function was called. The `this` pointer is implicitly available within all non-static member functions and cannot be modified.

The `this` pointer is particularly useful in the following scenarios:

1. **Distinguishing between member arguments and data members:**

```cpp
class Box {
private:
 int width;
public:
 void setWidth(int width) {
 this->width = width; // 'this->width' refers to member, 'width' refers to parameter
 }
};
```

2. **Returning the current object from a member function:**

```cpp
class Builder {
public:
 Builder* setX(int x) {
 // Process x
 return this; // Returns pointer to current object
 }
 Builder* setY(int y) {
 // Process y
 return this;
 }
};
```

3. **Print the address of the current object:**

```cpp
void displayAddress() {
 cout << "Object address: " << this << endl;
}
```

### Array of Objects and Pointers

Arrays of objects are commonly used in C++ programs. Each element in an array of objects is an object that can be accessed either through indexing or through pointer arithmetic.

```cpp
class Employee {
private:
 int id;
 string name;
public:
 void setData(int i, string n) {
 id = i;
 name = n;
 }
 void showData() {
 cout << "ID: " << id << ", Name: " << name << endl;
 }
};

int main() {
 Employee emp[3];
 Employee* ptr = emp; // Points to first element

 for(int i = 0; i < 3; i++) {
 (ptr + i)->setData(100 + i, "Employee" + to_string(i));
 (ptr + i)->showData();
 }

 return 0;
}
```

Alternatively, we can use array indexing with pointers:

```cpp
for(int i = 0; i < 3; i++) {
 ptr[i].setData(100 + i, "Employee" + to_string(i));
 ptr[i].showData();
}
```

### Pointers to Objects as Function Parameters

Passing pointers to objects as function parameters allows functions to modify the original objects rather than working with copies. This is particularly useful when dealing with large objects where copying would be inefficient.

```cpp
class SwapNumbers {
private:
 int a, b;
public:
 void setValues(int x, int y) {
 a = x;
 b = y;
 }
 void display() {
 cout << "a = " << a << ", b = " << b << endl;
 }
};

void swap(SwapNumbers* obj) {
 int temp = obj->a;
 obj->a = obj->b;
 obj->b = temp;
}

int main() {
 SwapNumbers num;
 num.setValues(10, 20);
 num.display(); // a = 10, b = 20
 swap(&num);
 num.display(); // a = 20, b = 10
 return 0;
}
```

### Constant Pointers and Pointer to Constant

Understanding the difference between these two concepts is essential:

1. **Pointer to constant:** The data being pointed to cannot be changed

```cpp
const int* ptr; // Cannot modify the value through ptr
int const* ptr; // Same as above
```

2. **Constant pointer:** The pointer itself cannot point to a different address

```cpp
int* const ptr; // Pointer cannot be reassigned to point elsewhere
```

3. **Constant pointer to constant:** Neither the address nor the data can be changed

```cpp
const int* const ptr;
```

## Examples

### Example 1: Implementing a Simple Stack Using Pointers

```cpp
#include <iostream>
using namespace std;

class Stack {
private:
 int top;
 int arr[5];
public:
 Stack() {
 top = -1;
 }
 void push(int value) {
 if(top >= 4) {
 cout << "Stack Overflow" << endl;
 return;
 }
 arr[++top] = value;
 }
 int pop() {
 if(top < 0) {
 cout << "Stack Underflow" << endl;
 return -1;
 }
 return arr[top--];
 }
 void display() {
 if(top < 0) {
 cout << "Stack is empty" << endl;
 return;
 }
 for(int i = top; i >= 0; i--) {
 cout << arr[i] << " ";
 }
 cout << endl;
 }
};

int main() {
 Stack* s = new Stack();
 s->push(10);
 s->push(20);
 s->push(30);

 cout << "Stack contents: ";
 s->display();

 cout << "Popped: " << s->pop() << endl;
 cout << "Popped: " << s->pop() << endl;

 delete s;
 return 0;
}
```

**Output:**

```
Stack contents: 30 20 10
Popped: 30
Popped: 20
```

### Example 2: Using this Pointer for Method Chaining

```cpp
#include <iostream>
#include <string>
using namespace std;

class Person {
private:
 string name;
 int age;
 string city;
public:
 Person() {
 name = "";
 age = 0;
 city = "";
 }

 Person* setName(string n) {
 name = n;
 return this;
 }

 Person* setAge(int a) {
 age = a;
 return this;
 }

 Person* setCity(string c) {
 city = c;
 return this;
 }

 void display() {
 cout << "Name: " << name << ", Age: " << age << ", City: " << city << endl;
 }
};

int main() {
 Person* p = new Person();

 // Method chaining using this pointer
 p->setName("John")->setAge(25)->setCity("Bangalore");
 p->display();

 delete p;
 return 0;
}
```

### Example 3: Array of Pointers to Objects

```cpp
#include <iostream>
using namespace std;

class Product {
private:
 int id;
 string name;
 double price;
public:
 void setProduct(int i, string n, double p) {
 id = i;
 name = n;
 price = p;
 }
 void showProduct() {
 cout << "ID: " << id << ", Name: " << name << ", Price: " << price << endl;
 }
};

int main() {
 // Array of pointers to objects
 Product* products[3];

 // Allocate memory for each product
 for(int i = 0; i < 3; i++) {
 products[i] = new Product();
 }

 // Initialize products
 products[0]->setProduct(1, "Laptop", 50000);
 products[1]->setProduct(2, "Mobile", 15000);
 products[2]->setProduct(3, "Tablet", 25000);

 // Display all products
 cout << "Product Details:" << endl;
 for(int i = 0; i < 3; i++) {
 products[i]->showProduct();
 }

 // Free memory
 for(int i = 0; i < 3; i++) {
 delete products[i];
 }

 return 0;
}
```

## Exam Tips

1. **Arrow Operator vs Dot Operator:** Remember that arrow operator (->) is used with pointers to objects, while dot operator (.) is used with objects directly. Never confuse these two in exam questions.

2. **this Pointer Properties:** The `this` pointer is always available in non-static member functions and cannot be reassigned. It points to the object that invoked the function.

3. **Memory Management:** Always remember to use `delete` for single objects and `delete[]` for arrays of objects to prevent memory leaks. Forgetting to delete dynamically allocated memory is a common mistake.

4. **Pointer Initialization:** Always initialize pointers before use. An uninitialized pointer contains garbage values and can cause segmentation faults.

5. **Arrow Operator Precedence:** The arrow operator has high precedence, similar to the dot operator. In expressions like `*ptr.member`, parentheses may be needed: `(*ptr).member` is equivalent to `ptr->member`.

6. **Constant Pointers:** Understand the difference between `const int* ptr`, `int* const ptr`, and `const int* const ptr` as exam questions frequently test this concept.

7. **Dynamic Object Creation:** When creating objects dynamically with `new`, constructors are called automatically. Similarly, destructors are called when using `delete`.

8. **Array of Objects vs Array of Pointers:** Remember that `ClassName arr[10]` creates 10 objects, while `ClassName* arr[10]` creates 10 pointers that can point to objects.

9. **Function Parameters:** Passing objects by value creates a copy (copy constructor is called), while passing by reference or pointer avoids this overhead.

10. **Virtual Destructors:** When using polymorphism with base class pointers to derived objects, always declare base class destructors as virtual to ensure proper cleanup.
