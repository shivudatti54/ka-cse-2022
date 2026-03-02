c
    #include <stdio.h>

    // Data (separate)
    float length;
    float width;

    // Function to operate on data
    float calculateArea(float l, float w) {
        return l * w;
    }

    int main() {
        length = 5.0;
        width = 3.0;
        float area = calculateArea(length, width); // Function called with data
        printf("Area: %.2f", area);
        return 0;
    }