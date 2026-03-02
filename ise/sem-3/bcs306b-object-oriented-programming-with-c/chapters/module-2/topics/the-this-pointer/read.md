cpp
#include <iostream>
using namespace std;

class Rectangle {
    int width, height;
  public:
    void setDimensions(int width, int height) {
        // 'width' here refers to the parameter, not the member.
        // 'this->width' explicitly refers to the class member.
        this->width = width;
        this->height = height;
    }
    void display() {
        cout << "Width: " << width << ", Height: " << height << endl;
    }
};

int main() {
    Rectangle rect;
    rect.setDimensions(5, 10);
    rect.display(); // Output: Width: 5, Height: 10
    return 0;
}