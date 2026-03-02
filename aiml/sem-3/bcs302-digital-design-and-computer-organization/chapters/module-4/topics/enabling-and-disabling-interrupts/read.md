asm
; Critical Section Begins
CLI                  ; Disable interrupts (IE = 0)

MOV AX, [shared_var] ; Read the shared variable
INC AX               | These three instructions must
MOV [shared_var], AX ; Update it         | not be interrupted

STI                  ; Re-enable interrupts (IE = 1)
; Critical Section Ends