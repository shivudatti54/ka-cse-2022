# Design a 4-bit Full Adder and Subtractor using Basic Gates

### Definitions

- **Full Adder**: A digital circuit that adds two binary digits and a carry digit, producing a sum and a new carry digit.
- **Full Subtractor**: A digital circuit that subtracts one binary digit from two other binary digits and a borrow digit, producing a difference and a new borrow digit.
- **Binary Half Adder**: A digital circuit that adds two binary digits and produces a sum and a carry digit.
- **Binary Full Adder**: A digital circuit that adds two binary digits and a carry digit, producing a sum and a new carry digit.

### Key Formulas

- **Full Adder**: $A, B, C_{in}, S, C_{out} \Rightarrow A \oplus B \oplus C_{in} = S$ $A \cdot B \cdot \overline{C_{in}} = C_{out}$
- **Full Subtractor**: $A, B, C_{in}, S, C_{out} \Rightarrow A \oplus B \oplus C_{in} = S$ $A \cdot B \cdot \overline{C_{in}} = C_{out}$

### Theorems

- **Complement Law**: $\overline{A+B} = \overline{A} \cdot \overline{B}$
- **Distributive Law**: $A(B+C) = AB + AC$
- **De Morgan's Law**: $\overline{AB} = \overline{A} + \overline{B}$

### 4-bit Full Adder and Subtractor Design

- **4-bit Full Adder**: Use 4 2-bit Full Adders to implement a 4-bit Full Adder.
- **4-bit Full Subtractor**: Use 4 2-bit Full Adders and an inverter to implement a 4-bit Full Subtractor.

### Simulation using Basic Gates

- Use a combination of AND, OR, NOT, and XOR gates to simulate the 4-bit Full Adder and Subtractor.

### Important Gates

- **AND Gate**: Produces an output of 1 only if all inputs are 1.
- **OR Gate**: Produces an output of 1 if any input is 1.
- **NOT Gate**: Produces an output that is the opposite of the input.
- **XOR Gate**: Produces an output of 1 if the inputs are different.

### Implementation Steps

1.  Design the 4-bit Full Adder and Subtractor using the formulas and theorems above.
2.  Use a simulation tool to implement the 4-bit Full Adder and Subtractor using basic gates.
3.  Verify the functionality of the 4-bit Full Adder and Subtractor using truth tables.

### Key Points

- The 4-bit Full Adder and Subtractor can be designed using basic gates.
- The formulas and theorems above provide a framework for designing the 4-bit Full Adder and Subtractor.
- The simulation tool can be used to verify the functionality of the 4-bit Full Adder and Subtractor.
