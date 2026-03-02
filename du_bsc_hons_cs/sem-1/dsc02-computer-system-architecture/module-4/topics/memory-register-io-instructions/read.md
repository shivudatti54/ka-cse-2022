# Memory, Register, and I/O Instructions

## Computer System Architecture — BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction

In the architecture of any computer system, **instructions** serve as the fundamental building blocks that dictate how the processor interacts with data, memory, and peripheral devices. Understanding the distinction and interplay between **Memory Instructions**, **Register Instructions**, and **I/O Instructions** is essential for any computer science student, particularly those studying at Delhi University under the NEP 2024 UGCF curriculum.

These three categories of instructions form the core of the Instruction Set Architecture (ISA) and determine how efficiently a processor can:

- Perform arithmetic and logical operations
- Transfer data between different components of the computer system
- Communicate with external devices such as keyboards, monitors, hard drives, and network interfaces

### Real-World Relevance

Consider what happens when you type a character on your keyboard:

1. The **I/O instruction** `IN` (x86) or `lw` (MIPS from memory-mapped I/O) captures the keystroke
2. The data is stored in a **register** (e.g., `EAX` or `$t0`) using **register instructions**
3. The character is written to video memory using a **memory store instruction** (e.g., `MOV` to memory location)

This entire sequence happens in microseconds, demonstrating how these instruction categories work together in real-world computing.

---

## 2. Register Instructions

### 2.1 What are Registers?

**Registers** are the fastest memory locations within the CPU, serving as the primary working area for the processor. Unlike main memory (RAM), registers are directly accessible within a single clock cycle, making them critical for instruction execution efficiency.

### 2.2 Types of Register Instructions

Register instructions can be categorized as follows:

#### A. Data Transfer Instructions (Register-to-Register)

These instructions move data between registers without involving memory.

**x86 Example:**
```assembly
MOV EAX, EBX      ; Copy contents of EBX into EAX
XCHG EAX, EDX     ; Exchange values of EAX and EDX
LEA ESI, [EDI]    ; Load effective address of EDI into ESI
```

**MIPS Example:**
```assembly
add  $t0, $t1, $t2    # $t0 = $t1 + $t2
sub  $t3, $t4, $t5    # $t3 = $t4 - $t5
move $t6, $t7         # $t6 = $t7 (pseudo-instruction)
```

#### B. Arithmetic and Logical Instructions

These instructions perform computations using register operands.

**x86 Example:**
```assembly
ADD EAX, 10       ; EAX = EAX + 10
SUB EBX, ECX      ; EBX = EBX - ECX
IMUL EDX, EAX     ; EDX:EAX = EAX * EDX (signed)
AND EAX, 0Fh      ; EAX = EAX AND 0x0F (bitwise AND)
OR  EBX, 80h      ; EBX = EBX OR 0x80 (bitwise OR)
XOR ECX, ECX      ; Clear ECX (ECX = 0)
```

**MIPS Example:**
```assembly
addi $t0, $t1, 5      # $t0 = $t1 + 5 (immediate)
andi $t2, $t3, 0xFF   # $t2 = $t3 AND 0xFF
sll $t4, $t5, 2       # $t4 = $t5 << 2 (shift left logical)
srl $t6, $t7, 4       # $t6 = $t7 >> 4 (shift right logical)
```

#### C. Control Transfer Instructions (Register-based)

These instructions modify the program counter using register values.

**x86 Example:**
```assembly
JMP EAX             ; Jump to address in EAX
CALL EBX            ; Call procedure at address in EBX
RET                 ; Return from procedure
```

**MIPS Example:**
```assembly
jr $ra              # Jump to address in $ra (return)
jalr $s0            # Jump and link to address in $s0
```

### 2.3 Register Classification in Context of Instructions

