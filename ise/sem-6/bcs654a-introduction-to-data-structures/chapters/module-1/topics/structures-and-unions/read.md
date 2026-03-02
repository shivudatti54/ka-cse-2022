c
// Define a structure template
struct Student {
    char name[50];
    char usn[11];
    int marks;
    long phone;
};

int main() {
    // Declare a structure variable
    struct Student s1;

    // Accessing members using the dot (.) operator
    strcpy(s1.name, "Ananya");
    strcpy(s1.usn, "1VT22CS001");
    s1.marks = 92;
    s1.phone = 9876543210;

    // Print the values
    printf("Name: %s\n", s1.name);
    printf("USN: %s\n", s1.usn);
    printf("Marks: %d\n", s1.marks);

    return 0;
}