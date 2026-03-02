# Software Quality Metrics

## Comprehensive Study Material for BSc (Hons) Computer Science

---

## 1. Introduction and Real-World Relevance

Software quality metrics are quantifiable measures used to assess the quality of software products and processes. In today's technology-driven world, where software systems control critical infrastructure—from healthcare systems to financial institutions—the importance of measuring and maintaining software quality cannot be overstated.

**Why Software Quality Metrics Matter:**

- **Cost Reduction**: Defects discovered in production can cost 100x more to fix than those found during development
- **Customer Satisfaction**: High-quality software leads to better user experience and retention
- **Competitive Advantage**: Organizations with robust quality metrics deliver more reliable products
- **Regulatory Compliance**: Many industries require documented quality metrics for certification

**Real-World Example**: In 2015, a bug in the Knight Capital Group's trading software caused a loss of $440 million in 45 minutes. This catastrophic failure was attributed to insufficient code review and lack of quality metrics. Such incidents highlight why Delhi University's NEP 2024 curriculum emphasizes software quality metrics as a core competency for future software engineers.

---

## 2. Software Quality Fundamentals

### 2.1 What is Software Quality?

Software quality refers to the degree to which a software product meets specified requirements and user expectations. Quality encompasses:

- **Functionality**: Does the software do what it's supposed to do?
- **Reliability**: Does it perform consistently without failures?
- **Usability**: Is it easy to learn and use?
- **Efficiency**: Does it use resources optimally?
- **Maintainability**: Can it be easily modified and extended?
- **Portability**: Can it run on different platforms?

### 2.2 Quality Models

#### ISO 25010 Standard (Replacement for ISO 9126)

The ISO 25010 standard defines a quality model for software products with two main categories:

**Functional Quality:**
- Functional suitability
- Functional completeness
- Functional correctness

**Non-Functional Quality:**
- **Performance Efficiency**: Time behavior, resource utilization, capacity
- **Compatibility**: Co-existence, interoperability
- **Usability**: Appropriateness recognizability, learnability, operability, user error protection, user interface aesthetics
- **Reliability**: Maturity, availability, fault tolerance, recoverability
- **Security**: Confidentiality, integrity, non-repudiation, accountability, authenticity
- **Maintainability**: Modularity, reusability, analyzability, modifiability, testability
- **Portability**: Adaptability, installability, replaceability

#### McCall's Quality Model

Another important model (though older) includes 11 quality factors organized into three categories:

- **Product Operation**: Correctness, Reliability, Efficiency, Integrity, Usability
- **Product Revision**: Maintainability, Flexibility, Testability
- **Product Transition**: Portability, Reusability, Interoperability

---

## 3. Software Metrics Overview

### 3.1 Classification of Software Metrics

Software metrics are broadly classified into three categories:

| Category | Description | Examples |
|----------|-------------|----------|
| **Process Metrics** | Measures of the software development process | Defect detection rate, code review efficiency |
| **Product Metrics** | Measures of the software product itself | Lines of code, cyclomatic complexity |
| **Project Metrics** | Measures specific to a project | Cost per FP, schedule variance |

### 3.2 Internal vs External Metrics

**Internal Metrics** (White-box):
- Measured by analyzing the software code
- Can be measured without executing the program
- Examples: Lines of code, cyclomatic complexity, coupling
- Used by developers during development

**External Metrics** (Black-box):
- Measured during software execution
- Require the software to be running
- Examples: Response time, defect rate, usability
- Visible to end-users and stakeholders

---

## 4. Product Metrics (Detailed)

### 4.1 Size Metrics

#### Lines of Code (LOC)

LOC measures the total number of lines in source code. There are two variants:

- **Physical LOC (PLOC)**: All lines including comments and blank lines
- **Logical LOC (SLOC)**: Only executable statements

**Example Calculation**:
```python
# This is a comment - not counted in SLOC

def calculate_sum(a, b):      # 1 logical line
    return a + b              # 1 logical line

def calculate_product(a, b):  # 1 logical line  
    return a * b              # 1 logical line

# Main program
x = 10                        # 1 logical line
y = 20                        # 1 logical line
result = calculate_sum(x, y) # 1 logical line
```

