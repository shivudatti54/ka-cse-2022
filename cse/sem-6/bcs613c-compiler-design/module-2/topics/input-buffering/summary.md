# Input Buffering

## Overview

Input buffering is an essential optimization technique that enables efficient character reading from source files. The two-buffer scheme minimizes I/O operations while supporting lookahead requirements for token recognition.

## Key Points

- **Purpose**: Reduces I/O operations, minimizes system call overhead, and supports efficient lookahead
- **Two-Buffer Scheme**: Divides buffer into two halves filled alternately, enabling continuous processing
- **Sentinel-Based Buffering**: Uses special characters at buffer ends to simplify boundary checking
- **Lookahead Operations**: Peek (examine without consuming), consume (advance), and retract (move back)
- **Pointer Management**: Lexemebegin marks token start, forward scans ahead until pattern matches
- **Buffer Sizes**: Typically 4KB to 64KB based on system architecture and cache characteristics

## Important Concepts

- Double buffering prevents I/O wait time
- Sentinels eliminate explicit boundary checks in inner loops
- Tokens spanning buffer boundaries require careful state management
- Memory-mapped files offer modern alternative to manual buffering

## Notes

- Draw and explain the two-buffer scheme with pointers
- Understand how sentinels simplify the scanning loop
- Explain why buffer size optimization depends on system architecture
