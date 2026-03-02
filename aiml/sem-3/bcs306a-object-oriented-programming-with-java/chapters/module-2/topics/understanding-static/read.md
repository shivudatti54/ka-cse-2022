java
class Student {
    int rollNo;                 // Instance variable (unique per object)
    String name;               // Instance variable
    static String collegeName = ""; // Static variable (shared by all objects)
    static int count = 0;      // Static variable to count objects

    public Student(int r, String n) {
        rollNo = r;
        name = n;
        count++; // Increment the shared counter for every new object created
    }

    void display() {
        System.out.println(rollNo + " " + name + " " + collegeName);
    }
}

public class TestStatic {
    public static void main(String args[]) {
        Student s1 = new Student(101, "Alice");
        Student s2 = new Student(102, "Bob");
        Student s3 = new Student(103, "Charlie");

        s1.display();
        s2.display();

        // Accessing static variable using class name (Recommended)
        System.out.println("Total Students created: " + Student.count);
        System.out.println("College: " + Student.collegeName);

        // Also possible, but NOT recommended (compiler will replace it with ClassName.variable)
        // System.out.println(s1.count);
    }
}