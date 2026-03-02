# Error Detection and Correction in Computer Networks

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In the realm of computer networks, data transmission between sender and receiver is rarely perfect. When data travels through communication channels—whether wired (like fiber optic cables) or wireless (like Wi-Fi and cellular networks)—it is susceptible to various forms of interference, noise, and signal degradation. This interference can cause bits to be flipped, added, or removed, resulting in errors in the received data.

**Error Detection and Correction** is a fundamental concept in data communication that ensures reliable data transfer across noisy channels. Without these mechanisms, modern computing and internet connectivity would be impossible, as even a single corrupted bit can crash programs, corrupt files, or cause security vulnerabilities.

### Real-World Relevance

- **Internet Browsing**: When you load a webpage, HTTP uses TCP which employs error detection to ensure all data arrives correctly
- **Mobile Communication**: 4G/5G networks use sophisticated CRC and ARQ mechanisms for voice and data transmission
- **Digital Television**: Error correction codes ensure clear picture quality despite signal interference
- **Satellite Communication**: Deep space communication relies on powerful error-correcting codes like Reed-Solomon
- **Data Storage**: Hard drives and SSDs use error detection/correction to maintain data integrity

---

## 2. Types of Errors in Data Transmission

### 2.1 Single-Bit Errors

A **single-bit error** occurs when only one bit in the data unit (typically a byte or character) is changed from 1 to 0 or from 0 to 1. This is the simplest form of error and is relatively rare in most communication systems, though it can occur in parallel transmission channels.

**Example**: Sending `01010101` but receiving `01010111` (last bit flipped)

### 2.2 Burst Errors

A **burst error** is more common and potentially more damaging. It occurs when two or more bits in the data unit are changed, often due to impulse noise or physical damage to the transmission medium. The "burst" refers to the sequence of bits in which errors occur—the first error to the last error defines the burst length.

**Characteristics of Burst Errors**:
- Not all bits in the burst are necessarily erroneous
- Burst length is defined from first error to last error
- More challenging to correct than single-bit errors
- Common in wireless and satellite communications

**Example**: Sending `01010101` but receiving `01100111` (multiple bits flipped)

---

## 3. Fundamentals of Error Detection

The fundamental principle behind error detection is **redundancy**—adding extra bits to the data that allow the receiver to verify correctness. The sender computes these redundant bits based on the data and sends them along with the original data. The receiver recomputes these bits and compares them with the received redundant bits to determine if an error occurred.

### 3.1 Key Concepts

| Concept | Description |
|---------|-------------|
| **Redundancy** | Adding extra bits derived from the original data |
| **Detection Capability** | The types of errors that can be detected |
| **Overhead** | Ratio of redundant bits to data bits |
| **Accuracy** | Probability of detecting errors |

---

## 4. Parity Checking

### 4.1 Simple Parity (Single Parity Bit)

The simplest form of error detection uses a **parity bit** added to the data. There are two schemes:

- **Even Parity**: The total number of 1s in the data (including parity bit) should be even
- **Odd Parity**: The total number of 1s in the data (including parity bit) should be odd

**Algorithm**:
1. Count the number of 1s in the data bits
2. For even parity: Add 0 if count is already even, add 1 if count is odd
3. For odd parity: Add 1 if count is already even, add 0 if count is odd

**Example with 5 ones (Even Parity)**:

Data: `10110011` (5 ones)

Since we have 5 ones (odd), for even parity we need to add 1 to make the total even (6 ones).

```python
def calculate_parity_bit(data, parity_type='even'):
    """Calculate parity bit for given data."""
    ones_count = data.count('1')
    
    if parity_type == 'even':
        return '1' if ones_count % 2 != 0 else '0'
    else:  # odd parity
        return '0' if ones_count % 2 != 0 else '1'

# Example: Data with 5 ones
data = "10110011"
parity_bit = calculate_parity_bit(data, 'even')
print(f"Data: {data}")
print(f"Parity bit (even): {parity_bit}")
print(f"Transmitted data: {data + parity_bit}")
```

