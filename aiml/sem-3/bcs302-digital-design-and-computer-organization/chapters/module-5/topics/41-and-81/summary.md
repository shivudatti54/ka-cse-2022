# 4:1 and 8:1

## Digital Design and Computer Organization

### Definitions and Formulas

- **4:1 Decoders:** A 4:1 decoder is a digital logic circuit that selects one of four input bits and produces a single output bit.
- **8:1 Decoders:** An 8:1 decoder is a digital logic circuit that selects one of eight input bits and produces a single output bit.
- **Code Words:** A code word is a sequence of bits used to represent a particular binary number.
- **Binary Number System:** A 4-bit binary number system represents numbers from 0000 to 1111 (16 possible values).

### Key Points

- **4:1 Decoders:**
  - Select one of four input bits
  - Use 2 bits to select the output bit (binary 01, 10, 11, or 00)
  - Formula: `Y = A'B'C'D`
- **8:1 Decoders:**
  - Select one of eight input bits
  - Use 3 bits to select the output bit (binary 000, 001, 010, 011, 100, 101, 110, or 111)
  - Formula: `Y = A'B'C`
- **Theorem:** A 4:1 decoder can be implemented using 2 AND gates, 1 OR gate, and 1 inverter.
- **Theorem:** An 8:1 decoder can be implemented using 3 AND gates, 1 OR gate, and 1 inverter.

### Important Facts

- **4:1 Decoders are faster and more efficient than 8:1 decoders.**
- **8:1 decoders are used when there are more than eight input bits.**
