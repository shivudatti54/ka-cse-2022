java
class Person {
String name;
// Superclass Parameterized Constructor
Person(String name) {
this.name = name;
System.out.println("Inside Person constructor");
}
}

class Student extends Person {
int rollNo;
// Subclass Constructor
Student(String name, int rollNo) {
super(name); // Must be the first line. Calls Person(String name)
this.rollNo = rollNo;
System.out.println("Inside Student constructor");
}
}

public class Main {
public static void main(String[] args) {
Student s1 = new Student("Alice", 101);
System.out.println("Name: " + s1.name + ", Roll No: " + s1.rollNo);
}
}
