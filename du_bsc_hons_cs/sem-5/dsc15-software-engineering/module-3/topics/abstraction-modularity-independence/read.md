# Abstraction, Modularity, and Independence in Software Engineering

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

Software engineering is the disciplined approach to designing, developing, testing, and maintaining software systems. At its foundation lie three interconnected principles that every competent software engineer must master: **Abstraction**, **Modularity**, and **Independence**. These concepts form the bedrock of well-structured, maintainable, and scalable software.

Consider the smartphone you use daily. When you tap to make a call, you interact with a simple interface—you don't need to understand how radio waves are transmitted or how the operating system manages hardware resources. This is abstraction in action. Similarly, your phone consists of distinct hardware components (camera, processor, battery) that work independently yet cohesively—this is modularity. Each component can be upgraded or replaced without affecting others—this is independence.

These principles become critical in enterprise-level software development. When building systems for banking, healthcare, or e-commerce, the difference between a maintainable codebase and an unmanageable one often rests on how well these principles are applied. For Delhi University students preparing for industry roles or higher studies, mastering these concepts is not optional—it is essential.

This study material provides comprehensive coverage aligned with the UGCF NEP 2024 syllabus, addressing abstraction types, coupling/cohesion metrics, SOLID principles, and practical applications with complete code examples.

---

## 2. Understanding Abstraction

### 2.1 Definition

**Abstraction** is the process of hiding complex implementation details while exposing only the essential features of an object or system. It allows developers to work with concepts at an appropriate level of detail without concerning themselves with underlying complexities.

In software engineering, abstraction serves as a mental tool for managing complexity. It enables programmers to:

- Focus on *what* a system does rather than *how* it does it
- Create reusable, general-purpose components
- Reduce cognitive load by limiting necessary information at any given time

### 2.2 Types of Abstraction

Software engineering recognizes several distinct types of abstraction:

#### 2.2.1 Data Abstraction

Data abstraction focuses on representing data in terms of its essential characteristics while hiding implementation details. The classic example is the **Abstract Data Type (ADT)**.

Consider a Stack data structure:

```python
from abc import ABC, abstractmethod

# Abstract Data Type for Stack
class Stack(ABC):
    @abstractmethod
    def push(self, item):
        """Add item to top of stack"""
        pass
    
    @abstractmethod
    def pop(self):
        """Remove and return top item"""
        pass
    
    @abstractmethod
    def peek(self):
        """View top item without removing"""
        pass
    
    @abstractmethod
    def is_empty(self):
        """Check if stack is empty"""
        pass

# Concrete implementation using List
class ListStack(Stack):
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self):
        return len(self._items) == 0

# Client code uses abstraction without knowing implementation
def process_items(stack: Stack):
    stack.push(10)
    stack.push(20)
    while not stack.is_empty():
        print(stack.pop())

process_items(ListStack())
```

In this example, the client code (`process_items`) works with the `Stack` abstraction without knowing whether it's implemented using a list, linked list, or array. This is data abstraction—the user sees only the interface, not the implementation.

#### 2.2.2 Control Abstraction

Control abstraction involves hiding the sequence of operations required to perform a task, exposing only the high-level operation itself.

```python
# Without control abstraction - client manages details
def process_order_without_abstraction(customer_id, items, payment_method):
    # Validate customer
    customer = database.get_customer(customer_id)
    if not customer.is_active:
        raise Exception("Inactive customer")
    
    # Check inventory
    for item in items:
        inventory_item = database.get_inventory(item.sku)
        if inventory_item.quantity < item.quantity:
            raise Exception(f"Insufficient stock for {item.sku}")
    
    # Reserve inventory
    for item in items:
        database.reserve_inventory(item.sku, item.quantity)
    
    # Process payment
    payment = PaymentProcessor()
    total = sum(item.price * item.quantity for item in items)
    payment.charge(payment_method, total)
    
    # Create order
    order = Order(customer_id, items, total)
    database.save_order(order)
    
    # Send notification
    NotificationService().send_email(customer.email, "Order confirmed")

# With control abstraction - simple interface
def process_order(customer_id, items, payment_method):
    """Process an order - abstraction hides all implementation details"""
    order_service = OrderService()
    return order_service.create_order(customer_id, items, payment_method)

# Client code is dramatically simplified
order = process_order(customer_id="CUST001", items=cart_items, payment_method="credit_card")
```

