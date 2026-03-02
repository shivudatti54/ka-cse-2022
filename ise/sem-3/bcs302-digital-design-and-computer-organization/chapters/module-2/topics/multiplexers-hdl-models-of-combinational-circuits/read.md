verilog
module FullAdder (
input wire A, B, Cin,
output wire S, Cout
);
// Dataflow modeling using continuous assignments
assign S = A ^ B ^ Cin;
assign Cout = (A & B) | (Cin & (A ^ B));
endmodule
