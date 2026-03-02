java
class Grandparent {
Grandparent() {
System.out.println("Grandparent Constructor Executed");
}
}

class Parent extends Grandparent {
Parent() {
// Compiler adds super() here implicitly
System.out.println("Parent Constructor Executed");
}
}

class Child extends Parent {
Child() {
// Compiler adds super() here implicitly
System.out.println("Child Constructor Executed");
}
}

public class ConstructorChainingDemo {
public static void main(String[] args) {
Child child = new Child(); // Creating a Child object
}
}
