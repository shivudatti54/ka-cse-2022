cpp
#include <iostream>
#include <cstdlib> // For malloc and free

class MyClass {
int data;
public:
MyClass(int d) : data(d) {}

    // Overloaded class-specific new
    static void* operator new(size_t size) {
        std::cout << "Custom new: Allocating " << size << " bytes.\n";
        void* p = malloc(size);
        if (!p) {
            throw std::bad_alloc(); // Must throw bad_alloc on failure
        }
        return p;
    }

    // Overloaded class-specific delete
    static void operator delete(void* p, size_t size) {
        std::cout << "Custom delete: Freeing memory of size " << size << ".\n";
        free(p);
    }

};

int main() {
MyClass\* obj = new MyClass(10); // Calls overloaded new
delete obj; // Calls overloaded delete
return 0;
}
