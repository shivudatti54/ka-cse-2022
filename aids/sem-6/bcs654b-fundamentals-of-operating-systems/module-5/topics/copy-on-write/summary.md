# Copy-on-Write

## Overview

Copy-on-write (COW) is an optimization technique where parent and child processes initially share same pages after fork(). Pages are copied only when one process modifies shared page, reducing memory usage and speeding up process creation.

## Key Points

- **Fork Optimization**: Initially child shares parent's pages instead of copying, marked copy-on-write
- **Page Modification**: When process writes to COW page, trap occurs, OS copies page, updates page table
- **Memory Savings**: Avoid copying unused pages, child often immediately exec() replacing address space
- **Page Table Entries**: COW pages marked read-only, write attempt triggers page fault
- **Free Page Pool**: OS maintains pool of free frames for COW copies and new allocations
- **Zero-Fill-On-Demand**: New pages filled with zeros before first use, security measure
- **vfork()**: Variant where child borrows parent's address space without copying, must immediately exec()

## Important Concepts

- COW makes fork() much faster by deferring and avoiding copies
- Most forked processes exec() immediately, making full copy wasteful
- Write to COW page triggers page fault, OS allocates new frame and copies content
- COW especially beneficial in systems with many short-lived child processes

## Notes

- Understand COW mechanism: share until write, then copy
- Know page fault sequence for COW: detect write to read-only COW page → allocate frame → copy → update page table → restart
- Practice scenarios: fork() followed by exec() benefits most from COW
- Remember COW applies to other resources too (files, buffers)
