cpp
class MyClass {
public:
int data;
char character;
};

int main() {
MyClass obj1;
obj1.data = 10;
obj1.character = 'A';

    MyClass obj2;
    obj2 = obj1; // Default assignment: member-wise copy

    // Now, obj2.data is 10 and obj2.character is 'A'
    return 0;

}
