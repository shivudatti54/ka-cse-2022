# 5 Design Verilog HDL to implement Decimal adder

=====================================

## Table of Contents

---

1. [Introduction](#introduction)
2. [Decimal Adder Basics](#decimal-adder-basics)
3. [Verilog HDL Implementation](#verilog-hdl-implementation)
4. [Example Design](#example-design)
5. [Key Concepts](#key-concepts)

## Introduction

---

A decimal adder is a digital circuit that adds two decimal numbers. It is a crucial component in various digital systems, including calculators and computers. In this study material, we will explore the basics of decimal adder design and implement it using Verilog HDL.

## Decimal Adder Basics

---

A decimal adder consists of the following components:

- **Full Adder (FA):** A full adder is a basic digital circuit that adds three bits: two input bits and a carry-in bit. It produces an output bit and a carry-out bit.
- **Half Adder (HA):** A half adder is a digital circuit that adds two bits. It produces an output bit and a carry-out bit.
- **Decimal Adder:** A decimal adder is a combination of half adders and full adders that adds two decimal numbers.

## Verilog HDL Implementation

---

We will implement a decimal adder using Verilog HDL. The design consists of the following components:

- **Full Adder (FA):**
  ```
  // Full Adder
  module fa(a, b, c, sum, carry_out);
      input a, b, c;
      output sum, carry_out;
      assign sum = (a == 1) ? (b == 1) ? 1 : (c == 1) ? 1 : 0 : (a == 1) ? 1 : 0;
      assign carry_out = (a == 1) ? (b == 1 && c == 1) ? 1 : (a == 1) ? 1 : 0;
  endmodule
  ```
- **Half Adder (HA):**
  ```
  // Half Adder
  module ha(a, b, sum, carry_out);
      input a, b;
      output sum, carry_out;
      assign sum = (a == 1) ? (b == 1) ? 1 : 0 : 0;
      assign carry_out = (a == 1) ? (b == 1) ? 1 : 0;
  endmodule
  ```

## Example Design

---

We will implement a decimal adder that adds the numbers 12 and 25.

```
// Decimal Adder
module decimal_adder(a, b, sum, carry_out);
    input a, b;
    output sum, carry_out;
    assign sum = 0;
    assign carry_out = 0;

    // Half Adder for decimal 12 (00010000)
    ha ha_12(a[3], a[2], sum[3], carry_12);
    // Full Adder for decimal 12 (00010000)
    fa fa_12(carry_12, b[3], sum[3], sum[2], carry_12);
    // Half Adder for decimal 12 (00010000)
    ha ha_12(carry_12, b[2], sum[3], carry_12);
    // Full Adder for decimal 12 (00010000)
    fa fa_12(carry_12, b[1], sum[2], sum[1], carry_12);

    // Half Adder for decimal 25 (01010101)
    ha ha_25(a[3], b[3], sum[3], carry_25);
    // Full Adder for decimal 25 (01010101)
    fa fa_25(carry_25, b[2], sum[3], sum[2], carry_25);
    // Half Adder for decimal 25 (01010101)
    ha ha_25(carry_25, b[1], sum[3], carry_25);
    // Full Adder for decimal 25 (01010101)
    fa fa_25(carry_25, b[0], sum[2], sum[1], carry_25);
    // Half Adder for decimal 25 (01010101)
    ha ha_25(carry_25, b[0], sum[3], carry_25);
    // Full Adder for decimal 25 (01010101)
    fa fa_25(carry_25, 1, sum[2], sum[0], carry_25);

endmodule
```

## Key Concepts

---

- **Full Adder (FA):** A full adder is a digital circuit that adds three bits: two input bits and a carry-in bit.
- **Half Adder (HA):** A half adder is a digital circuit that adds two bits.
- **Decimal Adder:** A decimal adder is a combination of half adders and full adders that adds two decimal numbers.
- **Verilog HDL:** Verilog HDL is a hardware description language used to design digital circuits.
- **Module:** A module is a reusable block of Verilog code that can be instantiated in a design.
- **Instantiation:** Instantiation is the process of creating an instance of a module in a design.

By understanding these key concepts and implementing a decimal adder using Verilog HDL, you can design complex digital systems and understand the basics of digital circuit design.
