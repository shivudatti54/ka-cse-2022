# Double Transposition Cipher

### Introduction

A double transposition cipher is a type of transposition cipher that involves two separate transpositions. It is a polyalphabetic substitution cipher that uses a combination of transposition and substitution techniques to encrypt and decrypt messages.

### How it Works

The double transposition cipher works as follows:

1. **First Transposition**: The plaintext message is first transposed in a way that rearranges the characters in a predetermined pattern. This is typically done by rearranging the characters in a grid or table.
2. **Second Transposition**: The transposed message from the first step is then transposed again in a different pattern. This is usually done by rearranging the rows and columns of a grid.
3. **Substitution**: The final transposed message is then substituted with a corresponding encrypted character, usually using a Caesar cipher or a similar technique.

### Types of Double Transposition Ciphers

There are several types of double transposition ciphers, including:

- **Rail Fence Cipher**: This type of cipher uses a rectangular grid to transpose the message.
- **Columnar Transposition Cipher**: This type of cipher uses a grid with rows and columns to transpose the message.
- **Hill Cipher**: This type of cipher uses a matrix to transpose the message.

### Key Concepts

- **Key**: The key is used to determine the transposition pattern and the substitution rule.
- **Plaintext**: The plaintext message is the original message to be encrypted.
- **Ciphertext**: The ciphertext message is the encrypted message.
- **Transposition**: The transposition is the process of rearranging the characters in a predetermined pattern.
- **Substitution**: The substitution is the process of replacing each character with a corresponding encrypted character.

### Example

Suppose we want to encrypt the message "ATTACKATDAWN" using the rail fence cipher with a key of 3. We can follow these steps:

1. First Transposition:
   - Create a grid with 3 rows and 11 columns.
   - Write the plaintext message in the grid, rearranging the characters in a zigzag pattern.
   - The resulting grid looks like this:

```
A T T A
T A C K
A D W N
```

2. Second Transposition:
   - Rearrange the rows and columns of the grid to get a new grid with 11 rows and 3 columns.
   - The resulting grid looks like this:

```
A D
T A
T A
K C
A
W N
```

3. Substitution:
   - Replace each character with a corresponding encrypted character using a Caesar cipher with a shift of 3.
   - The resulting ciphertext message is "BEGKDGFFHJ".

### Code Implementation

Here is an example code implementation in Python for the double transposition cipher:

```python
def double_transposition_cipher(message, key):
    # First transposition
    rows = key
    cols = len(message) // rows
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(message[i * cols + j])
        grid.append(row)

    # Second transposition
    transposed_grid = []
    for i in range(cols):
        col = []
        for j in range(rows):
            col.append(grid[j][i])
        transposed_grid.append(col)

    # Substitution
    ciphertext = ""
    for i in range(rows):
        for j in range(cols):
            ciphertext += chr((ord(transposed_grid[i][j]) + key) % 256)

    return ciphertext

# Example usage:
message = "ATTACKATDAWN"
key = 3
ciphertext = double_transposition_cipher(message, key)
print(ciphertext)
```

This code implements the double transposition cipher using a grid-based approach. It first creates a grid with the specified number of rows and columns, and then rearranges the characters in a zigzag pattern. The resulting grid is then transposed again to get the final ciphertext message.
