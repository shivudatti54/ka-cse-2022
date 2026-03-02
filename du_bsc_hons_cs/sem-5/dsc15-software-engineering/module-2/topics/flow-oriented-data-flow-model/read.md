# Flow-Oriented Data Flow Model: Comprehensive Study Material

## Software Engineering | BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

### What is the Flow-Oriented Data Flow Model?

The **Flow-Oriented Data Flow Model** (DFD) is a graphical representation technique used in software engineering to visualize how data moves through a system. Unlike structure-oriented models that focus on program structure, DFD emphasizes the **flow of information** and **transformation processes** within a system. This model is fundamental to the **Structured Systems Analysis and Design Methodology (SSADM)** and remains a critical skill for software engineers, business analysts, and system designers.

### Why This Topic Matters in Real World

In today's software development landscape, understanding how data moves through business processes is essential:

- **Banking Systems**: When you transfer money, DFD helps visualize the flow from your account → validation process → recipient's account → confirmation
- **E-Commerce Platforms**: Order processing involves multiple data flows between customers, payment gateways, inventory systems, and shipping departments
- **Hospital Management Systems**: Patient records flow between registration, diagnosis, pharmacy, and billing modules
- **University Administration**: Student enrollment data flows through admission → examination → grade recording → certificate generation

For **Delhi University CS students**, DFD questions frequently appear in Software Engineering papers (Paper Code: CSCI-302), making this a high-weightage topic in your examinations.

---

## 2. Understanding Data Flow Diagrams (DFDs)

### Definition

A **Data Flow Diagram (DFD)** is a hierarchical graphical representation that depicts:
- External entities that interact with the system
- Processes that transform data
- Data stores where information is kept
- Data flows that connect these elements

### Key Characteristics of Flow-Oriented Model

| Characteristic | Description |
|----------------|-------------|
| **Function-Oriented** | Emphasizes what happens to data, not how it happens |
| **Top-Down Decomposition** | Complex systems are broken into manageable levels |
| **Symbolic Representation** | Uses standard symbols to represent system components |
| **Logical Design** | Represents business functions, not physical implementation |

---

## 3. Components of DFD

A DFD consists of four fundamental building blocks:

### 3.1 External Entity (External Agent)

Represents people, organizations, or systems outside the system being modeled.

- **Symbol (Gane-Sarson)**: Square or rectangle with rounded corners
- **Symbol (Yourdon)**: Rectangle with two vertical lines on each side
- **Also called**: Source, Sink, Terminator, External Actor
- **Example**: Customer, Bank, Government Agency, Supplier

### 3.2 Process

Represents a transformation of data or a business function that converts input to output.

- **Symbol (Gane-Sarson)**: Rounded rectangle (bubble/circle)
- **Symbol (Yourdon)**: Circle (bubble) with process name inside
- **Must have**: At least one input and one output
- **Example**: "Calculate Total", "Validate Order", "Generate Invoice"

### 3.3 Data Store

Represents a repository of data that is stored for later use.

- **Symbol (Gane-Sarson)**: Open-ended rectangle (horizontal lines on both ends)
- **Symbol (Yourdon)**: Open rectangle (parallel lines on left and right)
- **Also called**: File, Database, Repository
- **Example**: "Customer Database", "Order History", "Inventory File"

### 3.4 Data Flow

Represents the movement of data between components.

- **Symbol**: Arrow showing direction of data movement
- **Must connect**: Two components (never connects two external entities directly without a process)
- **Example**: "Order Details", "Payment Confirmation", "Student Report"

---

## 4. DFD Levels: Context Diagram to Level 2

The hierarchical decomposition of DFDs follows a specific pattern:

### 4.1 Context Diagram (Level 0)

- Shows the **entire system as a single process**
- Shows all **external entities** and their **data flows** to/from the system
- **No data stores** are shown at this level
- Also called **Context Level Diagram** or **Level 0 DFD**
- There is only **one process** representing the whole system

**Example Context Diagram:**

```
                    ┌─────────────┐
    Customer ──────►│             │
                    │   SYSTEM    │◄──── Supplier
    Manager  ──────►│             │◄──── Bank
                    └─────────────┘
```

### 4.2 Level 1 DFD

- Decomposes the single process from Context Diagram into **major processes**
- Shows **data stores** that are essential to the system
- Typically contains **7 ± 2 processes** (for manageability)
- All data flows entering/exiting the context diagram must appear in Level 1

**Example Level 1 DFD for an Order Processing System:**

```
    Customer ──►[1.0 Receive Order]────►[D1: Order File]
                      │                        │
                      ▼                        ▼
              [2.0 Validate]─────────────►[3.0 Process Payment]
              [D2: Customer File]              │
                      │                        ▼
                      └─────────────────►[4.0 Dispatch Order]──► Customer
```