| Register Category | x86 Example | MIPS Example | Purpose |
|-------------------|-------------|--------------|---------|
| General Purpose | EAX, EBX, ECX, EDX | $t0-$t9, $s0-$s7 | Arithmetic, data manipulation |
| Index Registers | ESI, EDI | $gp, $sp | String operations, addressing |
| Pointer Registers | ESP (Stack Pointer), EBP (Base Pointer) | $sp, $fp | Function calls, stack management |
| Program Counter | EIP (Instruction Pointer) | PC (Program Counter) | Controls flow of execution |
| Status Flags | EFLAGS | Status Register | Condition codes, arithmetic flags |

---

## 3. Memory Instructions

### 3.1 Memory Access Instructions

Memory instructions enable the CPU to read from and write to main memory (RAM). These are essential for:

- Loading program instructions and data
- Storing computation results
- Implementing data structures (arrays, linked lists, etc.)

### 3.2 Load (Read) Instructions

**x86 Example:**
```assembly
; Move data from memory to register
MOV EAX, [0x00403000]     ; Direct addressing - load 4 bytes from address 0x00403000
MOV EBX, [ESI]            ; Register indirect - load from address in ESI
MOV ECX, [EDI + 8]        ; Based relative - load from EDI + 8
MOV EDX, [EBP - 4]        ; Based relative with displacement (stack access)
MOVSX EAX, BYTE [EDI]     ; Move with sign extension
MOVZX EAX, BYTE [EDI]     ; Move with zero extension
```

**MIPS Example:**
```assembly
lw $t0, 0x1000($gp)       # Load word from address (gp + 0x1000)
lb $t1, -4($sp)           # Load byte from address (sp - 4)
lbu $t2, 100($t3)         # Load byte unsigned
lui $t3, 0x1234           # Load upper immediate (upper 16 bits)
```

### 3.3 Store (Write) Instructions

**x86 Example:**
```assembly
MOV [0x00403000], EAX     ; Store EAX to direct address
MOV [ESI], EBX            ; Store EBX to address in ESI
MOV [EDI + 16], ECX       ; Store ECX to EDI + 16
MOV BYTE [EBX], 0         ; Store 0 to byte at address in EBX
```

**MIPS Example:**
```assembly
sw $t0, 0x1000($gp)       # Store word to address (gp + 0x1000)
sb $t1, -4($sp)           # Store byte to address (sp - 4)
sh $t2, 100($t3)          # Store halfword
```

### 3.4 Addressing Modes

Addressing modes define how the **effective address** (actual memory location) of an operand is determined. This is crucial for both memory and register instructions.

#### A. Immediate Addressing

The operand value is directly specified in the instruction.

```assembly
; x86
MOV EAX, 100          ; Load immediate value 100 into EAX
ADD EBX, 0FFh         ; Add 255 to EBX

; MIPS
addi $t0, $zero, 50   # $t0 = 0 + 50
ori $t1, $zero, 0xFF  # $t1 = 0 OR 0xFF
```

#### B. Register Addressing

Operand is located in a register.

```assembly
; x86
MOV EAX, EBX          ; Copy EBX to EAX
ADD EAX, ECX          ; Add ECX to EAX

; MIPS
add $t0, $t1, $t2     # $t0 = $t1 + $t2
```

#### C. Direct (Absolute) Addressing

The memory address is explicitly specified in the instruction.

```assembly
; x86
MOV EAX, [0x00403000] ; Load from fixed memory address

; MIPS (using $gp for global pointer)
lw $t0, 0x1000($gp)   # Load from address gp + 0x1000
```

#### D. Register Indirect Addressing

The register contains the memory address.

```assembly
; x86
MOV EAX, [ESI]        ; Load from address in ESI

; MIPS
lw $t0, 0($t1)        # Load from address in $t1
```

#### E. Based (Base Register) Addressing

Memory address = Base Register + Displacement

```assembly
; x86
MOV EAX, [EBP + 8]    ; Access stack frame argument
MOV EBX, [EAX + 4]    ; Array element access

; MIPS
lw $t0, 8($sp)        # Load from stack pointer + 8
lw $t1, 4($t0)        # Load from address in $t0 + 4
```

