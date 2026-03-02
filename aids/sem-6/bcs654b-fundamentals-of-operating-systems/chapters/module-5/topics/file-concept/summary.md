# File Concept in Operating Systems - Summary

## Key Definitions and Concepts

A file is a named collection of related information stored on secondary storage, providing logical abstraction over physical storage details. The operating system's file system manages all file operations and storage allocation.

The file control block (FCB) or i-node is the kernel data structure that stores all information about a file except its name, including location, size, protection bits, and timestamps.

A file descriptor is a small non-negative integer returned by the operating system when a file is opened, used by processes to reference open files.

## Important Formulas and Theorems

Maximum file size depends on the addressing scheme used. For example, with n bits for block number and a block size of B bytes, the maximum file size is (2^n) × B bytes.

File access time for sequential access is O(n) where n is the number of records, while direct access provides O(1) access time to any record.

The open file table maintains a one-to-one mapping between process file descriptors and system-wide file table entries, allowing controlled file sharing.

## Key Points

Files are identified by unique names within their directory and possess attributes including type, size, protection permissions, creation/modification timestamps, and location information.

File types include regular files (user data), directories (organizational structures), character special files (sequential devices), and block special files (random access devices).

Core file operations include create, open, read, write, seek (for repositioning), close, delete, rename, and truncate—each requiring specific system calls.

Sequential access processes records in order; direct access enables random positioning to any file block; indexed access uses auxiliary index structures for efficient retrieval.

The open file table operates at two levels: per-process file descriptor table and system-wide open file table, with in-memory i-nodes providing metadata caching.

Multiple processes can share file table entries, allowing coordinated access through shared file descriptors or independent entries with separate file pointers.

File buffering improves performance by reducing disk I/O operations—data is accumulated in memory buffers and written to disk in chunks.

## Common Mistakes to Avoid

Confusing file descriptors with file names—descriptors are internal process references while names are user-visible identifiers.

Assuming all files support random access—some file types (like pipes and terminal devices) are inherently sequential.

Forgetting that file pointers are per-process—different processes opening the same file maintain separate file positions.

Overlooking the difference between deleting a file and truncating it—deletion removes the file entirely while truncation preserves the file entry but removes content.

Ignoring file buffering behavior—data written to a file may not be immediately persisted to disk, potentially causing data loss if the system crashes before buffers are flushed.

## Revision Tips

Draw diagrams showing the open file table structure and the relationship between file descriptors, system file table entries, and i-nodes to visualize data flow.

Create a comparison table of file access methods with their advantages, disadvantages, and typical applications.

Practice mapping high-level file operations to their corresponding system calls and understanding what happens in the kernel at each step.

Review how file concepts integrate with directory structures and protection mechanisms, as these topics are directly related in the module.