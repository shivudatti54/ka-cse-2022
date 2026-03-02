# Public Key Infrastructures

## 1. Introduction to Public Key Infrastructure

Public Key Infrastructure (PKI) constitutes a comprehensive framework of policies, procedures, hardware, software, and cryptographic technologies designed to facilitate the creation, distribution, management, storage, and revocation of digital certificates and public-private key pairs. PKI serves as the foundational security infrastructure enabling asymmetric cryptography in practical, scalable deployments across modern computing environments.

The fundamental challenge PKI addresses is establishing trust in electronic communications. In asymmetric cryptography, while public keys can be freely distributed, their association with specific entities must be reliably verified. PKI provides this trust through a hierarchical chain of authorities, wherein Certificate Authorities (CAs) vouch for the binding between public keys and identities through digitally signed certificates.

### 1.1 Need for PKI

The proliferation of electronic commerce, online banking, and internet communication necessitated a standardized mechanism for establishing identity in cyberspace. PKI emerged as the predominant solution, enabling:

- **Entity Authentication**: Verifying the identity of communicating parties
- **Data Integrity**: Ensuring messages have not been altered during transmission
- **Confidentiality**: Protecting sensitive information through encryption
- **Non-repudiation**: Preventing entities from denying prior commitments or actions

## 2. X.509 Certificate Structure

### 2.1 Certificate Fields

X.509 v3 certificates, as defined in RFC 5280, contain the following structural components:

**Certificate Fields:**

- **Version**: Indicates X.509 version (v1, v2, or v3)
- **Serial Number**: Unique positive integer assigned by the CA
- **Signature Algorithm**: OID identifying the algorithm used to sign the certificate
- **Issuer**: Distinguished Name (DN) of the signing CA
- **Validity**: NotBefore and NotAfter timestamps defining certificate lifetime
- **Subject**: DN of the entity whose public key is certified
- **Subject Public Key Info**: Algorithm identifier and public key value

**Standard Extensions (v3):**

- **Key Usage**: Defines permitted uses of the public key (digitalSignature, keyEncipherment, etc.)
- **Extended Key Usage**: Specific purposes (serverAuth, clientAuth, codeSigning)
- **Subject Alternative Names (SAN)**: Additional identities (DNS names, IP addresses, email)
- **Basic Constraints**: Indicates whether subject is a CA and maximum path length
- **Authority Key Identifier**: Identifies the signing CA's public key
- **Subject Key Identifier**: Identifies the subject's public key
- **CRL Distribution Points**: URLs for obtaining Certificate Revocation Lists

### 2.2 Certificate Chain Validation Algorithm

Certificate chain validation (path validation) constitutes a critical process wherein relying parties verify the complete trust chain from an end-entity certificate to a trusted root. The algorithm proceeds as follows:

**Algorithm: ValidateCertificateChain(Input: cert, trust_anchors, policy, constraints)**

```
1. Initialize empty chain ← []
2. If cert is self-issued and in trust_anchors:
      Return success with chain containing cert
3. For each candidate in FindIssuers(cert):
      If ValidateCertificateChain(candidate, trust_anchors, policy, constraints) succeeds:
          Append cert to candidate's chain
          If CheckConstraints(candidate, constraints) passes:
              Return success with validated chain
4. Return failure: no valid chain found
```

**Constraint Verification:**

- **Name Constraints**: Ensure all subject names fall within permitted namespace
- **Policy Constraints**: Verify certificate policies align with relying party requirements
- **Basic Constraints**: Validate CA status and path length limitations
- **Key Usage**: Confirm intended usage matches certificate permissions

## 3. PKI Trust Models

### 3.1 Hierarchical Trust Model

The hierarchical (tree) model represents the predominant PKI deployment, characterized by a single root CA from which trust cascades through intermediate CAs to end-entity certificates. This model provides:

- **Single Trust Anchor**: One root CA establishes trust for entire hierarchy
- **Deterministic Path Discovery**: Path from any certificate to root follows parent pointers
- **Scalability**: Supports large populations through distributed intermediate CAs

