java
// User-defined class
public class Student implements Comparable<Student> {
private int rollNo;
private String name;

// Constructor, Getters, Setters...

@Override
public boolean equals(Object obj) {
if (this == obj) return true;
if (obj == null || getClass() != obj.getClass()) return false;
Student student = (Student) obj;
return rollNo == student.rollNo; // Equality based on rollNo
}

@Override
public int hashCode() {
return Objects.hash(rollNo); // Hash code based on rollNo
}

@Override
public int compareTo(Student other) {
return Integer.compare(this.rollNo, other.rollNo); // Natural ordering by rollNo
}

}
