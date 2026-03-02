# A Model For Network Security - Summary

## Key Definitions

- **Plaintext (P)**: The original, readable message before encryption
- **Ciphertext (C)**: The encrypted, unreadable message after transformation
- **Secret Key (K)**: The parameter that controls encryption and decryption
- **Encryption Algorithm (E)**: The mathematical function that transforms plaintext to ciphertext
- **Decryption Algorithm (D)**: The inverse function that recovers plaintext from ciphertext
- **Security Service**: A processing or communication service that enhances security (confidentiality, integrity, authentication, non-repudiation, availability)
- **Security Attack**: Any attempt to compromise security services

## Important Formulas

- **Encryption**: C = E(K, P)
- **Decryption**: P = D(K, C)
- **Confidentiality**: Achieved when C = E(K, P) and only authorized parties with K can compute P = D(K, C)

## Key Points

1. The basic network security model involves sender, receiver, transmission medium, and adversary

2. The five OSI security services are: Confidentiality, Integrity, Authentication, Non-repudiation, and Availability

3. Passive attacks (eavesdropping, traffic analysis) monitor without altering data; they are hard to detect

4. Active attacks (modification, interruption, fabrication) alter system resources; they are easier to detect but harder to prevent

5. Encryption is the primary mechanism for achieving confidentiality

6. The same key is used for encryption and decryption in symmetric cryptography

7. Security mechanisms include encryption, digital signatures, access control, and intrusion detection

8. The model provides the foundation for understanding classical encryption techniques

## Common Mistakes

1. **Confusing security services with mechanisms**: Services are what we want to achieve; mechanisms are how we achieve them

2. **Misclassifying attacks**: Remember passive attacks don't alter data; active attacks do modify or disrupt

3. **Ignoring availability**: Many students forget availability as a security service, focusing only on confidentiality

4. **Overlooking the adversary**: The model explicitly includes the adversary as a central component