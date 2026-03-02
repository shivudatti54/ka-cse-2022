# **Designing Binary Adder-Subtractor in Verilog HDL**

## **Introduction**

In digital design, binary adder-subtractors are essential components used to perform arithmetic operations between two binary numbers. In this module, we will learn how to design and implement half and full adders using Verilog HDL, a hardware description language used to design digital circuits.

## **Definitions and Concepts**

- **Half Adder**: A half adder is a digital circuit that adds two binary digits (0 or 1) and produces a sum and a carry output.
- **Full Adder**: A full adder is a digital circuit that adds three binary digits (0, 1, and a carry input) and produces a sum, a carry output, and a borrow output.
- **Verilog HDL**: A hardware description language used to design digital circuits using a text-based language.

## **Half Adder Design in Verilog HDL**

### Half Adder Circuit Diagram

The half adder circuit diagram consists of two XOR gates (exclusive OR gates) and one AND gate.

### Verilog HDL Code for Half Adder

```verilog
module half_adder(a, b, sum, carry);
    input [1:0] a, b;
    output sum, carry;

    assign sum = a ^ b;
    assign carry = (a & b);

endmodule
```

### Explanation

- The `half_adder` module takes two input binary digits `a` and `b` and produces a sum and a carry output.
- The `sum` output is calculated using the XOR gate (`a ^ b`).
- The `carry` output is calculated using the AND gate (`a & b`).

## **Full Adder Design in Verilog HDL**

### Full Adder Circuit Diagram

The full adder circuit diagram consists of three XOR gates (exclusive OR gates), one AND gate, and one OR gate.

### Verilog HDL Code for Full Adder

```verilog
module full_adder(a, b, carry_in, sum, carry_out, borrow);
    input [1:0] a, b;
    input carry_in;
    output [1:0] sum;
    output carry_out;
    output borrow;

    assign sum = {a, b};
    assign carry_out = (a ^ b ^ carry_in);
    assign borrow = ((a & b) ^ (a & carry_in) ^ (b & carry_in));

endmodule
```

### Explanation

- The `full_adder` module takes three input binary digits `a`, `b`, and a carry input `carry_in` and produces a sum, a carry output, and a borrow output.
- The `sum` output is calculated by concatenating the two input binary digits (`{a, b}`).
- The `carry_out` output is calculated using the XOR gate (`a ^ b ^ carry_in`).
- The `borrow` output is calculated using the XOR gate (`((a & b) ^ (a & carry_in) ^ (b & carry_in)`).

## **Implementation and Simulation**

To implement and simulate the half and full adder designs, you can use a digital design tool such as ModelSim or Vivado. Here's an example of how to implement and simulate the half adder design using ModelSim:

```verilog
// Create a new project in ModelSim
create_project -force adder_project

// Create a new module for the half adder
create_module -force adder_half

// Copy the half adder Verilog code into the module
copy_file -force "half_adder.vhd" adder_half

// Create a new instance of the half adder module
create_instance -force half_instance adder_half/half_adder

// Set the input and output ports of the half adder instance
set_params -force half_instance.AIO [8'b0000]
set_params -force half_instance.BIO [8'b0000]
set_params -force half_instance.SUMO [8'b0000]
set_params -force half_instance.CARO [8'b0000]

// Create a new simulation for the half adder instance
create_simulation -force half_sim

// Run the simulation
run_simulation -force half_sim
```

This code creates a new project in ModelSim, creates a new module for the half adder, copies the half adder Verilog code into the module, creates a new instance of the half adder module, sets the input and output ports of the half adder instance, creates a new simulation for the half adder instance, and runs the simulation.

## **Conclusion**

In this module, we learned how to design and implement half and full adders using Verilog HDL. We also learned how to implement and simulate the designs using a digital design tool such as ModelSim. Understanding binary adder-subtractors is essential in digital design, and this module provided a comprehensive overview of the topic.
