# Combinational Logic: Revision Notes

=====================================

### Introduction

- Combinational Logic: A branch of digital electronics that deals with digital circuits that produce an output based on a combination of inputs.
- Combinational circuits: Digital circuits that do not have any feedback loops and produce an output based on the current input values.

### Combinational Circuits

- Types:
  - Series circuit: Multiple gates connected in series.
  - Parallel circuit: Multiple gates connected in parallel.
- Characteristics:
  - No feedback loop
  - Output depends on current input values

### Design Procedure

- Karnaugh map (K-map) method: A graphical method for simplifying digital circuits.
- Truth table method: A tabular method for analyzing digital circuits.
- Boolean algebra: A mathematical method for simplifying digital circuits.

### Binary Adder-Subtractor

- Types:
  - Binary full adder: A digital circuit that adds two binary numbers.
  - Binary full subtractor: A digital circuit that subtracts two binary numbers.
- Truth table:
  | A | B | Sum | Carry
  | --- | --- | --- | --- |
  | 0 | 0 | 0 | 0 |
  | 0 | 1 | 1 | 0 |
  | 1 | 0 | 1 | 0 |
  | 1 | 1 | 0 | 1 |

### Decoders

- Types:
  - Binary decoder: A digital circuit that decodes a binary number into a set of outputs.
- Truth table:
  | A3 | A2 | A1 | A0 | Output
  | --- | --- | --- | --- | --- |
  | 0 | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 1 | 1 |
  | ... | ... | ... | ... | ... |

### Encoders

- Types:
  - Binary encoder: A digital circuit that encodes a set of inputs into a binary number.
- Truth table:
  | A2 | A1 | A0 | Output
  | --- | --- | --- | --- |
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 1 | 1 |
  | ... | ... | ... | ... |

### Multiplexers

- Types:
  - Binary multiplexer: A digital circuit that selects one of several input signals and outputs the selected signal.
- Truth table:
  | A0 | A1 | Select | Output
  | --- | --- | --- | --- |
  | 0 | 0 | 0 | 0 |
  | 0 | 0 | 1 | 1 |
  | ... | ... | ... | ... |

### Important Formulas and Theorems

- Boolean algebra:
  - De Morgan's laws: $\overline{A \cdot B} = \overline{A} + \overline{B}$
  - Distributive laws: $A \cdot (B + C) = A \cdot B + A \cdot C$
- Karnaugh map:
  - Rules for simplifying digital circuits using K-map

Note: This summary provides a concise overview of the key points for the topic of Combinational Logic. It is intended to be a quick revision guide for exams.
