# Floating Point Representation

## Introduction

Fixed-point numbers have limited range and precision. **Floating-point** representation allows us to represent very large numbers (like 3.4 x 10^38) and very small numbers (like 1.2 x 10^-38) using a fixed number of bits.

## Scientific Notation Review

Any number can be written as:
**N = M x B^E**

Where:

- **M** = Mantissa (significand)
- **B** = Base (radix)
- **E** = Exponent

**Examples:**

- 6,023,000 = 6.023 x 10^6
- 0.000001 = 1.0 x 10^-6
- -234.5 = -2.345 x 10^2

## Binary Floating Point

In binary, a floating-point number is represented as:
**N = (-1)^S x M x 2^E**

Where:

- **S** = Sign bit (0 = positive, 1 = negative)
- **M** = Mantissa (normalized fraction)
- **E** = Exponent

## IEEE 754 Standard

The **IEEE 754** standard defines floating-point formats used by all modern computers.

### Single Precision (32-bit / float)

| Field        | Bits    | Position   |
| ------------ | ------- | ---------- |
| Sign (S)     | 1 bit   | Bit 31     |
| Exponent (E) | 8 bits  | Bits 30-23 |
| Mantissa (M) | 23 bits | Bits 22-0  |

**Total: 32 bits**

### Double Precision (64-bit / double)

| Field        | Bits    | Position   |
| ------------ | ------- | ---------- |
| Sign (S)     | 1 bit   | Bit 63     |
| Exponent (E) | 11 bits | Bits 62-52 |
| Mantissa (M) | 52 bits | Bits 51-0  |

**Total: 64 bits**

## Biased Exponent

Instead of storing the actual exponent, IEEE 754 uses a **biased exponent**:

**Stored Exponent = Actual Exponent + Bias**

| Format          | Bias | Exponent Range |
| --------------- | ---- | -------------- |
| Single (32-bit) | 127  | -126 to +127   |
| Double (64-bit) | 1023 | -1022 to +1023 |

**Why bias?**

- Allows unsigned comparison of floating-point numbers
- Simplifies hardware for sorting/comparing

## Normalized Form

A normalized binary floating-point number has the form:
**1.xxxxx x 2^exponent**

The leading **1** is implicit (hidden bit) - not stored!
This gives us one extra bit of precision for free.

## Converting Decimal to IEEE 754 Single Precision

**Example: Convert -13.625 to IEEE 754 single precision**

**Step 1:** Determine sign bit

- Negative number, so S = 1

**Step 2:** Convert magnitude to binary

- 13 = 1101
- 0.625 = 0.101 (0.5 + 0.125)
- 13.625 = 1101.101

**Step 3:** Normalize

- 1101.101 = 1.101101 x 2^3

**Step 4:** Calculate biased exponent

- Actual exponent = 3
- Biased exponent = 3 + 127 = 130 = 10000010

**Step 5:** Extract mantissa (without hidden 1)

- Mantissa = 10110100000000000000000 (23 bits)

**Final IEEE 754:**

- S = 1
- E = 10000010
- M = 10110100000000000000000

**Result:** 1 10000010 10110100000000000000000
**Hex:** C15A0000

## Converting IEEE 754 to Decimal

**Example: Convert 0 10000001 10100000000000000000000**

**Step 1:** Extract fields

- S = 0 (positive)
- E = 10000001 = 129
- M = 10100000000000000000000

**Step 2:** Calculate actual exponent

- Actual exponent = 129 - 127 = 2

**Step 3:** Add hidden bit to mantissa

- 1.10100000... = 1.101

**Step 4:** Apply exponent

- 1.101 x 2^2 = 110.1 = 6.5

**Step 5:** Apply sign

- Result = +6.5

## Special Values in IEEE 754

| Exponent | Mantissa | Value              |
| -------- | -------- | ------------------ |
| 00000000 | 0        | Zero (±0)          |
| 00000000 | ≠ 0      | Denormalized       |
| 11111111 | 0        | Infinity (±∞)      |
| 11111111 | ≠ 0      | NaN (Not a Number) |

**Examples:**

- +0 = 0 00000000 00000000000000000000000
- -0 = 1 00000000 00000000000000000000000
- +∞ = 0 11111111 00000000000000000000000
- NaN = 0 11111111 10000000000000000000000

## Range and Precision

### Single Precision (32-bit)

- **Smallest positive:** ≈ 1.18 x 10^-38
- **Largest positive:** ≈ 3.4 x 10^38
- **Precision:** ~7 decimal digits

### Double Precision (64-bit)

- **Smallest positive:** ≈ 2.23 x 10^-308
- **Largest positive:** ≈ 1.8 x 10^308
- **Precision:** ~15-16 decimal digits

## Common Pitfalls

1. **Rounding errors:** 0.1 cannot be exactly represented in binary
2. **Comparison:** Never use == for floating-point comparison
3. **Overflow:** Results too large become infinity
4. **Underflow:** Results too small become zero

## Summary

| Property          | Single (32-bit) | Double (64-bit) |
| ----------------- | --------------- | --------------- |
| Sign bits         | 1               | 1               |
| Exponent bits     | 8               | 11              |
| Mantissa bits     | 23              | 52              |
| Bias              | 127             | 1023            |
| Decimal precision | ~7 digits       | ~15 digits      |
