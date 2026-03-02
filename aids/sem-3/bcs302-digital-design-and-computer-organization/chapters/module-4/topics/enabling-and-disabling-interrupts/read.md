asm
    CLI           ; Disable interrupts (Enter critical section)
    MOV [AX], BX  ; Update first pointer
    MOV [DX], CX  ; Update second pointer
    STI           ; Enable interrupts (Exit critical section)