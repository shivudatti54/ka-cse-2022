java
class Parent {
    final int MAX_SPEED = 100; // Final variable

    void display() {
        System.out.println("Max speed is: " + MAX_SPEED);
    }
}

class Child extends Parent {
    // This would cause a compilation error. Cannot override or change final variable.
    // void changeSpeed() {
    //     MAX_SPEED = 150;
    // }
}