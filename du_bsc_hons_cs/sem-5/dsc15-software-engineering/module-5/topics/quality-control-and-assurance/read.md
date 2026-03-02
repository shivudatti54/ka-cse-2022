# Quality Control and Assurance in Software Engineering

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## Learning Objectives

After studying this chapter, you will be able to:

- Distinguish between Quality Assurance (QA) and Quality Control (QC) in software engineering
- Explain the differences between Verification and Validation
- Apply various software testing techniques to identify defects
- Interpret software quality metrics and their significance
- Understand international standards for software quality (ISO/IEC)
- Design and implement a defect management process
- Evaluate software quality using established frameworks

---

## 1. Introduction and Real-World Relevance

### What is Software Quality?

In today's digital age, software permeates every aspect of our lives—from banking applications and healthcare systems to aviation control systems and space exploration. The failure of software in critical systems can result in catastrophic consequences, including financial losses, reputational damage, and even loss of human life.

Consider these real-world examples:

- **Therac-25 Radiation Therapy Machine (1985-1987)**: A radiation therapy machine malfunctioned due to software bugs, delivering lethal doses to patients, resulting in multiple deaths. The root cause was inadequate testing and quality control.

- **Boeing 737 MAX Crashes (2018-2019)**: Software defects in the Maneuvering Characteristics Augmentation System (MCAS) contributed to two fatal crashes, resulting in 346 deaths and billions in financial losses.

- **Knight Capital Trading Disaster (2012)**: A software deployment error caused a trading firm to lose $440 million in 45 minutes due to a configuration issue that wasn't caught in testing.

These examples underscore why quality control and assurance are **critical competencies** for software engineers. The Delhi University syllabus emphasizes these topics because the industry demands professionals who can deliver reliable, maintainable, and bug-free software.

---

## 2. Understanding Quality in Software Engineering

### 2.1 What is Software Quality?

**Software Quality** refers to the degree to which a software product meets specified requirements and user expectations. It encompasses:

- **Functional correctness**: Does the software do what it's supposed to do?
- **Reliability**: Does the software perform consistently without failures?
- **Efficiency**: Does the software use resources optimally?
- **Usability**: Is the software easy to learn and use?
- **Maintainability**: Can the software be easily modified and extended?
- **Portability**: Can the software run on different platforms?
- **Reusability**: Can components be reused in other applications?

### 2.2 The Quality Mindset

Quality is not an afterthought—it must be built into the software from the beginning. This is captured in the famous quote:

> "Quality is not an act, it is a habit." — Aristotle

In software engineering, this translates to **building quality into every phase** of the software development life cycle (SDLC), not just testing at the end.

---

## 3. Quality Assurance (QA) vs Quality Control (QC)

A common point of confusion is the distinction between Quality Assurance and Quality Control. Let's clarify:

### 3.1 Quality Assurance (QA)

**QA is a proactive, process-oriented activity** that focuses on preventing defects. It involves:

- Defining quality standards and processes
- Establishing best practices and guidelines
- Conducting process audits
- Training team members
- Creating and implementing test strategies

**QA is about the process**—ensuring that the development process itself produces quality software.

### 3.2 Quality Control (QC)

**QC is a reactive, product-oriented activity** that focuses on identifying defects. It involves:

- Executing test cases
- Performing code reviews
- Identifying bugs and issues
- Reporting defects
- Verifying bug fixes

**QC is about the product**—ensuring that the final software meets quality standards.

### 3.3 Comparison Table

| Aspect | Quality Assurance (QA) | Quality Control (QC) |
|--------|------------------------|---------------------|
| **Focus** | Process | Product |
| **Approach** | Preventive | Corrective |
| **When** | Throughout SDLC | Primarily after development |
| **Goal** | Prevent defects | Find and fix defects |
| **Activities** | Process definition, training, audits | Testing, inspection, review |
| **Scope** | Entire organization | Specific software product |

### Example

Consider building a house:
- **QA** would ensure that the construction team follows proper building codes, uses quality materials, and follows correct procedures.
- **QC** would inspect the completed house for cracks, leaks, and other defects.

---