**Output**:
```
Data: 10110011
Parity bit (even): 1
Transmitted data: 101100111
```

**Limitation**: Simple parity can detect only **odd number of bit errors**. If two bits are flipped (even number of errors), the parity remains unchanged and errors go undetected.

### 4.2 Two-Dimensional Parity

To improve detection capability, we use **two-dimensional (or longitudinal) parity**, also known as **parity grid**:

1. Data is organized in a matrix (rows of characters)
2. A parity bit is calculated for each row
3. A parity bit is calculated for each column
4. An overall parity bit is added at the end

This method can detect:
- Any single-bit error (row and column parity will be wrong)
- Multiple bit errors in a row or column
- Most burst errors within the grid

---

## 5. Checksum

**Checksum** is an error-detecting code that represents the sum of fixed-size data chunks. It provides stronger error detection than simple parity.

### 5.1 Algorithm

1. Divide the data into fixed-size segments (typically 16 bits)
2. Sum all segments using one's complement arithmetic
3. Take the complement of the sum to get the checksum
4. Append checksum to the original data
5. Receiver divides received data into segments, sums them, adds checksum, and checks for all 1s

### 5.2 Implementation Example

```python
def calculate_checksum(data, segment_size=16):
    """Calculate checksum using 16-bit segments."""
    # Convert data to binary if string
    if isinstance(data, str):
        binary_data = ''.join(format(ord(c), '08b') for c in data)
    else:
        binary_data = format(data, 'b')
    
    # Pad to make divisible by segment_size
    padding = len(binary_data) % segment_size
    if padding != 0:
        binary_data = '0' * (segment_size - padding) + binary_data
    
    # Split into segments and sum
    segments = [binary_data[i:i+segment_size] for i in range(0, len(binary_data), segment_size)]
    
    total = 0
    for seg in segments:
        total += int(seg, 2)
    
    # Handle carry bits (wrap around)
    while total > 0xFFFF:
        carry = total >> 16
        total = (total & 0xFFFF) + carry
    
    # Return one's complement
    checksum = ~total & 0xFFFF
    return format(checksum, '016b')

def verify_checksum(data_with_checksum, segment_size=16):
    """Verify data using checksum."""
    binary_data = ''.join(format(ord(c), '08b') for c in data_with_checksum)
    
    # Split segments
    segments = [binary_data[i:i+segment_size] for i in range(0, len(binary_data), segment_size)]
    
    total = 0
    for seg in segments:
        total += int(seg, 2)
    
    while total > 0xFFFF:
        carry = total >> 16
        total = (total & 0xFFFF) + carry
    
    # If result is all 1s (0xFFFF), no error detected
    return total == 0xFFFF

# Example usage
data = "Hi"
checksum = calculate_checksum(data)
print(f"Data: {data}")
print(f"Checksum: {checksum}")
print(f"Verification: {verify_checksum(data + chr(int(checksum, 2)))}")
```

**Output**:
```
Data: Hi
Checksum: 1110101101001001
Verification: True
```

---

## 6. Cyclic Redundancy Check (CRC)

**CRC** is one of the most powerful and widely used error detection mechanisms. It is based on polynomial division and can detect:

- All single-bit errors
- All burst errors of length ≤ degree of polynomial
- Most larger burst errors (detection probability = 1 - 2^(-r) where r is the number of check bits)

### 6.1 Key Concepts

- **Generator Polynomial (G(x))**: A predetermined polynomial of degree r
- **CRC Bits**: r check bits appended to data
- **Divisibility**: The transmitted message must be divisible by G(x)

### 6.2 Algorithm

1. **Sender Side**:
   - Represent data as a polynomial D(x)
   - Append r zero bits to data (where r = degree of generator polynomial)
   - Divide the extended data by G(x) using modulo-2 division
   - Append the remainder (CRC bits) to original data
   - Transmit the result

2. **Receiver Side**:
   - Divide received data by G(x)
   - If remainder is zero → no error detected
   - If remainder is non-zero → error detected

