ADD R1, R2, R3  ; R1 = R2 + R3
    BZ  R1, LOOP    ; Branch to label LOOP if the result in R1 is Zero
    ...             ; Next instructions (executed if branch not taken)
LOOP:
    ...             ; Instructions for the loop