cpp
#include <iostream>
using namespace std;

// Function to add two integers
int add(int a, int b) {
return a + b;
}

// Overloaded function to add three integers (Different number of parameters)
int add(int a, int b, int c) {
return a + b + c;
}

// Overloaded function to add two doubles (Different type of parameters)
double add(double a, double b) {
return a + b;
}

int main() {
cout << add(5, 10) << endl; // Calls add(int, int) -> Output: 15
cout << add(5, 10, 15) << endl; // Calls add(int, int, int) -> Output: 30
cout << add(3.14, 2.71) << endl; // Calls add(double, double) -> Output: 5.85
return 0;
}