### 4.3 Level 2 DFD

- Decomposes each major process from Level 1 into **sub-processes**
- Shows **more detailed data flows** and additional data stores
- Must maintain **balance** with parent Level 1 process (all inputs/outputs must be preserved)
- Provides the most detailed view before moving to design

**Example: Decomposing Process 2.0 (Validate Order) into Level 2:**

```
    Order ──►[2.1 Check Format]────►[2.2 Verify Customer ID]
                   │                        │
                   └────────────────┬───────┘
                                    ▼
                           [2.3 Check Credit Limit]──► Validated Order
```

---

## 5. Notation Systems: Gane-Sarson vs Yourdon

Delhi University exams often test your knowledge of different DFD notations. Understanding both systems is crucial.

### Comparison Table

| Element | Gane-Sarson | Yourdon |
|---------|-------------|---------|
| **Process** | Rounded Rectangle | Circle (Bubble) |
| **Data Store** | Open-ended Rectangle | Rectangle with parallel lines |
| **External Entity** | Square (rounded corners) | Rectangle with double vertical lines |
| **Data Flow** | Arrow with label | Arrow with label |
| **Originator** | Chris Gane & Trish Sarson | Edward Yourdon |
| **Usage** | More common in business analysis | Popular in academic curricula |

### Visual Representation

**Gane-Sarson Notation:**
```
┌───────┐     ╔═══════╗     ╠═══════╣     ════════►
│ Entity│────►║Process║────►║D.Store║────►Data Flow
└───────┘     ╚═══════╝     ╠═══════╣
```

**Yourdon Notation:**
```
┌───────┐      ○          ╔═══════╗      ════════►
│ Entity│──────Process────║D.Store║──────Data Flow
└───────┘      ○          ╚═══════╝
```

### Which Notation to Use?

- **Delhi University Syllabus**: Yourdon notation is more commonly taught, but both are acceptable
- **Industry**: Gane-Sarson is more prevalent in modern business analysis
- **Exam Tip**: Be consistent throughout your answer—never mix notations

---

## 6. DFD Rules, Balancing, and Numbering

### 6.1 Construction Rules

**Must Follow:**
1. Every process must have at least one input and one output
2. Data cannot flow between two external entities directly
3. Data cannot flow from a data store back to the same data store without processing
4. Every data flow must connect to at least one process
5. External entities can be connected to processes via data flows
6. Data stores can only connect to processes (not external entities directly)

**Common Errors to Avoid:**
- **Black Hole**: Process with inputs but no outputs
- **Miracle**: Process with outputs but no inputs
- **Gray Hole**: Process with outputs that seem insufficient for the inputs

### 6.2 Balancing

**Balancing** ensures that parent and child DFD levels are consistent. The principle: **All data flows entering/exiting a parent process must be preserved in its child diagram**.

**Rules:**
- Level 1 DFD must include all external entities from Context Diagram
- All data flows into/out of a process in Level 1 must appear in Level 2 decomposition
- Data stores can be added in child levels but cannot remove existing connections

**Example of Balancing:**

*Level 1 Process 2.0 has:*
- Input: Customer Order
- Output: Validated Order, Error Report

*Level 2 (decomposition of 2.0) must have:*
- Same input: Customer Order
- Same outputs: Validated Order, Error Report

### 6.3 Numbering System

Systematic numbering helps track processes across levels:

| Level | Numbering Example | Meaning |
|-------|-------------------|---------|
| Context | 0 or System | Single process representing whole system |
| Level 1 | 1.0, 2.0, 3.0 | Major processes |
| Level 2 | 1.1, 1.2, 1.3 | Sub-processes of Process 1 |
| Level 3 | 1.1.1, 1.1.2 | Further decomposition (rarely used) |

---

## 7. Concrete Examples with Diagrams

### Example 1: Library Management System

**Context Diagram:**
```
         ┌──────────────────┐
         │                  │
Member ──►│                  │◄── Librarian
         │  LIBRARY         │
Book   ──►│  MANAGEMENT     │◄── Supplier
         │  SYSTEM          │
         │                  │
         └──────────────────┘
              ▲      │
              │      ▼
         Return/Issue
```

**Level 1 DFD:**

```
Member ──►[1.0 Member]───►[D1: Member]──┐
         Registration                   │
                                         ▼
              ┌────────────────────[2.0 Book]───►[D2: Book Inventory]
              │                         │
Book Info ◄──┘                         │
                                         ▼
              ┌────────────────────[3.0 Transaction]───►[D3: Issue Record]
              │                              │
              │   Returned ◄────────────────┘
              │
              ▼
[4.0 Reports]───► Librarian
```

**Level 2 DFD for Process 3.0 (Transaction):**

