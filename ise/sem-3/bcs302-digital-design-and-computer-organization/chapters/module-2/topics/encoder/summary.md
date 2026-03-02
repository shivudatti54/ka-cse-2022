# Encoder - Summary

## Key Definitions and Concepts

- ENCODER: A combinational circuit that converts 2^n input lines into n output lines, producing binary code corresponding to the active input line

- BINARY ENCODER: Simple encoder where only ONE input can be active at a time; outputs binary representation of the active input index

- PRIORITY ENCODER: Encoder that handles multiple simultaneous inputs by establishing priority hierarchy; outputs code for highest-priority active input

- VALID BIT (V): Output signal in priority encoders indicating whether a valid input is present (V=1 for valid, V=0 when all inputs are zero)

## Important Formulas and Theorems

For an 8-to-3 binary encoder:
- Y2 = I4 + I5 + I6 + I7
- Y1 = I2 + I3 + I6 + I7  
- Y0 = I1 + I3 + I5 + I7

For a 4-to-2 binary encoder:
- Y0 = I1 + I3
- Y1 = I2 + I3

## Key Points

- Encoders perform the inverse function of decoders: fewer output lines from more input lines

- Binary encoders require exactly one active input; ambiguous output results if multiple inputs are HIGH

- Priority encoders resolve multiple active inputs using priority (typically highest-index input wins)

- The 74LS148 is an 8-to-3 line priority encoder IC; 74LS147 is a 10-to-4 line decimal to BCD priority encoder

- Standard encoder outputs include a valid bit to indicate presence of at least one active input

- Encoders are used in keyboards, address encoding, and parallel-to-serial conversion

- Cascading priority encoders requires using enable input (EI) and enable output (EO) pins

## Common Mistakes to Avoid

- CONFUSING ENCODERS WITH DECODERS: Remember encoders have MORE inputs than outputs; decoders have MORE outputs than inputs

- IGNORING THE PRIORITY MECHANISM: In priority encoders, the highest-priority input always wins regardless of other active inputs

- FORGETTING THE VALID BIT: Output is meaningless when V=0 in priority encoders; don't assume output is correct when no inputs are active

- NOT UNDERSTANDING DON'T CARE CONDITIONS: In truth tables, X means the output can be either 0 or 1 since those input combinations cannot occur

## Revision Tips

1. PRACTICE TRUTH TABLE derivations for different encoder types until you can write them from memory

2. MEMORIZE THE BOOLEAN expressions for basic encoders (4-to-2 and 8-to-3) as they frequently appear in exams

3. DRAW CIRCUIT DIAGRAMS repeatedly for both binary and priority encoders to reinforce gate-level understanding

4. UNDERSTAND CASCADING by studying how multiple 74LS148 ICs can be connected to handle 16 inputs

5. REVIEW PREVIOUS DU EXAMINATION questions on encoders to understand the pattern and depth expected