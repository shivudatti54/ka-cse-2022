# File Transfer Protocol (FTP) - Summary

## Key Definitions and Concepts

- **FTP (File Transfer Protocol)**: A standard network protocol for transferring files between a client and server on a TCP/IP network, operating on ports 20 and 21.
- **Control Channel**: TCP Port 21 used for sending FTP commands and receiving responses.
- **Data Channel**: TCP Port 20 (active mode) or dynamic port (passive mode) used for actual file transfer.
- **Active Mode (PORT)**: Client informs server of its port; server initiates connection back to client.
- **Passive Mode (PASV)**: Server provides IP and port; client initiates connection to server (firewall-friendly).

## Important Formulas and Concepts

- Data Channel Port Calculation (Passive Mode): `Port = (first_octet × 256) + second_octet`
- Default FTP Ports: Control - 21, Data - 20
- Binary mode should be used for: Images, executables, ZIP files, PDFs, audio/video files
- ASCII mode should be used for: Plain text files (.txt, .csv, .log)

## Key Points

1. FTP uses two channels: Control channel (port 21) for commands and Data channel (port 20) for file transfer.

2. Active mode can fail behind firewalls because the server initiates the data connection back to the client.

3. Passive mode is recommended when the client is behind a firewall or NAT.

4. Binary mode transfers exact byte sequences; ASCII mode converts line endings between different OS formats.

5. FTP maintains session state, unlike stateless HTTP, enabling operations like resume and directory navigation.

6. Common response codes: 220 (ready), 230 (logged in), 226 (transfer complete), 530 (not logged in).

7. FTPS adds SSL/TLS encryption; SFTP is a different protocol running over SSH.

8. Anonymous FTP uses username "anonymous" with email as password for public access.

## Common Mistakes to Avoid

- Using ASCII mode for binary files (causes file corruption)
- Using active mode when behind a firewall (connection failures)
- Confusing SFTP with FTPS (they are different protocols)
- Forgetting to switch to binary mode before transferring non-text files

## Revision Tips

1. Practice tracing FTP sessions with both active and passive modes.

2. Memorize at least 8 common FTP commands: USER, PASS, LIST, RETR, STOR, CWD, PWD, QUIT.

3. Remember: Port 21 = Control, Port 20 = Data (in active mode).

4. Review FTP response code categories: 1xx (preliminary), 2xx (success), 3xx (intermediate), 4xx (transient error), 5xx (permanent error).

5. Understand that FTP is connection-oriented (TCP) unlike connectionless protocols.
