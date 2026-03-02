# Learning Objectives

After studying this topic, you should be able to:

1. **Define** cryptographic hash functions and explain the three essential security properties: pre-image resistance, second pre-image resistance, and collision resistance.

2. **Analyze** the birthday paradox and calculate the expected number of hash operations needed to find a collision for a given hash output length.

3. **Compare and contrast** major hash algorithms (MD5, SHA-1, SHA-2, SHA-3) in terms of output size, internal structure, and current security status.

4. **Explain** the Merkle-Damgård construction and identify its vulnerability to length extension attacks.

5. **Distinguish** between hash functions and Message Authentication Codes (MACs), clearly articulating how MACs provide both integrity and authentication.

6. **Derive and explain** the HMAC construction, including the role of ipad, opad, and the nested hashing structure in preventing known attacks.

7. **Evaluate** the three authenticated encryption compositions (Encrypt-then-MAC, MAC-then-Encrypt, Encrypt-and-MAC) and identify their usage in real-world protocols like TLS, IPSec, and SSH.

8. **Apply** hash functions and MACs to solve practical security problems such as password storage, message authentication, and software integrity verification.