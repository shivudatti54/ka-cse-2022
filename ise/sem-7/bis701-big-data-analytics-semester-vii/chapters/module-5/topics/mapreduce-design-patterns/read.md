# Structural Design Patterns

## Introduction to Structural Patterns

Structural design patterns are concerned with how classes and objects are composed to form larger structures. They help ensure that when a system changes, its structure doesn't need to. These patterns focus on relationships between entities, making it easier to design systems by identifying simple ways to realize relationships between different components.

Structural patterns use inheritance to compose interfaces or implementations and object composition to combine behaviors at runtime. They provide multiple ways to create class structures while keeping them flexible and efficient.

## Key Structural Patterns

### Adapter Pattern

**Purpose**: The Adapter pattern allows incompatible interfaces to work together. It acts as a bridge between two incompatible interfaces by converting the interface of a class into another interface that clients expect.

**Structure**:
```
Client -> Target Interface
                ^
                |
           Adapter Class -> Adaptee Class
```

**Example**: Consider a European plug that needs to work with a US socket.
```java
// Target Interface
interface USSocket {
    void providePower();
}

// Adaptee
class EuropeanPlug {
    public void receivePower() {
        System.out.println("Receiving 220V power");
    }
}

// Adapter
class EuropeanToUSAdapter implements USSocket {
    private EuropeanPlug plug;
    
    public EuropeanToUSAdapter(EuropeanPlug plug) {
        this.plug = plug;
    }
    
    @Override
    public void providePower() {
        System.out.println("Converting 110V to 220V");
        plug.receivePower();
    }
}

// Client
public class AdapterDemo {
    public static void main(String[] args) {
        EuropeanPlug plug = new EuropeanPlug();
        USSocket adapter = new EuropeanToUSAdapter(plug);
        adapter.providePower();
    }
}
```

### Decorator Pattern

**Purpose**: The Decorator pattern attaches additional responsibilities to an object dynamically. It provides a flexible alternative to subclassing for extending functionality.

**Structure**:
```
Component Interface
       ^
       |
Concrete Component    Decorator Class -> Component Reference
       ^                    ^
       |                    |
       +--------------------+
                |
        Concrete Decorator Classes
```

**Example**: Adding toppings to a pizza
```java
// Component
interface Pizza {
    String getDescription();
    double getCost();
}

// Concrete Component
class BasicPizza implements Pizza {
    public String getDescription() {
        return "Basic pizza";
    }
    
    public double getCost() {
        return 5.00;
    }
}

// Decorator
abstract class PizzaDecorator implements Pizza {
    protected Pizza pizza;
    
    public PizzaDecorator(Pizza pizza) {
        this.pizza = pizza;
    }
}

// Concrete Decorators
class CheeseDecorator extends PizzaDecorator {
    public CheeseDecorator(Pizza pizza) {
        super(pizza);
    }
    
    public String getDescription() {
        return pizza.getDescription() + ", cheese";
    }
    
    public double getCost() {
        return pizza.getCost() + 1.50;
    }
}

class PepperoniDecorator extends PizzaDecorator {
    public PepperoniDecorator(Pizza pizza) {
        super(pizza);
    }
    
    public String getDescription() {
        return pizza.getDescription() + ", pepperoni";
    }
    
    public double getCost() {
        return pizza.getCost() + 2.00;
    }
}

// Client
public class DecoratorDemo {
    public static void main(String[] args) {
        Pizza pizza = new BasicPizza();
        pizza = new CheeseDecorator(pizza);
        pizza = new PepperoniDecorator(pizza);
        
        System.out.println(pizza.getDescription() + " costs: $" + pizza.getCost());
    }
}
```

### Other Important Structural Patterns

#### Proxy Pattern
Provides a surrogate or placeholder for another object to control access to it.

#### Composite Pattern
Composes objects into tree structures to represent part-whole hierarchies.

#### Bridge Pattern
Decouples an abstraction from its implementation so they can vary independently.

#### Facade Pattern
Provides a unified interface to a set of interfaces in a subsystem.

#### Flyweight Pattern
Uses sharing to support large numbers of fine-grained objects efficiently.

## Comparison of Structural Patterns

| Pattern | Purpose | When to Use |
|---------|---------|-------------|
| Adapter | Makes incompatible interfaces work together | When you need to use an existing class but its interface doesn't match what you need |
| Decorator | Adds responsibilities to objects dynamically | When you need to add functionality to objects without affecting other objects |
| Proxy | Controls access to another object | When you need a more versatile or sophisticated reference to an object |
| Composite | Treats individual objects and compositions uniformly | When you want to represent part-whole hierarchies of objects |
| Bridge | Separates abstraction from implementation | When you want to avoid permanent binding between abstraction and implementation |
| Facade | Provides a simplified interface to a complex subsystem | When you need a simple interface to a complex subsystem |
| Flyweight | Uses sharing to support large numbers of objects | When a program uses a large number of objects with shared state |

## Implementation Considerations

### When to Use Structural Patterns

- **Adapter**: When you need to integrate legacy code or third-party libraries
- **Decorator**: When you need to add functionality dynamically without affecting other objects
- **Proxy**: When you need to control access or add additional functionality to objects
- **Composite**: When you need to work with tree structures of objects

### Benefits of Structural Patterns

1. **Increased flexibility**: Patterns allow for easier modification of system structure
2. **Reusability**: Components can be reused in different contexts
3. **Maintainability**: Clear separation of concerns makes systems easier to maintain
4. **Scalability**: Patterns provide foundations for building scalable systems

### Common Implementation Pitfalls

1. **Over-engineering**: Don't use patterns where simple inheritance would suffice
2. **Performance overhead**: Some patterns add layers that can impact performance
3. **Complexity**: Patterns can make simple problems more complex if misapplied

## Real-World Applications

Structural patterns are used extensively in:
- GUI frameworks (Composite for UI elements)
- Database access layers (Proxy for lazy loading)
- Logging frameworks (Decorator for adding logging functionality)
- Legacy system integration (Adapter for connecting old and new systems)

## Exam Tips

1. **Understand the differences**: Be able to distinguish between similar patterns (e.g., Adapter vs. Decorator)
2. **Know when to apply**: For scenario-based questions, identify which pattern solves the given problem
3. **Draw diagrams**: Practice drawing UML diagrams for each pattern
4. **Remember key characteristics**: 
   - Adapter: Interface conversion
   - Decorator: Dynamic responsibility addition
   - Proxy: Access control
   - Composite: Tree structure handling
5. **Focus on practical examples**: Be prepared to provide real-world examples for each pattern
6. **Compare and contrast**: Understand the trade-offs between different structural patterns