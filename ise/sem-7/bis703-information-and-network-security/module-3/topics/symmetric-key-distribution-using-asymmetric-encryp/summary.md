# Symmetric Key Distribution Using Asymmetric Encryption

=====================================

### Overview

Symmetric-key algorithms like AES are fast for bulk encryption but have a key distribution problem. Asymmetric encryption (e.g., RSA) solves this by allowing one party to securely transmit a symmetric session key encrypted with the recipient's public key. This creates a hybrid cryptosystem used in protocols like SSL/TLS.

### Key Points

- **Key Distribution Problem:** Two parties cannot safely share a symmetric key over an insecure network
- **Hybrid Cryptosystem:** Combines asymmetric encryption (for key exchange) with symmetric encryption (for bulk data)
- **Session Key:** A temporary symmetric key generated for a single communication session
- **Encryption Step:** Alice encrypts session key K with Bob's public key: C = E(PU_b, K)
- **Decryption Step:** Bob decrypts with his private key to recover K: K = D(PR_b, C)
- **PKI Dependency:** Alice must obtain Bob's authentic public key via digital certificates to prevent MITM attacks
- **Forward Secrecy:** Short-lived session keys limit damage if any single key is compromised
- **SSL/TLS Foundation:** This mechanism is the backbone of the key exchange phase in HTTPS connections

### Important Concepts

- Process: Generate session key K -> Encrypt K with recipient's public key -> Transmit -> Decrypt with private key -> Use K for symmetric encryption
- Asymmetric crypto is used only for key establishment (slow); symmetric crypto handles bulk data (fast)
- Security depends on two factors: secrecy of private keys and authenticity of public keys
- Session keys are temporary and unique per session, enhancing overall system security

### Notes

- Be able to draw the complete step-by-step key exchange process between Alice and Bob
- Emphasize that asymmetric encryption is too slow for bulk data -- that is why hybrid systems exist
- Mention SSL/TLS as a real-world example of this hybrid approach
- Remember that PKI and digital certificates are essential for authenticating the public keys used in the exchange
