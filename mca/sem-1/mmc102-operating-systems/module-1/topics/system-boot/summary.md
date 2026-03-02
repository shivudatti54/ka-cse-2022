# System Boot - Summary

## Key Definitions and Concepts

- **System Boot**: The process of initializing a computer from a powered-off state to a fully operational operating system
- **Bootstrap Loader**: Firmware code stored in ROM/flash memory that locates and loads the operating system kernel
- **BIOS (Basic Input/Output System)**: Traditional firmware operating in 16-bit real mode with 640KB memory limitations
- **UEFI (Unified Extensible Firmware Interface)**: Modern firmware operating in 32/64-bit protected mode with enhanced capabilities
- **POST (Power-On Self-Test)**: Hardware diagnostic routine executed during boot to verify essential components
- **MBR (Master Boot Record)**: 512-byte sector containing boot code and partition table for BIOS systems
- **GPT (GUID Partition Table)**: Modern partitioning scheme supporting disks larger than 2TB, required for UEFI
- **Secure Boot**: UEFI feature that verifies digital signatures of bootloaders to prevent unauthorized code execution

## Important Formulas and Theorems

- Boot sector size: 512 bytes (traditional MBR)
- Maximum disk size with MBR: 2TB
- Maximum partitions with MBR: 4 primary partitions
- BIOS execution mode: 16-bit real mode
- UEFI execution mode: 32-bit or 64-bit protected mode

## Key Points

- The boot process transforms hardware from dormant state to fully functional computing environment through five sequential stages
- BIOS is legacy firmware with limitations; UEFI is the modern standard with improved security and capabilities
- The bootstrap loader is the critical software component that bridges firmware and operating system
- Secure Boot prevents boot-time malware by verifying digital signatures before execution
- Warm boots skip POST and are faster; cold boots perform complete hardware initialization
- Boot order determines the sequence in which the firmware searches for bootable devices
- Understanding boot processes is essential for system administration, troubleshooting, and security implementation

## Common Mistakes to Avoid

- Confusing BIOS and UEFI boot mechanisms; remember BIOS reads MBR while UEFI reads from EFI System Partition
- Assuming Secure Boot is only a Windows feature; it is a UEFI feature available across operating systems
- Overlooking the fact that warm boots do not clear all hardware states, which can preserve problems
- Forgetting that GPT partitioning is necessary for disks larger than 2TB, regardless of operating system

## Revision Tips

- Create a flowchart diagram of the complete boot process to visualize the sequence of events
- Memorize the five boot stages in order and be able to explain what happens at each stage
- Practice explaining the differences between BIOS and UEFI in simple terms
- Review common boot failure scenarios and their troubleshooting approaches
- Understand Secure Boot's security purpose rather than memorizing it as an isolated feature