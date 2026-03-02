cpp
class Shape {
public:
void draw() {
cout << "Drawing a Shape" << endl;
}
};

class Circle : public Shape {
public:
void draw() {
cout << "Drawing a Circle" << endl;
}
};
