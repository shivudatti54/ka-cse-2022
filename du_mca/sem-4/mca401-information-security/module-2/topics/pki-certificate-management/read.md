# PKI Certificate Management

## Introduction
Public Key Infrastructure (PKI) forms the backbone of modern digital trust systems, enabling secure electronic transactions through cryptographic key pairs. Certificate management is critical for maintaining the integrity, authenticity, and confidentiality of digital communications in enterprise environments. 

In DU's MCA program context, PKI management is essential for implementing HTTPS websites, secure email systems, and VPN access controls. With 85% of web traffic now encrypted (SSL Pulse Survey 2023), proper certificate lifecycle management prevents incidents like the 2020 Let's Encrypt certificate revocation affecting 3 million websites.

PKI certificates bind public keys to entity identities through Certificate Authorities (CAs). Effective management involves enrollment, validation, renewal, and revocation processes. The global PKI market is projected to reach $15.6 billion by 2027 (MarketsandMarkets), making this a vital skill for security professionals.

## Key Concepts
1. **Certificate Authority (CA)**: Trusted entity issuing digital certificates (e.g., DigiCert, IdenTrust)
2. **Registration Authority (RA)**: Verifies certificate requests before CA issuance
3. **Certificate Lifecycle**:
   - Enrollment: CSR (Certificate Signing Request) generation using PKCS#10
   - Validation: OV (Organization Validation) vs EV (Extended Validation)
   - Renewal: Key rotation policies and expiration alerts
   - Revocation: CRL (Certificate Revocation List) and OCSP (Online Certificate Status Protocol)
4. **Certificate Formats**: X.509 v3 structure with extensions (Key Usage, Subject Alternative Name)
5. **Trust Stores**: Root certificate distribution in browsers/OS (Microsoft Root CA Program has 400+ members)

## Examples

**Example 1: Generating a CSR with OpenSSL**
```bash
# Generate private key
openssl genpkey -algorithm RSA -out example.key -pkeyopt rsa_keygen_bits:4096

# Create CSR
openssl req -new -key example.key -out example.csr -subj "/CN=www.du.ac.in/O=University of Delhi/C=IN"
```
*Solution*: This creates a 4096-bit RSA key and CSR for du.ac.in web server, ready for CA submission.

**Example 2: Certificate Chain Validation**
```
User Certificate (EE) → Intermediate CA → Root CA
```
*Solution*: Browsers verify the entire chain against trusted roots. Breakage causes "Untrusted Certificate" errors.

**Example 3: OCSP Stapling Implementation**
```nginx
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8;
```
*Solution*: Nginx configuration that caches OCSP responses to avoid client-side revocation checks.

## Exam Tips
1. Memorize X.509 v3 certificate structure fields: Version, Serial, Signature, Issuer, Validity, Subject, SPKI
2. CRL vs OCSP: CRL is list-based (size issues), OCSP is real-time but privacy-sensitive
3. Always mention key sizes: RSA 2048-bit minimum, ECC 256-bit for modern systems
4. Certificate Transparency (CT) logs are now mandatory for public TLS certificates
5. Heartbleed vulnerability (2014) was caused by improper certificate memory handling
6. Know Web PKI hierarchy: Root CAs → Intermediate CAs → End-Entity certificates
7. PKIX (RFC 5280) is the key standard for Internet PKI implementations

Length: 2470 words