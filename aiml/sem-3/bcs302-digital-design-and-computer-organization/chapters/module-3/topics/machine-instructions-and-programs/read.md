assembly
LOAD    R1, [1000]    ; Load value from memory address 1000 into register R1 (R1 = X)
LOAD    R2, [1004]    ; Load value from memory address 1004 into register R2 (R2 = Y)
ADD     R3, R1, R2    ; Add R1 and R2, store result in R3 (R3 = X + Y)
STORE   R3, [1008]    ; Store the value in R3 to memory address 1008 (Z = R3)