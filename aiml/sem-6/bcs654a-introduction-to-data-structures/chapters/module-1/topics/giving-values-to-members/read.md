c
#include <stdio.h>
#include <string.h>

// Define a structure named 'student'
struct student {
    char name[50];
    int usn;
    float cgpa;
};

int main() {
    // Declare a variable 's1' of type 'struct student'
    struct student s1;

    // Assign values to members using the '.' operator
    strcpy(s1.name, "Alan Turing"); // For string arrays, use strcpy
    s1.usn = 123;
    s1.cgpa = 9.8;

    // Print the values
    printf("Student Name: %s\n", s1.name);
    printf("USN: %d\n", s1.usn);
    printf("CGPA: %.2f\n", s1.cgpa);

    return 0;
}