# Classes - Summary

## Key Definitions and Concepts

- **Class**: Blueprint for creating objects (defines attributes and methods)
- **Object**: Instance of a class with actual data and behavior
- **Inheritance**: Creating new classes from existing ones (`class Child(Parent):`)
- **Encapsulation**: Bundling data with methods that operate on that data
- **Polymorphism**: Ability to use common interface for different data types
- **Constructor**: `__init__()` method for object initialization
- **self**: Reference to current class instance (first parameter in methods)

## Important Formulas and Theorems

```python
# Class definition template
class ClassName:
    def __init__(self, params):
        self.attributes = params

    def method(self):
        # method logic

# Inheritance syntax
class SubClass(SuperClass):
    pass

# Property decorator
@property
def attribute(self):
    return self._attribute

# Class composition example
class Sensor:
    def __init__(self, type):
        self.type = type

class Device:
    def __init__(self):
        self.sensor = Sensor('DHT11')
```

## Key Points

1. Classes model real-world IoT entities (sensors, actuators) as objects
2. `__init__()` initializes object state with instance attributes
3. Inheritance creates specialized IoT device types (e.g., `TemperatureSensor(Sensor)`)
4. Encapsulation protects sensor data using private attributes (\_variable)
5. Class methods represent device actions (e.g., `read_data()`, `calibrate()`)
6. Composition models complex IoT systems (Device containing multiple Sensor objects)
7. Magic methods (`__str__`, `__repr__`) enable meaningful object representations
8. Static methods (@staticmethod) handle device-related utilities without instance
9. Class variables maintain shared state across all instances (e.g., device_count)

## Common Mistakes to Avoid

1. Forgetting `self` parameter in instance methods
2. Confusing class variables (shared) with instance variables (object-specific)
3. Overusing inheritance when composition would be better ("favor composition over inheritance")
4. Not using `super().__init__()` in subclass constructors
5. Mishandling encapsulation (using public attributes instead of properties)

## Revision Tips

1. Practice creating class hierarchies for IoT components (Sensor → TemperatureSensor)
2. Use UML diagrams to visualize class relationships before coding
3. Study Python's magic methods for object customization (**str**, **eq**)
4. Review popular IoT libraries (gpiozero, paho-mqtt) to see real class implementations
5. Memorize syntax for:
   - Properties (@property, @attribute.setter)
   - Inheritance and method overriding
   - Class vs static methods
6. Relate class concepts to Module 4's weather monitoring case study
