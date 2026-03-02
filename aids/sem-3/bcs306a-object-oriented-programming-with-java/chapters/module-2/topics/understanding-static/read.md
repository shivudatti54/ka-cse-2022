java
class Student {
    int rollNo;              // Instance variable (per object)
    String name;            // Instance variable (per object)
    static String college = ""; // Static variable (shared by all objects)

    Student(int r, String n) {
        rollNo = r;
        name = n;
    }

    void display() {
        System.out.println(rollNo + " " + name + " " + college);
    }
}

public class TestStatic {
    public static void main(String args[]) {
        Student s1 = new Student(101, "Alice");
        Student s2 = new Student(102, "Bob");

        s1.display(); // Output: 101 Alice 
        s2.display(); // Output: 102 Bob 

        // Change the static variable - affects all objects
        Student.college = " Belgaum";

        s1.display(); // Output: 101 Alice  Belgaum
        s2.display(); // Output: 102 Bob  Belgaum
    }
}