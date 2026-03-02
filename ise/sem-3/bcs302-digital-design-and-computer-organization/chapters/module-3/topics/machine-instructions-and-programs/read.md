assembly
        LDI R1, #10      ; Load Immediate: R1 = 10
        LDI R2, #15      ; Load Immediate: R2 = 15
        ADD R3, R1, R2   ; Add: R3 = R1 + R2 (R3 now holds 25)
        STORE R3, SUM    ; Store the result in memory location 'SUM'
HALT:   JMP HALT         ; Halt the program (an infinite loop)
SUM:    .DATA 0          ; Reserve a word of data, initialized to 0