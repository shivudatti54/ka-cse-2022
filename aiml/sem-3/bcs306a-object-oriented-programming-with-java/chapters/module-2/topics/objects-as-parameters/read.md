java
class Student {
    String name;
    int usn;

    Student(String n, int u) {
        name = n;
        usn = u;
    }
}

public class Test {
    // Method that takes a Student object as a parameter
    public static void updateDetails(Student s, String newName) {
        s.name = newName; // This modifies the original object
        System.out.println("Inside method: " + s.name);
    }

    public static void main(String[] args) {
        Student student1 = new Student("Alice", 101);
        System.out.println("Before update: " + student1.name);

        updateDetails(student1, "Bob"); // Pass the object reference

        System.out.println("After update: " + student1.name);
    }
}