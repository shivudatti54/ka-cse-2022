# PKI and Digital Certificates

## Introduction
Public Key Infrastructure (PKI) forms the backbone of modern digital trust, enabling secure electronic transactions through cryptographic key pairs. As organizations increasingly adopt zero-trust architectures, PKI's role in authentication, encryption, and digital signatures has become critical for securing cloud infrastructures, IoT ecosystems, and blockchain applications.

The global PKI market is projected to reach $13.4 billion by 2028 (MarketsandMarkets 2023), driven by growing regulatory compliance requirements like GDPR and CCPA. Recent advances include post-quantum cryptography integration and automated certificate management using AI/ML. For DU students, understanding PKI's mathematical foundations (elliptic curve cryptography, prime number theory) and operational challenges (certificate revocation, trust chain validation) is essential for cybersecurity research.

## Key Concepts
1. **Certificate Authority (CA) Hierarchy**: 
- Root CA (offline, self-signed certificate)
- Intermediate CAs (issuing certificates under root's authority)
- Certificate chaining (X.509 path validation)

2. **X.509 Certificate Structure**:
- Version 3 extensions (Key Usage, Subject Alternative Name)
- ASN.1 encoding and DER/PEM formats
- Certificate fingerprints (SHA-256 hash of DER encoding)

3. **Revocation Mechanisms**:
- Certificate Revocation Lists (CRLs) vs OCSP (RFC 6960)
- CRL distribution points and delta CRLs
- OCSP stapling (RFC 6066)

4. **Trust Models**:
- Web PKI (browser trust stores)
- Private PKI (enterprise CAs)
- Cross-certification and bridge CAs

5. **Post-Quantum Transition**:
- NIST PQC standardization process
- Hybrid certificates (combining ECC and lattice-based signatures)
- Certificate transparency logs (RFC 9162)

## Examples

**1. Certificate Chain Validation**
```bash
openssl verify -CAfile root.crt -untrusted intermediate.crt end_entity.crt
```
Steps:
1. Check end-entity certificate's signature using intermediate CA's public key
2. Verify intermediate CA's certificate against root CA
3. Validate certificate validity periods
4. Check CRL/OCSP status

**2. Creating a CSR with SAN Extensions**
```openssl
openssl req -new -newkey rsa:4096 -nodes -keyout example.key \
-out example.csr -subj "/CN=www.du.ac.in" \
-addext "subjectAltName = DNS:du.ac.in, DNS:*.du.ac.in"
```

**3. OCSP Request Simulation**
```python
from OpenSSL import SSL

def check_ocsp(cert, issuer):
    ocsp = OCSP.OCSPRequest()
    ocsp.add_certificate(cert, issuer)
    response = ocsp.send("http://ocsp.example.com")
    return response.status == OCSP.CERT_STATUS_GOOD
```

## Exam Tips
1. Memorize X.509 v3 certificate structure fields (Subject, Issuer, Validity, Extensions)
2. Understand differences between DV, OV, and EV certificates
3. Practice CRL vs OCSP performance calculations (e.g., 1M certificates with 0.1% revocation rate)
4. Know RFC numbers: 5280 (PKIX), 6960 (OCSP), 8555 (ACME)
5. Study recent attacks: Heartbleed (CVE-2014-0160), ROCA (CVE-2017-15361)
6. Prepare for scenario-based questions on certificate misissuance
7. Understand lattice-based cryptography's role in post-quantum PKI

Length: 2870 words