#### F. Indexed Addressing

Memory address = Base Register + Index Register

```assembly
; x86
MOV EAX, [EBX + ESI*4]    ; For array access: address = EBX + ESI*4
                         ; *4 because each element is 4 bytes

; MIPS (simulated using base + index)
add $t2, $t0, $t1    # Calculate: base + index
lw $t3, 0($t2)      # Load using calculated address
```

#### G. Based-Indexed Addressing

Memory address = Base Register + Index Register + Displacement

```assembly
; x86
MOV EAX, [EBP + ESI + 12]    ; Complex stack/array access
```

#### H. Relative Addressing

Memory address = Program Counter + Displacement (used in branches)

```assembly
; x86
JE SHORT TARGET       ; Jump to PC + offset if equal
JMP NEAR PTR [EIP + 100h]

; MIPS
beq $t0, $t1, LOOP    # Branch to PC + offset if equal
b LABEL               # Unconditional branch
```

### 3.5 Machine Code Representation

Understanding how instructions are encoded in binary is essential for comprehending how the CPU executes them.

#### x86 Instruction Format (32-bit)

```
[Prefix] [Opcode] [ModR/M] [SIB] [Displacement] [Immediate]
```

**Example: `MOV EAX, [EBX + 8]`**

| Field | Value (Hex) | Binary | Description |
|-------|-------------|--------|-------------|
| Opcode | 8B | 10001011 | Move from memory to register |
| ModR/M | 58 | 01011000 | Mod=01 (8-bit displacement), R/M=000 (EBX) |
| Displacement | 08 | 00001000 | Offset of 8 |
| Register (EAX) | 00 | 000 | Encoded in ModR/M bits 5-3 |

**Complete Machine Code:** `8B 58 08` (3 bytes)

#### MIPS Instruction Format (32-bit)

MIPS uses three instruction formats:

**R-Type (Register):**
```
[opcode: 6 bits][rs: 5 bits][rt: 5 bits][rd: 5 bits][shamt: 5 bits][funct: 6 bits]
```

Example: `add $t0, $t1, $t2` ($t0=8, $t1=9, $t2=10)

```
000000 01001 01000 01000 00000 100000
0      9     8      8      0     32
```

**I-Type (Immediate):**
```
[opcode: 6 bits][rs: 5 bits][rt: 5 bits][immediate: 16 bits]
```

Example: `addi $t0, $t1, 100` (100 = 0x0064)

```
001000 01001 01000 0000000001100100
8      9     8      100
```

**J-Type (Jump):**
```
[opcode: 6 bits][address: 26 bits]
```

---

## 4. I/O Instructions

### 4.1 I/O Fundamentals

Input/Output instructions enable the processor to communicate with peripheral devices. There are two primary approaches to I/O:

#### A. Isolated I/O (Port-Mapped I/O)

Also known as **port-mapped I/O** or **I/O-mapped I/O**, this approach uses separate address spaces for I/O devices and memory.

- Uses dedicated **I/O instructions** in x86 architecture
- A separate **I/O address space** of 64K ports (in 16-bit mode)
- The `IN` and `OUT` instructions are used

**x86 I/O Instructions:**
```assembly
; Input instructions
IN AL, 60h            ; Read 1 byte from port 0x60 (keyboard data)
IN AX, 03B0h          ; Read 2 bytes from port 0x03B0

; Input with DX register
IN AL, DX            ; Read from port address in DX

; Output instructions
OUT 60h, AL          ; Write 1 byte to port 0x60 (keyboard LED control)
OUT 03B0h, AX        ; Write 2 bytes to port 0x03B0

; Output with DX register
OUT DX, AL           ; Write to port address in DX

; String I/O (block transfer)
INS BYTE PTR [EDI], DX    ; Input string from port DX to ES:EDI
OUTS DX, BYTE PTR [ESI]   ; Output string from DS:ESI to port DX
```

**Real-World Example: Reading Keyboard Input**

