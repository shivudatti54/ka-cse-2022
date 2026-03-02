# Enumerations in Java


## Table of Contents

- [Enumerations in Java](#enumerations-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Basic Enum Declaration](#basic-enum-declaration)
  - [Enum Internals and the Enum Class](#enum-internals-and-the-enum-class)
  - [Enum with Custom Fields and Constructors](#enum-with-custom-fields-and-constructors)
  - [Enum Methods and Abstract Methods](#enum-methods-and-abstract-methods)
  - [Enums in Switch Statements](#enums-in-switch-statements)
  - [EnumSet and EnumMap](#enumset-and-enummap)
- [Examples](#examples)
  - [Example 1: Traffic Light Simulation](#example-1-traffic-light-simulation)
  - [Example 2: Employee Status Management](#example-2-employee-status-management)
  - [Example 3: Using EnumMap for Salary Calculation](#example-3-using-enummap-for-salary-calculation)
- [Exam Tips](#exam-tips)

## Introduction

Enumeration (enum) is a special data type in Java that defines a fixed set of constants. Introduced in Java 5, enumerations provide a type-safe way to represent a predefined collection of related values. Unlike traditional constant definitions using static final variables, enums are strongly typed and prevent invalid values from being assigned. This chapter explores the Java enum type in depth, examining its syntax, internal representation, methods, and advanced features such as custom fields, constructors, and methods.

Enumerations in Java are far more powerful than simple constant lists. They are implemented as a special kind of class that extends the java.lang.Enum class implicitly. This inheritance provides numerous built-in methods and allows developers to add custom fields, constructors, and methods to create sophisticated enumerated types that can encapsulate behavior and state.

## Key Concepts

### Basic Enum Declaration

The simplest form of an enum declaration defines a set of named constants:

```java
public enum Day {
 SUNDAY, MONDAY, TUESDAY, WEDNESDAY,
 THURSDAY, FRIDAY, SATURDAY
}
```

Each enum constant is implicitly public, static, and final. The type of each constant is the enclosing enum class. You cannot instantiate enums using the new operator, as the constructor is implicitly private.

### Enum Internals and the Enum Class

All enums implicitly extend java.lang.Enum, which provides several important methods:

- `values()`: Returns an array of all enum constants in declaration order
- `valueOf(String name)`: Returns the enum constant with the specified name
- `name()`: Returns the name of the enum constant
- `ordinal()`: Returns the position of the enum constant (zero-based)

```java
Day[] days = Day.values(); // Array of all constants
Day monday = Day.valueOf("MONDAY"); // Converts string to enum
System.out.println(Day.MONDAY.ordinal()); // Output: 1
```

### Enum with Custom Fields and Constructors

Enums can have instance variables, constructors, and methods, making them powerful containers for related data:

```java
public enum Planet {
 MERCURY(3.303e+23, 2.4397e6),
 VENUS(4.869e+24, 6.0518e6),
 EARTH(5.976e+24, 6.37814e6),
 MARS(6.421e+23, 3.3972e6),
 JUPITER(1.899e+27, 7.1492e7),
 SATURN(5.685e+26, 6.0268e7),
 URANUS(8.683e+25, 2.5559e7),
 NEPTUNE(1.024e+26, 2.4746e7);

 private final double mass; // in kilograms
 private final double radius; // in meters

 // Private constructor
 Planet(double mass, double radius) {
 this.mass = mass;
 this.radius = radius;
 }

 // Method to calculate surface gravity
 public double surfaceGravity() {
 return 6.67300E-11 * mass / (radius * radius);
 }

 public double getMass() {
 return mass;
 }

 public double getRadius() {
 return radius;
 }
}
```

### Enum Methods and Abstract Methods

Enums can define abstract methods, with each constant providing its own implementation:

```java
public enum Operation {
 PLUS {
 public double evaluate(double x, double y) { return x + y; }
 },
 MINUS {
 public double evaluate(double x, double y) { return x - y; }
 },
 TIMES {
 public double evaluate(double x, double y) { return x * y; }
 },
 DIVIDE {
 public double evaluate(double x, double y) { return x / y; }
 };

 public abstract double evaluate(double x, double y);
}
```

### Enums in Switch Statements

Enums work seamlessly with switch statements, providing a clean alternative to if-else chains:

```java
public String getDayType(Day day) {
 switch(day) {
 case SATURDAY:
 case SUNDAY:
 return "Weekend";
 default:
 return "Weekday";
 }
}
```

Note that in switch statements with enums, you do not need to qualify the constants with the enum type name (use SATURDAY, not Day.SATURDAY).

### EnumSet and EnumMap

Java provides specialized collections for enums: EnumSet and EnumMap.

EnumSet is a Set implementation optimized for enum types:

```java
EnumSet<Day> weekend = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
EnumSet<Day> workDays = EnumSet.complementOf(weekend);
EnumSet<Day> allDays = EnumSet.allOf(Day.class);
```

EnumMap is a Map implementation with enum keys:

```java
EnumMap<Day, String> schedule = new EnumMap<>(Day.class);
schedule.put(Day.MONDAY, "Work from 9-5");
schedule.put(Day.SATURDAY, "Relax");
```

## Examples

### Example 1: Traffic Light Simulation

```java
enum TrafficLight {
 RED(30) {
 public TrafficLight next() { return GREEN; }
 },
 YELLOW(5) {
 public TrafficLight next() { return RED; }
 },
 GREEN(45) {
 public TrafficLight next() { return YELLOW; }
 };

 private final int duration; // seconds

 TrafficLight(int duration) {
 this.duration = duration;
 }

 public abstract TrafficLight next();

 public int getDuration() {
 return duration;
 }
}

public class TrafficLightDemo {
 public static void main(String[] args) {
 TrafficLight light = TrafficLight.RED;
 for (int i = 0; i < 5; i++) {
 System.out.println(light + " light for " +
 light.getDuration() + " seconds");
 light = light.next();
 }
 }
}
```

### Example 2: Employee Status Management

```java
enum EmployeeStatus {
 ACTIVE("Active", true),
 ON_LEAVE("On Leave", true),
 TERMINATED("Terminated", false),
 SUSPENDED("Suspended", false);

 private final String displayName;
 private final boolean working;

 EmployeeStatus(String displayName, boolean working) {
 this.displayName = displayName;
 this.working = working;
 }

 public boolean isWorking() {
 return working;
 }

 public String getDisplayName() {
 return displayName;
 }
}
```

### Example 3: Using EnumMap for Salary Calculation

```java
enum Department {
 IT, HR, SALES, MARKETING, FINANCE
}

public class SalaryCalculator {
 private static final EnumMap<Department, Double>
 baseSalaries = new EnumMap<>(Department.class);

 static {
 baseSalaries.put(Department.IT, 75000.0);
 baseSalaries.put(Department.HR, 60000.0);
 baseSalaries.put(Department.SALES, 65000.0);
 baseSalaries.put(Department.MARKETING, 55000.0);
 baseSalaries.put(Department.FINANCE, 70000.0);
 }

 public static double calculateSalary(Department dept, double bonus) {
 Double base = baseSalaries.get(dept);
 return base != null ? base + bonus : 0.0;
 }
}
```

## Exam Tips

1. Remember that enum constants are implicitly public, static, and final. You cannot extend an enum or create instances using new.

2. All enums implicitly extend java.lang.Enum. Since Java does not support multiple inheritance, an enum cannot extend any other class.

3. Enum constructors are always private (you can omit the modifier as it's enforced). Attempting to use public or protected constructors will result in a compilation error.

4. The values() method is not declared in java.lang.Enum but is added automatically by the compiler for every enum type.

5. Use EnumSet when you need a Set with enum keys for better performance and type safety. EnumSet is internally implemented as a bit vector.

6. In switch statements with enums, use just the constant name (MONDAY) not the fully qualified name (Day.MONDAY), otherwise the compiler will generate an error.

7. The ordinal() method returns the position in the enum declaration starting from 0. Do not use ordinal() for storing values in databases; use explicit fields instead.

8. Enum constants can implement interfaces, allowing for strategy pattern implementation through enums.
