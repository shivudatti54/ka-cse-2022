# Requirements to Design Model
## Software Engineering - BSc (Hons) Computer Science (Delhi University, NEP 2024 UGCF)

---

## 1. Introduction

The transition from **requirements** to **design** represents one of the most critical phases in the software development lifecycle (SDLC). While requirements engineering focuses on *what* the system must do, the design phase addresses *how* the system will achieve those objectives. This bridge between analysis and design is fundamental to building maintainable, scalable, and robust software systems.

In real-world software development, a poorly designed system—even with perfect requirements—can lead to catastrophic failures. Consider the case of **Therac-25 radiation therapy machine** (1985-1987), where inadequate design consideration for safety requirements resulted in patient deaths. Conversely, well-architected systems like **Netflix's recommendation engine** demonstrate how thoughtful design transforms simple functional requirements into revolutionary user experiences.

For Delhi University CS students, understanding this transformation is essential as organizations increasingly adopt model-driven development approaches and design-centric methodologies.

---

## 2. Requirements Engineering Fundamentals

### 2.1 What Are Requirements?

Requirements are documented representations of stakeholder needs, describing system functionality, constraints, and desired properties. They serve as the **contract** between stakeholders and developers.

### 2.2 Types of Requirements

#### Functional Requirements (FR)
Describe specific behaviors or functions the system must perform.

| Requirement Type | Description | Example |
|-----------------|-------------|---------|
| **Core Functions** | Primary system operations | "The system shall allow users to search for books by title, author, or ISBN" |
| **Data Processing** | Operations on input data | "The system shall calculate total bill including GST" |
| **User Interactions** | Operations users can perform | "The system shall allow online seat booking" |

#### Non-Functional Requirements (NFR)
Define quality attributes rather than specific behaviors:

- **Performance**: Response time < 2 seconds for 1000 concurrent users
- **Security**: AES-256 encryption for sensitive data
- **Reliability**: 99.9% uptime (8.76 hours downtime/year)
- **Usability**: Average task completion time < 30 seconds
- **Maintainability**: Mean time to repair (MTTR) < 4 hours
- **Scalability**: Support 10x load increase without architecture changes

#### Domain Requirements
Derived from the application domain:
- "Banking system must comply with RBI guidelines for transaction logging"
- "Healthcare system must follow HL7 FHIR standards for patient data"

### 2.3 Requirements Gathering Techniques

| Technique | Description | Best For |
|-----------|-------------|----------|
| **Interviews** | Direct stakeholder conversation | Detailed domain knowledge |
| **Questionnaires** | Survey large user groups | Statistical requirements |
| **Observation** | Studying work environments | Unspoken requirements |
| **Prototyping** | Interactive mockups | UI requirements |
| **Use Case Analysis** | Scenario-based requirements | Functional flow understanding |
| **JAD Sessions** | Joint application development | Rapid requirement consensus |

### 2.4 Software Requirements Specification (SRS)

The SRS document (IEEE 830 standard) provides a complete description of:

1. **Introduction**: Purpose, scope, definitions
2. **Overall Description**: User characteristics, product perspective, constraints
3. **Specific Requirements**: All functional and non-functional requirements
4. **Appendices**: Glossary, analysis models, issues list

---

## 3. From Requirements to Design Model

### 3.1 The Transformation Challenge

The requirements-to-design transformation is not merely a documentation exercise—it requires **creative problem-solving** and **technical expertise**. This transformation involves:

```
Requirements → Analysis Model → Design Model → Implementation
    (WHAT)       (Understanding)   (HOW)         (Code)
```

### 3.2 Design Goals

Based on requirements, designers establish clear goals:

1. **Correctness**: Does the design fulfill all requirements?
2. **Efficiency**: Are resources utilized optimally?
3. **Flexibility**: How easily can the system adapt to changes?
4. **Reusability**: Can components be reused in other systems?
5. **Understandability**: Is the design comprehensible to developers?

### 3.3 Design Inputs from Requirements

| Requirements Aspect | Design Impact |
|--------------------|---------------|
| Functional Requirements | Module decomposition, class design, algorithm selection |
| Performance Requirements | Architecture choices, caching strategies, database indexing |
| Security Requirements | Authentication mechanisms, encryption, access control |
| Integration Requirements | API design, middleware, message formats |
| User Interface Requirements | MVC/MVVM pattern, view technologies |

---

## 4. Design Models and UML Diagrams

### 4.1 Why UML for Design?

Unified Modeling Language (UML) provides standardized notation for visualizing, specifying, constructing, and documenting design artifacts. For design purposes, the following UML diagrams are most relevant:

### 4.2 Key UML Diagrams for Design

#### Class Diagram
Represents static structure showing classes, attributes, operations, and relationships.

