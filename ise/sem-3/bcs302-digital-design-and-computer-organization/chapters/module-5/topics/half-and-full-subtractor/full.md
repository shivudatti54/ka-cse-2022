# Half and Full Subtractor

## Table of Contents

- [Introduction](#introduction)
- [Historical Context](#historical-context)
- [Half Subtractor](#half-subtractor)
  - [Logic Diagrams](#logic-diagrams)
  - [Truth Table](#truth-table)
  - [Example](#example)
- [Full Subtractor](#full-subtractor)
  - [Logic Diagrams](#logic-diagrams-1)
  - [Truth Table](#truth-table-1)
  - [Example](#example-1)
- [Comparison and Applications](#comparison-and-applications)
- [Modern Developments](#modern-developments)
- [Conclusion](#conclusion)
- [Further Reading](#further-reading)

## Introduction

Subtraction is a fundamental operation in digital design and computer organization. In this module, we will delve into the world of half and full subtractors, two essential components used in digital circuits for performing subtraction operations.

## Historical Context

The concept of half and full subtractors dates back to the early days of digital computing. In the 1950s and 1960s, digital computers used vacuum tubes and transistors to perform arithmetic operations. The first digital computers used binary arithmetic, which relied heavily on binary subtrahends for performing subtraction operations.

Half and full subtractors were developed to simplify the subtraction process by reducing the number of bits required. The earliest implementations used half subtractors, which performed subtraction on two bits at a time. Later, full subtractors were developed to perform subtraction on a larger number of bits.

## Half Subtractor

A half subtractor is a digital circuit that performs subtraction on two bits at a time. It takes two binary inputs, `A` and `B`, and produces a binary output, `P`, and a borrow output, `B`.

### Logic Diagrams

Here is a simplified logic diagram for a half subtractor:

```
  +---------------+
  |  A  |  B  |
  +---------------+
           |
           |
           v
  +---------------+
  |  P  |  B  |
  +---------------+
```

### Truth Table

Here is the truth table for a half subtractor:

| | | | |
| | A | B | P | B |
| | | | | |
| 1 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 1 | 0 |
| 1 | 1 | 1 | 0 | 1 |

### Example

Suppose we want to perform the subtraction `1101 - 0011`. We can use a half subtractor to perform the subtraction bit by bit.

```
  +---------------+  +---------------+
  |  1101  |  |  0011  |
  +---------------+  +---------------+
           |           |
           |           |
           v           v
  +---------------+  +---------------+
  |  P  |  B  |  P  |  B  |
  +---------------+  +---------------+
```

The half subtractors are applied from right to left:

```
  +---------------+  +---------------+
  |  1101  |  |  0011  |
  +---------------+  +---------------+
           |           |
           |           |
           v           v
  +---------------+  +---------------+
  |  0  |  0  |  1  |  0  |
  +---------------+  +---------------+
  +---------------+  +---------------+
  |  11  |  |  01  |
  +---------------+  +---------------+
           |           |
           |           |
           v           v
  +---------------+  +---------------+
  |  0  |  1  |  0  |  1  |
  +---------------+  +---------------+
```

The result is `1100`, and the borrow is `1`.

## Full Subtractor

A full subtractor is a digital circuit that performs subtraction on three bits at a time. It takes three binary inputs, `A`, `B`, and `C`, and produces three binary outputs, `P`, `Q`, and `R`.

### Logic Diagrams

Here is a simplified logic diagram for a full subtractor:

```
  +---------------+
  |  A  |  B  |  C  |
  +---------------+
           |
           |
           v
  +---------------+
  |  P  |  Q  |  R  |
  +---------------+
```

### Truth Table

Here is the truth table for a full subtractor:

| | | | | | | |
| | A | B | C | P | Q | R |
| | | | | | | |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| 0 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

### Example

Suppose we want to perform the subtraction `1100 - 1000`. We can use a full subtractor to perform the subtraction bit by bit.

```
  +---------------+  +---------------+  +---------------+
  |  1100  |  |  1000  |  |  0000  |
  +---------------+  +---------------+  +---------------+
           |           |           |           |
           |           |           |           |
           v           v           v           v
  +---------------+  +---------------+  +---------------+
  |  P  |  Q  |  R  |  P  |  Q  |  R  |
  +---------------+  +---------------+  +---------------+
```

The full subtractors are applied from right to left:

```
  +---------------+  +---------------+  +---------------+
  |  1100  |  |  1000  |  |  0000  |
  +---------------+  +---------------+  +---------------+
           |           |           |           |
           |           |           |           |
           v           v           v           v
  +---------------+  +---------------+  +---------------+
  |  1  |  1  |  0  |  0  |  1  |  0  |
  +---------------+  +---------------+  +---------------+
  +---------------+  +---------------+  +---------------+
  |  11  |  |  01  |  |  00  |
  +---------------+  +---------------+  +---------------+
           |           |           |           |
           |           |           |           |
           v           v           v           v
  +---------------+  +---------------+  +---------------+
  |  0  |  0  |  1  |  0  |  1  |  0  |
  +---------------+  +---------------+  +---------------+
```

The result is `1000`, and the borrow is `0`.

## Comparison and Applications

Half and full subtractors are used extensively in digital design and computer organization. They are used in arithmetic circuits, comparison circuits, and control circuits.

Half subtractors are used in binary arithmetic operations, such as addition and subtraction. They are also used in comparison circuits, such as equality and inequality circuits.

Full subtractors are used in more complex arithmetic operations, such as multiplication and division. They are also used in control circuits, such as digital counters and registers.

## Modern Developments

In modern digital design, half and full subtractors have been replaced by more efficient and complex arithmetic circuits. These circuits use advanced techniques, such as pipelining and parallel processing, to perform arithmetic operations.

However, half and full subtractors are still used in some applications, such as in digital counters and registers, where simplicity and low cost are essential.

## Conclusion

In conclusion, half and full subtractors are essential components in digital design and computer organization. They are used extensively in arithmetic circuits, comparison circuits, and control circuits.

Their history dates back to the early days of digital computing, and they have evolved over time to meet the demands of modern digital design.

## Further Reading

- "Digital Design: A Practical Approach" by Peter J. Ashenden
- "Computer Organization and Design" by David A. Patterson and John L. Hennessy
- "Fundamentals of Digital Logic" by Stephen A. Wakerly
