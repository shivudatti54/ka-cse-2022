java
// This will cause a compile-time ERROR.
public int add(int a, int b) { return a + b; }
public double add(int a, int b) { return (double)(a + b); } // Invalid