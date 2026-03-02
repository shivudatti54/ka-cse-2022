java
class Student {
Student friend;
}

    Student s1 = new Student();
    Student s2 = new Student();
    s1.friend = s2;
    s2.friend = s1;

    s1 = null;
    s2 = null;
    // Both objects are now eligible for GC, as they reference only each other.
