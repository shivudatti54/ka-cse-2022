# Copy On Write (COW) - Summary

## Key Definitions

- **Copy On Write (COW)**: A memory management optimization technique where multiple processes share physical memory pages initially, with copying deferred until a process attempts to modify a page.

- **COW Page**: A memory page that is mapped as read-only in multiple processes' page tables but points to the same physical memory location.

- **Reference Count**: A counter maintained for each shared COW page indicating the number of processes currently sharing that physical page.

## Important Formulas

- **Memory savings**: With traditional fork, memory required = 2 × parent memory. With COW, actual memory = parent memory + (pages actually modified × page size).

- **Reference count management**: When reference count = 0, page is reclaimed; when count > 1, page remains shared; when count = 1 and write occurs, no copy is needed.

## Key Points

1. COW marks forked pages as read-only, allowing parent and child to share physical memory initially.

2. Page faults trigger the actual copying: write attempt → fault → allocate new page → copy → update page table.

3. COW dramatically improves `fork()` performance by avoiding immediate page copying.

4. Maximum benefit occurs when `fork()` is followed by `exec()`, as copied pages are discarded anyway.

5. Reference counting enables safe page reclamation when all sharing processes terminate.

6. Read-only file mappings (code segments) are permanently shared without COW overhead.

7. Modern Unix-like systems (Linux, BSD, macOS) extensively use COW for memory efficiency.

8. COW differs from `vfork()`: `vfork()` suspends the parent and shares the entire address space, while COW maintains separate address spaces with physical page sharing.

9. Linux implements COW through vm_area_struct structures that identify COW-eligible memory regions.

10. The technique was pioneered in research operating systems and became standard in commercial Unix systems.

## Common Mistakes

1. **Confusing COW with shared memory**: COW provides separate virtual address spaces with physical sharing, while System V shared memory allows direct address sharing.

2. **Assuming all pages are copied at fork**: Only modified pages are copied; most pages remain shared if never written to.

3. **Overlooking the page fault overhead**: COW adds overhead on first write to each shared page, which can be significant for processes that modify many pages.

4. **Confusing fork with vfork**: Students often believe `vfork()` uses COW, but `vfork()` literally shares the parent's address space without copying.