cpp
class MyArray {
private:
int\* data;
int size;
public:
// Constructor
MyArray(int sz) : size(sz) {
data = new int[size]; // Dynamic memory allocation
}

    // Destructor
    ~MyArray() {
        delete[] data; // Crucial cleanup to prevent memory leak
        cout << "MyArray Destructor: Memory freed." << endl;
    }

};
