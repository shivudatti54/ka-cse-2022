# Copy On Write - Summary

## Key Definitions and Concepts

- **Copy On Write (COW)**: A memory management optimization technique where memory pages are shared between processes until a write operation requires a private copy.
- **COW Page**: A memory page marked as read-only that triggers a page fault when written to, causing the kernel to create a private copy.
- **Reference Count**: A counter associated with each shared physical page indicating how many processes currently reference that page.
- **Lazy Evaluation**: The COW principle of deferring expensive operations (memory copying) until absolutely necessary.

## Important Formulas and Mechanisms

- **Fork with COW**: Child page table entries initially point to parent's physical frames with read-only protection.
- **Page Fault Sequence**: Write attempt → MMU triggers fault → Kernel identifies COW fault → Allocates new page → Copies data → Updates page table → Continues execution.
- **Reference Counting**: Increment on fork/shared page creation, decrement on process exit or COW copy. Page freed when count equals zero.

## Key Points

- COW allows multiple processes to share identical memory pages without consuming additional memory until modification is required.
- The fork() system call with COW optimization creates child processes that share parent pages in read-only mode.
- When either parent or child writes to a COW page, the kernel creates a private copy for the writing process.
- COW dramatically improves fork() performance because the actual copy is deferred or avoided entirely.
- Most child processes call exec() after fork(), making COW especially valuable since copied pages may never be used.
- Linux KSM (Kernel Same-page Merging) applies COW to merge identical pages across different processes.
- COW file systems like Btrfs and ZFS use copy-on-write semantics for atomic updates and snapshots.
- Reference counting is essential to ensure shared pages are freed only when no process needs them.

## Common Mistakes to Avoid

- Confusing COW with regular memory sharing—COW creates private copies on write, regular sharing does not.
- Thinking fork() always copies memory—COW means copying happens only on modification, not at fork time.
- Forgetting that COW requires hardware support (MMU) for page protection bits.
- Overlooking that reference counting must be tracked for proper memory management.

## Revision Tips

- Draw the memory layout before and after a fork with COW to visualize page sharing.
- Memorize the sequence: fork creates shared read-only pages → write triggers fault → kernel copies → remap.
- Practice explaining COW benefits in the context of fork-exec combination.
- Remember that COW is an optimization, not a requirement—it can be disabled if needed.
- Review how COW applies to modern technologies like containers and virtualization.