## 4. Verification vs Validation — A Critical Distinction

This is one of the most important and frequently tested concepts in software engineering. Let me explain thoroughly.

### 4.1 Verification

**Verification: "Are we building the product right?"**

Verification asks: *Are we developing the software according to its specifications?*

It checks if the **product design** is correct, regardless of implementation details. Verification is typically done through:

- Reviews
- Walkthroughs
- Inspections
- Desk checking
- Static analysis

### 4.2 Validation

**Validation: "Are we building the right product?"**

Validation asks: *Does the software meet the actual user needs and requirements?*

It checks if the **final product** satisfies the user's real-world needs. Validation is typically done through:

- Testing (functional, integration, system, acceptance)
- User acceptance testing (UAT)
- Beta testing
- Field testing

### 4.3 The Classic Waterfall Model Example

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOFTWARE DEVELOPMENT                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Requirements ──► Design ──► Coding ──► Testing ──► Deploy    │
│       │              │            │          │           │      │
│       ▼              ▼            ▼          ▼           ▼      │
│   Validation    Verification  Verification  Both       Validation│
│   (Are these     (Is design    (Is code    (Testing   (Does it   │
│   the right     correct for   correct for  ensures    meet user │
│   requirements?) requirements?) design?)    quality?) needs?)   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.4 Verification vs Validation: Concrete Example

Suppose you're developing a calculator app:

**Verification Question**: Is the code correctly implementing the square root function according to the design specification?

**Validation Question**: Does the calculator actually help users solve mathematical problems effectively in real use?

---

## 5. Software Quality Metrics

Quality metrics provide quantitative measures of software quality. They help teams make objective decisions and track quality improvements.

### 5.1 Key Quality Metrics

| Metric | Description | Formula | Target |
|--------|-------------|---------|--------|
| **Defect Density** | Number of defects per thousand lines of code | Defects / KLOC | < 1.0 |
| **Mean Time Between Failures (MTBF)** | Average time between system failures | Total operational time / Number of failures | High |
| **Mean Time to Repair (MTTR)** | Average time to fix a defect | Total repair time / Number of repairs | Low |
| **Test Coverage** | Percentage of code covered by tests | Lines tested / Total lines × 100 | > 80% |
| **Code Review Finding Rate** | Defects found per hour of review | Review findings / Review hours | Measured |
| **Requirement Stability Index** | Changes to requirements over time | (Final requirements - Initial requirements) / Initial requirements | < 10% |
| **Cyclomatic Complexity** | Complexity of program's decision paths | E - N + 2P (edges, nodes, connected components) | < 10 |

### 5.2 Interpreting Metrics

**Defect Density Example**:
If a software product has 50,000 lines of code (KLOC = 50) and 35 reported defects:

```
Defect Density = 35 / 50 = 0.7 defects/KLOC
```

This is considered **excellent** quality (typically < 1.0 is good, 1.0-2.0 is acceptable).

### 5.3 The GQM Approach (Goal-Question-Metric)

Delhi University syllabus emphasizes the GQM approach:

1. **Goal**: Define the quality goal (e.g., "Improve reliability")
2. **Question**: Formulate questions to achieve the goal (e.g., "What is our current MTBF?")
3. **Metric**: Identify metrics that answer the questions

---

## 6. Software Testing Techniques

Testing is a core component of Quality Control. Let's explore various testing techniques.

### 6.1 Static Testing Techniques

Static testing examines code **without executing** it.

#### a) Code Reviews
Systematic examination of source code by peers.

```python
# Example: Code with potential issues
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # Bug: Division by zero if list is empty!

# A code reviewer would catch this:
# - Missing input validation
# - No exception handling
# - No documentation
```

#### b) Walkthroughs
Informal meeting where the author explains the code to the team.

#### c) Inspections
Formal, structured review process with defined roles (moderator, author, reviewer, scribe).

#### d) Static Analysis Tools
Automated tools that analyze code for potential issues:

```python
# Example: Using pylint to analyze Python code
# Command: pip install pylint
# Run: pylint your_file.py

# Pylint checks for:
# - Coding standard violations
# - Potential bugs
# - Code complexity
# - Unused imports
```

