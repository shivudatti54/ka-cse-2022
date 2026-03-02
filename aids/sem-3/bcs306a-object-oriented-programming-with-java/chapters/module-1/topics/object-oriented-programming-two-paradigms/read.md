c
// Data (variables) are declared separately
float length;
float width;
float area;

// A function to perform a task
void calculateArea() {
    area = length * width;
}

// Main procedure
void main() {
    length = 10.0;
    width = 5.0;
    calculateArea(); // Function call
    printf("Area: %f", area);
}