cpp
#include <iostream>
using namespace std;

int main() {
int numerator, denominator;
cout << "Enter numerator and denominator: ";
cin >> numerator >> denominator;

    try {
        if (denominator == 0) {
            // Throw an exception (an integer in this case)
            throw 0;
        }
        double result = numerator / denominator;
        cout << "Result is: " << result << endl;
    }
    catch (int ex) { // Catch the thrown integer
        cout << "Error: Division by zero is not allowed!" << endl;
    }

    cout << "Program continues after try-catch." << endl;
    return 0;

}
