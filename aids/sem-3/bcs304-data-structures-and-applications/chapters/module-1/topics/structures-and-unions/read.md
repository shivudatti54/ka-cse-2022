c
// Step 1: Define the structure template (blueprint)
struct Student {
    char name[50];
    int usn;
    float marks;
}; // Notice the semicolon here

int main() {
    // Step 2: Declare a structure variable
    struct Student student1;

    // Step 3: Access and assign values to members
    strcpy(student1.name, "Ananya");
    student1.usn = 123;
    student1.marks = 92.5;

    // Step 4: Access and print values
    printf("Student Name: %s\n", student1.name);
    printf("USN: %d\n", student1.usn);
    printf("Marks: %.2f\n", student1.marks);

    return 0;
}