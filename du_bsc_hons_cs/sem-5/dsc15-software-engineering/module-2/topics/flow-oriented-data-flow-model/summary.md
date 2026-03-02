# Flow Oriented Data Flow Model

## Introduction
The Flow-Oriented Data Flow Model is a prominent **system analysis and design technique** that focuses on representing how data moves through a software system. It emphasizes the *functional transformation of data* rather than the control flow of programs. This model is extensively used during the **analysis phase** of the Software Development Life Cycle (SDLC) to capture system requirements in a graphical, easy-to-understand format. As per the Delhi University BSc (Hons) Computer Science (NEP 2024 UGCF) syllabus, this topic falls under **Software Engineering** and is essential for understanding system modeling techniques.

---

## Key Concepts

### **1. Data Flow Diagram (DFD)**
- A graphical representation showing how **data inputs** are transformed into **data outputs** through a series of processes
- Does not depict program logic or hardware details
- Complements other models like ER diagrams (which show data relationships)

### **2. DFD Components (Four Key Symbols)**
- **External Entity**: Source or destination of data (outside the system) — represented by a square
- **Process**: Transforms data, performs operations — represented by a circle/rounded rectangle
- **Data Store**: Where data is stored (files, database) — represented by an open-ended rectangle
- **Data Flow**: Movement of data between components — represented by arrows

### **3. DFD Levels**
- **Level 0 (Context Diagram)**: Shows the entire system as a single process with external entities
- **Level 1**: Breaks Level 0 into major processes (sub-systems)
- **Level 2+**: Further decomposition of processes for detailed understanding

### **4. DFD Rules**
- Process must have at least one input and one output
- Data cannot move directly between external entities
- Data cannot move directly between data stores
- Each process should have a meaningful name (verb phrase)
- Data stores can have inputs/outputs but cannot transform data

### **5. Advantages**
- Easy to understand for both technical and non-technical stakeholders
- Focuses on data movement, identifying bottlenecks
- Supports **top-down decomposition** for modular analysis
- Useful for **requirement gathering** and communication

### **6. Limitations**
- Does not show control flow (loops, decisions)
- Difficult to represent complex processes
- No indication of data structure or volume

---

## Exam Tips (Delhi University NEP 2024)

1. **Remember the four symbols** with their correct representations
2. **Difference between DFD and Flowchart**: DFD shows data flow; Flowchart shows control flow
3. **Context Diagram** is always Level 0 with a single process
4. **Balancing**: When decomposing DFDs, inputs/outputs must be preserved between levels

---

## Conclusion
The Flow-Oriented Data Flow Model is a fundamental tool in software engineering for visualizing system functionality from a data perspective. It bridges the gap between user requirements and system design, making it indispensable for the **Analysis and Design** phases of SDLC. Students should practice drawing DFDs for simple systems to master the technique.

---

*For detailed study, refer to: "Software Engineering" (Delhi University prescribed textbook)*