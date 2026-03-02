c
#include <stdio.h>

// Data (separate from functions)
float radius = 5.0;
float area;

// Function to calculate area
void calculateArea(float r) {
    area = 3.14 * r * r;
}

// Main procedure
int main() {
    calculateArea(radius);
    printf("Area of circle: %.2f", area);
    return 0;
}