```
┌─────────────────────────────────┐
│         <<interface>>           │
│         IPaymentProcessor       │
├─────────────────────────────────┤
│ + processPayment(amount:double) │
│ + refund(transactionId:String)  │
└───────────────┬─────────────────┘
                │ implements
                ▼
┌─────────────────────────────────┐
│         CreditCardPayment       │
├─────────────────────────────────┤
│ - cardNumber: String            │
│ - cvv: String                   │
│ - expiryDate: Date              │
├─────────────────────────────────┤
│ + processPayment(amount:double) │
│ + validateCard(): boolean       │
│ + refund(transactionId:String)  │
└─────────────────────────────────┘
```

#### Sequence Diagram
Illustrates object interactions arranged in time sequence—crucial for understanding runtime behavior.

#### Component Diagram
Shows organization and dependencies among software components—essential for architectural design.

#### Package Diagram
Groups related classes and indicates namespace organization.

### 4.3 Architectural Patterns

#### MVC (Model-View-Controller)
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    View    │◄───►│ Controller  │◄───►│    Model    │
│  (UI Layer)│     │  (Logic)    │     │   (Data)    │
└─────────────┘     └─────────────┘     └─────────────┘
```
- **Model**: Data and business logic
- **View**: Presentation layer
- **Controller**: Handles user input, coordinates Model and View

#### MVP (Model-View-Presenter)
Similar to MVC but Presenter handles all UI logic, making Views passive.

#### MVVM (Model-View-ViewModel)
Popular in modern frameworks (Angular, Vue.js) with two-way data binding.

---

## 5. Design Patterns

Design patterns provide reusable solutions to common software design problems. They represent **best practices** evolved over decades of software engineering.

### 5.1 Creational Patterns

#### Singleton Pattern
Ensures a class has only one instance and provides a global access point.

```java
public class DatabaseConnection {
    private static DatabaseConnection instance;
    private Connection connection;
    
    // Private constructor prevents external instantiation
    private DatabaseConnection() {
        // Initialize database connection
    }
    
    public static synchronized DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }
    
    public Connection getConnection() {
        return connection;
    }
}
```

#### Factory Method Pattern
Defines an interface for creating objects, letting subclasses decide which class to instantiate.

```java
// Product interface
interface Notification {
    void send(String message);
}

// Concrete products
class EmailNotification implements Notification {
    public void send(String message) {
        System.out.println("Sending Email: " + message);
    }
}

class SMSNotification implements Notification {
    public void send(String message) {
        System.out.println("Sending SMS: " + message);
    }
}

// Factory
class NotificationFactory {
    public static Notification createNotification(String type) {
        return switch (type.toLowerCase()) {
            case "email" -> new EmailNotification();
            case "sms" -> new SMSNotification();
            default -> throw new IllegalArgumentException("Unknown type");
        };
    }
}
```

### 5.2 Structural Patterns

#### Adapter Pattern
Converts one interface into another that clients expect.

```java
// Legacy payment system
class LegacyPaymentGateway {
    public void pay(String amount, Map<String, String> details) {
        System.out.println("Legacy payment: " + amount);
    }
}

// New expected interface
interface PaymentProcessor {
    void processPayment(double amount, PaymentDetails details);
}

// Adapter
class PaymentAdapter implements PaymentProcessor {
    private LegacyPaymentGateway legacyGateway;
    
    @Override
    public void processPayment(double amount, PaymentDetails details) {
        Map<String, String> legacyDetails = new HashMap<>();
        legacyDetails.put("card", details.getCardNumber());
        legacyGateway.pay(String.valueOf(amount), legacyDetails);
    }
}
```

### 5.3 Behavioral Patterns

#### Observer Pattern
Defines one-to-many dependency so that when one object changes state, all dependents are notified.

```java
// Subject interface
interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers();
}

// Concrete Subject
class Stock implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private double price;
    
    public void setPrice(double price) {
        this.price = price;
        notifyObservers();  // Notify all observers when price changes
    }
    
    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }
    
    @Override
    public void notifyObservers() {
        for (Observer obs : observers) {
            obs.update(this);
        }
    }
}

// Observer interface
interface Observer {
    void update(Stock stock);
}

// Concrete Observer
class Investor implements Observer {
    private String name;
    
    public Investor(String name) {
        this.name = name;
    }
    
    @Override
    public void update(Stock stock) {
        System.out.println(name + " notified: Stock price is now " + stock.getPrice());
    }
}
```

#### Strategy Pattern
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.

```java
// Strategy interface
interface PaymentStrategy {
    void pay(double amount);
}