The `process_order` function provides control abstraction—the caller doesn't know about inventory checking, payment processing, or notification sending. These details are encapsulated within the abstraction.

#### 2.2.3 Procedural Abstraction

Procedural abstraction allows using a procedure or function based on what it does without understanding how it achieves its result. The function signature (name and parameters) represents the abstraction, while the body contains the implementation.

```python
# Procedural abstraction - users care about what, not how
def calculate_loan_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest.
    
    Args:
        principal: Initial loan amount
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time period in years
    
    Returns:
        Total interest accrued
    """
    return principal * rate * time

def calculate_monthly_payment(principal: float, rate: float, months: int) -> float:
    """Calculate monthly payment for a loan"""
    if rate == 0:
        return principal / months
    monthly_rate = rate / 12
    payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return payment

# Users call these functions without understanding the mathematical formulas
loan_amount = 500000
annual_rate = 0.08
years = 20

interest = calculate_loan_interest(loan_amount, annual_rate, years)
monthly = calculate_monthly_payment(loan_amount, annual_rate / 12, years * 12)
```

### 2.3 Abstraction in Object-Oriented Programming

In OOP, abstraction is achieved through **abstract classes** and **interfaces**. These define contracts that concrete implementations must fulfill.

```python
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    """Abstraction for database operations"""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute(self, query: str):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass

class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database...")
    
    def execute(self, query: str):
        print(f"Executing MySQL query: {query}")
    
    def disconnect(self):
        print("Disconnecting from MySQL...")

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgreSQL database...")
    
    def execute(self, query: str):
        print(f"Executing PostgreSQL query: {query}")
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL...")

# Application code depends on abstraction, not concrete implementation
def fetch_users(db: DatabaseConnection):
    db.connect()
    db.execute("SELECT * FROM users")
    db.disconnect()

# Easily switch databases
fetch_users(MySQLConnection())
fetch_users(PostgreSQLConnection())
```

---

## 3. Understanding Modularity

### 3.1 Definition

**Modularity** is the principle of decomposing a software system into discrete, self-contained modules that can be independently created, modified, tested, and maintained. A module is a logical unit that groups related functionality and data.

Modularity provides:

- **Reusability**: Modules can be reused across different systems
- **Maintainability**: Changes to one module don't affect others
- **Understandability**: Each module can be understood independently
- **Testability**: Modules can be tested in isolation
- **Parallel Development**: Different developers can work on different modules simultaneously

### 3.2 Principles of Modularity

#### 3.2.1 High Cohesion

**Cohesion** measures how strongly related and focused the responsibilities of a single module are. **High cohesion** means a module has a single, well-defined purpose.

**Types of Cohesion (from best to worst):**

| Type | Description | Example |
|------|-------------|---------|
| **Functional** | Elements all contribute to a single task | Math library with arithmetic functions |
| **Sequential** | Output of one element is input to another | Data processing pipeline |
| **Communicational** | Elements operate on same data | Record processing module |
| **Procedural** | Elements belong to different tasks but ordered | Main program flow |
| **Temporal** | Elements related by time of execution | Initialization module |
| **Logical** | Elements logically related but diverse | Error handling module |
| **Coincidental** | No meaningful relationship | Random utility functions |

```python
# HIGH COHESION - Functional cohesion
class TemperatureConverter:
    """Module with single, well-defined purpose: temperature conversion"""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

# LOW COHESION - Logical/Coincidental cohesion
class Utilities:  # BAD DESIGN
    """Module with unrelated responsibilities - poor cohesion"""
    
    def temperature_conversion(self, value, unit):
        pass
    
    def send_email(self, recipient, message):
        pass
    
    def calculate_loan_interest(self, principal, rate, time):
        pass
    
    def generate_random_id(self):
        pass
    
    def read_file(self, filename):
        pass
```

#### 3.2.2 Low Coupling

**Coupling** measures the degree of interdependence between modules. **Low coupling** (also called loose coupling) means modules are independent and communicate through well-defined interfaces.

**Types of Coupling (from best to worst):**

| Type | Description |
|------|-------------|
| **Data Coupling** | Modules share only basic data parameters |
| **Stamp Coupling** | Modules share composite data (structures) |
| **Control Coupling** | One module controls another through parameters |
| **External Coupling** | Both depend on external formats/protocols |
| **Common Coupling** | Modules share global data |
| **Content Coupling** | One module directly modifies another's internal data |

