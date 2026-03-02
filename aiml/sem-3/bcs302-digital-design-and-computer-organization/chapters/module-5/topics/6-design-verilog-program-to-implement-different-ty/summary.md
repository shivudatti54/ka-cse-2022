# 6 Design Verilog Programs for Multiplexers

==============================================

## Introduction

---

Multiplexers are digital circuits that select one of several input signals to send to the output. A 2:1 multiplexer is a basic multiplexer that selects one of two input signals.

## Types of Multiplexers

---

- **2:1 Multiplexer**: Selects one of two input signals.
- **3:1 Multiplexer**: Selects one of three input signals.
- **4:1 Multiplexer**: Selects one of four input signals.

## Verilog Programs

---

### 2:1 Multiplexer

- **Truth Table**:
  - A, B: Input signals
  - S: Select signal
  - Z: Output
    | S | A | B | Z |
    | --- | --- | --- | --- |
    | 0 | 0 | 0 | B |
    | 0 | 0 | 1 | A |
    | 0 | 1 | 0 | A |
    | 0 | 1 | 1 | Z |
    | 1 | 0 | 0 | Z |
    | 1 | 0 | 1 | B |
    | 1 | 1 | 0 | B |
    | 1 | 1 | 1 | Z |
- **Verilog Code**:
  ```verilog
  module mux2_1(A, B, S, Z);
  input A, B;
  input S;
  output Z;

      assign Z = ((S == 0) ? B : (S == 1) ? A : (A && B));

  endmodule

````
*   **Logic Formula**:
    Z = (S \* B) + ((~S) \* A)

### 3:1 Multiplexer

*   **Truth Table**:
    *   A, B, C: Input signals
    *   S: Select signal
    *   Y: Output
    | S | A | B | C | Y |
    | --- | --- | --- | --- | --- |
    | 0 | 0 | 0 | 0 | B |
    | 0 | 0 | 0 | 1 | C |
    | 0 | 0 | 1 | 0 | B |
    | 0 | 0 | 1 | 1 | C |
    | 1 | 0 | 0 | 0 | A |
    | 1 | 0 | 0 | 1 | C |
    | 1 | 0 | 1 | 0 | A |
    | 1 | 0 | 1 | 1 | C |
    | 1 | 1 | 0 | 0 | A |
    | 1 | 1 | 0 | 1 | C |
    | 1 | 1 | 1 | 0 | A |
    | 1 | 1 | 1 | 1 | C |
*   **Verilog Code**:
    ```verilog
module mux3_1(A, B, C, S, Y);
    input A, B, C;
    input S;
    output Y;

    assign Y = ((S == 0) ? B : (S == 1) ? C : (S == 2) ? A : (A && (S == 3)));
endmodule
````

- **Logic Formula**:
  Y = (S \* B) + ((~S) \* C) + ((~S) \* (S == 2) \* A) + ((~S) \* (S == 3) \* (A && B))

### 4:1 Multiplexer

- **Truth Table**:
  - A, B, C, D: Input signals
  - S: Select signal
  - Y: Output
    | S | A | B | C | D | Y |
    | --- | --- | --- | --- | --- | --- |
    | 0 | 0 | 0 | 0 | 0 | B |
    | 0 | 0 | 0 | 0 | 1 | C |
    | 0 | 0 | 0 | 1 | 0 | C |
    | 0 | 0 | 0 | 1 | 1 | D |
    | 0 | 0 | 1 | 0 | 0 | B |
    | 0 | 0 | 1 | 0 | 1 | C |
    | 0 | 0 | 1 | 1 | 0 | C |
    | 0 | 0 | 1 | 1 | 1 | D |
    | 0 | 1 | 0 | 0 | 0 | B |
    | 0 | 1 | 0 | 0 | 1 | C |
    | 0 | 1 | 0 | 1 | 0 | C |
    | 0 | 1 | 0 | 1 | 1 | D |
    | 0 | 1 | 1 | 0 | 0 | B |
    | 0 | 1 | 1 | 0 | 1 | C |
    | 0 | 1 | 1 | 1 | 0 | C |
    | 0 | 1 | 1 | 1 | 1 | D |
    | 1 | 0 | 0 | 0 | 0 | A |
    | 1 | 0 | 0 | 0 | 1 | C |
    | 1 | 0 | 0 | 1 | 0 | A |
    | 1 | 0 | 0 | 1 | 1 | D |
    | 1 | 0 | 1 | 0 | 0 | A |
    | 1 | 0 | 1 | 0 | 1 | C |
    | 1 | 0 | 1 | 1 | 0 | A |
    | 1 | 0 | 1 | 1 | 1 | D |
    | 1 | 1 | 0 | 0 | 0 | A |
    | 1 | 1 | 0 | 0 | 1 | C |
    | 1 | 1 | 0 | 1 | 0 | A |
    | 1 | 1 | 0 | 1 | 1 | D |
    | 1 | 1 | 1 | 0 | 0 | A |
    | 1 | 1 | 1 | 0 | 1 | C |
    | 1 | 1 | 1 | 1 | 0 | A |
    | 1 | 1 | 1 | 1 | 1 | D |
- **Verilog Code**:
  ```verilog
  module mux4_1(A, B, C, D, S, Y);
  input A, B, C, D;
  input S;
  output Y;

      assign Y = ((S == 0) ? B : (S == 1) ? C : (S == 2) ? D : (S == 3) ? A : (S == 4) ? (B && (C && D)) : (A && (C && D)));

  endmodule

```
*   **Logic Formula**:
    Y = (S \* B) + ((~S) \* C) + ((~S) \* (S == 2) \* D) + ((~S) \* (S == 3) \* A) + ((~S) \* (S == 4) \* (B && C && D)) + ((~S) \* (S == 4) \* (A && C && D))

## Key Points
-------------

*   **Truth Tables**: Used to determine the output of a multiplexer based on input signals.
*   **Verilog Code**: Used to implement multiplexers using Verilog programming language.
*   **Logic Formulas**: Used to simplify the Verilog code and improve performance.

## Important Formulas, Definitions, and Theorems
----------------------------------------------

*   **Multiplexer Formula**: Z = (S \* B) + ((~S) \* A)
*   **Multiplexer Truth Table**: Used to determine the output of a multiplexer based on input signals.
*   **Verilog Programming Language**: Used to implement multiplexers and other digital circuits.
```