### 6.2 Dynamic Testing Techniques

Dynamic testing involves **executing** the code.

#### a) Unit Testing
Testing individual components in isolation.

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        """Test basic addition"""
        result = 2 + 3
        self.assertEqual(result, 5)
    
    def test_division_by_zero(self):
        """Test handling of division by zero"""
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0
    
    def test_empty_list_average(self):
        """Test average with empty list - boundary condition"""
        with self.assertRaises(ZeroDivisionError):
            calculate_average([])

if __name__ == '__main__':
    unittest.main()
```

#### b) Integration Testing
Testing interactions between components.

```python
def test_user_registration_flow():
    """Integration test: User registration to database"""
    # Step 1: Create user
    user = create_user("john", "john@example.com")
    
    # Step 2: Verify in database
    db_user = get_user_from_db("john")
    
    # Step 3: Verify email sent
    assert len(get_sent_emails()) > initial_count
    
    # All components working together
    assert db_user.email == "john@example.com"
```

#### c) System Testing
Testing the complete, integrated software system.

#### d) Acceptance Testing
Testing by end users to validate business requirements.

### 6.3 Black-Box vs White-Box Testing

| Aspect | Black-Box Testing | White-Box Testing |
|--------|-------------------|-------------------|
| **Knowledge required** | No knowledge of internal code | Requires code knowledge |
| **Focus** | Inputs and outputs | Internal logic and structure |
| **Techniques** | Equivalence partitioning, boundary value analysis, decision tables | Statement coverage, branch coverage, path coverage |
| **When used** | Acceptance testing, some system testing | Unit testing, integration testing |
| **Example** | Testing a login function with valid/invalid credentials | Testing all branches in an if-else statement |

### 6.4 Test Case Design Techniques

#### Equivalence Partitioning
Divide input data into partitions (equivalence classes) where all values behave similarly.

```python
# Example: Testing an age validation function
# Valid age: 0-120

def get_age_category(age):
    """
    Categorize age:
    - Child: 0-12
    - Teen: 13-19
    - Adult: 20-59
    - Senior: 60+
    """
    if age < 0 or age > 120:
        return "Invalid"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Equivalence classes:
# - Invalid: age < 0, age > 120
# - Valid: 0-12, 13-19, 20-59, 60-120
# 
# Test values:
# Boundary: -1, 0, 12, 13, 19, 20, 59, 60, 120, 121
```

#### Boundary Value Analysis
Test values at boundaries—most defects occur at boundaries.

```python
# For function accepting 1-100:
# Test: 0, 1, 2, 99, 100, 101
```

---

## 7. ISO/IEC Standards for Software Quality

The Delhi University syllabus requires understanding of international standards. Let's explore the key standards.

### 7.1 ISO 9001:2015

**Quality Management Systems** — A generic standard applicable to any organization.

Key principles:
1. Customer focus
2. Leadership
3. Engagement of people
4. Process approach
5. Improvement
6. Evidence-based decision making
7. Relationship management

### 7.2 ISO/IEC 25010:2011 (SQuaRE)

**Systems and Software Quality Requirements and Evaluation (SQuaRE)**

Defines quality models for software product quality:

**Functional Suitability**
- Functional completeness
- Functional correctness
- Functional appropriateness

**Performance Efficiency**
- Time behavior
- Resource utilization
- Capacity

**Compatibility**
- Co-existence
- Interoperability

**Usability**
- Appropriateness recognizability
- Learnability
- Operability
- User error protection
- User interface aesthetics
- Accessibility

**Reliability**
- Maturity
- Availability
- Fault tolerance
- Recoverability

**Security**
- Confidentiality
- Integrity
- Non-repudiation
- Accountability
- Authenticity

**Maintainability**
- Modularity
- Reusability
- Analysability
- Modifiability
- Testability

**Portability**
- Adaptability
- Installability
- Replaceability

### 7.3 ISO/IEC 12207:2008

**Software life cycle processes** — Provides a framework for software life cycle processes.

| Process Category | Processes |
|------------------|-----------|
| **Agreement** | Acquisition, Supply |
| **Organizational** | Management, Infrastructure, Improvement, Human Resource |
| **Technical** | Requirements, Design, Construction, Integration, Testing, Operation, Maintenance |

### 7.4 CMMI (Capability Maturity Model Integration)

A process improvement framework with 5 maturity levels:

| Level | Name | Description |
|-------|------|-------------|
| 1 | Initial | Ad hoc, unpredictable |
| 2 | Managed | Process characterized for projects |
| 3 | Defined | Process characterized organizationally |
| 4 | Quantitatively Managed | Process measured and controlled |
| 5 | Optimizing | Continuous improvement |

---

## 8. Defect Management

Defect management is the systematic process of identifying, tracking, and resolving software defects.

### 8.1 Defect Life Cycle

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  NEW     │────►│   OPEN   │────►│  ASSIGNED│────►│ IN PROGRESS│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
                                              │
                   ┌──────────┐     ┌──────────┐     │
                   │  CLOSED  │◄────│  TESTED  │◄────┘
                   └──────────┘     └──────────┘
                         ▲
                         │
                   ┌──────────┐
                   │ REOPENED │
                   └──────────┘
```