**Formal Trust Relationship:**

```
T(A, B) = TRUE if (∃ path A →* Root) ∧ (Root ∈ TrustAnchors) ∧ (∀ cert_i in path: Valid(cert_i))
```

### 3.2 Mesh Trust Model

In mesh (network) models, multiple CAs operate as trust anchors without centralized hierarchy. Cross-certificates establish peer-to-peer trust relationships between CAs.

**Advantages:**

- No single point of failure at root level
- Organizational autonomy in CA operations

**Challenges:**

- Path discovery complexity increases exponentially with CA count
- Potential for circular trust relationships
- Policy mapping complications across domains

### 3.3 Web of Trust Model

The Web of Trust (WoT), exemplified by PGP, distributes trust through peer endorsements rather than centralized authorities. Each participant may certify keys of others, creating decentralized trust graphs.

**Trust Metrics:**

- **Direct Trust**: Key explicitly trusted as introducer
- **Threshold Trust**: Path length to trusted key exceeds configured threshold
- **Marginal Trust**: Limited confidence based on path configuration

## 4. Certificate Revocation Mechanisms

### 4.1 Certificate Revocation Lists (CRL)

CRLs, as specified in RFC 5280, provide time-stamped lists of revoked certificate serial numbers issued by CAs. The CRL structure includes:

```
CRL ::= SEQUENCE {
    tbsCertList        TBSCertList,
    signatureAlgorithm AlgorithmIdentifier,
    signatureValue     BIT STRING
}

TBSCertList ::= SEQUENCE {
    version         Version OPTIONAL,
    signature       AlgorithmIdentifier,
    issuer          Name,
    thisUpdate      Time,
    nextUpdate      Time OPTIONAL,
    revokedCertificates SEQUENCE OF RevokedCertificate OPTIONAL,
    extensions      [0] Extensions OPTIONAL
}
```

**CRL Distribution Points (CDP):**

- LDAP-based directories for enterprise deployments
- HTTP URLs for public certificate distribution
- Multiple distribution points ensure availability

**Limitations:**

- Large CRLs consume significant bandwidth
- Freshness depends on CA's CRL publication frequency
- Client must download entire CRL for status verification

### 4.2 Online Certificate Status Protocol (OCSP)

OCSP, defined in RFC 6960, provides real-time certificate status via request-response protocol, addressing CRL limitations:

**OCSP Request:**

```
OCSPRequest ::= SEQUENCE {
    tbsRequest              TBSRequest,
    optionalSignature [0]   Signature OPTIONAL
}

TBSRequest ::= SEQUENCE {
    version           [0] EXPLICIT Version DEFAULT v1,
    requestorName     [1] EXPLICIT GeneralName OPTIONAL,
    requestList       SEQUENCE OF SingleRequest,
    extensions        [2] EXPLICIT Extensions OPTIONAL
}
```

**OCSP Response Types:**

- **Good**: Certificate is not revoked
- **Revoked**: Certificate is revoked (with reason code)
- **Unknown**: CA cannot determine certificate status

**OCSP Stapling (RFC 6066):**
Allows servers to pre-fetch and "staple" OCSP responses to clients, reducing client-CA communication and improving privacy. The server includes the cached OCSP response in the TLS handshake.

## 5. PKI Policy Framework

### 5.1 Certificate Policy (CP)

A Certificate Policy, as defined in RFC 3647, is a named set of rules indicating applicability of certificates to a particular community or class of application. The CP addresses:

- **Certificate Initial Validation Level**: Domain Validation (DV), Organization Validation (OV), Extended Validation (EV)
- **Key Usage Restrictions**: Permitted cryptographic operations
- **Certificate Lifecycle**: Validity period, renewal, re-key procedures
- **Revocation Handling**: Mechanisms and response times
- **Liability**: Warranties and limitations

### 5.2 Certificate Practice Statement (CPS)

The CPS is a document describing the practices a CA employs in issuing certificates. While the CP states what the CA does, the CPS explains how:

