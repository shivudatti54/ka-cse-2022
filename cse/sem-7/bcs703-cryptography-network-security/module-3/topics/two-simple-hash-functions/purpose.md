# Learning Purpose: Two Simple Hash Functions

**1. Why this topic matters**
Studying two simple hash functions provides an accessible introduction to how hash algorithms convert variable-length input into fixed-length output. Within Module 3, these basic constructions illustrate the core design principles and security properties of hash functions before progressing to more complex and secure algorithms, helping students understand what makes a hash function effective or vulnerable.

**2. What you will learn**
You will learn the mechanics of two simple hash function designs, such as XOR-based block hashing and one-bit circular shift hashing, and how they produce fixed-size hash values from arbitrary input. You will analyze their basic security properties, understand why they fail to provide adequate collision resistance, and recognize the design improvements that modern hash functions like SHA-256 incorporate.

**3. How it connects to other topics**
This topic complements the applications of cryptographic hash functions studied in Module 3 by providing concrete examples of hash construction and their limitations. Understanding these simple designs creates the foundation for appreciating why more sophisticated hash functions are required in the digital signatures, message authentication, and integrity verification used throughout Modules 4 and 5.

**4. Real-world relevance**
Simple hash functions like basic checksums are still used for error detection in data transmission and file integrity verification where security is not the primary concern. Understanding their weaknesses explains why critical applications such as password storage, digital certificates, and blockchain systems require cryptographically strong hash functions instead.
