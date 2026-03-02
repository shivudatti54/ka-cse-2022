**DomainKeys Identified Mail (DKIM)**

**Definition**

- A cryptographic method for authentication of emails, ensuring sender identity and prevention of spoofing

**Key Concepts**

- **DKIM Signature**:
  - A digital signature created using a public key
  - Comprises of:
    - Header: domain name, selector, and signature algorithm
    - Body: plain text of the email
  - Verifies authenticity and integrity of the email
- **DomainKeys**:
  - A cryptographic system for secure public key exchange and key management
  - Utilizes public key infrastructure (PKI)
- **Selector**:
  - A random string used to identify the DKIM key
  - Assigns a unique identifier to the key for each domain
- **Public Key**:
  - Used for verification of DKIM signatures
  - Can be obtained through DNS lookup (TXT record)
- **Algorithm**:
  - DKIM uses SHA-256 and RSA algorithms for digital signature creation
  - Algorithm and key size selected for the domain

**Important Formulas and Theorems**

- HMAC (Hash-based Message Authentication Code):
  - A one-way hash function for generating digital signatures
  - Used in DKIM signature creation
- RSA Algorithm:
  - An asymmetric cryptographic algorithm for key exchange and encryption
  - Used in DKIM key creation and verification

**Key Points for Revision**

- DKIM uses a hierarchical structure:
  - Email > Domain > DKIM public key
- DKIM validation process:
  1.  Extract DKIM signature from email
  2.  Verify signature using public key
  3.  Check header and body integrity
- Importance of key management and public key infrastructure (PKI)

**Key Terms**

- **Authentication**: Verification of sender identity and email integrity
- **Spoofing**: Fake email addresses used to deceive recipients
- **Key management**: Secure storage and distribution of public and private keys