```python
# DATA COUPLING - Best form of coupling
class OrderProcessor:
    def __init__(self, payment_gateway, inventory_service, notification_service):
        # Dependencies are injected through abstractions
        self.payment_gateway = payment_gateway
        self.inventory_service = inventory_service
        self.notification_service = notification_service
    
    def process_order(self, order_data: dict):
        # Only data (not internal structures) is shared
        customer_id = order_data['customer_id']
        items = order_data['items']
        payment_method = order_data['payment_method']
        
        # Process through interfaces
        self.inventory_service.reserve_items(items)
        total = self.payment_gateway.charge(order_data['payment_details'], order_data['total'])
        self.notification_service.send_confirmation(customer_id, order_data)
        
        return {"status": "success", "order_id": "ORD123"}

# COMMON COUPLING - Bad coupling (global state)
# Global variables create hidden dependencies
class GlobalConfig:
    DATABASE_HOST = "localhost"
    MAX_CONNECTIONS = 100
    TIMEOUT = 30

class UserRepository:  # Depends on global state
    def find_user(self, user_id):
        # Hidden dependency on GlobalConfig
        connection = connect(GlobalConfig.DATABASE_HOST, GlobalConfig.TIMEOUT)
        return query(f"SELECT * FROM users WHERE id = {user_id}")

class OrderRepository:  # Also depends on global state
    def find_order(self, order_id):
        # Same hidden dependency
        connection = connect(GlobalConfig.DATABASE_HOST, GlobalConfig.TIMEOUT)
        return query(f"SELECT * FROM orders WHERE id = {order_id}")
```

### 3.3 Complete Example: E-Commerce System

This example demonstrates modularity with high cohesion and low coupling:

```python
from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
from datetime import datetime

# ==================== DATA MODELS ====================
@dataclass
class Product:
    sku: str
    name: str
    price: float
    quantity: int

@dataclass
class OrderItem:
    product: Product
    quantity: int

@dataclass
class Order:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    total: float
    status: str
    created_at: datetime

# ==================== MODULE: INVENTORY ====================
class InventoryService:
    """Module responsible for inventory management - HIGH COHESION"""
    
    def __init__(self):
        self._inventory = {}
    
    def check_availability(self, product_sku: str, quantity: int) -> bool:
        product = self._inventory.get(product_sku)
        return product and product.quantity >= quantity
    
    def reserve_items(self, items: List[OrderItem]) -> bool:
        for item in items:
            if not self.check_availability(item.product.sku, item.quantity):
                return False
        
        # Reserve the items
        for item in items:
            self._inventory[item.product.sku].quantity -= item.quantity
        return True
    
    def add_stock(self, product: Product):
        if product.sku in self._inventory:
            self._inventory[product.sku].quantity += product.quantity
        else:
            self._inventory[product.sku] = product

# ==================== MODULE: PAYMENT ====================
class PaymentGateway(ABC):
    """Abstract interface - enables LOOSE COUPLING"""
    
    @abstractmethod
    def process_payment(self, amount: float, payment_details: dict) -> str:
        pass

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount: float, payment_details: dict) -> str:
        # Integration with payment processor
        print(f"Processing credit card payment of ${amount}")
        return "PAYMENT_SUCCESS_12345"

class PayPalPayment(PaymentGateway):
    def process_payment(self, amount: float, payment_details: dict) -> str:
        print(f"Processing PayPal payment of ${amount}")
        return "PAYMENT_SUCCESS_67890"

# ==================== MODULE: NOTIFICATION ====================
class NotificationService:
    """Module responsible for sending notifications - HIGH COHESION"""
    
    def send_order_confirmation(self, customer_email: str, order: Order):
        print(f"Sending order confirmation to {customer_email}")
        # Email sending logic
    
    def send_shipping_notification(self, customer_email: str, tracking_number: str):
        print(f"Sending shipping notification to {customer_email}")

# ==================== MODULE: ORDER PROCESSING ====================
class OrderService:
    """
    Order processing module - uses dependency injection for LOOSE COUPLING
    Each module has a single responsibility (high cohesion)
    """
    
    def __init__(self, inventory: InventoryService, 
                 payment_gateway: PaymentGateway,
                 notification: NotificationService):
        self.inventory = inventory
        self.payment_gateway = payment_gateway
        self.notification = notification
    
    def create_order(self, customer_id: str, customer_email: str,
                     items: List[OrderItem], payment_details: dict) -> Order:
        # Step 1: Check inventory
        if not self.inventory.reserve_items(items):
            raise ValueError("Insufficient inventory")
        
        # Step 2: Calculate total
        total = sum(item.product.price * item.quantity for item in items)
        
        # Step 3: Process payment
        payment_id = self.payment_gateway.process_payment(total, payment_details)
        
        # Step 4: Create order
        order = Order(
            order_id=f"ORD-{datetime.now().timestamp()}",
            customer_id=customer_id,
            items=items,
            total=total,
            status="CONFIRMED",
            created_at=datetime.now()
        )
        
        # Step 5: Send notification
        self.notification.send_order_confirmation(customer_email, order)
        
        return order

# ==================== CLIENT CODE ====================
# Demonstrate loose coupling - easily switch implementations
if __name__ == "__main__":
    # Setup products
    laptop = Product("LAPTOP-001", "Gaming Laptop", 1500.00, 10)
    mouse = Product("MOUSE-001", "Wireless Mouse", 25.00, 50)
    
    # Initialize modules
    inventory = InventoryService()
    inventory.add_stock(laptop)
    inventory.add_stock(mouse)
    
    # Create order with credit card
    credit_payment = CreditCardPayment()
    notification = NotificationService()
    order_service = OrderService(inventory, credit_payment, notification)
    
    # Place order
    items = [OrderItem(laptop, 1), OrderItem(mouse, 2)]
    order = order_service.create_order(
        customer_id="CUST001",
        customer_email="student@example.com",
        items=items,
        payment_details={"card_number": "4111111111111111"}
    )
    
    print(f"Order created: {order.order_id}, Total: ${order.total}")
```

