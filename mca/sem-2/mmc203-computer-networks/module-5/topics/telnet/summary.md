# Telnet - Summary

## Key Definitions and Concepts

- **Telnet (TELecommunication NETwork):** A network protocol that provides bidirectional interactive text-oriented communication using a virtual terminal connection over TCP.

- **Network Virtual Terminal (NVT):** A hypothetical standard device that allows different types of terminals to communicate by translating local terminal characteristics to a common format.

- **IAC (Interpret As Command):** A special character (ASCII 255) used to indicate that the following byte is a Telnet command rather than data.

- **Option Negotiation:** The mechanism by which Telnet clients and servers agree on optional features like echo mode, binary mode, and terminal type.

## Important Commands

| Command | Code | Purpose                       |
| ------- | ---- | ----------------------------- |
| IAC     | 255  | Command prefix                |
| WILL    | 251  | Indicate desire to use option |
| DO      | 252  | Request peer to use option    |
| WON'T   | 253  | Refuse to use option          |
| DON'T   | 254  | Demand peer not to use option |
| SB      | 250  | Subnegotiation start          |
| SE      | 240  | Subnegotiation end            |

## Key Points

- Telnet operates on TCP port 23 and uses client-server architecture.
- All data including passwords is transmitted in plain text without encryption.
- The protocol supports option negotiation to extend basic functionality.
- NVT abstraction enables heterogeneous terminal communication.
- Telnet is still used for network troubleshooting and testing services.
- SSH (Secure Shell) has replaced Telnet for secure remote access due to encryption.
- The escape character is Ctrl+] (ASCII 29) for breaking to command mode.
- Telnet operates at Application Layer (Layer 7) of OSI model.

## Common Mistakes to Avoid

1. **Confusing Telnet with SSH:** Remember Telnet sends data in plain text, while SSH encrypts all communications.

2. **Forgetting the default port:** Telnet uses port 23 by default; when testing services, you must specify the correct port number.

3. **Ignoring security implications:** Never use Telnet over untrusted networks; credentials can be easily intercepted.

4. **Not understanding option negotiation:** Many students confuse the WILL/DO commands - remember WILL indicates "I will use this option" and DO means "you should use this option."

## Revision Tips

1. Practice drawing the Telnet connection establishment flow diagram showing TCP connection, option negotiation, and data transfer phases.

2. Memorize the command codes for IAC, WILL, DO, WON'T, DON'T as these are frequently asked in examinations.

3. Remember the security limitations of Telnet and the advantages of SSH as this is a common exam question.

4. Use Telnet locally to test connectivity to various ports (25, 80, 443) to gain practical understanding.

5. Review previous question papers to identify the pattern of questions asked on Telnet.
