# Passing File Descriptors - Summary

## Key Definitions and Concepts

- **File Descriptor**: A non-negative integer used by a process to access files, pipes, sockets, and other I/O resources in Unix/Linux systems.
- **File Descriptor Passing**: The mechanism to transfer an open file descriptor from one process to another, allowing the receiving process to access the same underlying file description.
- **Unix Domain Sockets (AF_UNIX)**: Local communication sockets used as the transport channel for passing file descriptors.
- **Ancillary Data (Control Messages)**: Additional data transmitted alongside regular socket data, used to carry file descriptors.
- **SCM_RIGHTS**: The socket control message type used to pass file descriptors between processes.

## Important Formulas and Theorems

- **Control Message Buffer Size**: `CMSG_SPACE(n * sizeof(int))` - minimum buffer size for passing n file descriptors
- **Control Message Data Length**: `CMSG_LEN(n * sizeof(int))` - length value to set in cmsghdr

## Key Points

1. File descriptors are process-specific; passing integer values between processes doesn't transfer file access capability.

2. File descriptor passing uses Unix domain sockets with sendmsg()/recvmsg() system calls.

3. The msghdr structure contains msg_control and msg_controllen fields for ancillary data.

4. CMSG_FIRSTHDR, CMSG_DATA, CMSG_SPACE, and CMSG_LEN macros are essential for control message manipulation.

5. SCM_RIGHTS (value 1) in SOL_SOCKET level indicates file descriptor passing.

6. Multiple file descriptors can be passed in a single control message.

7. The sending process can close its copy after passing, transferring ownership to the receiving process.

8. socketpair() is commonly used to create connected sockets for parent-child fd passing.

## Common Mistakes to Avoid

- **Buffer Size Too Small**: Not allocating enough space for control messages; always use CMSG_SPACE() macro.
- **Forgetting msg_controllen**: Not setting msg_controllen correctly can cause receiving to fail.
- **Wrong cmsg Level/Type**: Must use SOL_SOCKET and SCM_RIGHTS for file descriptor passing.
- **Not Checking CMSG_FIRSTHDR**: Always verify control message header is not NULL before accessing.

## Revision Tips

1. Practice constructing msghdr and cmsghdr structures by hand for exams.

2. Remember the sequence: create socket pair → fork → send/recv with control messages → extract fd from cmsghdr.

3. Review the CMSG\_\* macro definitions and their purposes thoroughly.

4. Understand the difference between sending file descriptor value vs. passing the actual descriptor.
