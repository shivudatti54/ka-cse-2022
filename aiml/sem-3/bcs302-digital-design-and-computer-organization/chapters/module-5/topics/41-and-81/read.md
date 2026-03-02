# **4:1 and 8:1 Multiplexers**

## **Introduction**

In digital design and computer organization, multiplexers are essential components that allow multiple input signals to be combined into a single output signal. In this study material, we will focus on 4:1 and 8:1 multiplexers, which are two of the most commonly used types of multiplexers.

## **What is a Multiplexer?**

A multiplexer (MX) is a digital circuit that takes multiple input signals and combines them into a single output signal. The multiplexer is controlled by a select signal, which determines which input signal is selected as the output.

## **4:1 Multiplexer**

### Definition

A 4:1 multiplexer is a multiplexer that takes four input signals and combines them into a single output signal. It is commonly used in digital systems where multiple input signals need to be combined into a single output signal.

### Structure

The structure of a 4:1 multiplexer consists of four input lines (A, B, C, and D), a select line (S), and an output line (Y). The select line is used to select one of the four input signals as the output.

### Truth Table

| S   | A   | B   | C   | D   | Y   |
| --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | A   |
| 0   | 0   | 0   | 0   | 1   | B   |
| 0   | 0   | 0   | 1   | 0   | C   |
| 0   | 0   | 0   | 1   | 1   | D   |
| 0   | 1   | 0   | 0   | 0   | A   |
| 0   | 1   | 0   | 0   | 1   | B   |
| 0   | 1   | 0   | 1   | 0   | C   |
| 0   | 1   | 0   | 1   | 1   | D   |
| 0   | 1   | 1   | 0   | 0   | A   |
| 0   | 1   | 1   | 0   | 1   | B   |
| 0   | 1   | 1   | 1   | 0   | C   |
| 0   | 1   | 1   | 1   | 1   | D   |
| 1   | 0   | 0   | 0   | 0   | B   |
| 1   | 0   | 0   | 0   | 1   | C   |
| 1   | 0   | 0   | 1   | 0   | D   |
| 1   | 0   | 0   | 1   | 1   | A   |
| 1   | 0   | 1   | 0   | 0   | C   |
| 1   | 0   | 1   | 0   | 1   | D   |
| 1   | 0   | 1   | 1   | 0   | A   |
| 1   | 0   | 1   | 1   | 1   | B   |
| 1   | 1   | 0   | 0   | 0   | D   |
| 1   | 1   | 0   | 0   | 1   | A   |
| 1   | 1   | 0   | 1   | 0   | B   |
| 1   | 1   | 0   | 1   | 1   | C   |
| 1   | 1   | 1   | 0   | 0   | B   |
| 1   | 1   | 1   | 0   | 1   | C   |
| 1   | 1   | 1   | 1   | 0   | A   |
| 1   | 1   | 1   | 1   | 1   | D   |

### Example Use Case

A 4:1 multiplexer can be used to select one of four input signals (A, B, C, or D) as the output signal. For example, consider a digital circuit that needs to select one of four input signals (A, B, C, or D) based on a select signal (S). The 4:1 multiplexer can be used to achieve this selection.

## **8:1 Multiplexer**

### Definition

An 8:1 multiplexer is a multiplexer that takes eight input signals and combines them into a single output signal. It is commonly used in digital systems where multiple input signals need to be combined into a single output signal.

### Structure

The structure of an 8:1 multiplexer consists of eight input lines (A, B, C, D, E, F, G, and H), a select line (S), and an output line (Y). The select line is used to select one of the eight input signals as the output.

### Truth Table

