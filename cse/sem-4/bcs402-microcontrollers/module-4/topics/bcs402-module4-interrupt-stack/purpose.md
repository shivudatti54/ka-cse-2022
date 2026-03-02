# Learning Objectives

After studying this topic, you should students able to:

1. Explain the composition of the hardware stack frame pushed during ARM Cortex-M exception entry and identify which registers are automatically saved.

2. Describe the complete exception entry sequence, including stack frame push, LR loading with EXC_RETURN value, and CONTROL register updates.

3. Analyze the difference between MSP and PSP usage in ARM Cortex-M processors and select appropriate configurations for different application scenarios.

4. Design interrupt service routines with proper prologue and epilogue code, ensuring all modified registers are correctly saved and restored.

5. Calculate worst-case stack depth requirements for systems with nested interrupt handling, considering hardware frames, manual saves, and function call overhead.

6. Compare hardware-based and software-based stack overflow detection mechanisms, evaluating their suitability for different reliability requirements.

7. Explain the purpose and encoding of EXC_RETURN values in exception handling and describe how they control the return sequence.

8. Evaluate interrupt priority configurations for real-time systems, balancing response latency requirements against stack usage constraints.
