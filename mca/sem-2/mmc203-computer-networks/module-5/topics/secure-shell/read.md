# Secure Shell (SSH)


## Table of Contents

- [Secure Shell (SSH)](#secure-shell-ssh)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [SSH Architecture and Protocol](#ssh-architecture-and-protocol)
  - [SSH Encryption and Key Exchange](#ssh-encryption-and-key-exchange)
  - [SSH Authentication Methods](#ssh-authentication-methods)
  - [SSH Keys and Key Management](#ssh-keys-and-key-management)
  - [SSH Port Forwarding and Tunneling](#ssh-port-forwarding-and-tunneling)
  - [SCP and SFTP](#scp-and-sftp)
  - [SSH Configuration Files](#ssh-configuration-files)
- [Examples](#examples)
  - [Example 1: Generating SSH Key Pair and Configuring Passwordless Login](#example-1-generating-ssh-key-pair-and-configuring-passwordless-login)
  - [Example 2: Creating an SSH Tunnel for Secure Web Browsing](#example-2-creating-an-ssh-tunnel-for-secure-web-browsing)
  - [Example 3: SSH Server Hardening Configuration](#example-3-ssh-server-hardening-configuration)
- [Change default port](#change-default-port)
- [Disable protocol version 1](#disable-protocol-version-1)
- [Disable root login](#disable-root-login)
- [Allow specific users only](#allow-specific-users-only)
- [Disable password authentication (use keys only)](#disable-password-authentication-use-keys-only)
- [Enable strict host key checking](#enable-strict-host-key-checking)
- [Set idle timeout](#set-idle-timeout)
- [Disable empty passwords](#disable-empty-passwords)
- [Use strong ciphers](#use-strong-ciphers)
- [Restart SSH service](#restart-ssh-service)
- [Exam Tips](#exam-tips)

## Introduction

Secure Shell (SSH) is a cryptographic network protocol that provides a secure channel over an unsecured network by using client-server architecture. It was designed as a replacement for Telnet and other insecure remote shell protocols like rsh and rlogin, which transmit data including passwords in plain text, making them vulnerable to interception attacks. SSH enables secure remote login, file transfer (SCP/SFTP), and port forwarding, making it an essential tool for system administrators, developers, and security professionals.

In today's interconnected computing environment, SSH has become the de facto standard for secure remote access to servers, network devices, and cloud infrastructure. It provides confidentiality and integrity of data through strong encryption, while also offering authentication mechanisms that verify the identity of users and systems. The protocol operates on port 22 by default and is supported by virtually all Unix-like systems, Windows servers, and network equipment from vendors like Cisco, Juniper, and others.

Understanding SSH is crucial for CSE students because it forms the backbone of secure system administration, DevOps practices, and cloud computing operations. Whether managing remote servers, configuring automated deployments, or establishing secure tunnels, SSH knowledge is indispensable. Additionally, SSH concepts appear frequently in examinations and are tested in various competitive examinations and certification exams like CompTIA Security+, CISSP, and CEH.

## Key Concepts

### SSH Architecture and Protocol

SSH operates using a client-server model where the SSH client initiates a connection to an SSH server. The protocol consists of three major components:

1. **Transport Layer Protocol**: This layer handles initial key exchange, server authentication, and encryption setup. It establishes a secure channel between client and server, protecting data confidentiality and integrity.

2. **User Authentication Protocol**: This layer authenticates the client to the server using various methods like password authentication, public key authentication, or keyboard-interactive authentication.

3. **Connection Protocol**: This layer multiplexes the encrypted tunnel into multiple logical channels, enabling features like interactive login sessions, port forwarding, and X11 forwarding.

SSH has gone through two major versions: SSH1 and SSH2. SSH2 (SSH protocol version 2) is the current standard and addresses several security vulnerabilities present in SSH1, including a vulnerability in the CRC-32 compensation attack detector. SSH2 offers improved security features, better key exchange algorithms, and extensibility.

### SSH Encryption and Key Exchange

SSH uses symmetric encryption for bulk data encryption, asymmetric encryption for key exchange and authentication, and hashing for data integrity. During the SSH handshake, the client and server negotiate:

- **Key Exchange Method**: Algorithms like Diffie-Hellman Group Exchange (DH-GEX), Diffie-Hellman Group14, and Elliptic Curve Diffie-Hellman (ECDH)
- **Server Key Algorithm**: RSA or ECDSA for server authentication
- **Encryption Algorithm**: AES (256, 192, or 128-bit), ChaCha20-Poly1305, 3DES, or Blowfish
- **MAC (Message Authentication Code) Algorithm**: HMAC-SHA2, HMAC-SHA1, or UMAC

The initial key exchange establishes session keys that encrypt all subsequent communication. Perfect Forward Secrecy (PFS) ensures that compromising one session key doesn't compromise past or future sessions.

### SSH Authentication Methods

SSH supports multiple authentication mechanisms:

1. **Password Authentication**: The traditional method where users enter a username and password. While convenient, it's less secure than key-based authentication and vulnerable to brute-force attacks.

2. **Public Key Authentication**: The most secure and recommended method. Users generate a key pair consisting of a private key (kept secret on the client) and a public key (stored on the server in ~/.ssh/authorized_keys). This method supports passphrase protection for the private key.

3. **Keyboard-Interactive Authentication**: A flexible method where the server prompts the user for responses to one or more questions, commonly used for OTP (One-Time Password) systems.

4. **Host-Based Authentication**: Authenticates based on the client hostname, typically used in controlled environments.

### SSH Keys and Key Management

SSH key pairs are generated using the `ssh-keygen` command. The most common types are:

- **RSA Keys**: Widely supported, recommended 4096-bit length for security
- **ECDSA Keys**: Elliptic Curve Digital Signature Algorithm, faster with comparable security
- **Ed25519 Keys**: Modern algorithm offering excellent security with fast performance, recommended for new deployments

Key files include:

- `~/.ssh/id_rsa` or `~/.ssh/id_ed25519`: Private key (must have 600 permissions)
- `~/.ssh/id_rsa.pub` or `~/.ssh/id_ed25519.pub`: Public key
- `~/.ssh/authorized_keys`: File containing public keys permitted for login
- `~/.ssh/known_hosts`: Records host keys of previously connected servers

### SSH Port Forwarding and Tunneling

SSH port forwarding creates encrypted tunnels through which network traffic can be forwarded:

1. **Local Port Forwarding (-L)**: Forwards a local port to a remote destination through the SSH server. Syntax: `ssh -L local_port:destination_host:destination_port user@ssh_server`

2. **Remote Port Forwarding (-R)**: Allows remote hosts to access local services through the SSH server. Syntax: `ssh -R remote_port:localhost:local_port user@ssh_server`

3. **Dynamic Port Forwarding (-D)**: Creates a SOCKS proxy, allowing flexible forwarding through the SSH server. Syntax: `ssh -D local_port user@ssh_server`

### SCP and SFTP

- **SCP (Secure Copy)**: Command-line utility for secure file transfer using SSH. Example: `scp file.txt user@server:/path/`
- **SFTP (SSH File Transfer Protocol)**: Interactive file transfer protocol with additional features like directory listing, resume support, and remote file operations. Accessed via: `sftp user@server`

### SSH Configuration Files

Client configuration is managed through:

- `/etc/ssh/ssh_config`: System-wide client configuration
- `~/.ssh/config`: User-specific client configuration

Server configuration is in `/etc/ssh/sshd_config`, where administrators can customize port numbers, authentication methods, allowed users, and security options.

## Examples

### Example 1: Generating SSH Key Pair and Configuring Passwordless Login

**Problem**: Generate an Ed25519 SSH key pair and configure passwordless authentication to a remote server.

**Solution**:

Step 1: Generate the key pair on the client machine

```bash
ssh-keygen -t ed25519 -C "user@myserver"
```

When prompted:

- Enter file location: (press Enter for default ~/.ssh/id_ed25519)
- Enter passphrase: (enter a strong passphrase or press Enter for no passphrase)
- Confirm passphrase: (re-enter if passphrase was set)

Step 2: Copy public key to the server

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@192.168.1.100
```

Alternatively, manually:

```bash
cat ~/.ssh/id_ed25519.pub | ssh user@192.168.1.100 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

Step 3: Set proper permissions on server

```bash
ssh user@192.168.1.100 "chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys"
```

Step 4: Test the connection

```bash
ssh user@192.168.1.100
```

**Explanation**: The ssh-keygen command creates a 256-bit Ed25519 key pair. The public key is appended to the server's authorized_keys file, allowing the client to authenticate using the corresponding private key without entering a password.

### Example 2: Creating an SSH Tunnel for Secure Web Browsing

**Problem**: Access a web application running on a remote server's port 8080 through a secure SSH tunnel, accessing it locally on port 9090.

**Solution**:

Command:

```bash
ssh -L 9090:localhost:8080 user@remote-server.com -N
```

Breakdown:

- `-L 9090:localhost:8080`: Local port 9090 forwards to remote host's localhost port 8080
- `-N`: Don't execute remote command (just establish tunnel)
- `-f`: Could be added to run in background

To access: Open browser and navigate to `http://localhost:9090`

**Verification**: The traffic between local port 9090 and remote port 8080 is now encrypted through the SSH tunnel. Anyone monitoring the network sees only encrypted SSH traffic.

### Example 3: SSH Server Hardening Configuration

**Problem**: Configure sshd_config to improve security with specific settings.

**Solution**: Edit `/etc/ssh/sshd_config` with these recommendations:

```bash
# Change default port
Port 2222

# Disable protocol version 1
Protocol 2

# Disable root login
PermitRootLogin no

# Allow specific users only
AllowUsers admin developer@192.168.1.0/24

# Disable password authentication (use keys only)
PasswordAuthentication no
PubkeyAuthentication yes

# Enable strict host key checking
StrictHostKeyChecking ask

# Set idle timeout
ClientAliveInterval 300
ClientAliveCountMax 2

# Disable empty passwords
PermitEmptyPasswords no

# Use strong ciphers
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com

# Restart SSH service
sudo systemctl restart sshd
```

**Explanation**: These settings harden the SSH server by changing the default port (reducing automated attacks), disabling root login (preventing privilege escalation), enforcing key-based authentication, implementing connection timeouts, and specifying strong encryption algorithms.

## Exam Tips

1. **Remember SSH Default Port**: SSH uses port 22 by default. Know that this can be changed in sshd_config.

2. **Difference Between SSH1 and SSH2**: SSH2 is more secure, supports Perfect Forward Secrecy, and fixes vulnerabilities in SSH1's CRC-32 mechanism.

3. **Know Authentication Methods**: Be familiar with password authentication, public key authentication, keyboard-interactive, and host-based authentication. Public key is the most secure.

4. **Key Files Location**: Remember that SSH keys are stored in ~/.ssh/ directory with specific permissions (600 for private keys, 700 for .ssh directory).

5. **Port Forwarding Types**: Know the difference between local (-L), remote (-R), and dynamic (-D) port forwarding. Understand when each is used.

6. **SCP vs SFTP**: SCP is simpler for file transfers while SFTP offers more features like resume, directory operations, and is more firewall-friendly.

7. **Encryption Algorithms**: Know common symmetric algorithms (AES, ChaCha20), asymmetric (RSA, ECDSA, Ed25519), and key exchange methods (Diffie-Hellman).

8. **SSH vs Telnet**: Telnet transmits everything in plain text including passwords; SSH encrypts all traffic. This is a common exam comparison.

9. **ssh-keygen Flags**: Know common flags like -t (type), -b (bits), -C (comment), and -f (filename).

10. **Configuration Files**: Know the locations of ssh_config (client), sshd_config (server), and known_hosts.
