# Design Patterns & Architecture

## Introduction
Design patterns and software architecture form the backbone of maintainable, scalable software systems. Design patterns are proven solutions to recurring design problems, first systematically cataloged in the seminal "Gang of Four" book (1994). Architectural patterns operate at a higher level of abstraction, defining the structural organization of entire systems.

In modern software engineering, these concepts address critical challenges:
1. Managing complexity in large-scale systems
2. Enabling code reuse and modularity
3. Facilitating team collaboration through standardized approaches
4. Supporting evolutionary development through adaptable structures

The synergy between architectural patterns (system-level decisions) and design patterns (component-level implementations) creates robust systems that can withstand changing requirements. Industry surveys show 68% of enterprise systems use documented patterns to reduce technical debt (2023 Stack Overflow Survey).

## Key Concepts

**1. Design Pattern Categories:**
- *Creational*: Object creation mechanisms (Singleton, Factory)
- *Structural*: Object composition (Adapter, Decorator)
- *Behavioral*: Object interaction (Observer, Strategy)

**2. Architectural Styles:**
- **MVC (Model-View-Controller)**: Separation of concerns in UI systems
- **Microservices**: Distributed, independently deployable components
- **Layered Architecture**: Strict hierarchy with defined dependencies
- **Event-Driven**: Decoupled components through event propagation

**3. SOLID Principles:**
- Single Responsibility
- Open/Closed Principle
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

**4. Pattern Relationships:**
- Architectural patterns constrain design pattern choices
- Composite pattern often implements Tree structures in Component architectures
- Observer pattern enables Pub-Sub communication in Event-Driven systems

## Examples

**1. Singleton Pattern Implementation (Java):**
```java
public class DatabaseConnection {
    private static DatabaseConnection instance;
    
    private DatabaseConnection() {}  // Private constructor
    
    public static synchronized DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }
}
```
*Use Case*: Global database connection pool management

**2. Adapter Pattern for Legacy Integration:**
Problem: Integrate XML-based legacy system with JSON modern API
Solution:
```python
class XMLAdapter:
    def __init__(self, xml_service):
        self.xml_service = xml_service
        
    def get_json(self):
        xml_data = self.xml_service.get_xml()
        return convert_xml_to_json(xml_data)
```

**3. MVC Architecture in Web Application:**
- Model: User.java (Business logic)
- View: profile.jsp (Presentation layer)
- Controller: UserController.java (Handles HTTP requests)
Flow: Browser → Controller → Model updates → View rendering

## Exam Tips
1. Always mention pattern consequences - e.g., "Singleton improves resource utilization but introduces global state"
2. Draw UML diagrams with clear role annotations (15% weightage in DU papers)
3. Compare patterns: "Use Factory Method when subclassing, Abstract Factory for families of objects"
4. Relate patterns to SOLID principles - e.g., "Strategy pattern enables Open/Closed principle"
5. Discuss architecture tradeoffs: "Microservices improve scalability but increase network latency"
6. Prepare real-world examples: "Android uses Observer pattern for click listeners"
7. Memorize Gang of Four pattern classification chart