cpp
#include <iostream>
using namespace std;

class MyClass {
public:
    int data;
    MyClass(int d) : data(d) {}
};

int main() {
    int MyClass::*ptr = &MyClass::data; // Declare and assign pointer

    MyClass obj(10);
    MyClass *objPtr = &obj;

    // Access using .* operator
    cout << "obj.data: " << obj.*ptr << endl; // Output: 10

    // Access using ->* operator
    cout << "objPtr->data: " << objPtr->*ptr << endl; // Output: 10

    // Change value through pointer
    obj.*ptr = 20;
    cout << "New obj.data: " << obj.data << endl; // Output: 20

    return 0;
}