// Concrete strategies
class CreditCardPayment implements PaymentStrategy {
    private String cardNumber;
    public void pay(double amount) {
        System.out.println("Paid " + amount + " via Credit Card");
    }
}

class UPIPayment implements PaymentStrategy {
    private String upiId;
    public void pay(double amount) {
        System.out.println("Paid " + amount + " via UPI");
    }
}

// Context
class ShoppingCart {
    private PaymentStrategy paymentStrategy;
    
    public void setPaymentStrategy(PaymentStrategy strategy) {
        this.paymentStrategy = strategy;
    }
    
    public void checkout(double amount) {
        paymentStrategy.pay(amount);
    }
}
```

---

## 6. SOLID Principles

The SOLID principles are fundamental object-oriented design guidelines:

| Principle | Description | Example |
|-----------|-------------|---------|
| **S**ingle Responsibility | A class should have only one reason to change | `UserAuth` handles only authentication, not data storage |
| **O**pen/Closed | Open for extension, closed for modification | Use strategy pattern to add new behaviors without changing existing code |
| **L**iskov Substitution | Subtypes must be substitutable for base types | `Square` extending `Rectangle` violates this if `setWidth()` changes height |
| **I**nterface Segregation | Prefer small, specific interfaces over large ones | `Printer` interface separate from `Scanner` interface |
| **D**ependency Inversion | Depend on abstractions, not concretions | Inject `Repository` interface, not `MySQLRepository` class |

---

## 7. Practical Examples

### Example 1: Library Management System

**Requirements:**
- Users can borrow and return books
- System tracks due dates and generates fines
- Administrators can add/remove books
- System must handle concurrent access

**Design Model (Partial):**

```java
// Domain entities
class Book {
    private String isbn;
    private String title;
    private Author author;
    private int availableCopies;
    private List<Copy> copies;
}

class Member {
    private String memberId;
    private String name;
    private MembershipType type;
    private List<Loan> activeLoans;
}

class Loan {
    private LocalDate borrowDate;
    private LocalDate dueDate;
    private LocalDate returnDate;
    private BookCopy borrowedCopy;
    private Member member;
    private LoanStatus status;
}

// Design pattern: Observer for fine notifications
interface FineObserver {
    void onFineGenerated(Member member, double amount);
}

class EmailFineObserver implements FineObserver { }
class SMSFineObserver implements FineObserver { }
class DatabaseFineLogger implements FineObserver { }
```

**UML Class Diagram Relationships:**
- `Book` → `1:N` → `BookCopy`
- `Member` → `1:N` → `Loan`
- `Loan` → `1:1` → `BookCopy`
- `Loan` → `1:1` → `Member`

### Example 2: E-Commerce Platform

**Requirements:**
- Product catalog with search and filtering
- Shopping cart functionality
- Multiple payment options
- Order processing workflow
- Inventory management

**Architectural Design:**

```
┌─────────────────────────────────────────────────────────┐
│                    Presentation Layer                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐ │
│  │   Web    │  │ Mobile   │  │    Admin Dashboard    │ │
│  │   App    │  │   App    │  │                      │ │
│  └────┬─────┘  └────┬─────┘  └──────────┬───────────┘ │
└───────┼─────────────┼──────────────────┼─────────────┘
        │             │                  │
        ▼             ▼                  ▼
┌─────────────────────────────────────────────────────────┐
│                    Service Layer                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │Product   │  │  Order   │  │Payment   │  │Inventory│ │
│  │ Service  │  │ Service  │  │ Service  │  │ Service │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬────┘ │
└───────┼─────────────┼─────────────┼─────────────┼───────┘
        │             │             │             │
        ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────┐
│                   Repository Layer                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐ │
│  │Product   │  │  Order   │  │Payment   │  │Inventory│ │
│  │Repository│  │Repository│  │Repository│  │Repository│ │
│  └──────────┘  └──────────┘  └──────────┘  └────────┘ │
└─────────────────────────────────────────────────────────┘
        │             │             │             │
        ▼             ▼             ▼             ▼
┌─────────────────────────────────────────────────────────┐
│                      Data Layer                         │
│    ┌─────────────┐  ┌─────────────┐  ┌──────────────┐  │
│    │ PostgreSQL  │  │    Redis    │  │ Elasticsearch│  │
│    │  (Primary)  │  │   (Cache)   │  │   (Search)   │  │
│    └─────────────┘  └─────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**Key Design Decisions:**

| Requirement | Design Solution |
|-------------|-----------------|
| High traffic | Horizontal scaling, database sharding |
| Search functionality | Elasticsearch integration |
| Payment flexibility | Strategy pattern for payment methods |
| Order processing | State machine for order status |
| Inventory consistency | Distributed transactions |

---

## 8. Assessment Questions

### Multiple Choice Questions

