java
class Student {
    String name;
    int rollNumber;

    // Constructor
    Student(String n, int r) {
        name = n;
        rollNumber = r;
    }

    // Method to display student info
    void displayInfo() {
        System.out.println("Name: " + name + ", Roll Number: " + rollNumber);
    }
}