# Binary Number System

## Introduction

The binary number system is the foundation of all digital electronics and computer systems. It uses only two digits: 0 and 1, called **bits** (binary digits). Every digital circuit, from simple gates to complex processors, operates using binary numbers.

## Why Binary?

Digital circuits use **two voltage levels**:
- **High voltage (typically 3.3V or 5V)** represents **1**
- **Low voltage (typically 0V)** represents **0**

This two-state system is more reliable than multi-state systems because:
1. **Noise immunity** - Easy to distinguish between two states
2. **Simple circuits** - ON/OFF switches are easy to implement
3. **Reliable storage** - Magnetic/optical media store binary data efficiently

## Binary Number Structure

A binary number consists of bits arranged by **positional weight**:

| Position | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|---|---|---|
| Weight | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| Value | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

**Example:** (1011)_2 = 1x2^3 + 0x2^2 + 1x2^1 + 1x2^0 = 8 + 0 + 2 + 1 = (11)_10

## Binary Terminology

| Term | Definition | Example |
|------|------------|---------|
| **Bit** | Single binary digit | 0 or 1 |
| **Nibble** | 4 bits | 1010 |
| **Byte** | 8 bits | 10110101 |
| **Word** | System-dependent (16/32/64 bits) | Depends on processor |
| **MSB** | Most Significant Bit (leftmost) | In 1011, MSB = 1 |
| **LSB** | Least Significant Bit (rightmost) | In 1011, LSB = 1 |

## Powers of 2 (Must Memorize)

| Power | Value | Common Name |
|-------|-------|-------------|
| 2^0 | 1 | - |
| 2^1 | 2 | - |
| 2^2 | 4 | - |
| 2^3 | 8 | - |
| 2^4 | 16 | - |
| 2^5 | 32 | - |
| 2^6 | 64 | - |
| 2^7 | 128 | - |
| 2^8 | 256 | - |
| 2^10 | 1024 | 1 Kilo (K) |
| 2^20 | 1,048,576 | 1 Mega (M) |
| 2^30 | 1,073,741,824 | 1 Giga (G) |

## Range of n-bit Binary Numbers

For an **n-bit unsigned** binary number:
- **Minimum value:** 0
- **Maximum value:** 2^n - 1
- **Total numbers:** 2^n

| Bits | Range | Total Values |
|------|-------|--------------|
| 4 | 0 to 15 | 16 |
| 8 | 0 to 255 | 256 |
| 16 | 0 to 65,535 | 65,536 |
| 32 | 0 to 4,294,967,295 | 4,294,967,296 |

## Binary Fractions

Binary can also represent fractional numbers using negative powers of 2:

| Position | -1 | -2 | -3 | -4 |
|----------|----|----|----|----|
| Weight | 2^-1 | 2^-2 | 2^-3 | 2^-4 |
| Value | 0.5 | 0.25 | 0.125 | 0.0625 |

**Example:** (101.11)_2 = 4 + 0 + 1 + 0.5 + 0.25 = (5.75)_10

## Advantages of Binary System

1. **Simple arithmetic** - Only 4 rules for addition (0+0, 0+1, 1+0, 1+1)
2. **Easy implementation** - Uses simple electronic switches
3. **Reliable transmission** - Two states are easy to detect
4. **Boolean algebra** - Direct mapping to logic operations (AND, OR, NOT)

## Applications in Digital Design

1. **Memory addressing** - RAM locations identified by binary addresses
2. **Data storage** - All files stored as binary data
3. **Arithmetic operations** - ALU performs binary arithmetic
4. **Control signals** - Enable/disable signals are binary
5. **State machines** - States represented in binary

## Summary

- Binary uses base-2 with digits 0 and 1
- Each position has weight of power of 2
- n bits can represent 2^n different values (0 to 2^n - 1)
- MSB is leftmost, LSB is rightmost
- Foundation for all digital systems and computing
