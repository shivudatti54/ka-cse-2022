# Structure Charts: Comprehensive Study Material

## Software Engineering - BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

A **Structure Chart** is a hierarchical diagram that depicts the modular structure of a software system by showing the relationships between modules, their control flow, and data communication. It represents the high-level architecture of a system before detailed design or coding begins, serving as a blueprint for implementation.

In the context of the Delhi University BSc (Hons) Computer Science curriculum (NEP 2024 UGCF), Structure Charts are a fundamental artifact in the **Software Engineering** course, specifically under the module covering "System Design" and "Software Architecture." This topic carries significant weight as it bridges the gap between requirements analysis and coding, enabling developers to visualize system organization before diving into implementation details.

---

## 2. Historical Context and Real-World Relevance

Structure Charts emerged in the 1970s as part of the **Jackson Structured Programming (JSP)** and **Jackson System Development (JSD)** methodologies. They gained prominence through the work of Michael A. Jackson and later standardized through various software engineering methodologies including **Yourdon's structured design**.

### Real-World Applications

In contemporary software development, Structure Charts remain relevant in:

- **Legacy System Modernization**: Understanding existing mainframe and COBOL applications
- **Enterprise Application Architecture**: Large-scale systems in banking, healthcare, and ERP systems
- **Embedded Systems**: Automotive control systems, IoT device software
- **Academic Foundation**: Essential prerequisite for understanding modern architectural patterns like microservices and modular monoliths

---

## 3. Basic Notation and Symbols

### 3.1 Module Symbols

| Symbol | Meaning |
|--------|---------|
| **Rectangle** | Represents a module (subprogram, procedure, function) |
| **Double-lined Rectangle** | Indicates a physical module (file, program) |
| **Dashed Rectangle** | Logic module (abstract grouping) |

### 3.2 Module Names

Modules are labeled with:

- **Procedure names** (e.g., `Calculate_Total`, `Validate_Input`)
- **Function names** (e.g., `Compute_Average`)
- **Abstract names** for groups (e.g., `Student_Records_Module`)

### 3.3 Data Communication

```
┌─────────────────┐
│   MODULE NAME   │
├─────────────────┤
│  Data Couples   │  ← Information passed between modules
│  Control Flags  │  ← Control information
└─────────────────┘
```

- **Data Couples**: Arrows with filled arrowheads representing data elements passed between modules
- **Control Flags**: Arrows with hollow arrowheads representing control information (flags, switches, conditions)

### 3.4 Connection Lines

- **Solid lines with arrows**: Show module invocation hierarchy
- **Curved arrows**: Indicate data/control flow direction

### 3.5 Notation Example

```
                    ┌──────────────────┐
                    │   MAIN_MODULE    │
                    └────────┬─────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │   SUB_MOD_A  │  │   SUB_MOD_B  │  │   SUB_MOD_C  │
    └──────────────┘  └──────────────┘  └──────────────┘
```

---

## 4. Module Types

Understanding module types is crucial for effective structure chart design:

### 4.1 Transform Modules (Transform-Centered)

These modules accept input data, transform/process it, and produce output. They follow the **input-process-output** pattern.

```
                    ┌──────────────────┐
                    │  PROCESS_ORDER   │
                    └────────┬─────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
  │ READ_ORDER   │───▶│ VALIDATE     │───▶│ GENERATE     │
  │   DATA       │    │   ORDER      │    │   REPORT     │
  └──────────────┘    └──────────────┘    └──────────────┘
```

### 4.2 Transaction Modules (Transaction-Centered)

These modules analyze input and route to appropriate processing paths based on transaction type. They implement **dispatching logic**.

```
                    ┌──────────────────┐
                    │  TRANSACTION     │
                    │    DISPATCHER    │
                    └────────┬─────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
  │  PROCESS     │    │  PROCESS     │    │  PROCESS     │
  │  DEPOSIT     │    │  WITHDRAWAL  │    │  TRANSFER    │
  └──────────────┘    └──────────────┘    └──────────────┘
```

### 4.3 Coordination Modules

These modules orchestrate the execution of subordinate modules but perform no actual data transformation. They manage workflow and sequence.

---

## 5. Coupling and Cohesion

### 5.1 Coupling (Inter-module Dependencies)

Coupling measures the strength of connections between modules. **Lower coupling is desirable.**

