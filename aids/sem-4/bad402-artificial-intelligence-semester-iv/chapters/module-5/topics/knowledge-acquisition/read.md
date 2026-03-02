# Mobile Device Acquisition Methods

## Introduction to Mobile Forensics Acquisition

Mobile device acquisition is the process of extracting digital evidence from mobile devices such as smartphones and tablets. Unlike traditional computer forensics, mobile forensics presents unique challenges due to the diversity of operating systems (primarily iOS and Android), hardware, security features, and constant connectivity. The primary goal of acquisition is to create a forensically sound bit-for-bit copy of the device's data without altering the original evidence.

The acquisition process is the critical first step in mobile forensics and directly influences the quantity and quality of data that can be recovered and analyzed. A flawed acquisition can render evidence inadmissible in court.

## Key Concepts and Challenges

### Forensic Soundness
This principle requires that the acquisition method:
*   **Does not alter the original data** on the device.
*   Is **documented thoroughly**, including all tools and steps used.
*   Preserves the **integrity** of the evidence, often through hashing (e.g., MD5, SHA-1, SHA-256).
*   Maintains a **clear chain of custody**.

### Common Challenges in Mobile Acquisition
*   **Device Security:** PINs, passwords, pattern locks, biometrics (fingerprint, face ID).
*   **Hardware Diversity:** Thousands of different device models with varying connectors (USB-C, Lightning), storage types, and chipsets.
*   **Software Diversity:** Multiple OS versions, custom manufacturer skins (e.g., Samsung's One UI), and encryption implementations.
*   **Data Volatility:** Data can be easily modified, overwritten, or remotely wiped.
*   **Cloud Integration:** Data is often synced with cloud services (iCloud, Google Drive), requiring a multi-faceted approach.
*   **Fast Changing Technology:** Rapid development cycles mean forensic tools and techniques must constantly evolve.

## Physical Acquisition

Physical acquisition aims to create a complete bit-for-bit copy of the device's physical storage. This is the most desired method as it can recover deleted files and unallocated space, provided the device is not fully encrypted.

### Methods of Physical Acquisition

1.  **JTAG (Joint Test Action Group):**
    *   **What it is:** A method that involves soldering a hardware interface directly to the device's printed circuit board (PCB) to access the memory chip.
    *   **When to use:** When the device is damaged (e.g., broken screen) but the memory chip is functional, or when other methods are blocked.
    *   **Advantages:** Can bypass user lock screens; effective on damaged devices.
    *   **Disadvantages:** Highly technical, requires micro-soldering expertise; risk of permanent device damage; time-consuming.

2.  **Chip-Off:**
    *   **What it is:** The most invasive method. It involves physically removing the memory chip from the device and reading its contents using a specialized chip reader.
    *   **When to use:** As a last resort for damaged devices or when JTAG is not feasible.
    *   **Advantages:** Provides the most direct access to the raw data storage.
    *   **Disadvantages:** Destructive method; almost always voids device warranty; requires extensive skill and expensive equipment; can be defeated by chip-level encryption.

3.  **ISP (In-System Programming):**
    *   **What it is:** Similar to JTAG but often involves accessing test points on the board without soldering, using a special ISP cable or adapter.
    *   **When to use:** For specific device models where test points are known and accessible.
    *   **Advantages:** Less invasive than JTAG or Chip-Off.
    *   **Disadvantages:** Not available for all devices; requires specific adapters and knowledge.

## Logical Acquisition

Logical acquisition extracts a logical copy of the file system and user data through the device's normal operating system and APIs. It does not recover deleted data or unallocated space.

*   **How it works:** Uses the device's USB cable and a forensic tool to communicate with the operating system. The tool requests files, and the OS delivers them.
*   **When to use:** As a quick first step to get user data (contacts, messages, call logs); when a physical acquisition is not possible due to encryption or tool support.
*   **Advantages:** Fast; simple; supported by a wide range of tools; low risk of data alteration.
*   **Disadvantages:** Recovers only active, allocated files; access is controlled by the OS, which may hide or restrict data; cannot recover deleted data.

## File System Acquisition

File System acquisition is a hybrid method that often requires root (Android) or jailbreak (iOS) access. It provides a deeper level of access than a logical extraction but not as complete as a physical one.

*   **How it works:** The forensic tool exploits privileges on the device to access the raw file system data, allowing it to copy files and folders that are normally restricted.
*   **When to use:** When physical acquisition is not possible, but more data than a logical extraction provides is needed.
*   **Advantages:** Can recover some deleted data (depending on the file system); provides access to more system files and application data.
*   **Disadvantages:** Requires modifying the device state (rooting/jailbreaking), which can alter data and be challenged in court; not always successful.

## Cloud Acquisition

With the proliferation of cloud services, a significant amount of user data is stored remotely. Cloud acquisition involves legally obtaining data from service providers like Apple (iCloud), Google (Google Drive/Backup), and social media companies.

*   **How it works:** Typically executed via a legal request (subpoena, warrant) to the service provider. Some tools can also extract data from a synced desktop client or a backup file stored on a computer.
*   **When to use:** When the physical device is unavailable, encrypted, or to obtain a more complete historical record (e.g., older backups).
*   **Advantages:** Can contain historical data not present on the device; bypasses device encryption.
*   **Disadvantages:** Requires legal authority; response times from providers can be slow; data may be incomplete depending on backup settings.

## Comparison of Acquisition Methods

| Method | Data Integrity | Deleted Data Recovery | Invasiveness | Required Skill Level | Speed |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Physical** | High | Yes | Low to High | Medium to Expert | Slow |
| **Logical** | High | No | Non-Invasive | Beginner | Fast |
| **File System** | Medium | Sometimes | Medium (requires root/jb) | Medium | Medium |
| **Cloud** | High | Possible (from backups) | Non-Invasive | Medium (legal process) | Very Slow |
| **JTAG/Chip-Off** | High | Yes | Highly Invasive | Expert | Very Slow |

## The Acquisition Process: A Step-by-Step Guide

A forensically sound acquisition follows a strict procedure.

```
+-----------------------------------------------------------------------+
| [Start]                                                               |
| 1. Receive & Document Evidence: Note make, model, condition, state.  |
+----------------------------+------------------------------------------+
                             |
+----------------------------v------------------------------------------+
| 2. Isolate the Device: Place in a Faraday bag/box to prevent         |
| network connectivity (calls, SMS, remote wipe).                      |
+----------------------------+------------------------------------------+
                             |
+----------------------------v------------------------------------------+
| 3. Identify Method: Based on device model, OS, lock status, and      |
| available tools. Always choose the least invasive method possible.    |
+----------------------------+------------------------------------------+
                             |
+----------------------------v------------------------------------------+
| 4. Acquire Data: Perform the chosen method (Logical -> File System ->|
| Physical). Document every tool, command, and hash value.             |
+----------------------------+------------------------------------------+
                             |
+----------------------------v------------------------------------------+
| 5. Verify & Validate: Verify the integrity of the acquired image with|
| hashes. Validate the tools and methods used.                         |
+----------------------------+------------------------------------------+
                             |
+----------------------------v------------------------------------------+
| 6. Analyze & Report: Proceed to analysis on a forensic workstation  |
| using the image, not the original device.                            |
+----------------------------+------------------------------------------+
                             |
+----------------------------v------------------------------------------+
| [End] Store original device and image securely, maintaining chain of |
| custody.                                                              |
+-----------------------------------------------------------------------+
```

## Tools for Mobile Acquisition

*   **Cellebrite UFED (Universal Forensic Extraction Device):** Industry standard. Supports physical, logical, and file system extraction for thousands of devices.
*   **Grayshift:** Known for tools like "GrayKey" which can bypass iPhone passcodes.
*   **Oxygen Forensic Detective:** Provides extensive support for application data analysis and cloud extraction.
*   **Magnet AXIOM:** Integrates mobile, computer, and cloud forensics into one workflow.
*   **Open-Source Tools:** Autopsy (with mobile plugins), Andriller (for Android).

## Legal and Ethical Considerations

*   **Search Authority:** Ensure you have proper legal authority (warrant, consent) before seizing or acquiring data from a device.
*   **Expert Witness:** The forensic examiner may need to testify in court about the methods used. Thorough documentation is crucial.
*   **Privacy:** Only extract and analyze data relevant to the investigation.

## Exam Tips

*   **Priority Order:** Remember the order of methods: always try **Logical** first (least invasive), then **File System**, then **Physical**. **Cloud** is a parallel avenue.
*   **Hashing is Non-Negotiable:** Always hash the original evidence and the acquired image to prove integrity. Be prepared to define MD5, SHA-1, SHA-256.
*   **Define "Forensic Soundness":** Be able to list its core tenets: no alteration, documentation, hashing, chain of custody.
*   **Know the Challenges:** Be ready to discuss why mobile acquisition is harder than disk acquisition (diversity, security, volatility).
*   **JTAG vs. Chip-Off:** Understand that JTAG reads the chip while it's still on the board; Chip-Off removes it. Chip-Off is more destructive.
*   **Practice Terminology:** Ensure you can clearly differentiate between Physical, Logical, and File System acquisition.