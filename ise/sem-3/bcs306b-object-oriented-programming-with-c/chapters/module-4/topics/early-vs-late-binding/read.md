cpp
#include <iostream>
using namespace std;

class Base {
public:
void show() {
cout << "Inside Base class" << endl;
}
};

class Derived : public Base {
public:
void show() { // Redefines Base's show()
cout << "Inside Derived class" << endl;
}
};

int main() {
Base\* bptr; // Base class pointer
Derived d; // Derived class object
bptr = &d; // Pointing to Derived object

    // Early Binding - Decision based on pointer type (Base*)
    bptr->show();       // Output: "Inside Base class"

    return 0;

}