| Type | Description | Desirability |
|------|-------------|--------------|
| **Content Coupling** | One module directly references internal code of another | Worst |
| **Common Coupling** | Modules share global data | Poor |
| **Control Coupling** | One module controls another via flags | Moderate |
| **Stamp Coupling** | Modules share composite data structure | Fair |
| **Data Coupling** | Modules communicate via parameters only | Best |

### 5.2 Cohesion (Intra-module Strength)

Cohesion measures how well a module's elements belong together. **Higher cohesion is desirable.**

| Type | Description |
|------|-------------|
| **Coincidental** | Random grouping of elements (worst) |
| **Logical** | Elements perform similar functions |
| **Temporal** | Elements related by timing |
| **Procedural** | Elements in specific execution sequence |
| **Communicational** | Elements operate on same data |
| **Sequential** | Output of one serves as input to next |
| **Functional** | Single purpose (best) |

---

## 6. Fan-in and Fan-out Analysis

### 6.1 Fan-out

**Fan-out** measures the number of modules directly controlled by a given module.

```
High Fan-out (problematic):
        ┌─────────────┐
        │  CONTROLLER │  ← Fan-out = 7 (too high)
        └──────┬──────┘
               │
     ┌───┬───┬─┴─┬───┬───┬───┐
     │   │   │   │   │   │   │
     ▼   ▼   ▼   ▼   ▼   ▼   ▼
   M1  M2  M3  M4  M5  M6  M7
```