```
Issue Request ──►[3.1 Check Availability]───►[3.2 Update Inventory]
                         │                        │
                         │                   [D2: Book Inventory]
                         ▼
                  [3.3 Record Issue]───►[D3: Issue Record]───► Issue Slip
                         │
                         └───────────────────────► Member
```

### Example 2: ATM Banking System

**Level 1 DFD:**

```
Customer ──►[1.0 Validate]────────────►[D1: Customer PIN DB]
            Card Details                   │
                    │                       ▼
                    │              [2.0 Process Request]
                    │                       │
         ◄──────────┴───────────────────────┤
         │                    Account Info  │
         ▼                                   ▼
[3.0 Dispense Cash]◄───[D2: Transaction Log]───►[4.0 Generate Receipt]
       │                                          │
       └───────────────────► Customer ◄───────────┘
```

**Code Representation (Pseudo-code for Process 2.0):**

```python
# Process 2.0: Process Request
def process_request(transaction_type, account_number, amount):
    """
    Transforms input data to perform banking operations
    """
    # Input: transaction_type, account_number, amount
    
    # Validate account exists
    account = get_account(account_number)
    if not account:
        return "ERROR: Invalid Account"
    
    # Perform transaction based on type
    if transaction_type == "WITHDRAW":
        if account.balance >= amount:
            account.balance -= amount
            log_transaction("WITHDRAWAL", account_number, amount)
            return "SUCCESS", amount
        else:
            return "ERROR: Insufficient Funds"
    
    elif transaction_type == "BALANCE":
        return "SUCCESS", account.balance
    
    # Output: transaction_result, amount/balance
```

---

## 8. Differences from Other Data Flow Models

| Aspect | Flow-Oriented DFD | Transform-Oriented | Transaction-Oriented |
|--------|-------------------|-------------------|---------------------|
| **Focus** | Data movement | Single input-output path | Multiple processing paths |
| **Use Case** | General business processes | Scientific/calculations | Menu-driven systems |
| **Decomposition** | By function | By transform analysis | By transaction types |
| **Example** | Order processing | Payroll calculation | ATM transactions |

---

## 9. Advantages and Limitations

### Advantages

1. **Communication Tool**: Easy to understand for stakeholders without technical background
2. **Hierarchical Structure**: Complex systems can be broken into manageable levels
3. **Technology Independent**: Represents logical design, not physical implementation
4. **Identifies Data Redundancy**: Highlights unnecessary data duplication
5. **Supports Reusability**: Common processes can be identified and reused

### Limitations

1. **No Control Flow**: Does not show the sequence of operations
2. **No Decision Logic**: Cannot represent conditional branches
3. **Can Become Complex**: Large systems generate many diagrams
4. **Version Control**: Difficult to maintain when changes occur
5. **Incomplete Picture**: Does not show system state or timing

---

## 10. Key Takeaways

1. **DFD Components**: Master the four elements—External Entity, Process, Data Store, Data Flow
2. **Notation Systems**: Know both Gane-Sarson and Yourdon symbols
3. **Hierarchy**: Context → Level 1 → Level 2 is the standard decomposition approach
4. **Balancing**: Child diagrams must preserve all inputs/outputs of parent processes
5. **Rules**: No direct flow between external entities, every process needs input/output
6. **Real-World Application**: Used extensively in banking, e-commerce, healthcare systems
7. **Delhi University Focus**: Expect questions on drawing diagrams, identifying errors, and notation differences

---

## 11. Higher-Order Assessment Questions

### Multiple Choice Questions (Application Level)

**Question 1:** In a DFD for an online examination system, the process "Evaluate Answer" has an input "Student Response" and outputs "Marks Awarded" and "Performance Report". What type of error exists if "Marks Awarded" is never used anywhere else in the system?

- a) Black Hole
- b) Gray Hole
- c) Miracle
- d) Unbalanced DFD

**Answer: b) Gray Hole** — The process produces output that appears unused, suggesting incomplete modeling.

---

**Question 2:** Which of the following data flows would be INVALID in a properly constructed DFD?

- a) External Entity → Process
- b) Process → Data Store
- c) Data Store → External Entity
- d) Process → Process

**Answer: c) Data Store → External Entity** — Data stores can only connect to processes, not directly to external entities.

---

**Question 3:** During the decomposition of a Level 1 process "Process Payment" into Level 2, you discover you need to add a new data store "Audit Log" that didn't exist in Level 1. This is:

- a) A violation of balancing rules
- b) Acceptable since new data stores can be added in child diagrams
- c) Not allowed unless approved by the client
- d) An error that requires redesigning Level 1

**Answer: b) Acceptable** — Child diagrams can add data stores as long as all parent inputs/outputs are preserved.

---

**Question 4:** Yourdon notation represents a process using:
- a) Rounded Rectangle
- b) Circle (Bubble)
- c) Rectangle with parallel lines
- d) Square