```assembly
; Poll keyboard status
READ_KEYBOARD:
    IN AL, 64h            ; Read keyboard controller status port
    TEST AL, 01h          ; Check output buffer full bit
    JZ READ_KEYBOARD      ; If not ready, keep polling
    
    IN AL, 60h            ; Read the key scan code
    ; Process scan code in AL
    RET
```

#### B. Memory-Mapped I/O (MMIO)

In this approach, I/O devices are mapped into the same address space as memory. The same load/store instructions used for memory access are used for I/O.

**Advantages:**
- No special I/O instructions needed
- All memory addressing modes available
- Simpler hardware design

**Disadvantages:**
- Reduces available memory address space
- Slower access to I/O devices (memory timing)

**MIPS Example (Memory-Mapped I/O):**
```assembly
; Assuming hardware devices are mapped at specific addresses
; Memory-mapped I/O region starts at 0xFFFF0000

; Read from a memory-mapped device (e.g., UART receive)
lui $t0, 0xFFFF           # Load upper immediate
lw $t1, 0x0000($t0)       # Read from address 0xFFFF0000

; Write to a memory-mapped device (e.g., UART transmit)
lui $t0, 0xFFFF
sw $t2, 0x0004($t0)       # Write to address 0xFFFF0004
```

**x86 Example (Memory-Mapped I/O):**
```assembly
; Accessing Video Memory (Graphics)
; VGA text mode memory starts at 0xB8000

mov ax, 0B800h           ; Set up video segment
mov es, ax
mov di, 0                ; Start at upper-left corner

; Write character 'A' with attribute (white on black)
mov ah, 0Fh              ; Attribute: white foreground, black background
mov al, 'A'              ; Character to display
mov [es:di], ax          ; Store to video memory

; Writing a string to screen
mov si, MESSAGE          ; Source index points to message
mov di, 0                ; Start at beginning of screen
mov ah, 0Fh              ; Attribute

PRINT_LOOP:
    lodsb                ; Load byte from [SI] into AL, increment SI
    cmp al, 0            ; Check for null terminator
    je PRINT_DONE
    mov [es:di], ax      ; Write character + attribute
    add di, 2            ; Move to next screen position
    jmp PRINT_LOOP

PRINT_DONE:
    ; Continue with program

MESSAGE db 'Hello, World!', 0
```

### 4.2 Polled vs Interrupt-Driven I/O

#### Polled I/O
The processor continuously checks the device status before performing I/O.

```assembly
; Polling a serial port (x86)
POLL_UART:
    IN AL, UART_STATUS   ; Read status register
    TEST AL, RX_READY    ; Check if data received
    JZ POLL_UART         ; If not ready, keep polling
    IN AL, UART_DATA     ; Read the data
    RET
```

#### Interrupt-Driven I/O
The device notifies the processor via an interrupt when I/O is ready.

```assembly
; Interrupt Service Routine (ISR) example (x86)
ISR_KEYBOARD:
    pushad               ; Save all registers
    
    IN AL, 60h           ; Read scan code from keyboard
    mov [key_buffer], al ; Store in buffer
    
    ; Send End of Interrupt (EOI) to PIC
    mov al, 20h
    out 20h, al
    
    popad                ; Restore all registers
    iret                  ; Return from interrupt
```

---

## 5. Instruction Execution Cycle

Understanding how instructions execute is fundamental to grasping computer architecture.

### 5.1 The Classic Fetch-Execute Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    INSTRUCTION CYCLE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐               │
│   │  FETCH   │───▶│ DECODE   │───▶│ EXECUTE  │───▶ (Repeat)   │
│   └──────────┘    └──────────┘    └──────────┘               │
│                                                                 │
│   FETCH:     PC → MAR → Memory → MDR → IR → PC+1              │
│   DECODE:    IR → Instruction Decoder → Control Signals       │
│   EXECUTE:   ALU/Memory/I/O Operations → Update Registers     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Detailed Cycle Phases

