java
// Declare a final class
final class SuperSecretAlgorithm {
public void calculate() {
System.out.println("Top Secret Calculation!");
}
}

// This will cause a COMPILATION ERROR
// Error: Cannot inherit from final 'SuperSecretAlgorithm'
class Hacker extends SuperSecretAlgorithm {
// Attempt to override or break the algorithm
}