---

## 4. Understanding Independence

### 4.1 Definition

**Independence** in software engineering refers to the degree to which software components can be developed, modified, maintained, and replaced independently without affecting other components. It is achieved through the combined application of abstraction and modularity.

Independent software systems exhibit:

- **Functional Independence**: Each module performs a specific task with minimal interaction with other modules
- **Temporal Independence**: Modules can be executed or developed at different times
- **Technological Independence**: Components can be implemented with different technologies

### 4.2 How Abstraction and Modularity Achieve Independence

Abstraction and modularity work together to achieve independence:

1. **Encapsulation**: Abstraction hides internal details; modularity packages related functionality. Together, they create self-contained units that don't expose internals.

2. **Well-Defined Interfaces**: Modules communicate through abstract interfaces, not implementation details. This allows replacing implementations without affecting clients.

3. **Information Hiding**: Each module hides its implementation decisions, preventing ripple effects when changes occur.

```python
# INDEPENDENCE achieved through abstraction and encapsulation

class DatabaseInterface(ABC):
    """Abstraction defines the contract"""
    @abstractmethod
    def save(self, key: str, value: str):
        pass
    
    @abstractmethod
    def get(self, key: str) -> str:
        pass

class RedisDatabase(DatabaseInterface):
    """Independent implementation"""
    def __init__(self):
        self._store = {}
    
    def save(self, key: str, value: str):
        self._store[key] = value
    
    def get(self, key: str) -> str:
        return self._store.get(key, "")

class FileDatabase(DatabaseInterface):
    """Alternative independent implementation"""
    def __init__(self, filename: str):
        self._filename = filename
        self._cache = {}
        self._load()
    
    def _load(self):
        try:
            with open(self._filename, 'r') as f:
                for line in f:
                    key, value = line.strip().split('=')
                    self._cache[key] = value
        except FileNotFoundError:
            pass
    
    def save(self, key: str, value: str):
        self._cache[key] = value
        with open(self._filename, 'a') as f:
            f.write(f"{key}={value}\n")
    
    def get(self, key: str) -> str:
        return self._cache.get(key, "")

# Application code is INDEPENDENT of the database implementation
class UserService:
    def __init__(self, database: DatabaseInterface):  # Depends on abstraction
        self.database = database
    
    def create_user(self, username: str, email: str):
        # Completely independent of how data is stored
        self.database.save(username, email)
        return {"username": username, "email": email}

# Can use either implementation without changing UserService
redis_db = RedisDatabase()
user_service_1 = UserService(redis_db)

file_db = FileDatabase("users.txt")
user_service_2 = UserService(file_db)
```

---

## 5. SOLID Principles — Advanced Coverage

The SOLID principles are five design principles that promote maintainable, flexible, and scalable object-oriented software. They directly relate to abstraction, modularity, and independence.

### 5.1 Single Responsibility Principle (SRP)

**A class should have only one reason to change.**