**Design Principle**: Keep fan-out below 7 (Yourdon's guideline). If fan-out exceeds 7, consider introducing intermediate coordination modules.

### 6.2 Fan-in

**Fan-in** measures how many modules call a particular module.

```
High Fan-in (desirable):
         ┌───┐  ┌───┐  ┌───┐
         │A1 │  │A2 │  │A3 │
         └─┬─┘  └─┬─┘  └─┬─┘
           │     │     │
           └─────┼─────┘
                 ▼
          ┌─────────────┐
          │  SHARED     │  ← Fan-in = 3 (good reuse)
          │  MODULE     │
          └─────────────┘
```

**Design Principle**: Aim for high fan-in to maximize module reuse and reduce code duplication.

---

## 7. Design Principles and Guidelines

### 7.1 Structure Chart Design Heuristics

1. **Depth over Width**: Prefer deeper hierarchies with fewer modules at each level
2. **Fan-out Rule**: No module should call more than 7 other modules directly
3. **Fan-in Maximization**: Design modules to be reusable across multiple parent modules
4. **Single Entry/Exit**: Each module should have one entry point and one exit point
5. **Scope of Control**: A module should control all its subordinates
6. **Data Hiding**: Modules should hide implementation details
7. **Appropriate Abstraction**: Use meaningful module names at appropriate abstraction levels

### 7.2 Design Process

1. **Create first-cut structure chart** from data flow diagrams (DFD)
2. **Balance** the structure chart with DFD elements
3. **Refine** using coupling and cohesion analysis
4. **Optimize** fan-in and fan-out metrics
5. **Document** module specifications

---

## 8. Advanced Notation

### 8.1 Libraries and Packages

```
┌─────────────────────────────────────────┐
│          LIBRARY: UTILITIES             │
│  ┌─────────────────────────────────┐   │
│  │        Math_Functions           │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │        String_Utils             │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### 8.2 Iteration and Conditional Invocation

- **Circle with number**: Iteration (e.g., process all items)
- **Asterisk (*)**: Conditional invocation
- **Half-arrow**: Indicates direction of data

### 8.3 Physical Module Boundaries

```
╔════════════════════════════════════╗
║  PROGRAM: ACCOUNTS_SYSTEM          ║
╠════════════════════════════════════╣
║  ┌──────────────────────────────┐  ║
║  │       MODULE_A               │  ║
║  └──────────────────────────────┘  ║
║  ┌──────────────────────────────┐  ║
║  │       MODULE_B               │  ║
║  └──────────────────────────────┘  ║
╚════════════════════════════════════╝
```

---

## 9. Concrete Examples with Code

### Example 1: Library Management System

#### Structure Chart

```
                    ┌─────────────────────────────────┐
                    │      LIBRARY_MANAGEMENT         │
                    └───────────────┬─────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ MANAGE_BOOKS    │      │ MANAGE_MEMBERS  │      │ MANAGE_ISSUES   │
└────────┬────────┘      └────────┬────────┘      └────────┬────────┘
         │                        │                        │
    ┌────┴────┐             ┌────┴────┐             ┌────┴────┐
    ▼         ▼             ▼         ▼             ▼         ▼
┌───────┐ ┌───────┐    ┌───────┐ ┌───────┐    ┌───────┐ ┌───────┐
│ADD_   │ │SEARCH_│    │ADD_   │ │SEARCH_│    │ISSUE_ │ │RETURN_│
│BOOK   │ │BOOK   │    │MEMBER │ │MEMBER │    │BOOK   │ │BOOK   │
└───────┘ └───────┘    └───────┘ └───────┘    └───────┘ └───────┘
```

#### Corresponding Implementation (Python-like Pseudocode)

```python
# Main Program
class LibraryManagement:
    def __init__(self):
        self.books = ManageBooks()
        self.members = ManageMembers()
        self.issues = ManageIssues()
    
    def run(self):
        while True:
            choice = self.display_menu()
            self.dispatch(choice)
    
    def dispatch(self, choice):
        if choice == 1:
            self.books.add_book()
        elif choice == 2:
            self.books.search_book()
        elif choice == 3:
            self.members.add_member()
        elif choice == 4:
            self.issues.issue_book()
        # ... etc

# Transform Modules
class ManageBooks:
    def add_book(self):
        book_id = self.read_book_id()
        details = self.read_book_details()
        self.validate_book(details)
        self.save_book(book_id, details)
    
    def search_book(self):
        query = self.read_search_query()
        results = self.query_database(query)
        self.display_results(results)

class ManageIssues:
    def issue_book(self):
        member_id = self.validate_member()
        book_id = self.check_availability()
        self.update_issue_record(member_id, book_id)
        self.update_book_status(book_id, "ISSUED")
    
    def return_book(self):
        issue_id = self.read_issue_id()
        self.calculate_fine(issue_id)
        self.update_return_record(issue_id)
```

---

### Example 2: Payroll Processing System

#### Structure Chart

```
                    ┌─────────────────────────────────┐
                    │       PAYROLL_PROCESSOR        │
                    └───────────────┬─────────────────┘
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          │                         │                         │
          ▼                         ▼                         ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ READ_EMPLOYEE   │      │ CALCULATE_PAY   │      │ GENERATE_REPORT │
│    DATA         │      │    COMPONENTS   │      │                 │
└────────┬────────┘      └────────┬────────┘      └────────┬────────┘
         │                        │                        │
    ┌────┴────┐             ┌─────┴─────┐            ┌────┴────┐
    ▼         ▼             ▼    ▼    ▼            ▼         ▼
┌───────┐ ┌───────┐   ┌─────────┐ ┌────────┐  ┌──────────┐ ┌──────────┐
│READ_  │ │VALID- │   │CALC_    │ │CALC_   │  │PRINT_    │ │PRINT_    │
│BASIC  │ │ATE_ID │   │HRA      │ │PF      │  │PAY_SLIP  │ │SUMMARY   │
└───────┘ └───────┘   └─────────┘ └────────┘  └──────────┘ └──────────┘
                              │    │
                              ▼    ▼
                        ┌─────────┐ ┌─────────┐
                        │CALC_    │ │CALC_    │
                        │DA       │ │INCOME_TAX│
                        └─────────┘ └─────────┘
```

#### Implementation (Java-like Pseudocode)

```java
public class PayrollProcessor {
    private ReadEmployeeData empReader;
    private CalculatePayComponents calculator;
    private GenerateReport reportGenerator;
    
    public void processPayroll(List<Employee> employees) {
        for (Employee emp : employees) {
            // Transform: Read → Calculate → Generate
            EmployeeData data = empReader.readBasicData(emp.getId());
            empReader.validateEmployee(data);
            
            PayComponents components = new PayComponents();
            components.setBasic(data.getBasicSalary());
            components.setHRA(calculator.calculateHRA(data.getBasicSalary()));
            components.setDA(calculator.calculateDA(data.getBasicSalary()));
            components.setPF(calculator.calculatePF(data.getBasicSalary()));
            components.setTax(calculator.calculateIncomeTax(data));
            
            double netPay = calculator.calculateNetPay(components);
            
            reportGenerator.printPaySlip(emp, components, netPay);
        }
        reportGenerator.printSummary();
    }
}

class CalculatePayComponents {
    public double calculateHRA(double basic) {
        return basic * 0.10; // 10% HRA
    }
    
    public double calculateDA(double basic) {
        return basic * 0.08; // 8% DA
    }
    
    public double calculatePF(double basic) {
        return basic * 0.12; // 12% PF contribution
    }
    
    public double calculateNetPay(PayComponents comp) {
        return comp.getBasic() + comp.getHRA() + comp.getDA() 
               - comp.getPF() - comp.getTax();
    }
}
```

---

## 10. Comparison with Other Design Tools

| Aspect | Structure Chart | DFD | UML Class Diagram |
|--------|-----------------|-----|-------------------|
| **Focus** | Module hierarchy | Data flow | Object relationships |
| **Abstraction** | High-level | Process-oriented | Object-oriented |
| **Use Case** | Architectural design | Requirements analysis | Object design |
| **Notation** | Boxes and arrows | Circles and arrows | Classes and connectors |
| **Evolution** | Static structure | Dynamic processes | Dynamic + static |

---

## 11. Key Takeaways

1. **Structure Charts** provide a hierarchical view of system modularity, essential for top-down design
2. **Module types** include transform modules (input-process-output), transaction modules (dispatching), and coordination modules (workflow management)
3. **Fan-out** should be kept ≤7; **Fan-in** should be maximized for module reuse
4. **Data coupling** (passing parameters) is preferred over control coupling (passing flags)
5. **Functional cohesion** (single, well-defined purpose) is the highest quality cohesion type
6. Structure charts should be balanced with corresponding DFDs during design
7. Advanced notation includes libraries, conditional/iterative invocation, and physical module boundaries
8. Real-world applications span legacy systems, enterprise applications, and embedded systems

---

## 12. Challenging MCQs

```json
{
  "mcqs": [
    {
      "question": "In a structure chart, a module with fan-out of 12 is considered problematic because:",
      "options": [
        "It violates the single exit principle",
        "It exceeds the recommended fan-out limit of 7, increasing complexity",
        "It indicates high cohesion in the module",
        "It means the module is receiving too much data input"
      ],
      "correct_answer": 1,
      "explanation": "According to Yourdon's design guidelines, a module should directly control no more than 7 sub-modules. High fan-out increases complexity and maintenance difficulty."
    },
    {
      "question": "Which type of coupling involves one module passing control flags to influence the execution of another module?",
      "options": [
        "Data Coupling",
        "Control Coupling",
        "Stamp Coupling",
        "Common Coupling"
      ],
      "correct_answer": 1,
      "explanation": "Control coupling occurs when one module passes control information (flags, switches, operation codes) to another module to influence its internal logic."
    },
    {
      "question": "A module that analyzes input and routes to appropriate processing paths based on transaction type is called a:",
      "options": [
        "Transform Module",
        "Transaction Module",
        "Coordination Module",
        "Interface Module"
      ],
      "correct_answer": 1,
      "explanation": "Transaction modules implement dispatching logic, analyzing input and directing flow to appropriate processing paths based on transaction type."
    },
    {
      "question": "In structure chart terminology, 'fan-in' refers to:",
      "options": [
        "The depth of the module hierarchy",
        "The number of modules that call a particular module",
        "The number of parameters passed to a module",
        "The complexity of a module's internal logic"
      ],
      "correct_answer": 1,
      "explanation": "Fan-in measures how many modules invoke or call a particular module. High fan-in indicates good module reuse."
    },
    {
      "question": "Which cohesion type represents the highest quality (most desirable)?",
      "options": [
        "Procedural Cohesion",
        "Communicational Cohesion",
        "Functional Cohesion",
        "Logical Cohesion"
      ],
      "correct_answer": 2,
      "explanation": "Functional cohesion is the highest quality where all elements in a module contribute to a single, well-defined purpose or function."
    },
    {
      "question": "In structure chart notation, data couples are represented by:",
      "options": [
        "Hollow arrowheads",
        "Filled (solid) arrowheads",
        "Dashed lines",
        "Diamond shapes"
      ],
      "correct_answer": 1,
      "explanation": "Data couples (actual data elements passed between modules) are represented by arrows with filled/solid arrowheads, while control flags use hollow arrowheads."
    },
    {
      "question": "A 'balanced' structure chart refers to:",
      "options": [
        "Equal fan-in and fan-out values",
        "Correspondence between DFD and structure chart elements",
        "Symmetrical tree structure",
        "Modules with similar complexity"
      ],
      "correct_answer": 1,
      "explanation": "Balancing means ensuring that the structure chart accurately reflects the processes and data flows shown in the corresponding Data Flow Diagram."
    },
    {
      "question": "Content coupling (tightest coupling) occurs when:",
      "options": [
        "Modules share global data",
        "One module directly modifies another module's internal code",
        "Modules communicate via parameters only",
        "Modules share composite data structures"
      ],
      "correct_answer": 1,
      "explanation": "Content coupling is the worst form where one module directly references or modifies another module's internal code, data, or control flow."
    },
    {
      "question": "Which module type performs no actual data transformation but orchestrates subordinate modules?",
      "options": [
        "Transform Module",
        "Transaction Module",
        "Coordination Module",
        "Utility Module"
      ],
      "correct_answer": 2,
      "explanation": "Coordination modules manage workflow and sequence of subordinate modules but do not perform actual data transformation themselves."
    },
    {
      "question": "The recommended depth of a structure chart hierarchy should generally be:",
      "options": [
        "Very shallow (2-3 levels)",
        "Very deep (10+ levels)",
        "Moderately deep with controlled width",
        "Depth does not matter"
      ],
      "correct_answer": 2,
      "explanation": "A moderately deep hierarchy with fewer modules at each level is preferred over very shallow or very deep structures."
    }
  ]
}
```

---

## 13. Comprehensive Flashcards

```json
{
  "flashcards": [
    {
      "term": "Structure Chart",
      "definition": "A hierarchical diagram representing the modular structure of a software system, showing relationships between modules, control flow, and data communication."
    },
    {
      "term": "Module",
      "definition": "A logically grouped set of program statements that performs a specific function. Represented as a rectangle in structure charts."
    },
    {
      "term": "Fan-out",
      "definition": "The number of modules directly controlled by a given module. Recommended to be ≤7 for maintainability."
    },
    {
      "term": "Fan-in",
      "definition": "The number of modules that invoke or call a particular module. Higher fan-in indicates better module reuse."
    },
    {
      "term": "Data Coupling",
      "definition": "The best form of coupling where modules communicate by passing data parameters only (no control information)."
    },
    {
      "term": "Control Coupling",
      "definition": "Moderate coupling where one module passes control flags to influence the execution logic of another module."
    },
    {
      "term": "Transform Module",
      "definition": "A module that accepts input, transforms/processes it, and produces output (input-process-output pattern)."
    },
    {
      "term": "Transaction Module",
      "definition": "A module that analyzes input and dispatches to appropriate processing paths based on transaction type."
    },
    {
      "term": "Coordination Module",
      "definition": "A module that orchestrates the execution of subordinate modules without performing actual data transformation."
    },
    {
      "term": "Data Couple",
      "definition": "A data element passed between modules, represented by an arrow with a filled/solid arrowhead."
    },
    {
      "term": "Control Flag",
      "definition": "Control information passed between modules to influence execution, represented by an arrow with a hollow arrowhead."
    },
    {
      "term": "Functional Cohesion",
      "definition": "The highest quality cohesion where all elements within a module contribute to a single, well-defined purpose."
    },
    {
      "term": "Coincidental Cohesion",
      "definition": "The worst form of cohesion where elements are randomly grouped without logical relationship."
    },
    {
      "term": "Content Coupling",
      "definition": "The tightest (worst) form of coupling where one module directly modifies or references another module's internal code."
    },
    {
      "term": "Balancing",
      "definition": "The process of ensuring correspondence between elements in a DFD and the structure chart during design."
    },
    {
      "term": "Module Specification",
      "definition": "Documentation describing a module's purpose, input/output parameters, interfaces, and internal logic."
    },
    {
      "term": "Physical Module",
      "definition": "An actual program file, subroutine, or component that can be executed independently."
    },
    {
      "term": "Logic Module",
      "definition": "An abstract grouping of modules that represents a conceptual organization without physical existence."
    },
    {
      "term": "Abstraction",
      "definition": "The process of hiding implementation details while exposing only essential features of a module."
    },
    {
      "term": "Information Hiding",
      "definition": "Design principle where modules encapsulate their implementation details and expose only necessary interfaces."
    },
    {
      "term": "Scope of Control",
      "definition": "The principle that a module should control all its subordinate/child modules in the hierarchy."
    }
  ]
}
```

---

*Study Material prepared for Delhi University BSc (Hons) Computer Science (NEP 2024 UGCF) - Software Engineering Course*