# **Error Detecting Code using CRC-CCITT (16-bits)**

## **1. Introduction**

Error detecting codes are a crucial component of data transmission in computer networks. They enable the detection of errors that may occur during data transmission, ensuring the integrity of the received data. In this study material, we will focus on the CRC-CCITT (16-bits) error detecting code, which is widely used in digital communication systems.

## **2. What is CRC-CCITT?**

CRC-CCITT (Cyclic Redundancy Check - CCITT) is a type of error detecting code that uses a polynomial to detect errors in data transmission. It is a 16-bit code, which means it uses 16 bits to represent the data and the error detecting information.

## **3. How CRC-CCITT Works**

Here's a step-by-step explanation of how CRC-CCITT works:

- **Data Preparation**: The data to be transmitted is divided into 16-bit blocks.
- **Polynomial Calculation**: The polynomial is calculated for each block using the following formula: `CRC = (CRC << 1) XOR data_block`.
- **Error Detection**: The CRC value is compared to the expected CRC value. If the two values are not equal, an error has occurred, and the error can be detected.

## **4. CRC-CCITT (16-bits) Polynomial**

The CRC-CCITT (16-bits) polynomial is: `X^16 + X^12 + X^11 + X^10 + X^8 + X^7 + X^5 + X^4 + X^3 + X + 1`

## **5. Example of CRC-CCITT (16-bits) Calculation**

Let's consider an example to illustrate how CRC-CCITT works:

Suppose we want to transmit the data block `ABCD` using CRC-CCITT (16-bits).

| Bit | Data | CRC |
| --- | ---- | --- |
| 1   | A    | 0   |
| 2   | B    | 0   |
| 3   | C    | 0   |
| 4   | D    | 0   |

Using the polynomial, we calculate the CRC as follows:

`CRC = (CRC << 1) XOR data_block`

| CRC | Data | CRC |
| --- | ---- | --- |
| 0   | A    | 0   |
| 0   | B    | 0   |
| 0   | C    | 0   |
| 0   | D    | 0   |
| 0   |      | 0   |

Now, let's calculate the CRC for the next 16-bit block:

| Bit | Data | CRC |
| --- | ---- | --- |
| 1   | E    | 0   |
| 2   | F    | 0   |
| 3   | G    | 0   |
| 4   | H    | 0   |
| 5   |      | 0   |

Using the polynomial, we calculate the CRC as follows:

`CRC = (CRC << 1) XOR data_block`

| CRC | Data | CRC |
| --- | ---- | --- |
| 0   | E    | 0   |
| 0   | F    | 0   |
| 0   | G    | 0   |
| 0   | H    | 0   |
| 0   |      | 0   |

Now, we have calculated the CRC for the first 16-bit block, and the CRC is equal to `0`. This means that the data block `ABCD` is error-free.

## **6. Program Implementation**

Here's an example program implementation in Python to calculate the CRC-CCITT (16-bits):

```python
def crc_ccitt(data):
    CRC = 0
    polynomial = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    for bit in data:
        CRC = (CRC << 1) ^ polynomial[bit]
    return CRC

# Test the function
data = [0, 0, 0, 0, 1, 0, 1, 0]
CRC = crc_ccitt(data)
print("CRC:", CRC)
```

## **7. Conclusion**

In this study material, we have discussed the CRC-CCITT (16-bits) error detecting code, its working principle, and its polynomial. We have also provided an example program implementation in Python to calculate the CRC-CCITT (16-bits). Understanding CRC-CCITT is crucial for implementing error detecting codes in digital communication systems.

## **Recommended Reading**

- "A Survey of Error Detection Codes" by S. W. McMillan
- "CRC Handbook" by David V. Schober
- "Error Detection and Correction" by S. B. Wicker

## **Key Concepts**

- Error detecting codes
- CRC-CCITT (16-bits)
- Polynomial
- Data preparation
- CRC calculation
- Error detection
- Program implementation

## **Practice Problems**

1.  Calculate the CRC-CCITT (16-bits) for the data block `ABCD`.
2.  Implement the CRC-CCITT (16-bits) algorithm using a programming language of your choice.
3.  Explain the error detection process using the CRC-CCITT (16-bits) algorithm.
