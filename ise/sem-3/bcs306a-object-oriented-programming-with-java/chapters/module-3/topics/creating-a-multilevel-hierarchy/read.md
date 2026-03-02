java
class Vehicle {
private String registrationNumber;

    public Vehicle(String regNo) {
        this.registrationNumber = regNo;
    }

    public void start() {
        System.out.println("Vehicle engine started.");
    }

    public String getRegistrationNumber() {
        return registrationNumber;
    }

}