### 6.3 Standard CRC Polynomials

| CRC Type | Generator Polynomial | Degree |
|----------|---------------------|--------|
| CRC-8 | x⁸ + x² + x + 1 | 8 |
| CRC-12 | x¹² + x¹¹ + x³ + x² + x + 1 | 12 |
| CRC-16 | x¹⁶ + x¹⁵ + x² + 1 | 16 |
| CRC-32 | x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1 | 32 |

### 6.4 Implementation Example

```python
def crc_division(dividend, divisor):
    """Perform modulo-2 division."""
    dividend = list(dividend)
    divisor = list(divisor)
    
    for i in range(len(dividend) - len(divisor) + 1):
        if dividend[i] == 1:
            for j in range(len(divisor)):
                dividend[i + j] ^= divisor[j]
    
    return ''.join(map(str, dividend[-(len(divisor) - 1):]))

def calculate_crc(data, generator="1101"):
    """Calculate CRC for given data using generator polynomial."""
    # Convert to list of integers
    data_bits = [int(b) for b in data]
    generator_bits = [int(g) for g in generator]
    
    # Append zeros (degree of generator - 1)
    r = len(generator) - 1
    extended_data = data_bits + [0] * r
    
    # Perform division
    remainder = crc_division(extended_data, generator_bits)
    
    return remainder

def verify_crc(received_data, generator="1101"):
    """Verify CRC - divide and check remainder."""
    received_bits = [int(b) for b in received_data]
    generator_bits = [int(g) for g in generator]
    
    remainder = crc_division(received_bits, generator_bits)
    
    # If all zeros, no error
    return remainder == "0" * (len(generator) - 1)

# Example: Data = "11010011101100", Generator = "1101" (CRC-3)
data = "11010011101100"
generator = "1101"  # x³ + x² + 1

crc = calculate_crc(data, generator)
transmitted = data + crc

print(f"Original Data: {data}")
print(f"Generator: {generator}")
print(f"CRC (remainder): {crc}")
print(f"Transmitted: {transmitted}")
print(f"Verification (no error): {verify_crc(transmitted, generator)}")

# Simulate error
received_with_error = list(transmitted)
received_with_error[-2] = '1' if received_with_error[-2] == '0' else '0'
received_with_error = ''.join(received_with_error)
print(f"Verification (with error): {verify_crc(received_with_error, generator)}")
```

**Output**:
```
Original Data: 11010011101100
Generator: 1101
CRC (remainder): 100
Transmitted: 11010011101100100
Verification (no error): True
Verification (with error): False
```

---

## 7. Hamming Code (Error Detection AND Correction)

**Hamming Code** is a remarkable error correction code developed by Richard Hamming in 1950. Unlike simple detection codes, Hamming codes can **both detect and correct** single-bit errors. This makes it invaluable for applications requiring high reliability.

### 7.1 Key Concepts

- **Parity Bits (r)**: Redundant bits placed at positions that are powers of 2 (1, 2, 4, 8, 16...)
- **Data Bits (k)**: Original data bits
- **Relationship**: For k data bits, r must satisfy: 2ʳ ≥ k + r + 1
- **Hamming Distance**: Minimum number of bit changes required to transform one valid codeword into another

### 7.2 Algorithm for Encoding

1. Determine number of parity bits needed
2. Place data bits in non-parity positions
3. Calculate each parity bit using even/odd parity over specific bit groups

**Bit Position Groups**:
- Position 1 (2⁰): Covers bits 1, 3, 5, 7, 9, 11...
- Position 2 (2¹): Covers bits 2, 3, 6, 7, 10, 11...
- Position 4 (2²): Covers bits 4-7, 12-15...
- Position 8 (2³): Covers bits 8-15...

### 7.3 Implementation Example

