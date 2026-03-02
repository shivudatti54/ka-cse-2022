# 4:1 and 8:1 Digital Design and Computer Organization Revision Notes

===========================================================

## Definitions and Theorems

- A 4:1 decoder is a digital circuit that takes four input bits and produces one output bit.
- An 8:1 decoder is a digital circuit that takes eight input bits and produces one output bit.
- The number of possible output locations is determined by the number of input bits.

## 4:1 Decoder

- Formula: `2^n - 1`
- Number of possible output locations: `2^4 - 1 = 15`
- Truth table:

| A   | B   | C   | D   | Output |
| --- | --- | --- | --- | ------ |
| 0   | 0   | 0   | 0   | 0      |
| 0   | 0   | 0   | 1   | 1      |
| 0   | 0   | 1   | 0   | 2      |
| 0   | 0   | 1   | 1   | 3      |
| 0   | 1   | 0   | 0   | 4      |
| 0   | 1   | 0   | 1   | 5      |
| 0   | 1   | 1   | 0   | 6      |
| 0   | 1   | 1   | 1   | 7      |
| 1   | 0   | 0   | 0   | 8      |
| 1   | 0   | 0   | 1   | 9      |
| 1   | 0   | 1   | 0   | 10     |
| 1   | 0   | 1   | 1   | 11     |
| 1   | 1   | 0   | 0   | 12     |
| 1   | 1   | 0   | 1   | 13     |
| 1   | 1   | 1   | 0   | 14     |
| 1   | 1   | 1   | 1   | 15     |

## 8:1 Decoder

- Formula: `2^n - 1`
- Number of possible output locations: `2^8 - 1 = 255`
- Truth table ( truncated to 16 rows for brevity):

| A   | B   | C   | D   | E   | F   | G   | H   | Output |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0      |
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1      |
| ... | ... | ... | ... | ... | ... | ... | ... | ...    |
| 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 255    |

Note: This is a concise summary of key points. For a more detailed understanding, refer to the respective chapters or textbooks.