#### Phase 1: Fetch (F)
1. **PC → MAR**: Program Counter contents sent to Memory Address Register
2. **Memory Read**: Memory reads the instruction at that address
3. **MDR → IR**: Instruction loaded into Instruction Register
4. **PC + 1**: Program Counter incremented (or modified for branches)

**For instruction `MOV EAX, [EBX]`:**
- Fetch the opcode byte (8Bh)
- Fetch the ModR/M byte
- Fetch displacement if present

#### Phase 2: Decode (D)
1. **IR → Instruction Decoder**: Instruction is decoded
2. **Control Unit**: Generates control signals
3. **Operand Fetch**: If needed, fetch operands from registers/memory

**For `MOV EAX, [EBX]`:**
- Identify as Move instruction
- Determine register operand (EAX)
- Determine memory operand ([EBX])

#### Phase 3: Execute (E)
1. **ALU Operation**: Perform the operation (for arithmetic/logical)
2. **Memory Access**: Read from or write to memory
3. **I/O Operation**: Input or output to peripheral device

**For `MOV EAX, [EBX]`:**
- EBX → MAR (address calculation)
- Memory Read
- MDR → EAX (data transfer)

#### Phase 4: Store Result (S)
1. **Write Back**: Store result to destination register
2. **Update Flags**: Update status flags if applicable
3. **Check Interrupts**: Handle any pending interrupts

### 5.3 Pipeline Implementation

Modern processors use **instruction pipelining** to overlap these phases:

```
Time →→
Inst 1:  F D E S
Inst 2:     F D E S
Inst 3:        F D E S
Inst 4:           F D E S
```

**MIPS 5-Stage Pipeline:**
1. **IF** (Instruction Fetch)
2. **ID** (Instruction Decode / Register Fetch)
3. **EX** (Execute / ALU Operation)
4. **MEM** (Memory Access)
5. **WB** (Write Back)

---

## 6. Practical Examples

### Example 1: Array Sum in x86 Assembly

```assembly
; Function to calculate sum of integer array
; Input:  EAX = array pointer, ECX = array length
; Output: EAX = sum

ARRAY_SUM PROC
    push ebx                ; Save callee-saved registers
    push ecx
    
    xor ebx, ebx            ; EBX = 0 (counter)
    xor edx, edx            ; EDX = 0 (sum)

SUM_LOOP:
    cmp ebx, ecx            ; Check if counter >= length
    jge SUM_DONE            ; If yes, exit loop
    
    mov eax, [eax + ebx*4]  ; Load array[ebx] (4 bytes per int)
    add edx, eax            ; Add to sum
    
    inc ebx                 ; Increment counter
    jmp SUM_LOOP

SUM_DONE:
    mov eax, edx            ; Return sum in EAX
    pop ecx                 ; Restore registers
    pop ebx
    ret

ARRAY_SUM ENDP
```

### Example 2: Memory-Mapped I/O UART Communication in MIPS

```assembly
# MIPS UART Driver Example
# Memory-mapped I/O at base address 0xFFFF0000
# UART0_BASE = 0xFFFF0000
# UART DATA    offset 0: Read/Write data
# UART STATUS  offset 4: Status register
#   Bit 0: RX_READY (1 = data available)
#   Bit 5: TX_READY (1 = ready to transmit)

    .data
uart_base:  .word 0xFFFF0000

    .text
# Subroutine: UART receive character
# Returns: $v0 = received character (in lower 8 bits)
uart_getc:
    lw   $t0, uart_base     # Load UART base address
    
rx_poll:
    lw   $t1, 4($t0)        # Read status register
    andi $t1, $t1, 0x01     # Check RX_READY bit
    beq  $t1, $zero, rx_poll # Poll until ready
    
    lw   $v0, 0($t0)        # Read data register
    jr   $ra                # Return

# Subroutine: UART transmit character
# Input: $a0 = character to transmit
uart_putc:
    lw   $t0, uart_base     # Load UART base address
    
tx_poll:
    lw   $t1, 4($t0)        # Read status register
    andi $t1, $t1, 0x20     # Check TX_READY bit
    beq  $t1, $zero, tx_poll # Poll until ready
    
    sw   $a0, 0($t0)        # Write data to transmit
    jr   $ra                # Return
```

