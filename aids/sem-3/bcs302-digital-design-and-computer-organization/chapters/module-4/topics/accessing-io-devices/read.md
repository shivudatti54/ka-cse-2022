assembly
LOOP: IN STATUS_REGISTER    ; Read the device status register
      TEST READY_BIT        ; Check the "ready" bit
      JZ LOOP               ; If not ready, jump back to LOOP
      IN DATA_REGISTER      ; If ready, read the data