cpp
class Shape {
public:
void area() {
cout << "Shape Area Calculation" << endl;
}
};

class Rectangle : public Shape {
public:
void area() {
cout << "Area of Rectangle (l\*b)" << endl;
}
};

int main() {
Shape \*shapePtr;
Rectangle rectObj;

    shapePtr = &rectObj;  // Base class pointer pointing to derived class object
    shapePtr->area();     // Output: "Shape Area Calculation"

}
