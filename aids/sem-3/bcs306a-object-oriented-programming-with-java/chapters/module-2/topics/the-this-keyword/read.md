java
public class Student {
    private String name;
    private int usn;

    // Constructor parameters have same names as instance variables
    public Student(String name, int usn) {
        // 'this.name' refers to the instance variable
        // 'name' refers to the constructor parameter
        this.name = name;
        this.usn = usn;
    }

    // A setter method
    public void setName(String name) {
        this.name = name; // Resolves the naming conflict
    }
}