### 8.2 Defect Severity and Priority

**Severity** (Technical impact):
- **Critical**: System crash, data loss
- **Major**: Major function not working
- **Minor**: Minor function affected
- **Cosmetic**: UI issues

**Priority** (Business urgency):
- **High**: Must fix immediately
- **Medium**: Should fix in current release
- **Low**: Fix if time permits

### 8.3 Defect Tracking Example

```python
# Example: Simple defect tracking data structure
class Defect:
    def __init__(self, defect_id, title, description, severity, priority, status):
        self.id = defect_id
        self.title = title
        self.description = description
        self.severity = severity  # Critical, Major, Minor, Cosmetic
        self.priority = priority  # High, Medium, Low
        self.status = status      # New, Open, Assigned, In Progress, Tested, Closed
        self.assignee = None
        self.comments = []
    
    def __repr__(self):
        return f"Defect({self.id}: {self.title}, Severity={self.severity}, Priority={self.priority})"

# Create defects
defects = [
    Defect(101, "Login crashes on empty password", "App crashes when password field is empty", 
           "Critical", "High", "Open"),
    Defect(102, "Typo in welcome message", "Welcome message says 'Wlcome' instead of 'Welcome'",
           "Minor", "Low", "New"),
    Defect(103, "Export PDF not working", "Export to PDF button does nothing",
           "Major", "High", "Assigned"),
]

# Display defect report
print("DEFECT REPORT")
print("=" * 50)
for d in defects:
    print(f"ID: {d.id} | Priority: {d.priority} | Severity: {d.severity}")
    print(f"   Title: {d.title}")
    print()
```

### 8.4 Defect Metrics

```python
# Example: Defect metrics calculation
def calculate_defect_metrics(defects, total_lines_of_code):
    """Calculate key defect metrics"""
    
    # Defect density
    defect_density = len(defects) / (total_lines_of_code / 1000)
    
    # By severity
    by_severity = {}
    for d in defects:
        by_severity[d.severity] = by_severity.get(d.severity, 0) + 1
    
    # By status
    by_status = {}
    for d in defects:
        by_status[d.status] = by_status.get(d.status, 0) + 1
    
    # Fix rate (closed / total)
    closed_count = by_status.get("Closed", 0)
    fix_rate = (closed_count / len(defects) * 100) if defects else 0
    
    return {
        "defect_density": round(defect_density, 2),
        "by_severity": by_severity,
        "by_status": by_status,
        "fix_rate_percent": round(fix_rate, 2)
    }

# Sample calculation
total_kloc = 50  # 50,000 lines
sample_defects = ["Critical", "Major", "Minor", "Major", "Closed", "Closed", "Critical", "Open"]
# (Simplified - using strings for demo)

metrics = calculate_defect_metrics(sample_defects, total_kloc)
print(f"Defect Density: {metrics['defect_density']} defects/KLOC")
print(f"Fix Rate: {metrics['fix_rate_percent']}%")
```

