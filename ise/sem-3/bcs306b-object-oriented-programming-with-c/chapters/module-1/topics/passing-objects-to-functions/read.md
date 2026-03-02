cpp
#include <iostream>
using namespace std;

class Number {
int num;
public:
Number(int n) : num(n) {}
void setNum(int n) { num = n; }
int getNum() const { return num; }
};

// Function accepting object by value
void modifyValue(Number numObj) {
numObj.setNum(100); // Modifies only the copy
cout << "Inside function (value): " << numObj.getNum() << endl;
}

int main() {
Number original(5);
modifyValue(original); // copy is created here
cout << "After function call (original): " << original.getNum() << endl;
return 0;
}
