# **CRC-CCITT (16-bits) Error Detecting Code**

## **Key Points**

- **Definition:** CRC-CCITT (16-bits) is a type of cyclic redundancy check (CRC) algorithm used for error detection in digital data transmission.
- **Formula:** `CRC = (a, m, n)`
  - `a`: initial value
  - `m`: polynomial
  - `n`: number of bits
- **Polynomial:** `x^16 + x^12 + x^5 + 1`
- **Calculating CRC:**
  1.  Initialize `CRC = a`
  2.  For each data bit `d` (0 to `n-1`):
      - XOR `CRC` with `d`
      - Shift `CRC` right by 1 bit
      - XOR `CRC` with result of step 2
  3.  Return `CRC`
- **Theorem:** If the received data includes any errors, the resulting `CRC` will not be equal to the original `CRC`.
- **Use Case:** CRC-CCITT (16-bits) is commonly used in data communication protocols such as X.25 and Ethernet.

## **Important Formulas and Definitions**

- `CRC = (a, m, n) = (a \* (m^(n-1))) mod m`
- `a`: initial value
- `m`: polynomial
- `n`: number of bits
- `x^16 + x^12 + x^5 + 1`: polynomial for CRC-CCITT (16-bits)