---

## 9. Practical Example: Building a Test Strategy

Let's apply what we've learned with a comprehensive example.

### 9.1 Scenario: E-Commerce Checkout System

```python
# checkout.py - A simple checkout system

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discounts = []
    
    def add_item(self, item_id, name, price, quantity):
        """Add item to cart"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        self.items.append({
            'item_id': item_id,
            'name': name,
            'price': price,
            'quantity': quantity
        })
    
    def apply_discount(self, discount_code, discount_percent):
        """Apply discount code"""
        if discount_percent < 0 or discount_percent > 100:
            raise ValueError("Discount must be 0-100%")
        self.discounts.append({
            'code': discount_code,
            'percent': discount_percent
        })
    
    def calculate_total(self):
        """Calculate final total"""
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        
        # Apply discounts (can't exceed subtotal)
        total_discount = 0
        for discount in self.discounts:
            total_discount += subtotal * (discount['percent'] / 100)
        
        total_discount = min(total_discount, subtotal)  # Cap at subtotal
        return subtotal - total_discount


class CheckoutSystem:
    def __init__(self):
        self.cart = ShoppingCart()
        self.tax_rate = 0.08  # 8% tax
    
    def process_checkout(self, payment_method):
        """Process checkout"""
        if not self.cart.items:
            raise ValueError("Cart is empty")
        
        if payment_method not in ['credit', 'debit', 'upi', 'cash']:
            raise ValueError(f"Invalid payment method: {payment_method}")
        
        subtotal = self.cart.calculate_total()
        tax = subtotal * self.tax_rate
        final_total = subtotal + tax
        
        return {
            'subtotal': subtotal,
            'tax': tax,
            'total': final_total,
            'payment_method': payment_method,
            'items_count': len(self.cart.items)
        }
```

### 9.2 Test Strategy for Checkout System

```python
# test_checkout.py - Comprehensive test suite

import unittest

class TestShoppingCart(unittest.TestCase):
    """Unit tests for ShoppingCart"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.cart = ShoppingCart()
    
    def test_add_item_valid(self):
        """Test adding valid item"""
        self.cart.add_item("BOOK001", "Python Guide", 500, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['quantity'], 2)
    
    def test_add_item_invalid_quantity(self):
        """Test adding item with zero/negative quantity"""
        with self.assertRaises(ValueError) as context:
            self.cart.add_item("BOOK001", "Python Guide", 500, 0)
        self.assertIn("positive", str(context.exception))
    
    def test_add_item_negative_price(self):
        """Test adding item with negative price"""
        with self.assertRaises(ValueError):
            self.cart.add_item("BOOK001", "Python Guide", -100, 1)
    
    def test_apply_discount_valid(self):
        """Test applying valid discount"""
        self.cart.add_item("BOOK001", "Python Guide", 500, 1)
        self.cart.apply_discount("SAVE10", 10)
        self.assertEqual(len(self.cart.discounts), 1)
    
    def test_discount_capped_at_subtotal(self):
        """Test that discount doesn't exceed subtotal"""
        self.cart.add_item("BOOK001", "Python Guide", 100, 1)
        self.cart.apply_discount("SUPER50", 50)  # 50% = 50
        self.cart.apply_discount("ANOTHER50", 50)  # Another 50% = 50
        # Total discount = 100, but subtotal = 100, so max discount = 100
        total = self.cart.calculate_total()
        self.assertEqual(total, 0)  # Fully covered by discounts
    
    def test_calculate_total_empty_cart(self):
        """Test total calculation with empty cart"""
        total = self.cart.calculate_total()
        self.assertEqual(total, 0)


class TestCheckoutSystem(unittest.TestCase):
    """Integration tests for CheckoutSystem"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.checkout = CheckoutSystem()
    
    def test_process_checkout_success(self):
        """Test successful checkout"""
        self.checkout.cart.add_item("BOOK001", "Python Guide", 500, 1)
        result = self.checkout.process_checkout("credit")
        
        self.assertEqual(result['subtotal'], 500)
        self.assertEqual(result['tax'], 40)  # 8% of 500
        self.assertEqual(result['total'], 540)
    
    def test_process_checkout_empty_cart(self):
        """Test checkout with empty cart"""
        with self.assertRaises(ValueError) as context:
            self.checkout.process_checkout("credit")
        self.assertIn("empty", str(context.exception))
    
    def test_process_checkout_invalid_payment(self):
        """Test checkout with invalid payment method"""
        self.checkout.cart.add_item("BOOK001", "Python Guide", 500, 1)
        with self.assertRaises(ValueError) as context:
            self.checkout.process_checkout("cryptocurrency")
        self.assertIn("Invalid payment method", str(context.exception))
    
    def test_process_checkout_with_discount(self):
        """Test checkout with discount applied"""
        self.checkout.cart.add_item("BOOK001", "Python Guide", 1000, 1)
        self.checkout.cart.apply_discount("SAVE20", 20)
        
        result = self.checkout.process_checkout("upi")
        
        self.assertEqual(result['subtotal'], 800)  # 1000 - 20%
        self.assertEqual(result['tax'], 64)  # 8% of 800
        self.assertEqual(result['total'], 864)


# Boundary value analysis test
class TestBoundaryConditions(unittest.TestCase):
    """Boundary value analysis tests"""
    
    def test_max_discount_boundary(self):
        """Test discount at exactly 0%"""
        cart = ShoppingCart()
        cart.add_item("BOOK001", "Python Guide", 100, 1)
        cart.apply_discount("ZERO", 0)
        self.assertEqual(cart.calculate_total(), 100)
    
    def test_max_discount_boundary_100(self):
        """Test discount at exactly 100%"""
        cart = ShoppingCart()
        cart.add_item("BOOK001", "Python Guide", 100, 1)
        cart.apply_discount("FREE", 100)
        self.assertEqual(cart.calculate_total(), 0)
    
    def test_over_max_discount(self):
        """Test discount exceeding 100%"""
        cart = ShoppingCart()
        cart.add_item("BOOK001", "Python Guide", 100, 1)
        with self.assertRaises(ValueError):
            cart.apply_discount("INVALID", 101)


if __name__ == '__main__':
    # Run tests with verbosity
    unittest.main(verbosity=2)
```