**Answer: b) Circle (Bubble)** — Yourdon uses circles for processes, while Gane-Sarson uses rounded rectangles.

---

**Question 5:** In the context of DFD decomposition, "balancing" refers to:

- a) Ensuring all data flows have equal input and output rates
- b) Maintaining consistency between parent and child diagrams
- c) Verifying that all data stores have read and write operations
- d) Checking that processes are evenly distributed across levels

**Answer: b) Maintaining consistency** — Balancing ensures parent process inputs/outputs are preserved in child diagrams.

---

### Short Answer Questions

**Question 6:** Draw a Context Diagram for an "Online Food Ordering System" showing at least 3 external entities and their data flows.

**Answer:** Students should draw:
- Customer (Entity) → System: Order Details
- Restaurant (Entity) ← System: Order Confirmation
- Delivery Partner (Entity) ← System: Delivery Instructions
- Payment Gateway (Entity) ↔ System: Payment Details

---

**Question 7:** Explain why DFDs cannot show loops or iteration, and suggest an alternative notation for representing such control flow.

**Answer:** DFDs are flow-oriented but not control-oriented—they show data transformation, not execution sequence. For loops/iteration, use Flowcharts or Structured English.

---

**Question 8:** A student drew a DFD where "Student" entity sends "Application Form" directly to "Admission Database" without any process. Identify the error and explain how to fix it.

**Answer:** This violates DFD rules—data cannot flow directly from external entity to data store. The fix: Insert a process "Process Admission Application" between Student and Database.

---

## 12. Flashcards (Non-Redundant Content)

### Flashcard Set

| # | Term/Concept | Definition |
|---|--------------|------------|
| 1 | **Data Flow Diagram (DFD)** | A graphical representation showing how data moves through a system using processes, data stores, external entities, and data flows |
| 2 | **Context Diagram** | The highest-level DFD (Level 0) showing the entire system as a single process with all external entities |
| 3 | **Balancing** | The principle ensuring that child-level DFDs preserve all inputs and outputs of their parent process |
| 4 | **Black Hole Error** | A process that consumes inputs but produces no meaningful outputs |
| 5 | **Miracle Error** | A process that produces outputs without any inputs |
| 6 | **External Entity** | A person, organization, or system outside the system being modeled (source or destination of data) |
| 7 | **Data Store** | A repository of data that is stored for later use (file, database, table) |
| 8 | **Decomposition** | The top-down process of breaking down a complex system into simpler, more detailed levels |
| 9 | **Gane-Sarson Notation** | DFD notation using rounded rectangles for processes, open-ended rectangles for data stores, squares for entities |
| 10 | **Yourdon Notation** | DFD notation using circles for processes, rectangles with parallel lines for data stores |
| 11 | **Gray Hole Error** | A process where outputs seem insufficient for the inputs, suggesting incomplete modeling |
| 12 | **Level 1 DFD** | First decomposition level showing major processes of the system |
| 13 | **Data Flow** | The pathway by which data moves from one component to another |
| 14 | **Process** | A transformation that converts input data into output data |
| 15 | **SSADM** | Structured Systems Analysis and Design Methodology—a popular methodology using DFDs |

---

## 13. Examination Tips for Delhi University Students

### Preparation Strategy

1. **Know Both Notations**: Be comfortable drawing in both Gane-Sarson and Yourdon
2. **Practice Drawing**: Draw at least 3-4 complete DFD examples (Context → Level 1 → Level 2)
3. **Understand Balancing**: This is a frequently tested concept
4. **Memorize Rules**: Know all DFD construction rules and common errors
5. **Time Management**: In exams, spend 10-15 minutes per diagram question

### Common Exam Questions Pattern

- **5-mark question**: Draw Context Diagram for a given scenario
- **10-mark question**: Draw Level 1 and Level 2 DFDs
- **3-mark question**: Identify errors in a given DFD
- **2-mark question**: Differentiate between notation systems

### Answer Presentation

- Use proper symbols (consistent notation)
- Label all components clearly
- Show data flow direction with arrows
- Number processes systematically (1.0, 1.1, 1.2, etc.)
- Include brief explanations where required

### What Examiners Look For

- ✅ Correct use of symbols
- ✅ Proper labeling
- ✅ No rule violations
- ✅ Balanced decomposition
- ✅ Clean, readable diagram
- ✅ Logical process flow

---

## Conclusion

The Flow-Oriented Data Flow Model remains a fundamental skill for software engineers. This model bridges the gap between business requirements and technical design, enabling clear communication across all stakeholders. Mastery of DFDs—including notation differences, decomposition levels, balancing rules, and practical applications—will not only help you ace your Delhi University examinations but also prepare you for real-world systems analysis roles.

**Remember**: Practice drawing diagrams regularly, understand the underlying principles, and apply the rules consistently. Good luck with your examinations!