For this example:
- Physical LOC = 10 lines
- Logical LOC = 6 lines

**Industry Standards**:
- A typical function should be 50-150 lines
- A module should not exceed 500-1000 lines
- Very large files (>10,000 lines) indicate poor modularity

#### Function Points (FP)

Function Points measure software size based on functionality from user's perspective. The basic calculation:

```
FP = Total Count × [0.65 + 0.01 × Σ(VAF)]
```

Where VAF (Value Adjustment Factor) considers 14 general system characteristics.

**Function Point Types**:
1. External Inputs (EI)
2. External Outputs (EO)
3. External Inquiries (EQ)
4. Internal Logical Files (ILF)
5. External Interface Files (EIF)

### 4.2 Structural Metrics

#### Coupling

Coupling measures the degree of interdependence between software modules. Lower coupling is desirable.

**Types of Coupling** (from best to worst):
1. **Content Coupling** (worst): One module modifies another's internal data
2. **Common Coupling**: Modules share global data
3. **Control Coupling**: One module controls the flow of another
4. **Stamp Coupling**: Modules share composite data structures
5. **Data Coupling** (best): Modules share only primitive data

**Example - Data Coupling (Good)**:
```python
# Module A - Provides data
def get_user_name(user_id):
    return "John Doe"

def get_user_age(user_id):
    return 25

# Module B - Uses data
name = get_user_name(101)  # Passes simple data
age = get_user_age(101)
print(f"User: {name}, Age: {age}")
```

**Example - Stamp Coupling (Less Desirable)**:
```python
# Module A - Shares entire structure
class User:
    def __init__(self, name, age, address, phone, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email

# Module B - Uses entire object but only needs name
def print_user_name(user):
    print(user.name)  # Only needs name but gets full object
```

#### Cohesion

Cohesion measures how strongly related and focused the responsibilities of a single module are. Higher cohesion is desirable.

**Types of Cohesion** (from worst to best):
1. **Coincidental** (worst): Elements are unrelated
2. **Logical**: Elements perform similar activities
3. **Temporal**: Elements related by time of execution
4. **Procedural**: Elements in a specific execution order
5. **Communicational**: Elements operate on same data
6. **Sequential**: Output of one serves as input to next
7. **Functional** (best): Elements contribute to single function

**Example - Functional Cohesion (Best)**:
```python
# Highly cohesive - single, well-defined purpose
def calculate_rectangle_area(width, height):
    """Calculate and return the area of a rectangle."""
    return width * height

def calculate_rectangle_perimeter(width, height):
    """Calculate and return the perimeter of a rectangle."""
    return 2 * (width + height)
```

**Example - Logical Cohesion (Less Desirable)**:
```python
# Less cohesive - unrelated operations grouped
def handle_user_operations(operation_type, data):
    if operation_type == "validate":
        # validation logic
        pass
    elif operation_type == "format":
        # formatting logic
        pass
    elif operation_type == "save":
        # saving logic
        pass
```

#### Depth of Inheritance Tree (DIT)

DIT measures the maximum depth of the class hierarchy. While deeper hierarchies enable reuse, they also increase complexity.

```
DIT = 1 (Class A)
DIT = 2 (Class A → Class B)  
DIT = 3 (Class A → Class B → Class C)
```

**Example**:
```python
class Animal:  # DIT = 1
    def speak(self):
        pass

class Dog(Animal):  # DIT = 2
    def speak(self):
        return "Woof"

class Labrador(Dog):  # DIT = 3
    def speak(self):
        return "Loud bark"
```

#### Response for a Class (RFC)

RFC measures the number of different methods that can be invoked in response to a message to an object. High RFC indicates complex classes.

**Calculation**:
```
RFC = |M| + |R|
```
Where:
- |M| = number of methods in the class
- |R| = number of different methods called by these methods

**Example**:
```python
class OrderProcessor:
    def process_order(self, order):
        # Calls 3 different methods
        self.validate_order(order)
        self.calculate_total(order)
        self.save_order(order)
    
    def validate_order(self, order):
        pass
    
    def calculate_total(self, order):
        # Internal method
        self.apply_discount(order)
        self.add_tax(order)
    
    def apply_discount(self, order):
        pass
    
    def add_tax(self, order):
        pass
    
    def save_order(self, order):
        pass

# RFC = 5 (methods) + 2 (methods called internally) = 7
```

