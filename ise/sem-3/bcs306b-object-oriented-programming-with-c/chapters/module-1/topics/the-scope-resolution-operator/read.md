cpp
#include <iostream>
using namespace std;

int num = 100; // Global variable

int main() {
int num = 50; // Local variable

    cout << "Local variable num: " << num << endl;       // Outputs 50
    cout << "Global variable num: " << ::num << endl;    // Outputs 100 (using ::)

    return 0;

}
