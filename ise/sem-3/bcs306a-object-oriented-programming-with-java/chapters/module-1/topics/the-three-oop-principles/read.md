java
public class Student {
    // Private data members (encapsulated)
    private String name;
    private int rollNumber;

    // Public getter method for 'name'
    public String getName() {
        return name;
    }

    // Public setter method for 'name' with validation
    public void setName(String name) {
        if (name != null && !name.isEmpty()) {
            this.name = name;
        }
    }

    // Similarly for rollNumber
    public int getRollNumber() {
        return rollNumber;
    }

    public void setRollNumber(int rollNumber) {
        if (rollNumber > 0) {
            this.rollNumber = rollNumber;
        }
    }
}