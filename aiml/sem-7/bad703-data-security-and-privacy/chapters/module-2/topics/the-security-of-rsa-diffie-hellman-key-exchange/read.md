# The Security of RSA & Diffie-Hellman Key Exchange

**Subject:** Data Security and Privacy  
**Module:** Module 2  
**Topic:** The Security of RSA & Diffie-Hellman Key Exchange

## 1. Introduction

In secure communication, two parties (traditionally Alice and Bob) need to establish a **shared secret key** to encrypt their subsequent messages. Two fundamental pillars for achieving this are **RSA** (used for key exchange and digital signatures) and the **Diffie-Hellman Key Exchange**. While both are used to establish a shared secret, they operate on entirely different principles and face distinct security challenges. Understanding their security is crucial for any security engineer.

## 2. Core Concepts & Security Explained

### RSA Key Exchange Security

RSA is an **asymmetric encryption algorithm**. It can be used for a key exchange protocol often called *"encryption with RSA."*

*   **How it works:** Alice obtains Bob's public key. She generates a random symmetric session key (e.g., for AES), encrypts it using Bob's public key, and sends the ciphertext to Bob. Bob, and only Bob, can decrypt it using his private key. Now both share the same session key.

*   **Security Basis:** The security of RSA relies on the **difficulty of the Integer Factorization Problem**. It is computationally infeasible to derive the private key from the public key because doing so requires factoring a very large composite number `N` (the modulus) into its two prime factors, `p` and `q`. The strength is directly tied to the key size; 2048-bit or 4096-bit keys are currently considered secure.

*   **Vulnerabilities:**
    *   **Brute Force:** Infeasible with large keys.
    *   **Mathematical Advances:** Improvements in factorization algorithms (e.g., General Number Field Sieve) constantly push the required key size upward.
    *   **Implementation Flaws:** Poor randomness in key generation, side-channel attacks, or using a common modulus can break RSA security.
    *   **Man-in-the-Middle (MitM) Attack:** This is a critical weakness of the basic RSA key exchange protocol. If an attacker, Mallory, can intercept the communication *before* Alice gets Bob's authentic public key, Mallory can substitute his own public key. Alice will then encrypt the session key with Mallory's public key. Mallory decrypts it, re-encrypts it with Bob's real public key, and forwards it. Neither Alice nor Bob knows the key has been compromised. **Solution:** This vulnerability is mitigated by using **digital certificates** and a **Public Key Infrastructure (PKI)** to authenticate the public keys.

### Diffie-Hellman Key Exchange Security

Diffie-Hellman (DH) is a **key agreement protocol**, not an encryption algorithm. It allows two parties to jointly establish a shared secret over an insecure channel.

*   **How it works:**
    1.  **Public Parameters:** Alice and Bob agree on a large prime number `p` and a generator `g` (a primitive root modulo `p`). These are public.
    2.  **Private Computations:**
        *   Alice chooses a private key `a` (a large random integer) and computes her public key `A = g^a mod p`.
        *   Bob chooses a private key `b` and computes his public key `B = g^b mod p`.
    3.  **Exchange:** They exchange `A` and `B`.
    4.  **Shared Secret Calculation:**
        *   Alice computes `S = B^a mod p = (g^b)^a mod p = g^(ab) mod p`.
        *   Bob computes `S = A^b mod p = (g^a)^b mod p = g^(ab) mod p`.
        *   They now share the secret `S`.

*   **Security Basis:** The security of DH relies on the **difficulty of the Discrete Logarithm Problem (DLP)**. Given `g`, `p`, `A = g^a mod p`, it is computationally infeasible to calculate the private exponent `a`. Similarly, calculating `b` from `B` is infeasible. Without `a` or `b`, an eavesdropper cannot compute `g^(ab) mod p`.

*   **Vulnerabilities:**
    *   **Discrete Log Calculation:** Advances in solving DLP (e.g., Pohlig-Hellman algorithm) mean the prime `p` must be very large ("2048-bit" or larger).
    *   **Man-in-the-Middle (MitM) Attack:** The basic DH protocol is also vulnerable to MitM attacks for the same reason as basic RSA: lack of authentication. Mallory can establish separate keys with Alice and Bob and relay messages between them. **Solution:** DH must be combined with an authentication mechanism (e.g., **Digital Signatures**, leading to **Authenticated Diffie-Hellman**) to prevent this.

## 3. Example: Diffie-Hellman in Action (Small Numbers)

*   **Public Parameters:** `p = 23`, `g = 5`
*   **Alice:** Chooses private key `a = 6`, computes public key `A = 5^6 mod 23 = 15625 mod 23 = 8`
*   **Bob:** Chooses private key `b = 15`, computes public key `B = 5^15 mod 23 = 30517578125 mod 23 = 19`
*   **Exchange:** Alice sends `8` to Bob. Bob sends `19` to Alice.
*   **Shared Secret:**
    *   Alice computes `S = 19^6 mod 23 = 47,045,881 mod 23 = 2`
    *   Bob computes `S = 8^15 mod 23 = 35,184,372,088,832 mod 23 = 2`

Both parties independently arrive at the shared secret `2`. An eavesdropper only sees `23`, `5`, `8`, and `19`. Solving `5^x mod 23 = 8` to find `a=6` is easy for these tiny numbers, but astronomically hard for 2048-bit primes.

## 4. Key Points & Summary

| Feature | RSA (for Key Exchange) | Diffie-Hellman Key Exchange |
| :--- | :--- | :--- |
| **Type** | Asymmetric Encryption | Key Agreement Protocol |
| **Security Basis** | Integer Factorization Problem (IFP) | Discrete Logarithm Problem (DLP) |
| **Key Properties** | Provides encryption and authentication (via PKI). | Only establishes a shared secret. |
| **Main Strength** | Directly encrypts a pre-generated key. | Perfect Forward Secrecy (PFS) – a compromised long-term key does not compromise past session keys. |
| **Main Vulnerability** | MitM attack (without PKI). | MitM attack (without authentication). |
| **Mitigation** | Use a PKI with digital certificates. | Combine with digital signatures for authentication (e.g., DSA). |

**Summary:** Both RSA and Diffie-Hellman are secure based on different hard mathematical problems. Their primary weakness in a key exchange scenario is not the underlying math but the **lack of authentication** in their basic forms, leaving them open to MitM attacks. Therefore, they are almost always used in conjunction with a authentication framework like PKI to create a secure and trusted communication channel. Modern protocols like TLS often use a combination of both: RSA to authenticate the server and sometimes to encrypt a DH exchange, which then provides forward secrecy.