```python
# BAD - Multiple responsibilities
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Responsibility: Data persistence
        pass
    
    def send_email(self, message: str):
        # Responsibility: Communication
        pass
    
    def validate(self):
        # Responsibility: Validation
        pass

# GOOD - Single responsibility each
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user: User):
        pass

class UserValidator:
    def validate(self, user: User):
        pass

class EmailService:
    def send(self, to: str, message: str):
        pass
```

### 5.2 Open/Closed Principle (OCP)

**Software entities should be open for extension but closed for modification.**

```python
# BAD - Must modify to add new shapes
class AreaCalculator:
    def calculate_area(shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height
        # Adding Triangle requires modifying this class

# GOOD - Open for extension, closed for modification
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height

# New shapes can be added without modifying existing code
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
    
    def area(self) -> float:
        return 0.5 * self.base * self.height

class AreaCalculator:
    def total_area(self, shapes: List[Shape]) -> float:
        return sum(shape.area() for shape in shapes)
```

### 5.3 Liskov Substitution Principle (LSP)

**Objects of a superclass should be replaceable with objects of a subclass without affecting correctness.**

```python
# BAD - Violates LSP
class Bird:
    def fly(self):
        pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins cannot fly")

# GOOD - Proper inheritance
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Penguin(Bird):
    # Cannot fly, but that's okay - doesn't break contract
    def swim(self):
        pass
```

### 5.4 Interface Segregation Principle (ISP)

**Clients should not be forced to depend on interfaces they do not use.**

```python
# BAD - Fat interface
class Machine(ABC):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass
    
    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")
    
    def scan(self, document):
        raise NotImplementedError("Cannot scan")
    
    def fax(self, document):
        raise NotImplementedError("Cannot fax")

# GOOD - Segregated interfaces
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")
```

### 5.5 Dependency Inversion Principle (DIP)

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

```python
# BAD - High-level depends on low-level
class MySQLUserRepository:
    def get_user(self, user_id):
        # MySQL specific code
        pass

class UserService:
    def __init__(self):
        self.repository = MySQLUserRepository()  # Direct dependency
    
    def find_user(self, user_id):
        return self.repository.get_user(user_id)

# GOOD - Depend on abstractions
class UserRepository(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

class MySQLUserRepository(UserRepository):
    def get_user(self, user_id):
        # MySQL specific code
        pass

class PostgreSQLUserRepository(UserRepository):
    def get_user(self, user_id):
        # PostgreSQL specific code
        pass

class UserService:
    def __init__(self, repository: UserRepository):  # Depends on abstraction
        self.repository = repository
```

---

## 6. Key Takeaways

### 6.1 Abstraction

- **Definition**: Hiding complex implementation details while exposing essential features
- **Types**: Data abstraction (ADTs), Control abstraction (hiding process details), Procedural abstraction (function interfaces)
- **Implementation**: Achieved through abstract classes, interfaces, and encapsulation
- **Benefit**: Reduces complexity, enables reuse, allows working at appropriate detail levels

### 6.2 Modularity

- **Definition**: Decomposing software into independent, self-contained modules
- **Key Metrics**:
  - **Cohesion**: How related a module's responsibilities are (aim for HIGH)
  - **Coupling**: How interdependent modules are (aim for LOW)
- **Types of Coupling**: Data (best), Stamp, Control, External, Common, Content (worst)
- **Types of Cohesion**: Functional (best), Sequential, Communicational, Procedural, Temporal, Logical, Coincidental (worst)
- **Benefit**: Enables parallel development, testing, maintenance, and reuse

### 6.3 Independence

- **Definition**: The ability to develop, modify, and replace components without affecting others
- **Achieved Through**: Combination of abstraction (well-defined interfaces) and modularity (encapsulated, cohesive modules)
- **Types**: Functional, Temporal, and Technological independence

### 6.4 SOLID Principles

| Principle | Key Idea | Relationship to Abstraction/Modularity |
|-----------|----------|----------------------------------------|
| SRP | One reason to change | Achieves high cohesion |
| OCP | Open for extension, closed for modification | Enables independent changes |
| LSP | Subtypes must be substitutable | Maintains abstraction contracts |
| ISP | Specific interfaces over general ones | Creates focused modules |
| DIP | Depend on abstractions | Achieves loose coupling |

---

## 7. Assessment Questions

### 7.1 Multiple Choice Questions

