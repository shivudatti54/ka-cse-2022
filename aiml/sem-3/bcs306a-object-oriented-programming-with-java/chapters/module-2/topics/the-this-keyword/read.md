java
class Student {
    int id; // Instance Variable
    String name; // Instance Variable

    // Constructor parameters shadow instance variables
    Student(int id, String name) {
        this.id = id; // 'this.id' refers to the instance variable
        this.name = name; // 'this.name' refers to the instance variable
        // The right-hand side 'id' and 'name' refer to the parameters.
    }
}