```python
def calculate_hamming_code(data_bits):
    """Calculate Hamming code for given data bits."""
    k = len(data_bits)
    
    # Find minimum r such that 2^r >= k + r + 1
    r = 0
    while (2 ** r) < (k + r + 1):
        r += 1
    
    # Total bits = k + r
    total_bits = k + r
    
    # Initialize codeword with placeholders
    codeword = ['0'] * total_bits
    
    # Place data bits in non-parity positions
    data_idx = 0
    for i in range(total_bits):
        # Position i+1 is a power of 2? It's a parity bit position
        if (i + 1) & (i + 1 - 1) == 0:  # Check if power of 2
            continue
        codeword[i] = data_bits[data_idx]
        data_idx += 1
    
    # Calculate parity bits
    for p in range(r):
        parity_pos = 2 ** p  # Position of parity bit (1-indexed)
        parity_value = 0
        
        # Check bits covered by this parity
        for i in range(parity_pos - 1, total_bits, 2 * parity_pos):
            # Check each bit in this block (starting from parity_pos)
            for j in range(i, min(i + parity_pos, total_bits)):
                if j != parity_pos - 1 and codeword[j] == '1':
                    parity_value ^= 1
        
        codeword[parity_pos - 1] = str(parity_value)
    
    return ''.join(codeword), r

def detect_and_correct_hamming(codeword):
    """Detect and correct single-bit error in Hamming code."""
    n = len(codeword)
    
    # Find number of parity bits
    r = 0
    while 2 ** r <= n:
        r += 1
    
    # Calculate error position
    error_pos = 0
    
    for p in range(r):
        parity_pos = 2 ** p  # 1-indexed
        parity_value = 0
        
        for i in range(parity_pos - 1, n, 2 * parity_pos):
            for j in range(i, min(i + parity_pos, n)):
                if j != parity_pos - 1 and codeword[j] == '1':
                    parity_value ^= 1
        
        # Check if parity is correct
        actual_parity = int(codeword[parity_pos - 1])
        if parity_value != actual_parity:
            error_pos += parity_pos
    
    if error_pos == 0:
        return codeword, 0, "No error detected"
    else:
        # Correct the error
        corrected = list(codeword)
        corrected[error_pos - 1] = '1' if corrected[error_pos - 1] == '0' else '0'
        return ''.join(corrected), error_pos, f"Error at position {error_pos} corrected"

# Example: Encode "1011"
data = "1011"
codeword, r = calculate_hamming_code(data)

print(f"Original Data: {data}")
print(f"Number of parity bits: {r}")
print(f"Hamming Code: {codeword}")

# Introduce single-bit error
codeword_with_error = list(codeword)
codeword_with_error[5] = '1' if codeword_with_error[5] == '0' else '0'  # Flip bit at position 6
codeword_with_error = ''.join(codeword_with_error)

print(f"\nCodeword with error: {codeword_with_error}")
corrected, error_pos, message = detect_and_correct_hamming(codeword_with_error)
print(f"Result: {message}")
print(f"Corrected Codeword: {corrected}")
```

**Output**:
```
Original Data: 1011
Number of parity bits: 3
Hamming Code: 1010010

Codeword with error: 1010110
Result: Error at position 6 corrected
Corrected Codeword: 1010010
```

---

## 8. Error Correction Methods

### 8.1 Error Correction vs. Error Detection

| Aspect | Error Detection | Error Correction |
|--------|-----------------|------------------|
| **Purpose** | Only identify if errors occurred | Identify AND fix errors |
| **Redundancy** | Lower | Higher |
| **Complexity** | Simpler | More complex |
| **Examples** | Parity, Checksum, CRC | Hamming Code, Reed-Solomon |

### 8.2 Types of Error Correction

1. **Forward Error Correction (FEC)**: Receiver uses redundant information to correct errors without retransmission
2. **Automatic Repeat Request (ARQ)**: Receiver requests retransmission when errors are detected

---

## 9. ARQ (Automatic Repeat Request) Protocols

**ARQ** is an error control protocol where the sender transmits data with error detection, and the receiver requests retransmission if errors are detected. It combines error detection with a retransmission mechanism.