**1. Which type of abstraction focuses on hiding data representation details?**
- (a) Control Abstraction
- (b) Procedural Abstraction
- (c) Data Abstraction
- (d) Physical Abstraction
- **Answer: (c)**

**2. In the context of modularity, what does HIGH COHESION indicate?**
- (a) A module has many unrelated responsibilities
- (b) A module has a single, well-defined purpose
- (c) Modules are highly dependent on each other
- (d) A module shares global data with other modules
- **Answer: (b)**

**3. Which type of coupling is considered the BEST form?**
- (a) Content Coupling
- (b) Common Coupling
- (c) Data Coupling
- (d) Control Coupling
- **Answer: (c)**

**4. The Liskov Substitution Principle states that:**
- (a) Classes should have multiple interfaces
- (b) Subclasses can modify parent class behavior arbitrarily
- (c) Subclass objects should be substitutable for superclass objects without altering correctness
- (d) High-level modules should depend on low-level modules
- **Answer: (c)**

**5. Dependency Inversion Principle promotes:**
- (a) Tight coupling between modules
- (b) Dependence on concrete implementations
- (c) Dependence on abstractions
- (d) Direct access to private members
- **Answer: (c)**

**6. Which SOLID principle is violated when a class has multiple unrelated responsibilities?**
- (a) Open/Closed Principle
- (b) Single Responsibility Principle
- (c) Interface Segregation Principle
- (d) Liskov Substitution Principle
- **Answer: (b)**

**7. Functional cohesion in a module means:**
- (a) Elements are related by the order of execution
- (b) Elements contribute to different unrelated tasks
- (c) All elements work together to perform a single task
- (d) Elements operate on the same data but do different things
- **Answer: (c)**

**8. In software engineering, independence is achieved primarily through:**
- (a) Writing longer functions
- (b) Using global variables for sharing data
- (c) Combining abstraction and modularity
- (d) Minimizing the use of interfaces
- **Answer: (c)**

### 7.2 Short Answer Questions

**1. Explain the difference between data abstraction and control abstraction with examples.**

**2. Define modularity in software engineering and list at least three benefits it provides.**

**3. What is the difference between cohesion and coupling? Why should we aim for high cohesion and low coupling?**

**4. Explain the Open/Closed Principle with a code example showing how new functionality can be added without modifying existing code.**

**5. How does the Dependency Inversion Principle help achieve loose coupling between modules?**

**6. Describe the types of cohesion from best to worst with one example for each.**

### 7.3 Long Answer / Application-Based Questions

**1. (Application)** You are designing a Banking System with the following requirements:
- Customer management (create, update, delete customers)
- Account management (savings, checking accounts)
- Transaction processing (deposits, withdrawals, transfers)
- Interest calculation for different account types
- Notification system (SMS, email alerts)

Apply the principles of abstraction, modularity, and SOLID to design this system. Identify:
- The modules you would create and their responsibilities
- How you would achieve loose coupling between modules
- How abstraction would be used to allow different account types
- Which SOLID principles apply to each module design

**2. (Analysis)** A legacy e-commerce system has the following problems:
- Adding a new payment method requires modifying the checkout code
- Changes to the database schema break multiple parts of the application
- The inventory module directly accesses database tables
- Testing any component requires the entire system to be running

Analyze which software engineering principles have been violated and explain how refactoring using abstraction, modularity, and SOLID principles would address each issue.

**3. (Design)** Design a library management system demonstrating:
- At least 3 abstract classes/interfaces showing data abstraction
- Modules with high cohesion and low coupling
- Implementation of at least 3 SOLID principles
- Dependency injection to achieve independence

Provide the class diagram description and key code snippets.

**4. (Evaluation)** Compare and contrast:
- Data coupling vs. Common coupling
- Functional cohesion vs. Temporal cohesion
- Traditional monolithic design vs. Modular design

Explain scenarios where each would be appropriate.

---

## 8. References and Further Reading

1. **Software Engineering** by Ian Sommerville (10th Edition) — Chapter 8: Software Design
2. **Clean Code** by Robert C. Martin — Chapters on SOLID principles
3. **Design Patterns** by Erich Gamma et al. — Abstract Factory, Strategy, Observer patterns
4. **UGCF NEP 2024 Syllabus** — Software Engineering (Core Course)
5. **Delhi University BSc (Hons) Computer Science** — Course materials and lecture notes

---

*This study material has been prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. It covers all learning objectives related to Abstraction, Modularity, and Independence in Software Engineering.*