### 4.3 Complexity Metrics

#### Cyclomatic Complexity (CC)

Cyclomatic Complexity measures the number of linearly independent paths through a program's source code.

**Formula**:
```
CC = E - N + 2P
```
Where:
- E = Number of edges
- N = Number of nodes
- P = Number of connected components (usually 1)

**Simplified Formula for Single Function**:
```
CC = Number of Decision Points + 1
```

**Decision Points Include**: if, while, for, case, &&, ||

**Example**:
```python
def calculate_grade(score):  # CC = 1 (start)
    if score >= 90:          # CC +1 = 2
        return "A"
    elif score >= 80:        # CC +1 = 3
        return "B"
    elif score >= 70:        # CC +1 = 4
        return "C"
    elif score >= 60:        # CC +1 = 5
        return "D"
    else:                    # CC +1 = 6
        return "F"
```

**Complexity Interpretation**:
| Complexity | Risk Level | Description |
|------------|------------|-------------|
| 1-10 | Low | Simple, well-structured code |
| 11-20 | Moderate | More complex, moderate risk |
| 21-50 | High | Complex, high risk |
| >50 | Very High | Untestable, very high risk |

---

## 5. Quality Metrics

### 5.1 Defect Density (DD)

Defect Density measures the number of defects per unit size (typically per 1000 lines of code).

**Formula**:
```
Defect Density = Total Defects / Size (KLOC)
```

**Example**:
```
Total Defects Found = 25
Total Lines of Code = 10,000

Defect Density = 25 / 10 = 2.5 defects/KLOC
```

**Industry Benchmarks**:
- Excellent: < 1.0 defects/KLOC
- Good: 1.0 - 2.0 defects/KLOC
- Average: 2.0 - 3.0 defects/KLOC
- Poor: > 3.0 defects/KLOC

### 5.2 Mean Time To Repair (MTTR)

MTTR measures the average time taken to repair a defect after it has been identified.

**Formula**:
```
MTTR = Total Downtime / Number of Repairs
```

**Complete Worked Example**:

A software system experienced 4 failures over a 30-day period. The repair times were:
- Failure 1: Discovered at 8:00 AM, Fixed at 10:30 AM (2.5 hours)
- Failure 2: Discovered at 2:00 PM, Fixed at 3:00 PM (1.0 hour)
- Failure 3: Discovered at 11:00 PM, Fixed at 1:30 AM next day (2.5 hours)
- Failure 4: Discovered at 9:00 AM, Fixed at 11:45 AM (2.75 hours)

**Calculation**:
```
Total Repair Time = 2.5 + 1.0 + 2.5 + 2.75 = 8.75 hours

MTTR = 8.75 / 4 = 2.1875 hours

MTTR ≈ 2 hours 11 minutes
```

### 5.3 Mean Time Between Failures (MTBF)

MTBF measures the average time between system failures.

**Formula**:
```
MTBF = (Total Operational Time) / (Number of Failures)
```

**Example**:
```
System was operational for 720 hours in a month
Number of failures = 4

MTBF = 720 / 4 = 180 hours (or 7.5 days)
```

**Relationship with MTTR**:
```
Availability = MTBF / (MTBF + MTTR)

For the above example:
Availability = 180 / (180 + 2.1875) = 0.988 = 98.8%
```

### 5.4 Test Coverage Metrics

#### Statement Coverage
```
Statement Coverage = (Statements Executed / Total Statements) × 100%
```

#### Branch Coverage
```
Branch Coverage = (Branches Executed / Total Branches) × 100%
```

**Example**:
```python
def get_discount(user_type, purchase_amount):
    if user_type == "premium":      # Branch 1
        discount = 0.20              # Statement 1
    elif user_type == "regular":    # Branch 2
        discount = 0.10              # Statement 2
    else:                            # Branch 3
        discount = 0.05              # Statement 3
    
    return purchase_amount * discount
```