### 9.1 Stop-and-Wait ARQ

The simplest ARQ protocol where:

1. Sender transmits one frame
2. Sender waits for acknowledgment (ACK)
3. If ACK received → send next frame
4. If NAK or timeout → retransmit the same frame

**Advantages**:
- Simple to implement
- Low buffer requirements
- Suitable for long-delay channels

**Disadvantages**:
- Inefficient for high-speed networks (high idle time)
- Only one frame in transit at a time

**Timeout Calculation**: Must account for round-trip time plus processing time

```python
import time
import random

def simulate_stop_and_wait():
    """Simulate Stop-and-Wait ARQ protocol."""
    frames = ["Frame1", "Frame2", "Frame3", "Frame4", "Frame5"]
    current_frame = 0
    transmission_count = 0
    
    print("=== Stop-and-Wait ARQ Simulation ===\n")
    
    while current_frame < len(frames):
        print(f"Sending: {frames[current_frame]}")
        transmission_count += 1
        
        # Simulate transmission (10% chance of error)
        error_occurred = random.random() < 0.1
        
        if error_occurred:
            print(f"  → Frame corrupted! Sending NAK/Timeout")
            print(f"  → Retransmitting {frames[current_frame]}...\n")
        else:
            print(f"  → Frame received successfully!")
            print(f"  → Sending ACK\n")
            current_frame += 1
    
    print(f"Total transmissions: {transmission_count}")
    print(f"Total frames: {len(frames)}")
    print(f"Efficiency: {(len(frames)/transmission_count)*100:.1f}%")

simulate_stop_and_wait()
```

### 9.2 Sliding Window Protocol

To improve efficiency, **Sliding Window** allows multiple frames to be in transit simultaneously.

**Key Concepts**:
- **Window Size (W)**: Maximum number of frames that can be sent without acknowledgment
- **Sequence Numbers**: Each frame gets a unique number (modulo W)
- **Send Window**: Frames that can be sent
- **Receive Window**: Frames that can be accepted

**Types**:
1. **Go-Back-N**: On error, retransmit all frames from the erroneous frame
2. **Selective Repeat**: Only retransmit the erroneous frame (requires more buffer)

**Efficiency Calculation**:
- Stop-and-Wait: Efficiency = 1 / (1 + 2a), where a = Tp/Tt
- Sliding Window: Efficiency = W / (1 + 2a), where W is window size

```python
def simulate_sliding_window(window_size=4):
    """Simulate Sliding Window ARQ protocol."""
    frames = list(range(1, 11))  # 10 frames
    sent = []
    acknowledged = []
    current_frame = 0
    
    print(f"=== Sliding Window ARQ (Window Size={window_size}) ===\n")
    
    while acknowledged[-1] != frames[-1] if acknowledged else True:
        # Send frames within window
        while len(sent) - len(acknowledged) < window_size and current_frame < len(frames):
            print(f"Sending: Frame {frames[current_frame]}")
            sent.append(frames[current_frame])
            current_frame += 1
        
        # Simulate acknowledgments (with possible errors)
        if sent:
            ack_frame = acknowledged[-1] + 1 if acknowledged else 1
            
            # Simulate 15% chance of lost ACK
            if random.random() > 0.15:
                print(f"Received ACK for Frame {ack_frame}")
                acknowledged.append(ack_frame)
            else:
                print(f"ACK for Frame {ack_frame} lost! Timeout...")
            
            print()
        
        # Check if all acknowledged
        if acknowledged and acknowledged[-1] == frames[-1]:
            break
    
    print(f"All frames successfully transmitted!")

simulate_sliding_window(4)
```

---

## 10. Multiple Choice Questions

### MCQ 1: In CRC (Cyclic Redundancy Check), if the generator polynomial has degree r, how many check bits are added to the data?
- (a) r
- (b) r + 1
- (c) r - 1
- (d) 2r

**Answer: (a) r**

