# Passing File Descriptors in Unix/Linux

## Introduction

File descriptors are fundamental to Unix/Linux operating systems, serving as integer handles that processes use to access files, pipes, sockets, and other I/O resources. In inter-process communication (IPC), there often arises a need to transfer an open file descriptor from one process to another. This capability is crucial for implementing sophisticated IPC mechanisms like Unix domain sockets, privilege delegation, and custom server architectures.

The passing of file descriptors (also known as "file descriptor passing" or "file descriptor transfer") allows one process to transfer ownership of an open file descriptor to another process within the same system. Unlike simply passing the integer value of a file descriptor, which would be meaningless to the receiving process (as it would refer to a different entry in that process's file descriptor table), this mechanism enables the actual transfer of the kernel-level file description along with all its associated states, including file offset, access mode, and flags.

This topic is particularly important for CSE students as it represents an advanced IPC technique that demonstrates deep understanding of Unix kernel internals, file descriptor management, and process communication paradigms. It is extensively used in production systems for implementing servers, daemons, and various forms of inter-process coordination.

## Key Concepts

### File Descriptor Fundamentals

A file descriptor is a small non-negative integer that the kernel uses to identify an open file for a process. When a process opens a file, the kernel creates a file description (struct file in kernel terms) and allocates a file descriptor, which is essentially an index into the process's file descriptor table. The file descriptor table entry points to the file description, which in turn points to the actual file or device.

Key characteristics of file descriptors include:

- Each process has its own file descriptor table
- File descriptors are typically inherited across fork() but can be manipulated
- Standard file descriptors: 0 (stdin), 1 (stdout), 2 (stderr)
- File descriptors are process-specific resources

### The Need for File Descriptor Passing

Consider a scenario where process A opens a file and wants process B to read from or write to that file. Simply sending the integer file descriptor value (say, 5) to process B would be useless because:

- Process B's file descriptor table may have different entries at index 5
- Process B has no knowledge of the file that process A opened

File descriptor passing solves this by transferring the actual kernel file description, allowing process B to obtain a new file descriptor that refers to the same underlying file description.

### Mechanisms for Passing File Descriptors

#### 1. Unix Domain Sockets with Ancillary Data

The primary and most common method for passing file descriptors uses Unix domain sockets (AF_UNIX) along with ancillary data (also called control messages). This approach uses the sendmsg() and recvmsg() system calls, which support sending auxiliary data alongside regular data.

**Components involved:**

- **cmsghdr structure**: Control message header that contains metadata about the passed file descriptor
- **cmsg**: Control message containing the actual file descriptor(s)
- **SCM_RIGHTS**: The protocol-level type indicating file descriptor passing

The control message is embedded in the msghdr structure using the msg_control and msg_controllen fields.

#### 2. The sendmsg() System Call

```c
#include <sys/socket.h>
#include <sys/uio.h>

ssize_t sendmsg(int sockfd, const struct msghdr *msg, int flags);
```

For passing file descriptors, the msghdr structure must include:

- msg_name: Socket address (for connected sockets, can be NULL)
- msg_iov: I/O vector for data
- msg_iovlen: Number of elements in msg_iov
- msg_control: Pointer to control message buffer
- msg_controllen: Size of control message buffer

The control message (cmsghdr) must be constructed with:

- cmsg_len: Length of control message
- cmsg_level: SOL_SOCKET
- cmsg_type: SCM_RIGHTS
- cmsg_data: Array of file descriptors to pass

#### 3. The recvmsg() System Call

```c
#include <sys/socket.h>

ssize_t recvmsg(int sockfd, struct msghdr *msg, int flags);
```

The receiving process uses recvmsg() to receive both data and file descriptors. The file descriptors are extracted from the control message after receiving.

### Important Considerations

1. **File Descriptor Duplication**: When a file descriptor is passed, it is duplicated in the receiving process. The sending process can choose to close its copy or keep it open.

2. **Number of Descriptors**: Multiple file descriptors can be passed in a single control message using an array.

3. **Socket Pair**: Typically, a pair of connected Unix domain sockets (created using socketpair()) is used as the communication channel.

4. **Inheritance**: File descriptors passed via Unix domain sockets are properly handled across fork() and can be used for parent-child communication.

5. **Close-on-Exec Flag**: While not directly related to passing, it's good practice to manage the close-on-exec flag for passed file descriptors.

## Examples

### Example 1: Basic File Descriptor Passing Between Parent and Child

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <string.h>
#include <errno.h>

// Helper function to create control message for passing fd
void send_fd(int socket, int fd_to_send) {
 struct msghdr msg = {0};
 struct cmsghdr *cmsg;
 char buf[CMSG_SPACE(sizeof(int))];
 int zero = 0;

 // Set up I/O vector (sending one zero byte)
 struct iovec iov[1];
 iov[0].iov_base = &zero;
 iov[0].iov_len = sizeof(int);
 msg.msg_iov = iov;
 msg.msg_iovlen = 1;

 // Set up control message
 msg.msg_control = buf;
 msg.msg_controllen = CMSG_SPACE(sizeof(int));

 cmsg = CMSG_FIRSTHDR(&msg);
 cmsg->cmsg_level = SOL_SOCKET;
 cmsg->cmsg_type = SCM_RIGHTS;
 cmsg->cmsg_len = CMSG_LEN(sizeof(int));

 // Copy file descriptor to control message
 *((int *)CMSG_DATA(cmsg)) = fd_to_send;

 // Send the file descriptor
 if (sendmsg(socket, &msg, 0) < 0) {
 perror("sendmsg failed");
 exit(1);
 }
}

// Helper function to receive file descriptor
int receive_fd(int socket) {
 struct msghdr msg = {0};
 struct cmsghdr *cmsg;
 char buf[CMSG_SPACE(sizeof(int))];
 int received_fd = -1;
 int zero = 0;

 // Set up I/O vector
 struct iovec iov[1];
 iov[0].iov_base = &zero;
 iov[0].iov_len = sizeof(int);
 msg.msg_iov = iov;
 msg.msg_iovlen = 1;

 // Set up control message buffer
 msg.msg_control = buf;
 msg.msg_controllen = CMSG_SPACE(sizeof(int));

 // Receive the message
 if (recvmsg(socket, &msg, 0) < 0) {
 perror("recvmsg failed");
 return -1;
 }

 // Extract file descriptor from control message
 cmsg = CMSG_FIRSTHDR(&msg);
 if (cmsg && cmsg->cmsg_level == SOL_SOCKET &&
 cmsg->cmsg_type == SCM_RIGHTS) {
 received_fd = *((int *)CMSG_DATA(cmsg));
 }

 return received_fd;
}

int main() {
 int sv[2]; // Socket pair
 int file_fd;

 // Create socket pair for parent-child communication
 if (socketpair(AF_UNIX, SOCK_STREAM, 0, sv) < 0) {
 perror("socketpair");
 exit(1);
 }

 // Open a test file
 file_fd = open("test.txt", O_RDWR | O_CREAT, 0644);
 if (file_fd < 0) {
 perror("open");
 exit(1);
 }

 printf("Original file descriptor: %d\n", file_fd);

 // Fork to create child process
 if (fork() == 0) {
 // Child process
 close(sv[0]); // Close unused end

 // Receive file descriptor from parent
 int received_fd = receive_fd(sv[1]);
 printf("Child received file descriptor: %d\n", received_fd);

 // Write to the file using received fd
 const char *msg = "Hello from child!\n";
 write(received_fd, msg, strlen(msg));

 close(received_fd);
 close(sv[1]);
 exit(0);
 } else {
 // Parent process
 close(sv[1]); // Close unused end

 // Send file descriptor to child
 send_fd(sv[0], file_fd);

 // Parent can still use the file
 const char *msg = "Hello from parent!\n";
 write(file_fd, msg, strlen(msg));

 close(file_fd);
 close(sv[0]);
 wait(NULL); // Wait for child
 }

 return 0;
}
```

### Example 2: Server-Client File Descriptor Passing

This example demonstrates a server process passing a connected socket to a worker process:

```c
// Server process passes client socket to worker
void pass_client_to_worker(int worker_socket, int client_fd) {
 struct msghdr msg = {0};
 struct cmsghdr *cmsg;
 char buf[CMSG_SPACE(sizeof(int))];

 char dummy = 'x';
 struct iovec iov[1];
 iov[0].iov_base = &dummy;
 iov[0].iov_len = 1;
 msg.msg_iov = iov;
 msg.msg_iovlen = 1;

 msg.msg_control = buf;
 msg.msg_controllen = CMSG_SPACE(sizeof(int));

 cmsg = CMSG_FIRSTHDR(&msg);
 cmsg->cmsg_level = SOL_SOCKET;
 cmsg->cmsg_type = SCM_RIGHTS;
 cmsg->cmsg_len = CMSG_LEN(sizeof(int));
 *((int *)CMSG_DATA(cmsg)) = client_fd;

 if (sendmsg(worker_socket, &msg, 0) < 0) {
 perror("sendmsg");
 }
}

// Worker process receives client socket
int receive_client_socket(int worker_socket) {
 struct msghdr msg = {0};
 struct cmsghdr *cmsg;
 char buf[CMSG_SPACE(sizeof(int))];
 char dummy;
 int client_fd = -1;

 struct iovec iov[1];
 iov[0].iov_base = &dummy;
 iov[0].iov_len = 1;
 msg.msg_iov = iov;
 msg.msg_iovlen = 1;

 msg.msg_control = buf;
 msg.msg_controllen = CMSG_SPACE(sizeof(int));

 if (recvmsg(worker_socket, &msg, 0) < 0) {
 perror("recvmsg");
 return -1;
 }

 for (cmsg = CMSG_FIRSTHDR(&msg); cmsg != NULL;
 cmsg = CMSG_NXTHDR(&msg, cmsg)) {
 if (cmsg->cmsg_level == SOL_SOCKET &&
 cmsg->cmsg_type == SCM_RIGHTS) {
 client_fd = *((int *)CMSG_DATA(cmsg));
 break;
 }
 }

 return client_fd;
}
```

## Exam Tips

1. **Understand the Difference**: Distinguish between passing file descriptor values (integers) versus passing actual file descriptors. Only the latter transfers the kernel file description.

2. **Remember the Key System Calls**: The sendmsg() and recvmsg() system calls are essential for file descriptor passing. Understand their structure, especially the msghdr and cmsghdr structures.

3. **SCM_RIGHTS is Critical**: Remember that SCM_RIGHTS (socket control message rights) is the protocol-level type used for file descriptor passing in Unix domain sockets.

4. **CMSG\_\* Macros**: Be familiar with CMSG_FIRSTHDR, CMSG_NXTHDR, CMSG_DATA, CMSG_SPACE, and CMSG_LEN macros for manipulating control messages.

5. **Socketpair Usage**: In parent-child scenarios, socketpair() is commonly used to create connected Unix domain sockets for fd passing.

6. **Buffer Size Calculation**: When receiving file descriptors, the control message buffer must be at least CMSG_SPACE(sizeof(int)) bytes to accommodate the control message header and data.

7. **Common Use Cases**: Remember common applications include Unix domain socket passing (for privilege dropping in servers), passing open files between processes, and implementing custom IPC mechanisms.

8. **Process-Specific Descriptors**: Understand that file descriptors are process-specific; passing a descriptor from one process to another creates a new descriptor entry in the receiving process that points to the same kernel file description.
