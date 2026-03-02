# Secure Shell (SSH) - Summary

## Key Definitions and Concepts

- **Secure Shell (SSH)**: A cryptographic network protocol providing secure remote login, file transfer, and port forwarding over unsecured networks
- **SSH Client**: Software that initiates connection to SSH server for remote access
- **SSH Server**: Daemon (sshd) listening for incoming SSH connections
- **Public Key Authentication**: Method using asymmetric key pairs for server authentication
- **Port Forwarding**: Creating encrypted tunnels through which network traffic is forwarded

## Important Formulas and Techniques

- **Key Generation**: `ssh-keygen -t ed25519 -C "comment"` for modern keys
- **Local Port Forwarding**: `ssh -L local_port:dest_host:dest_port user@server`
- **Remote Port Forwarding**: `ssh -R remote_port:local_host:local_port user@server`
- **Dynamic Port Forwarding**: `ssh -D local_port user@server` (SOCKS proxy)
- **Secure Copy**: `scp source user@host:destination`
- **SFTP Connection**: `sftp user@host`

## Key Points

- SSH replaces insecure protocols like Telnet, rlogin, and rsh by encrypting all transmitted data
- SSH operates on port 22 by default and uses TCP for reliable communication
- SSH2 (protocol version 2) is the current standard with improved security over SSH1
- Three layers: Transport Layer, User Authentication Layer, and Connection Layer
- Public key authentication is more secure than password authentication
- SSH keys require proper permissions: 600 for private keys, 700 for .ssh directory
- Ed25519 keys are recommended for new deployments due to security and performance
- SSH provides confidentiality, integrity, and authentication in network communications
- Known_hosts file stores server fingerprints to prevent man-in-the-middle attacks

## Common Mistakes to Avoid

1. Setting incorrect file permissions on private keys (should be 600), which prevents SSH from using them
2. Confusing local port forwarding with remote port forwarding direction
3. Leaving password authentication enabled when keys are configured, reducing security
4. Not verifying server fingerprints on first connection, risking MITM attacks
5. Using weak key sizes (less than 2048-bit for RSA) or outdated key types

## Revision Tips

1. Practice generating keys and configuring passwordless login in a lab environment
2. Draw the SSH client-server architecture and label all components
3. Remember the port numbers: 22 (SSH), 21 (FTP), 23 (Telnet)
4. Create a cheat sheet of common ssh, scp, and sftp command variations
5. Review sshd_config directives and understand their security implications
