# Exception Priorities in ARM Cortex-M - Summary

## Key Definitions and Concepts

- **Exception**: Any event that disrupts normal program flow, including hardware interrupts, faults, and system calls
- **NVIC**: Nested Vectored Interrupt Controller - the interrupt management unit in ARM Cortex-M processors
- **Priority Level**: A numeric value determining exception handling order; lower numbers = higher priority
- **Preemption**: The ability of a higher-priority exception to interrupt a lower-priority exception handler
- **Priority Grouping**: Splitting priority bits into group priority (for preemption) and sub-priority (for ordering)
- **BASEPRI**: Register that masks exceptions below a configurable priority threshold
- **PRIMASK**: Register that masks all configurable exceptions (except NMI and Hard Fault)
- **Stack Frame**: The 8-register context (R0-R3, R12, LR, PC, xPSR) automatically saved during exception entry

## Important Formulas and Concepts

- **Maximum Priority Levels**: 2^n where n = number of implemented priority bits (typically 4-8 bits)
- **Priority Grouping**: Total bits = group bits + sub-priority bits; PRIGROUP value determines split
- **Priority Comparison**: Exception A can preempt Exception B if Priority(A) < Priority(B)
- **Stack Requirement**: 32 bytes minimum for exception stack frame; more for nested handlers

## Key Points

1. ARM Cortex-M supports up to 240 external interrupts plus system exceptions like Reset, NMI, Hard Fault, SVCall, PendSV, and SysTick

2. Priority 0 is the highest priority; maximum priority value depends on implementation (commonly 15 or 255)

3. The NVIC handles priority automatically - no software intervention needed for basic nested interrupts

4. Priority grouping divides priority bits into group priority (for preemption) and sub-priority (for ordering among same-group exceptions)

5. BASEPRI provides finer control than PRIMASK by allowing selective masking based on priority threshold

6. Exception handlers must clear pending flags before returning to prevent repeated interrupts

7. Stack size must account for nested exception scenarios - worst-case nesting depth determines minimum stack requirement

8. Higher-priority exceptions (lower numbers) can preempt lower-priority exceptions (higher numbers)

9. The vector table contains the initial SP value followed by handler addresses for each exception type

10. Cortex-M0 supports 2-4 priority bits, M3/M4 support 4-8 priority bits depending on implementation

## Common Mistakes to Avoid

1. **Reversing Priority Logic**: Many students confuse that lower numeric values mean higher priority. Remember: Priority 0 = highest, Priority 255 = lowest.

2. **Forgetting to Enable Interrupts**: Configuring priority without enabling the interrupt in NVIC_ISER is a common error.

3. **Not Clearing Pending Flags**: Leaving interrupt pending flags set causes the handler to be called repeatedly.

4. **Insufficient Stack Allocation**: Underestimating stack requirements for nested exceptions leads to stack overflow.

5. **Incorrect BASEPRI Interpretation**: Remember BASEPRI masks exceptions with priority ≥ BASEPRI value (numerically greater or equal).

## Revision Tips

1. Draw the exception processing sequence and priority comparison flowchart to reinforce conceptual understanding

2. Practice writing code to configure NVIC registers with different priority values and observe the behavior in simulation

3. Memorize the standard exception types and their default priority values (Reset = -3, NMI = -2, Hard Fault = -1)

4. Review sample questions on priority grouping calculations and priority masking with BASEPRI

5. Understand the difference between preemption priority (group priority) and sub-priority by working through multiple-interrupt scenarios
