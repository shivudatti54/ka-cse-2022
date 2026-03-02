cpp
#include <iostream>
using namespace std;

// Base exception class
class BaseException {
public:
virtual const char\* what() const { return "BaseException occurred"; }
};

// Derived exception class
class DerivedException : public BaseException {
public:
const char\* what() const override { return "DerivedException occurred"; }
};

int main() {
try {
throw DerivedException(); // Throw a derived class object
}
catch (const DerivedException &e) { // CORRECT: Most derived first
cout << "Caught: " << e.what() << endl;
}
catch (const BaseException &e) { // CORRECT: Base class next
cout << "Caught: " << e.what() << endl;
}

    cout << "\n--- Incorrect Order Example ---\n";

    try {
        throw DerivedException(); // Throw the same derived class object
    }
    catch (const BaseException &e) {     // ERROR: Base class first!
        cout << "Caught: " << e.what() << endl;
        // This block will catch the DerivedException due to the inheritance.
        // The DerivedException-specific handler below will never be called.
    }
    catch (const DerivedException &e) {  // This block is unreachable
        cout << "Caught: " << e.what() << endl;
    }

    return 0;

}
