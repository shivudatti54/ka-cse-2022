verilog
    module half_adder(
        input A, B,
        output S, C_out
    );
        assign S = A ^ B;       // XOR operation for Sum
        assign C_out = A & B;   // AND operation for Carry
    endmodule