- **Operational Procedures**: Certificate enrollment, issuance, delivery
- **Infrastructure Security**: Physical security, personnel controls
- **Audit Procedures**: Logging, monitoring, incident response
- **Compliance**: Regulatory and standard conformance

### 5.3 Policy vs. Practice: Critical Distinction

The distinction between CP and CPS carries significant legal and operational implications:

| Aspect   | Certificate Policy        | Certificate Practice Statement |
| -------- | ------------------------- | ------------------------------ |
| Purpose  | States requirements       | Describes implementation       |
| Audience | Relying parties, auditors | CA operations, auditors        |
| Scope    | Applicability criteria    | Procedural details             |
| Binding  | Defines trust             | Defines compliance             |

## 6. Cross-Certification

### 6.1 Concept and Architecture

Cross-certification establishes trust relationships between separate PKI domains, enabling certificate validation across organizational boundaries. This is achieved through cross-certificates wherein CA A issues a certificate to CA B (and vice versa).

**Cross-Certificate Structure:**

```
CrossCertificate ::= SEQUENCE {
    certificate         Certificate
}
```

### 6.2 Qualified Subordination

Qualified subordination allows one CA to constrain another's authority through policy constraints in cross-certificates:

- **Name Constraints**: Restrict subject name space
- **Policy Constraints**: Require specific certificate policies
- **Path Length**: Limit subordinate CA hierarchy depth

## 7. Key Management and HSM

### 7.1 Private Key Protection

Private key security is paramount in PKI. Cryptographically Secure Pseudo-Random Number Generators (CSPRNGs) generate keys using entropy sources (hardware RNG, system interrupts, user input).

**Key Generation Standards:**

- RSA: 2048-bit minimum (4096-bit recommended for long-term security)
- ECDSA/ECDHE: P-256 or P-384 curves (per NIST recommendations)

### 7.2 Hardware Security Modules (HSMs)

HSMs provide tamper-resistant, FIPS 140-2/3 certified environments for cryptographic operations:

- **Key Generation**: Secure key creation within HSM boundaries
- **Key Storage**: Protected key material storage
- **Signing Operations**: Private key never exported for signing
- **Audit Logging**: Tamper-evident operation logs

## 8. Practical Certificate Validation: Browser Perspective

Modern browsers perform comprehensive certificate validation during TLS handshakes:

1. **Chain Construction**: Build certificate chain from end-entity to root
2. **Signature Verification**: Verify each certificate signature using issuer's public key
3. **Validity Period Check**: Confirm current time falls within NotBefore and NotAfter
4. **Revocation Checking**: Query CRL/OCSP for certificate status
5. **Hostname Verification**: Match certificate SAN/DN to requested hostname
6. **Constraint Verification**: Validate all path constraints
7. **Trust Anchor Match**: Confirm root CA is in browser's trust store

**Certificate Transparency (CT):**
RFC 6962 mandates that CAs publicly log all issued certificates, enabling detection of unauthorized certificate issuance. Browsers verify SCT (Signed Certificate Timestamp) inclusion during validation.

## 9. Mathematical Foundations

### 9.1 RSA Security

RSA security rests on the computational hardness of integer factorization:

**Theorem**: Given n = pq where p and q are distinct primes, computing φ(n) = (p-1)(q-1) requires factoring n.

**Proof Sketch**: If an adversary can compute φ(n), they can recover p and q via:

```
p + q = n - φ(n) + 1
(p - q) = √((p + q)² - 4n)
p = (p + q + (p - q))/2
```

Thus, factoring n is equivalent to breaking RSA.

### 9.2 Digital Signature Verification

Certificate signatures employ RSA-PSS or ECDSA:

**Verification Algorithm**:

```
Input: Certificate data D, Signature S, CA public key (n, e)
1. Compute H = Hash(D) using specified hash function
2. Recover message hash: H' = S^e mod n
3. Return (H == H')
```

The security relies on the one-way property of the hash function and the RSA hardness assumption.