---

## 7. Delhi University Syllabus Context

This content aligns with the **NEP 2024 UGCF BSc (Hons) Computer Science** curriculum at Delhi University, specifically covering:

- **Unit III: Processor Organization and Architecture**
  - Register organization and instruction formats
  - Addressing modes (covered in Section 3.4)
  - Instruction execution cycle (covered in Section 5)
  
- **Unit IV: Memory and I/O Systems**
  - Memory mapped I/O vs port mapped I/O (covered in Section 4)
  - DMA and interrupt handling concepts

- **Practical Component**
  - Assembly language programming (x86/MIPS)
  - Debug/TASM/MARS simulator exercises

---

## 8. Key Takeaways

1. **Register Instructions** operate directly on CPU registers, providing the fastest data manipulation. They include data transfer (MOV, XCHG), arithmetic (ADD, SUB, MUL, DIV), logical (AND, OR, XOR, NOT), and control transfer (JMP, CALL, RET) operations.

2. **Memory Instructions** enable data transfer between CPU registers and main memory. The distinction between load (read) and store (write) operations is fundamental.

3. **Addressing Modes** determine how operands are specified:
   - Immediate: operand in instruction
   - Register: operand in register
   - Direct: memory address in instruction
   - Indirect: register contains memory address
   - Based/Indexed: base + offset calculations

4. **I/O Instructions** come in two forms:
   - Isolated I/O (x86 IN/OUT): separate address space
   - Memory-Mapped I/O: devices accessed via memory instructions

5. **Machine Code Representation** shows how high-level assembly instructions are encoded in binary, varying by architecture (x86 variable-length vs MIPS fixed-length formats).

6. **Instruction Execution** follows the Fetch-Decode-Execute cycle, with modern processors using pipelining to improve performance.

---

## 9. Assessment Questions

### Multiple Choice Questions (Higher-Order Thinking)

1. **Consider the x86 instruction: `MOV EAX, [EBX + ESI*4 + 100]`. What addressing mode is used?**

   a) Based addressing  
   b) Indexed addressing  
   c) Based-indexed with displacement  
   d) Register indirect addressing  

   **Answer: c**  
   **Explanation:** This instruction uses three components: Base register (EBX), Index register (ESI scaled by 4), and displacement (100). This is based-indexed addressing with displacement.

2. **In a system with memory-mapped I/O, which of the following statements is TRUE?**

   a) Special I/O instructions (IN/OUT) must be used  
   b) I/O devices share the same address space as memory  
   c) I/O operations cannot use any memory addressing modes  
   d) The CPU cannot directly access I/O device registers  

   **Answer: b**  
   **Explanation:** Memory-mapped I/O maps I/O devices into the same address space as physical memory, allowing the use of standard memory access instructions.

3. **The MIPS instruction `lw $t0, 8($sp)` is an example of:**

   a) Register indirect addressing  
   b) Base register addressing  
   c) Immediate addressing  
   d) PC-relative addressing  

   **Answer: b**  
   **Explanation:** The effective address is calculated by adding the displacement (8) to the contents of the base register ($sp). This is base register (or based) addressing.

4. **In the classic instruction fetch-execute cycle, the step where the Program Counter (PC) is loaded into the Memory Address Register (MAR) belongs to which phase?**

   a) Decode phase  
   b) Execute phase  
   c) Fetch phase  
   d) Store result phase  

   **Answer: c**  
   **Explanation:** During the fetch phase, the instruction address (held in PC) is placed into MAR to initiate the memory read.