Test case: user_type = "premium", purchase_amount = 100
- Statement Coverage: 2/6 = 33.3%
- Branch Coverage: 1/3 = 33.3%

---

## 6. Practical Applications

### 6.1 Quality Metrics in Agile Development

In modern software development, quality metrics guide decision-making:

1. **Sprint Planning**: Use defect density to estimate testing effort
2. **Code Reviews**: Monitor coupling and cohesion before merging
3. **Release Decisions**: Use MTBF and MTTR to determine release readiness

### 6.2 Real-World Quality Dashboard Example

```
┌─────────────────────────────────────────────────────────┐
│              SOFTWARE QUALITY DASHBOARD                  │
├─────────────────────────────────────────────────────────┤
│  Defect Density:    1.8 defects/KLOC     [GOOD]         │
│  Cyclomatic Avg:    8.5                  [LOW RISK]    │
│  Test Coverage:     87%                  [GOOD]         │
│  Code Duplication:  3.2%                 [ACCEPTABLE]  │
│  MTTR:              2.1 hours            [EXCELLENT]   │
│  MTBF:              168 hours            [GOOD]         │
│  RFC Average:       12.3                 [MODERATE]     │
│  Coupling:          Low                  [GOOD]         │
│  Cohesion:          Functional            [EXCELLENT]   │
└─────────────────────────────────────────────────────────┘
```

---

## 7. Key Takeaways

1. **Quality Models**: ISO 25010 is the current standard, covering functional and non-functional quality characteristics including reliability, maintainability, security, and usability.

2. **Internal vs External Metrics**: Internal metrics (LOC, CC, coupling) are measured from code; external metrics (MTBF, defect rate) require execution.

3. **Size Metrics**: LOC and Function Points help estimate project effort and compare software size across projects.

4. **Structural Metrics**: Aim for high cohesion and low coupling. DIT and RFC help assess class complexity.

5. **Quality Indicators**: Defect Density < 1.0/KLOC is excellent; MTBF and MTTR directly impact system availability.

6. **Cyclomatic Complexity**: Keep complexity below 10 for maintainable code; above 20 indicates high risk.

7. **Continuous Monitoring**: Quality metrics should be tracked throughout the development lifecycle, not just at the end.

---

## 8. Assessment Section

### 8.1 Multiple Choice Questions

**Question 1**: According to ISO 25010, which of the following is NOT a sub-characteristic of the "Maintainability" quality characteristic?
- A) Modularity
- B) Reusability
- C) Installability
- D) Analyzability

**Correct Answer**: C (Installability is a sub-characteristic of Portability)

---

**Question 2**: What type of cohesion is considered the BEST and most desirable?
- A) Communicational Cohesion
- B) Sequential Cohesion
- C) Functional Cohesion
- D) Temporal Cohesion

**Correct Answer**: C (Functional Cohesion - elements work together to perform a single, well-defined function)

---

**Question 3**: In the calculation of Cyclomatic Complexity, what does each decision point (if, while, for) contribute?
- A) +1 to the complexity count
- B) +2 to the complexity count
- C) Multiplies the complexity by 2
- D) Does not affect complexity

**Correct Answer**: A (Each decision point adds 1 to the base complexity of 1)

---

**Question 4**: A software module has 150 lines of code and 5 defects were found. What is the defect density per KLOC?
- A) 0.033 defects/KLOC
- B) 3.33 defects/KLOC
- C) 33.3 defects/KLOC
- D) 0.33 defects/KLOC

**Correct Answer**: B (Defect Density = 5 / 0.150 = 33.3 defects/KLOC - Note: 150 lines = 0.150 KLOC)

---

**Question 5**: Which of the following metrics would be classified as an EXTERNAL metric?
- A) Lines of Code
- B) Cyclomatic Complexity
- C) Response Time
- D) Coupling

**Correct Answer**: C (Response Time requires the software to be executing and is observed by users)

---

**Question 6**: In McCall's Quality Model, which category does "Reliability" belong to?
- A) Product Revision
- B) Product Transition
- C) Product Operation
- D) None of the above

**Correct Answer**: C (Reliability is one of the five factors in Product Operation)

---