| S   | A   | B   | C   | D   | E   | F   | G   | H   | Y   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | A   |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | B   |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | C   |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | D   |
| 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | E   |
| 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | F   |
| 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | G   |
| 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | H   |
| 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | E   |
| 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | F   |
| 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | G   |
| 0   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | 1   | H   |
| 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | F   |
| 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | 1   | G   |
| 0   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 0   | H   |
| 0   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 1   | I   |
| 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 0   | G   |
| 0   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | H   |
| 0   | 0   | 0   | 0   | 1   | 0   | 1   | 1   | 0   | I   |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | H   |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | I   |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | 0   | I   |
| 0   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | 1   | J   |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | 0   | I   |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | 1   | J   |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | K   |
| 0   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | L   |
| 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | E   |
| 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | F   |
| 0   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | G   |
| 0   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | 1   | H   |
| 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 0   | G   |
| 0   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | 1   | H   |
| 0   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 0   | I   |
| 0   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | 1   | J   |
| 0   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 0   | H   |
| 0   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | 1   | I   |
| 0   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 0   | J   |
| 0   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | 1   | K   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 0   | I   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | 1   | J   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 0   | K   |
| 0   | 1   | 0   | 0   | 0   | 1   | 1   | 1   | 1   | L   |
| 0   | 1   | 0   | 0   | 1   | 0   | 0   | 0   | 0   | F   |
| 0   | 1   | 0   | 0   | 1   | 0   | 0   | 0   | 1   | G   |
| 0   | 1   | 0   | 0   | 1   | 0   | 0   | 1   | 0   | H   |
| 0   | 1   | 0   | 0   | 1   | 0   | 0   | 1   | 1   | I   |
| 0   | 1   | 0   | 0   | 1   | 0   | 1   | 0   | 0   | H   |
| 0   | 1   | 0   | 0   | 1   | 0   | 1   | 0   | 1   | I   |
| 0   | 1   | 0   | 0   | 1   | 0   | 1   | 1   | 0   | J   |
| 0   | 1   | 0   | 0   | 1   | 0   | 1   | 1   | 1   | K   |
| 0   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 0   | I   |
| 0   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | 1   | J   |
| 0   | 1   | 0   | 0   | 1   | 1   | 0   | 1   | 0   | K   |
| 0   | 1   | 0   | 0   | 1   | 1   | 0   | 1   | 1   | L   |
| 0   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 0   | J   |
| 0   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | 1   | K   |
| 0   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 0   | L   |
| 0   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | 1   | M   |
| 0   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | E   |
| 0   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | 1   | F   |
| 0   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 0   | G   |
| 0   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | 1   | H   |
| 0   | 1   | 1   | 0   | 0   | 0   | 1   | 0   | 0   | G   |
| 0   | 1   | 1   | 0   | 0   | 0   | 1   | 0   | 1   | H   |
| 0   | 1   | 1   | 0   | 0   | 0   | 1   | 1   | 0   | I   |
| 0   | 1   | 1   | 0   | 0   | 0   | 1   | 1   | 1   | J   |
| 0   | 1   | 1   | 0   | 0   | 1   | 0   | 0   | 0   | H   |
| 0   | 1   | 1   | 0   | 0   | 1   | 0   | 0   | 1   | I   |
| 0   | 1   | 1   | 0   | 0   | 1   | 0   | 1   | 0   | J   |
| 0   | 1   | 1   | 0   | 0   | 1   | 0   | 1   | 1   | K   |
| 0   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 0   | I   |
| 0   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | 1   | J   |
| 0   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 0   | K   |
| 0   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | 1   | L   |
| 0   | 1   | 1   | 0   | 1   | 0   | 0   | 0   | 0   | F   |
| 0   | 1   | 1   | 0   | 1   | 0   | 0   | 0   | 1   | G   |
| 0   | 1   | 1   | 0   | 1   | 0   | 0   | 1   | 0   | H   |
| 0   | 1   | 1   | 0   | 1   | 0   | 0   | 1   | 1   | I   |
| 0   | 1   | 1   | 0   | 1   | 0   | 1   | 0   | 0   | H   |
| 0   | 1   | 1   | 0   | 1   | 0   | 1   | 0   | 1   | I   |
| 0   | 1   | 1   | 0   | 1   | 0   | 1   | 1   | 0   | J   |
| 0   | 1   | 1   | 0   | 1   | 0   | 1   | 1   | 1   | K   |
| 0   | 1   | 1   | 0   | 1   | 1   | 0   | 0   | 0   | I   |
| 0   | 1   | 1   | 0   | 1   | 1   | 0   | 0   | 1   | J   |
| 0   | 1   | 1   | 0   | 1   | 1   | 0   | 1   | 0   | K   |
| 0   | 1   | 1   | 0   | 1   | 1   | 0   | 1   | 1   | L   |
| 0   | 1   | 1   | 0   | 1   | 1   | 1   | 0   | 0   | K   |
| 0   | 1   | 1   | 0   | 1   | 1   | 1   | 0   | 1   | L   |
| 0   | 1   | 1   | 0   | 1   | 1   | 1   | 1   | 0   | M   |
| 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 0   | G   |
| 0   | 1   | 1   | 1   | 0   | 0   | 0   | 0   | 1   | H   |
| 0   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | 0   | I   |
| 0   | 1   | 1   | 1   | 0   | 0   | 0   | 1   | 1   | J   |
| 0   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 0   | I   |
| 0   | 1   | 1   | 1   | 0   | 0   | 1   | 0   | 1   | J   |
| 0   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 0   | K   |
| 0   | 1   | 1   | 1   | 0   | 0   | 1   | 1   | 1   | L   |
| 0   | 1   | 1   | 1   | 0   | 1   | 0   | 0   | 0   | I   |
| 0   | 1   | 1   | 1   | 0   | 1   | 0   | 0   | 1   | J   |
| 0   | 1   | 1   | 1   | 0   | 1   | 0   | 1   | 0   | K   |
| 0   | 1   | 1   | 1   | 0   | 1   | 0   |
