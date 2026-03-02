cpp
#include <iostream>
using namespace std;

// Base class
class Base {
public:
    int base_var;
    void show_base() { cout << "Base: " << base_var << endl; }
};

// Derived class
class Derived : public Base {
public:
    int derived_var;
    void show_derived() { cout << "Derived: " << derived_var << endl; }
};

int main() {
    Derived derived_obj;
    Base* base_ptr; // Pointer of base type

    base_ptr = &derived_obj; // Perfectly valid: base_ptr points to a Derived object

    base_ptr->base_var = 10;
    base_ptr->show_base(); // Works correctly

    // base_ptr->derived_var = 20; // ERROR: Compiler doesn't know about derived members
    // base_ptr->show_derived();   // ERROR

    return 0;
}