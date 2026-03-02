# Overflow Attacks and Countermeasures - Summary

## Key Definitions and Concepts

- **Buffer Overflow**: Writing data beyond the allocated buffer boundaries, potentially corrupting adjacent memory
- **Stack-Based Overflow**: Exploits local buffers on the stack, overwriting return addresses to control program execution
- **Heap-Based Overflow**: Exploits dynamically allocated memory by corrupting allocator metadata structures
- **Shellcode**: Machine code injected by attackers to perform malicious operations
- **Return-Oriented Programming (ROP)**: Exploitation technique chaining existing code fragments (gadgets) to bypass DEP
- **Stack Canary**: Security value placed between buffers and return addresses to detect overflows

## Important Formulas and Techniques

- Buffer offset calculation: `buffer_size + sizeof(saved_registers) + sizeof(return_address)`
- Heap chunk structure: `prev_size + size + user_data + metadata`
- Exploit payload structure: `[padding][overwritten_address][shellcode/gadget_addresses]`

## Key Points

- Buffer overflows occur when programs write beyond allocated memory boundaries without bounds checking
- Stack overflows target return addresses to hijack program control flow
- Heap overflows corrupt memory allocator metadata for exploitation
- Integer overflows can cause incorrect size calculations leading to buffer overflows
- Compile-time protections: Stack canaries, PIE, FORTIFY_SOURCE
- Runtime protections: ASLR randomizes memory addresses, DEP prevents code execution
- Modern systems use multiple overlapping defenses (defense-in-depth)
- Safe functions: strncpy, snprintf, fgets instead of strcpy, sprintf, gets

## Common Mistakes to Avoid

1. Assuming Stack Canaries are unbreakable - they can be brute-forced or leaked
2. Using strncpy without ensuring null-termination (it doesn't guarantee null byte)
3. Forgetting that integer overflows can bypass size checks before allocation
4. Relying solely on one security measure without defense-in-depth approach

## Revision Tips

1. Draw the stack frame layout from memory - practice until automatic
2. List all dangerous functions and their safer alternatives
3. Understand why each countermeasure helps and its limitations
4. Review recent CVEs related to buffer overflows for real-world context
5. Practice identifying vulnerable code patterns in exam-style questions