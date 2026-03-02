assembly
section .text
; ... some code ...
CLI ; Clear Interrupt Flag (Disable Interrupts)
; CRITICAL SECTION START
; Code that updates a shared variable in memory
; CRITICAL SECTION END
STI ; Set Interrupt Flag (Enable Interrupts)
; ... resume normal code ...