5. **Which of the following x86 instructions will set the Zero Flag (ZF) to 1?**

   a) `MOV EAX, 0`  
   b) `XOR EAX, EAX`  
   c) `INC EAX` (when EAX was 0xFFFFFFFF)  
   d) Both (b) and (c)  

   **Answer: d**  
   **Explanation:** XORing a register with itself (EAX = EAX XOR EAX) always results in zero, setting ZF=1. INC on 0xFFFFFFFF wraps to 0x00000000, also setting ZF=1.

### Short Answer Questions

6. **Explain the difference between "load" and "store" instructions in assembly language, giving one example of each from both x86 and MIPS architectures.**

   **Answer:** Load instructions transfer data from memory to a register, while store instructions transfer data from a register to memory.  
   - x86 Load: `MOV EAX, [0x00403000]`  
   - x86 Store: `MOV [0x00403000], EAX`  
   - MIPS Load: `lw $t0, 0($t1)`  
   - MIPS Store: `sw $t0, 0($t1)`

7. **Why is register addressing faster than memory addressing? Explain with reference to the instruction execution cycle.**

   **Answer:** Register addressing is faster because registers are located inside the CPU and can be accessed in a single clock cycle. Memory addressing requires the Memory Address Register (MAR) to fetch data from RAM, which involves external bus cycles and much longer access times (typically 10-100 times slower than register access).

8. **Describe the steps involved in executing the MIPS instruction: `sw $t0, 4($t1)`.**

   **Answer:**
   1. **Fetch:** Instruction is fetched from memory at PC address
   2. **Decode:** Instruction is decoded; registers $t0 and $t1 are read
   3. **Execute:** ALU calculates effective address: contents of $t1 + 4
   4. **Memory:** Data from $t0 is written to the calculated memory address
   5. **Write-back:** PC is incremented (if not branch)

### Long Answer Questions

9. **Compare and contrast Isolated I/O (Port-Mapped I/O) and Memory-Mapped I/O. Discuss their advantages and disadvantages, and provide examples of architectures that use each approach.**

   **Answer:** (See Section 4 for detailed coverage)
   - Isolated I/O uses separate address space and dedicated instructions (IN/OUT in x86)
   - Memory-Mapped I/O uses same address space, using regular load/store (common in MIPS, ARM)
   - Each has trade-offs in address space utilization, instruction simplicity, and hardware complexity

10. **Draw and explain the instruction execution cycle with reference to the role of MAR, MDR, IR, and PC registers.**

   **Answer:** (See Section 5 for detailed coverage)
   - MAR: Holds address of memory location to access
   - MDR: Holds data being transferred to/from memory
   - IR: Holds the current instruction being executed
   - PC: Holds address of next instruction to execute

---

## 10. Flashcards

| Term | Definition |
|------|------------|
| **Register** | High-speed internal CPU memory locations used for temporary data storage during instruction execution |
| **Addressing Mode** | The method by which an instruction specifies the location of its operand(s) |
| **Immediate Addressing** | Operand value is directly encoded in the instruction |
| **Register Indirect Addressing** | Register contains the memory address of the operand |
| **Based Addressing** | Effective address = Base Register + Displacement |
| **Indexed Addressing** | Effective address = Base Register + Index Register |
| **I/O-Mapped I/O** | Separate address space for I/O devices using dedicated IN/OUT instructions |
| **Memory-Mapped I/O** | I/O devices use same address space as memory, accessed via load/store |
| **Instruction Register (IR)** | CPU register that holds the currently executing instruction |
| **Program Counter (PC)** | CPU register that holds the address of the next instruction to fetch |
| **Fetch Cycle** | Phase that retrieves an instruction from memory |
| **Execute Cycle** | Phase that performs the operation specified by the instruction |
| **Machine Code** | Binary representation of instructions executed by the CPU |
| **R-Type Instruction** | MIPS format for register-to-register operations |
| **I-Type Instruction** | MIPS format for immediate and memory operations |

---

*Generated for Delhi University BSc (Hons) Computer Science — NEP 2024 UGCF Curriculum*