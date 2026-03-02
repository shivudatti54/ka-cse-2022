java
public class Student {
    // Private data members (encapsulated)
    private String name;
    private int rollNo;

    // Public getter method for 'name'
    public String getName() {
        return name;
    }

    // Public setter method for 'name' (with validation)
    public void setName(String name) {
        if (name != null && !name.isEmpty()) {
            this.name = name;
        }
    }

    // Getter and Setter for rollNo...
}