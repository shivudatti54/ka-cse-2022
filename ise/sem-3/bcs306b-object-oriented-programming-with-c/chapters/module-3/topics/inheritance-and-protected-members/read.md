cpp
#include <iostream>
using namespace std;

// Base Class
class Vehicle {
protected: // Accessible in derived classes, but not outside
string brand = "Unknown";

public:
void honk() {
cout << "Honk! Honk!" << endl;
}
};

// Derived Class (public inheritance)
class Car : public Vehicle {
private:
int numOfDoors;

public:
void setBrand(string b) {
brand = b; // OK: brand is protected, so Car can access it
}
void displayInfo() {
cout << "Brand: " << brand << endl; // OK
honk(); // OK: public member is inherited
}
};

int main() {
Car myCar;
myCar.setBrand("Maruti");
myCar.displayInfo();
// myCar.brand = "Honda"; // Error! 'brand' is protected and not accessible here.
return 0;
}