#### Level 1: Basic (Easy)
**Q1. Which UML diagram best represents the static structure of a system?**
- (a) Sequence Diagram
- (b) Activity Diagram
- (c) Class Diagram ✓
- (d) State Diagram

**Q2. The Singleton design pattern ensures:**
- (a) Multiple instances of a class
- (b) Only one instance of a class ✓
- (c) No instance of a class
- (d) Random number of instances

**Q3. Non-functional requirements describe:**
- (a) What the system must do
- (b) How the system performs certain functions ✓
- (c) Only user interface elements
- (d) Database schema

#### Level 2: Intermediate
**Q4. In MVC architecture, which component handles business logic?**
- (a) View
- (b) Controller
- (c) Model ✓
- (d) Database

**Q5. The Observer pattern is used when:**
- (a) Creating objects with complex construction
- (b) One object needs to notify other objects of state changes ✓
- (c) Converting interface of one class to another
- (d) Managing object creation

**Q6. According to SOLID principles, a class should have:**
- (a) Multiple responsibilities
- (b) Only one responsibility ✓
- (c) No responsibility
- (d) Responsibility decided at runtime

**Q7. Which design pattern is most appropriate for adding new payment methods without modifying existing code?**
- (a) Singleton
- (b) Factory Method ✓
- (c) Observer
- (d) Adapter

#### Level 3: Advanced (Challenging)
**Q8. In the Strategy pattern, the context object:**
- (a) Defines the algorithm interface ✓
- (b) Implements the algorithm
- (c) Creates algorithm objects
- (d) Destroys algorithm objects

**Q9. The Liskov Substitution Principle states that:**
- (a) Subclasses can have additional methods not in parent
- (b) Objects of superclass shall be replaceable with subclass objects without altering program correctness ✓
- (c) Private methods can override public methods
- (d) Interfaces should have many methods

**Q10. Which pattern would you use to integrate a legacy payment system with a modern application requiring a different interface?**
- (a) Factory
- (b) Observer
- (c) Adapter ✓
- (d) Singleton

**Q11. In requirements engineering, a "use case" primarily helps in:**
- (a) Writing code directly
- (b) Visualizing functional requirements from user perspective ✓
- (c) Designing database schema
- (d) Testing the system

**Q12. High coupling and low cohesion in software design typically results in:**
- (a) Easy maintenance and better reusability
- (b) Difficult maintenance and poor reusability ✓
- (c) Faster execution
- (d) Better security

### Fill in the Blanks

1. The process of gathering user needs and converting them into formal requirements is called **Requirements Engineering**.

2. A **Class Diagram** shows the attributes, operations, and relationships between classes.

3. The design pattern that ensures only one instance of a class is created is called **Singleton**.

4. In the **Model-View-Controller (MVC)** architecture, the Controller acts as an intermediary between Model and View.

5. **Non-functional requirements** specify criteria that judge the operation of a system rather than specific behaviors.

### True or False

1. **True/False:** Functional requirements describe "what" the system should do. → **True**

2. **True/False:** The Adapter pattern converts one interface to another the client expects. → **True**

3. **True/False:** In Singleton pattern, the constructor should be public. → **False** (It should be private)

4. **True/False:** Cohesion refers to how closely related and focused the responsibilities of a module are. → **True**

5. **True/False:** Use case diagrams are primarily used for database design. → **False** (They are for requirements visualization)

---

## 9. Key Takeaways

1. **Requirements Engineering** is the foundation—poor requirements lead to poor design. Master functional vs. non-functional requirements distinction.

2. **The Requirements-to-Design bridge** requires translating "what" into "how"—this transformation demands creative technical decisions.

3. **UML diagrams** (Class, Sequence, Component, Package) are essential communication tools for design documentation.

4. **Design patterns** (Creational, Structural, Behavioral) provide proven solutions—understand when and how to apply them.

5. **SOLID principles** guide object-oriented design—these are frequently tested in university examinations.

6. **Architectural patterns** (MVC, MVP, MVVM) structure application organization—choose based on requirements.

7. **Coupling and Cohesion**—strive for low coupling (independence between modules) and high cohesion (focused responsibilities within modules).

8. **Practical application** is crucial—understand not just patterns in theory but when to apply them in real scenarios.

---

## References

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.

2. Sommerville, I. (2015). *Software Engineering* (10th ed.). Pearson.

3. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.

4. IEEE Std 830-1998. *IEEE Recommended Practice for Software Requirements Specifications*.

5. Delhi University, NEP 2024 UGCF Syllabus - Software Engineering (Core Course).

---

*This study material covers the complete "Requirements to Design Model" topic as per Delhi University BSc (Hons) Computer Science curriculum under NEP 2024.*