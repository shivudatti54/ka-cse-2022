# Structure Charts — Quick Revision Summary

## Introduction
Structure Charts are a graphical notation tool in software engineering used for top-down design of modular systems. They represent the hierarchical relationships between modules (sub-systems) and are essential for structured design methodology, a key component of the Delhi University B.Sc. (Hons) Computer Science syllabus under Software Engineering (NEP 2024 UGCF).

---

## Key Concepts

### • Purpose & Use
- Represent system architecture from top-level to detailed design
- Show how large systems are broken into smaller, manageable modules
- Used in **structured analysis and design** (Yourdon methodology)
- Focus on **what** the system does, not **how** it does it

### • Main Components
- **Module**: Represents a subsystem or program unit
- **Data Coupling**: Information passed between modules
- **Control Coupling**: Information controlling module execution
- **Invocation Lines**: Connect parent modules to child modules

### • Types of Modules
- **Transform Modules**: Perform computations
- **Control Modules**: Coordinate other modules
- **Physical Modules**: Actual files or program units

### • Levels in Structure Charts
1. **Context Level (Level 0)**: Shows system as single module with external entities
2. **Level 1**: Major subsystems/summary level
3. **Level 2+**: Detailed decomposition of each subsystem

### • Symbols & Notation
- **Rectangle**: Represents a module
- **Arrows**: Show invocation/procedure calls
- **Data Symbols (open arrow)**: Data passed between modules
- **Control Symbols (filled arrow)**: Control information passed
- **Curved Arrow**: Loop/iteration indicator

### • Documentation Annotations
- **Frequency**: How often a module is called
- **Complexity**: Cognitive complexity measure
- **Shared Modules**: Modules used by multiple parents (diamond symbol)

---

## Advantages
- Easy to understand hierarchical design
- Shows module independence clearly
- Facilitates code generation from design
- Good communication tool between analysts and programmers

---

## Limitations
- Doesn't show sequence of operations
- Doesn't depict data structures
- Becomes complex for large systems

---

## Conclusion
Structure Charts are fundamental to structured design, enabling engineers to visualize system modularity and data flow. They remain essential for designing maintainable, modular software systems and are a must-know topic for the Software Engineering exam under Delhi University NEP 2024 syllabus.

---

*Reference: Delhi University B.Sc. (Hons) CS - Software Engineering (NEP 2024 UGCF)*