---

## 10. Key Takeaways

### Core Concepts Summary

1. **Quality Assurance (QA) vs Quality Control (QC)**
   - QA is process-oriented and preventive
   - QC is product-oriented and corrective

2. **Verification vs Validation**
   - Verification: "Are we building the product right?" (Does it meet specifications?)
   - Validation: "Are we building the right product?" (Does it meet user needs?)

3. **Quality Metrics**
   - Defect Density: defects per KLOC
   - Test Coverage: percentage of code tested
   - MTBF/MTTR: reliability measures

4. **Testing Techniques**
   - Static: Reviews, walkthroughs, inspections, static analysis
   - Dynamic: Unit, integration, system, acceptance testing

5. **International Standards**
   - ISO 9001: Quality management
   - ISO/IEC 25010: Software quality model
   - ISO/IEC 12207: Life cycle processes

6. **Defect Management**
   - Follow defect life cycle
   - Track severity and priority
   - Use metrics to measure quality

---

## 11. Assessment Questions

### Multiple Choice Questions

**Q1. What is the primary focus of Quality Assurance?**
- A) Finding bugs in the software
- B) Preventing defects through process improvement
- C) Testing the final product
- D) Fixing reported issues

**Answer: B) Preventing defects through process improvement**

*Explanation: QA is about building quality into the process, not just finding defects. It's preventive rather than corrective.*

---

**Q2. Verification asks which question?**
- A) "Are we building the right product?"
- B) "Is the code correct?"
- C) "Are we building the product right?"
- D) "Does the user like it?"

**Answer: C) "Are we building the product right?"**

*Explanation: Verification checks if the product is being built according to specifications (the design). Validation checks if the right product is being built (meeting user needs).*

---

**Q3. Which ISO standard defines the Software Quality Model?**
- A) ISO 9001
- B) ISO/IEC 12207
- C) ISO/IEC 25010
- D) CMMI

