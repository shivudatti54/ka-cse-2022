cpp
#include <iostream>
using namespace std;

class Rectangle {
private:
int length;
int breadth;

public:
// 1. Default Constructor (initializes to default values)
Rectangle() {
length = 0;
breadth = 0;
cout << "Default Constructor called." << endl;
}

    // 2. Parameterized Constructor (initializes with given values)
    Rectangle(int l, int b) {
        length = l;
        breadth = b;
        cout << "Parameterized Constructor called." << endl;
    }

    // 3. Another Parameterized Constructor (for a square)
    Rectangle(int side) {
        length = side;
        breadth = side;
        cout << "Constructor for Square called." << endl;
    }

    int area() {
        return length * breadth;
    }

};

int main() {
Rectangle obj1; // Calls Default Constructor
Rectangle obj2(10, 5); // Calls Parameterized Constructor (int, int)
Rectangle obj3(7); // Calls Parameterized Constructor (int) for square

    cout << "Area of obj2: " << obj2.area() << endl; // Output: 50
    cout << "Area of obj3: " << obj3.area() << endl; // Output: 49

    return 0;

}
