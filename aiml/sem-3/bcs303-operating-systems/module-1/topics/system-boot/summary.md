# System Boot - Summary

## Key Definitions

- **Bootstrapping:** The process of loading the operating system into memory when a computer is powered on or reset
- **Bootstrap Program:** Initial software executed at power-on, stored in ROM/EEPROM, that initializes hardware and loads the OS
- **POST (Power-On Self-Test):** Diagnostic procedure performed by firmware to verify hardware functionality
- **BIOS (Basic Input/Output System):** Traditional firmware interface operating in 16-bit real mode
- **UEFI (Unified Extensible Firmware Interface):** Modern firmware interface with 64-bit support and enhanced security
- **MBR (Master Boot Record):** First 512-byte sector containing boot code and partition table
- **Boot Loader:** Specialized program that loads the operating system kernel into memory
- **Secure Boot:** UEFI feature that verifies digital signatures before executing boot components

## Important Formulas

- MBR Structure: 512 bytes total = 446 bytes (boot code) + 64 bytes (partition table) + 2 bytes (signature)
- BIOS operates in 16-bit real mode with 1 MB maximum addressable memory
- UEFI supports GPT for disks up to 256 TB with 64-bit addressing

## Key Points

1. The boot process transforms powered-off hardware into a functional computing environment through staged software loading
2. Bootstrap firmware (BIOS/UEFI) provides the critical interface between hardware and operating system
3. POST diagnostics ensure essential hardware components are functional before proceeding with boot
4. Boot order configuration in firmware determines which device is checked first for bootable media
5. The MBR contains both boot loader code and partition table information in its 512-byte structure
6. Modern systems employ multi-stage boot loaders to overcome the size limitations of initial boot sectors
7. GRUB, Windows Boot Manager, and LILO are examples of operating system boot loaders
8. UEFI provides significant advantages including Secure Boot, GPT support, and faster initialization
9. Secure Boot prevents malware injection by requiring cryptographic verification of all boot components
10. After kernel loading, the operating system initializes system services and presents a login interface

## Common Mistakes

1. **Confusing BIOS and UEFI:** Treating them as interchangeable; they are fundamentally different firmware architectures with distinct boot procedures
2. **Assuming boot process ends at kernel loading:** The OS initialization phase (systemd, Windows services) is integral to the boot process
3. **Ignoring Secure Boot implications:** Failing to understand that Secure Boot affects operating system installation and boot loader compatibility
4. **Overlooking multi-stage design:** Thinking the boot loader is a single program rather than a coordinated sequence of components
5. **Neglecting boot order configuration:** Not understanding that boot priority determines which OS or device loads when multiple options exist
6. **Misunderstanding MBR contents:** The MBR contains executable boot code, not just partition information
7. **Ignoring firmware updates:** BIOS/UEFI updates are critical for security patches and hardware compatibility improvements