**Answer: C) ISO/IEC 25010**

*Explanation: ISO/IEC 25010 (SQuaRE) defines the quality model for software products, including characteristics like functional suitability, reliability, and usability.*

---

**Q4. Defect density is calculated as:**
- A) Total defects × KLOC
- B) Total defects / KLOC
- C) KLOC / Total defects
- D) Total defects - KLOC

**Answer: B) Total defects / KLOC**

*Explanation: Defect density measures defects per thousand lines of code (KLOC). A lower density indicates higher quality.*

---

**Q5. Which testing technique examines code without executing it?**
- A) Unit Testing
- B) Integration Testing
- C) Static Testing
- D) System Testing

**Answer: C) Static Testing**

*Explanation: Static testing (reviews, walkthroughs, inspections) examines code without running it. Dynamic testing (unit, integration, system) requires execution.*

---

### Short Answer Questions

**Q6. Explain the difference between verification and validation with an example.**

**Answer:** Verification checks if the product conforms to specifications ("building it right"), while validation checks if the product meets user needs ("building the right product"). For example, verifying a calculator ensures the add() function adds correctly according to specs. Validating the same calculator ensures users can actually perform calculations they need in their daily work.

---

**Q7. List three static and three dynamic testing techniques.**

**Answer:**
- **Static**: Code Reviews, Walkthroughs, Inspections, Static Analysis
- **Dynamic**: Unit Testing, Integration Testing, System Testing, Acceptance Testing

---

**Q8. What is the defect life cycle? List at least 5 states.**

**Answer:** The defect life cycle includes: New → Open → Assigned → In Progress → Tested → Closed. Some cycles also include Reopened when a fix doesn't work.

---

**Q9. Why is boundary value analysis important in testing?**

**Answer:** Most errors occur at boundaries (e.g., array indices, input ranges). Testing boundaries (0, 1, max-1, max) catches these common errors that equivalence partitioning might miss.

---

### Long Answer Questions

**Q10. Design a comprehensive test strategy for a student marks management system that stores, calculates, and displays student performance data. Include unit tests, integration tests, and quality metrics you would track.**

**Answer:** (Suggested outline)
- **Unit Tests**: Test individual functions (calculate average, grade assignment, CGPA calculation)
- **Integration Tests**: Test database interactions, file I/O, UI integration
- **Quality Metrics**: Track defect density, test coverage (>80%), test execution time
- **Standards**: Follow ISO/IEC 25010 for quality characteristics
- **Process**: Use version control, code reviews, continuous integration

---

## 12. Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **Quality Assurance (QA)** | Process-oriented activities focused on preventing defects by improving development processes |
| **Quality Control (QC)** | Product-oriented activities focused on detecting and fixing defects in the software |
| **Verification** | "Building the product right" - checking if software conforms to specifications |
| **Validation** | "Building the right product" - checking if software meets user needs |
| **Defect Density** | Number of defects per thousand lines of code (KLOC); measures software quality |
| **Static Testing** | Testing without executing code (reviews, inspections, static analysis) |
| **Dynamic Testing** | Testing by executing code (unit, integration, system tests) |
| **Equivalence Partitioning** | Dividing input into groups that should behave similarly to reduce test cases |
| **Boundary Value Analysis** | Testing at boundary values where most defects occur |
| **CMMI** | Capability Maturity Model Integration - 5-level process improvement framework |
| **MTBF** | Mean Time Between Failures - measures system reliability |
| **MTTR** | Mean Time to Repair - measures how quickly defects are fixed |
| **Test Coverage** | Percentage of code executed by tests; higher coverage generally means better quality |

---

## References

1. Pressman, R. S. & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill.
2. Sommerville, I. (2015). *Software Engineering* (10th ed.). Pearson.
3. ISO/IEC 25010:2011 - Systems and Software Quality Requirements and Evaluation (SQuaRE)
4. Delhi University BSc (Hons) Computer Science Syllabus, NEP 2024 UGCF

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University as part of the NEP 2024 UGCF curriculum. For additional practice, refer to software engineering textbooks and attempt previous year question papers.*