# Operating System Debugging


## Table of Contents

- [Operating System Debugging](#operating-system-debugging)
- [Introduction](#introduction)
- [Failure Analysis](#failure-analysis)
  - [Log Files](#log-files)
  - [Core Dumps](#core-dumps)
  - [Kernel Crash (Panic/BSOD)](#kernel-crash-panicbsod)
- [Performance Tuning and Monitoring](#performance-tuning-and-monitoring)
  - [Key Performance Metrics](#key-performance-metrics)
  - [Important Monitoring Tools](#important-monitoring-tools)
  - [Performance Bottleneck Identification](#performance-bottleneck-identification)
- [Tracing](#tracing)
  - [strace (Linux)](#strace-linux)
  - [ltrace (Linux)](#ltrace-linux)
  - [DTrace](#dtrace)
  - [BCC (BPF Compiler Collection) Tools](#bcc-bpf-compiler-collection-tools)
- [Profiling](#profiling)
  - [Profiling Tools](#profiling-tools)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

**Debugging** is the activity of finding and fixing errors (bugs) in a system -- both hardware and software. Operating system debugging involves identifying and resolving issues related to performance bottlenecks, system crashes, and process failures. The OS provides tools and mechanisms to help with debugging at various levels.

> **Definition:** OS debugging involves failure analysis, performance tuning, and the use of tracing and profiling tools to find and fix errors in the operating system and the applications running on it.

## Failure Analysis

When a process fails, the OS can capture information about the error to help developers diagnose the problem.

### Log Files

The OS writes error information and diagnostic messages to **log files**. These logs record events, errors, and warnings that can be analyzed to find the cause of failures.

```
Common Log Locations (Linux):
+------------------------------------------+
| /var/log/syslog - System messages |
| /var/log/kern.log - Kernel messages |
| /var/log/auth.log - Authentication logs |
| /var/log/dmesg - Boot messages |
| /var/log/messages - General messages |
+------------------------------------------+
```

**Example log entry:**

```
Feb 12 10:15:23 server kernel: Out of memory: Kill process 1234 (firefox)
Feb 12 10:15:23 server kernel: Killed process 1234 (firefox) total-vm:2048kB
```

### Core Dumps

When a process crashes (e.g., segmentation fault, division by zero), the OS can save a snapshot of the process's memory to a file called a **core dump**. Developers can then analyze this file using a debugger to determine the exact point of failure.

```
Process Running
 |
 Error occurs (e.g., segfault)
 |
 v
+------------------+ +------------------+
| OS captures | --> | Core Dump File |
| process memory | | (core, core.1234)|
| state | +------------------+
+------------------+ |
 Developer uses
 debugger (gdb)
 |
 +------v-------+
 | Analyze dump |
 | Find bug |
 +--------------+
```

**Analyzing a core dump with gdb:**

```bash
$ gdb ./program core
(gdb) backtrace # Show the call stack at crash
(gdb) info registers # Show CPU register values
(gdb) print variable # Show variable values
```

### Kernel Crash (Panic/BSOD)

When the **kernel** itself crashes:

- **Linux:** Produces a **kernel panic** message on the console and optionally a **crash dump** (vmcore)
- **Windows:** Displays the **Blue Screen of Death (BSOD)** and creates a **memory dump** file (MEMORY.DMP)

```
Kernel Error:
+------------------------------------------+
| Linux: "Kernel panic - not syncing: ..." |
| -> Crash dump saved to /var/crash/ |
| -> Analyzed using 'crash' utility |
| |
| Windows: Blue Screen of Death (BSOD) |
| -> Memory dump saved to MEMORY.DMP |
| -> Analyzed using WinDbg |
+------------------------------------------+
```

## Performance Tuning and Monitoring

Performance tuning involves identifying and removing **bottlenecks** -- components that limit system performance. The OS provides various tools for monitoring system performance.

### Key Performance Metrics

| Metric                 | Description                      | Tool (Linux)            |
| ---------------------- | -------------------------------- | ----------------------- |
| **CPU usage**          | Percentage of CPU time used      | `top`, `htop`, `mpstat` |
| **Memory usage**       | RAM used vs available            | `free`, `vmstat`        |
| **Disk I/O**           | Read/write operations per second | `iostat`, `iotop`       |
| **Network throughput** | Data transfer rate               | `netstat`, `iftop`      |
| **Process status**     | State of running processes       | `ps`, `top`             |
| **Load average**       | Average system load over time    | `uptime`, `w`           |

### Important Monitoring Tools

#### top / htop

Interactive real-time process viewer. Shows CPU, memory, and process information.

```
$ top
top - 10:30:15 up 5 days, 3:22, 2 users, load average: 1.23, 0.98, 0.87
Tasks: 256 total, 2 running, 254 sleeping, 0 stopped, 0 zombie
%Cpu(s): 15.3 us, 3.2 sy, 0.0 ni, 80.5 id, 0.7 wa, 0.0 hi, 0.3 si
MiB Mem : 16384.0 total, 4096.0 free, 8192.0 used, 4096.0 cached

 PID USER PR NI VIRT RES SHR S %CPU %MEM COMMAND
 1234 user 20 0 2048m 512m 64m R 25.3 3.1 firefox
 5678 root 20 0 256m 32m 16m S 5.1 0.2 Xorg
```

#### ps (Process Status)

Shows a snapshot of current processes.

```bash
$ ps aux # All processes with details
$ ps -ef # Full format listing
$ ps -p 1234 # Info about specific process
```

#### vmstat (Virtual Memory Statistics)

Reports information about processes, memory, paging, block I/O, and CPU activity.

```bash
$ vmstat 1 5 # Report every 1 second, 5 times
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r b swpd free buff cache si so bi bo in cs us sy id wa st
 1 0 0 4096000 32000 2048000 0 0 10 20 150 300 15 3 80 2 0
```

#### iostat

Reports CPU and I/O statistics for devices.

```bash
$ iostat -x 1 # Extended I/O stats every 1 second
Device: rrqm/s wrqm/s r/s w/s rMB/s wMB/s await %util
sda 0.00 5.00 10.0 20.0 0.50 1.00 5.00 15.00
```

### Performance Bottleneck Identification

```
+------------------------------------------+
| Bottleneck Identification Process |
+------------------------------------------+
| |
| 1. Monitor system metrics (top, vmstat) |
| 2. Identify the bottleneck: |
| - CPU bound? (high CPU %, low I/O) |
| - Memory bound? (high swap usage) |
| - I/O bound? (high wait time) |
| - Network bound? (high latency) |
| 3. Investigate the specific component |
| 4. Apply fix (tune parameters, upgrade) |
| 5. Re-measure to verify improvement |
+------------------------------------------+
```

## Tracing

**Tracing** involves recording the sequence of system calls, signals, and other events that a process generates. Tracing tools help developers understand how a program interacts with the OS.

### strace (Linux)

`strace` traces all system calls made by a process.

```bash
$ strace ls
execve("/bin/ls", ["ls"], ...) = 0
openat(AT_FDCWD, ".", O_RDONLY) = 3
getdents64(3, ...) = 512
write(1, "file1.txt file2.txt\n", 21) = 21
close(3) = 0
exit_group(0) = ?
```

### ltrace (Linux)

`ltrace` traces library calls (e.g., calls to libc functions like printf, malloc).

```bash
$ ltrace ./program
printf("Hello, World!\n") = 14
malloc(100) = 0x55a1234
free(0x55a1234) = <void>
```

### DTrace

**DTrace** is a comprehensive dynamic tracing framework originally developed by Sun Microsystems for Solaris. It allows administrators to trace both user-level and kernel-level events in real time without restarting the system.

**Key features:**

- Traces both user-space and kernel-space events
- Uses the D scripting language for defining trace probes
- Minimal performance impact when enabled
- Available on Solaris, macOS, FreeBSD, and (partially) Linux

### BCC (BPF Compiler Collection) Tools

**BCC** is a modern tracing toolkit for Linux based on **eBPF (extended Berkeley Packet Filter)**. It provides powerful tools for performance analysis and debugging.

| BCC Tool     | Purpose                                |
| ------------ | -------------------------------------- |
| `execsnoop`  | Trace new process execution            |
| `opensnoop`  | Trace file opens                       |
| `biolatency` | Block I/O latency histogram            |
| `tcpconnect` | Trace TCP connections                  |
| `cachestat`  | Page cache hit/miss statistics         |
| `funccount`  | Count kernel function calls            |
| `profile`    | CPU profiling by sampling stack traces |

```bash
$ execsnoop # Watch processes being created
$ opensnoop # Watch files being opened
$ biolatency # Measure disk I/O latency distribution
```

## Profiling

**Profiling** is a form of dynamic program analysis that measures the frequency and duration of function calls. It helps identify which parts of a program consume the most time.

```
Profiling Output Example:
+------------------------------------------+
| Function | Time | Calls |
+------------------------------------------+
| sort_array() | 45.2% | 1000 |
| read_data() | 30.1% | 500 |
| write_output() | 15.5% | 500 |
| parse_input() | 9.2% | 1000 |
+------------------------------------------+
```

### Profiling Tools

| Tool                           | Platform | Purpose                                           |
| ------------------------------ | -------- | ------------------------------------------------- |
| `gprof`                        | Linux    | GNU profiler for C/C++ programs                   |
| `perf`                         | Linux    | Performance analysis tool using hardware counters |
| `valgrind`                     | Linux    | Memory debugging and profiling                    |
| `Instruments`                  | macOS    | Apple's profiling tool                            |
| `Windows Performance Analyzer` | Windows  | Windows profiling suite                           |

## Summary

```
+--------------------------------------------------+
| OS Debugging Summary |
+--------------------------------------------------+
| |
| Failure Analysis: |
| - Log files (/var/log/syslog, kern.log) |
| - Core dumps (analyzed with gdb) |
| - Kernel panic/BSOD |
| |
| Performance Monitoring: |
| - top, ps, vmstat, iostat |
| - Identify: CPU/Memory/IO/Network bottleneck |
| |
| Tracing: |
| - strace (system calls) |
| - ltrace (library calls) |
| - DTrace (dynamic tracing framework) |
| - BCC tools (eBPF-based) |
| |
| Profiling: |
| - gprof, perf, valgrind |
| - Identify hotspots in code |
+--------------------------------------------------+
```

## Exam Tips

1. **Log files and core dumps** are the two main failure analysis mechanisms. Know what each is and how they are used.
2. **Core dump analysis:** Know that `gdb` is used to analyze core dumps and that the `backtrace` command shows the call stack at the point of crash.
3. **Performance monitoring tools:** Memorize at least `top`, `ps`, `vmstat`, and `iostat` with their purposes. Draw a simple output example if asked.
4. **strace vs ltrace:** strace traces system calls; ltrace traces library calls. Both help understand how a program interacts with the system.
5. **DTrace:** Know that it is a dynamic tracing framework from Sun/Solaris, available on macOS and FreeBSD. It traces both user and kernel events.
6. **BCC tools:** Mentioned in recent editions of Silberschatz. Know that they are eBPF-based Linux tracing tools.
7. **Profiling:** Understand that profiling measures function call frequency and duration to identify performance hotspots.
8. ** commonly asks:** "Explain the various debugging techniques used in an OS" or "What are the tools used for OS performance tuning?"