**Question 7**: Calculate the Cyclomatic Complexity for the following code:
```python
if a > b:
    if c == d:
        print("Hello")
    else:
        print("World")
```
- A) 2
- B) 3
- C) 4
- D) 1

**Correct Answer**: B (Decision points: 2 if statements = 2, plus base 1 = 3)

---

**Question 8**: What is the main disadvantage of having a very high Depth of Inheritance Tree (DIT)?
- A) Code becomes difficult to test
- B) Increased complexity and tight coupling between classes
- C) Reduces reusability
- D) Decreases maintainability only

**Correct Answer**: B (High DIT increases complexity and creates tight coupling, making the system harder to maintain and understand)

---

### 8.2 Numerical Problems

**Problem 1**: A software system has 50,000 lines of code. During testing, 85 defects were discovered. After release, 15 more defects were found in the first month. Calculate:
- Defect Density during testing
- Defect Density after one month
- Total Defect Density

**Solution**:
```
Testing Defects = 85
Size = 50 KLOC
Testing Defect Density = 85 / 50 = 1.7 defects/KLOC

Post-release Defects = 15
Total Defects = 85 + 15 = 100
Total Defect Density = 100 / 50 = 2.0 defects/KLOC
```

---

**Problem 2**: A system was operational for 840 hours in a month and experienced 6 failures. The total repair time was 12 hours. Calculate:
- MTBF
- MTTR
- System Availability percentage

**Solution**:
```
MTBF = Total Operational Time / Number of Failures
     = 840 / 6
     = 140 hours

MTTR = Total Repair Time / Number of Repairs
     = 12 / 6
     = 2 hours

Availability = MTBF / (MTBF + MTTR)
             = 140 / (140 + 2)
             = 140 / 142
             = 0.9859 = 98.59%
```

---

**Problem 3**: Calculate Cyclomatic Complexity for the following function and determine its risk level:

```python
def process_payment(payment):
    if payment.amount > 0:
        if payment.method == "credit":
            if payment.validate():
                payment.process()
                if payment.send_receipt():
                    return "Success"
                else:
                    return "Receipt failed"
            else:
                return "Validation failed"
        elif payment.method == "debit":
            payment.process()
            return "Success"
        else:
            return "Invalid method"
    else:
        return "Invalid amount"
```

**Solution**:
```
Decision Points:
1. if payment.amount > 0
2. if payment.method == "credit"
3. if payment.validate()
4. if payment.send_receipt()
5. elif payment.method == "debit" (else after #2)
6. else (after #1)

Total Decision Points = 6

Cyclomatic Complexity = 6 + 1 = 7

Risk Level: LOW (Complexity 1-10 is considered low risk)
```

---

**Problem 4**: A class has 8 methods. These methods internally call 5 different additional methods. What is the Response for a Class (RFC)?

**Solution**```
RFC = Number of methods + Number of different methods called
    = 8 + 5
    = 13
```

---

### 8.3 Flashcards

| Term | Definition |
|------|------------|
| **Defect Density** | Number of defects per thousand lines of code (KLOC) |
| **Cyclomatic Complexity** | Number of linearly independent paths through a program's source code |
| **Cohesion** | The degree to which elements inside a module belong together |
| **Coupling** | The degree of interdependence between software modules |
| **MTTR** | Mean Time To Repair - average time to fix a defect |
| **MTBF** | Mean Time Between Failures - average time between system failures |
| **Function Point** | A unit of measurement for software size based on functionality |
| **ISO 25010** | Current international standard for software quality models |
| **DIT** | Depth of Inheritance Tree - maximum depth of class hierarchy |
| **RFC** | Response for a Class - number of methods that can be invoked in response to a message |
| **Internal Metrics** | Metrics measured without executing the program (e.g., LOC, complexity) |
| **External Metrics** | Metrics measured during program execution (e.g., response time, defects) |
| **Availability** | Percentage of time system is operational: MTBF/(MTBF+MTTR) |
| **Functional Cohesion** | Best type - elements work together to perform a single function |
| **Data Coupling** | Best type of coupling - modules share only primitive data parameters |

---

*This study material aligns with the Delhi University NEP 2024 UGCF syllabus for Software Engineering and covers all essential topics for the Software Quality Metrics unit.*