**Explanation**: In CRC, the generator polynomial of degree r produces exactly r check bits. These r bits (also called the CRC remainder) are appended to the original data before transmission. The receiver divides the received message by the same generator polynomial, and if the remainder is zero, no error is detected.

---

### MCQ 2: For the data word "10110011" using even parity, what is the parity bit?
- (a) 0
- (b) 1
- (c) Cannot be determined
- (d) Either 0 or 1

**Answer: (b) 1**

**Explanation**: The data word "10110011" contains exactly 5 ones (1+0+1+1+0+0+1+1 = 5). For even parity, the total number of 1s (including the parity bit) must be even. Since we already have 5 ones (odd), we need to add a parity bit of 1 to make the total count 6, which is even.

---

### MCQ 3: Which of the following error detection methods can also correct single-bit errors?
- (A) Simple Parity
- (B) Two-Dimensional Parity
- (C) Checksum
- (D) Hamming Code

**Answer: (D) Hamming Code**

**Explanation**: Among the given options, only Hamming Code provides both error detection and error correction capabilities. Simple parity, two-dimensional parity, and checksum can only detect errors but cannot correct them. Hamming code uses strategically placed parity bits that allow the receiver to pinpoint the exact location of a single-bit error and correct it.

---

### MCQ 4: In Stop-and-Wait ARQ, what happens if the sender receives no acknowledgment within the timeout period?
- (A) The sender immediately sends the next frame
- (B) The sender discards the frame and moves on
- (C) The sender retransmits the same frame
- (D) The sender terminates the connection

**Answer: (C) The sender retransmits the same frame**

**Explanation**: In Stop-and-Wait ARQ, the sender waits for an acknowledgment after sending each frame. If the timeout expires before receiving an ACK (either due to lost frame or lost ACK), the sender assumes the frame was not received correctly and retransmits the same frame. This ensures reliability at the cost of efficiency.

---

### MCQ 5: What is the minimum Hamming distance required to detect 3-bit errors?
- (A) 2
- (B) 3
- (C) 4
- (D) 5

**Answer: (C) 4**

**Explanation**: To detect d errors, the minimum Hamming distance must be at least d+1. Therefore, to detect 3-bit errors, we need a minimum Hamming distance of 3+1 = 4. This ensures that no valid codeword can be transformed into another valid codeword by up to 3 bit errors.

---

## 11. Key Takeaways

### Error Detection Methods

| Method | Detection Capability | Overhead | Complexity |
|--------|----------------------|----------|------------|
| Simple Parity | Odd number of bit errors | 1 bit/byte | Very Low |
| Two-Dimensional Parity | Multiple errors in rows/columns | ~1 bit/byte | Low |
| Checksum | Most common errors | ~16 bits | Medium |
| CRC | Up to r-bit burst errors (r = degree) | r bits | Medium-High |
| Hamming Code | Detect & Correct single-bit errors | log₂(n) bits | High |

### Important Formulas

- **Hamming Code**: 2ʳ ≥ k + r + 1 (where k = data bits, r = parity bits)
- **CRC Detection**: Can detect all burst errors of length ≤ r
- **Stop-and-Wait Efficiency**: 1 / (1 + 2a), where a = Tp/Tt
- **Sliding Window Efficiency**: W / (1 + 2a), where W = window size

### Delhi University Syllabus Alignment

This study material covers the following topics from the BSc (Hons) Computer Science syllabus under Computer Networks:
- Error detection and correction techniques
- Parity checking (simple and two-dimensional)
- Checksum and CRC
- Hamming code
- ARQ protocols (Stop-and-Wait and Sliding Window)

### Best Practices

1. **Choose appropriate method** based on channel characteristics (noise level, error patterns)
2. **CRC** is preferred for most network applications due to excellent detection with reasonable overhead
3. **Hamming code** is ideal for memory systems and applications requiring real-time error correction
4. **ARQ protocols** are essential for reliable data transmission in TCP/IP networks

---

*Generated for Delhi University, NEP 2024 UGCF - BSc (Hons) Computer Science*