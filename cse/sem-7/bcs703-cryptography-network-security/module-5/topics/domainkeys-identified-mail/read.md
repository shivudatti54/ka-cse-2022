# DomainKeys Identified Mail (DKIM)

## 1. Introduction

DomainKeys Identified Mail (DKIM) is an email authentication protocol that provides cryptographic verification of the authenticity and integrity of email messages. Defined in RFC 6376, DKIM enables the receiving mail server to verify that an email message was legitimately sent by the claimed domain owner and has not been altered during transit. This study material provides a comprehensive analysis of DKIM, covering its cryptographic foundations, header structure, canonicalization processes, and integration with broader email security frameworks.

## 2. Formal Definition and Cryptographic Foundation

### 2.1 Definition

DKIM is a digital signature-based authentication mechanism that binds a domain name to an email message. The domain owner associates a public key with a specific selector through a DNS TXT record, and the sending mail server signs portions of the email (specific headers and the body) using its private key. The receiving server retrieves the public key from DNS and verifies the signature.

### 2.2 Cryptographic Basis

DKIM employs asymmetric cryptography (RSA or ECDSA) in conjunction with hash functions (typically SHA-256) to provide:

- **Authentication**: Verification that the message originated from the authorized domain
- **Integrity**: Assurance that the message content has not been modified since signing
- **Non-repudiation**: The domain owner cannot deny having sent the message (within key validity periods)

The signing process computes a hash of the canonicalized email components and encrypts this hash using the sender's private key. The verification process decrypts the signature using the sender's public key and compares the result with a freshly computed hash of the received message components.

**Mathematical Framework:**

For RSA-based DKIM:

- Let M represent the canonicalized message (headers + body)
- Let H(M) denote the SHA-256 hash of M: H(M) = SHA-256(M)
- Let d and n represent the private key components (exponent and modulus)
- The signature σ is computed as: σ = H(M)^d mod n

Verification computes: H(M) ?= σ^e mod n, where e is the public exponent.

## 3. DKIM-Signature Header Field Structure

The DKIM signature is transmitted in the DKIM-Signature header field, which contains multiple tag-value pairs:

```
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple;
                d=example.com; s=selector1;
                h=from:to:subject:date:message-id;
                bh=base64HashValue=; b=base64SignatureValue=
```

### 3.1 Header Field Tags

| Tag | Description                                                 | Required |
| --- | ----------------------------------------------------------- | -------- |
| v   | Protocol version (must be "1")                              | Yes      |
| a   | Signing algorithm (rsa-sha256 or ecdsa-sha256)              | Yes      |
| c   | Canonicalization algorithm for header/body (relaxed/simple) | Yes      |
| d   | Signing domain                                              | Yes      |
| s   | Selector for public key lookup                              | Yes      |
| h   | List of signed header fields                                | Yes      |
| bh  | Hash of the body (body fingerprint)                         | Yes      |
| b   | Digital signature (base64 encoded)                          | Yes      |
| i   | Identity of the signer (optional)                           | No       |
| l   | Body length count (optional)                                | No       |
| t   | Signature timestamp (optional)                              | No       |
| x   | Expiration time (optional)                                  | No       |

## 4. Canonicalization Algorithms

Canonicalization converts email headers and body into a standardized format before hashing, accommodating minor variations that occur during message transit while preserving semantic integrity.

### 4.1 Header Canonicalization

**Simple Canonicalization:**

- Converts all header field names to lowercase
- Unfolding of long header lines (removing CRLF followed by whitespace)
- Removal of trailing whitespace from header field values
- No modification of header field values

Example transformation:

```
From: John Doe <john@example.com>
To: Jane Smith <jane@recipient.org>
```

becomes:

```
from:john doe <john@example.com>
to:jane smith <jane@recipient.org>
```

**Relaxed Canonicalization:**

- Converts all header field names to lowercase
- Unfolds header lines
- Converts sequences of WSP to a single space
- Removes leading/trailing WSP from values
- Lowercases header field values (except for comments)

### 4.2 Body Canonicalization

**Simple Body Canonicalization:**

- Removes all trailing CRLF from the body
- Removes empty lines (CRLF only) at the end of the body

**Relaxed Body Canonicalization:**

- Processes the body similarly to simple
- Does not remove any whitespace within the body

The body hash (bh tag) is computed from the canonicalized body, providing a fingerprint that detects any modification to the message body.

## 5. The Selector Mechanism

### 5.1 Purpose and Function

The selector mechanism enables domain owners to rotate keys and support multiple simultaneous signing keys. The selector is an arbitrary string that, combined with the domain, forms the DNS query for retrieving the public key.

### 5.2 DNS TXT Record Format

The public key is published in a DNS TXT record at:

```
selector1._domainkey.example.com
```

The TXT record format:

```
v=DKIM1; k=rsa; p=Base64EncodedPublicKey...; n=1024
```

**TXT Record Tags:**

- v: Protocol version (DKIM1)
- k: Key type (rsa or ed25519)
- p: Public key data (base64 encoded)
- n: Key size (optional, informational)
- s: Key usage (email or \* for all)
- t: Flags (y for testing, s for strict)

## 6. The DKIM Signing Process

The complete DKIM signing process involves the following steps:

### Step 1: Prepare the Message

- The sending Mail Transfer Agent (MTA) receives the email message
- The email is prepared with all standard headers

### Step 2: Select Header Fields

- The signing algorithm selects which headers to sign (specified in h= tag)
- Typically includes From, To, Subject, Date, Message-ID
- The From header must always be signed

### Step 3: Canonicalize Headers

- Apply the specified canonicalization algorithm (relaxed or simple) to the selected headers
- Maintain header field order as specified in the h= tag

### Step 4: Construct Signed Headers

- Create a string consisting of the canonicalized selected headers
- Each header ends with a CRLF

### Step 5: Canonicalize Body

- Apply body canonicalization to the message body
- Compute the body hash (bh tag)

### Step 6: Compute Signature

- Form the DKIM-Signature header value (without the b= signature)
- Compute: signature_input = "DKIM-Signature:" + header_value
- Hash this string and encrypt with private key to produce the signature

### Step 7: Add Signature Header

- Prepend the DKIM-Signature header to the message
- The signature covers itself except the b= value (which is set to empty during computation)

## 7. The DKIM Verification Process

### Step 1: Extract Signature Header

- The receiving MTA parses the DKIM-Signature header
- Extracts the selector (s=) and domain (d=) tags

### Step 2: DNS Lookup

- Construct the DNS query: selector.\_domainkey.domain
- Retrieve the public key from the TXT record

### Step 3: Parse Public Key

- Decode the key type (k=) and extract the public key data (p=)
- Verify key parameters (algorithm compatibility, key size)

### Step 4: Canonicalize Received Message

- Apply the same canonicalization algorithms specified in c= tag
- Use the header list from h= tag

### Step 5: Verify Signature

- Compute the hash of canonicalized headers
- Decrypt the signature using the public key
- Compare the computed hash with the decrypted signature

### Step 6: Check Body Hash

- Canonicalize the message body
- Compute the body hash
- Compare with bh= value from the signature

### Step 7: Evaluate Results

- If all checks pass: DKIM pass → email is authenticated
- If any check fails: DKIM fail → email may be suspect

## 8. Integration with SPF and DMARC

### 8.1 Sender Policy Framework (SPF)

SPF verifies the sending mail server's IP address against the domain's published policy (published via DNS TXT records at the domain root). While DKIM authenticates the message content and signing domain, SPF authenticates the sending server.

**Key Differences:**
| Aspect | SPF | DKIM |
|--------|-----|------|
| Verifies | SMTP server IP | Message content |
| Lookup | Domain's root TXT | Selector DNS record |
| Alignment | N/A | Requires domain match |

### 8.2 Domain-based Message Authentication, Reporting, and Conformance (DMARC)

DMARC builds upon SPF and DKIM by adding domain alignment verification and policy enforcement. A DMARC policy specifies:

- Which authentication methods must pass (SPF, DKIM, or both)
- The required alignment between the RFC 5322 From address and the authenticated domains
- Disposition instructions for failing messages (none, quarantine, reject)

DMARC resolves the fundamental weakness of individual authentication protocols by ensuring that the claimed sender domain (From header) aligns with the domains validated by SPF and DKIM.

## 9. Security Considerations and Limitations

### 9.1 Security Properties

DKIM provides:

- **Message Integrity**: Any modification to signed content invalidates the signature
- **Sender Authentication**: Only the domain owner possesses the private key
- **Cryptographic Strength**: RSA-2048 and SHA-256 provide adequate security for current threats

### 9.2 Limitations

- **No Encryption**: DKIM does not encrypt message content
- **No Delivery Guarantee**: Valid DKIM does not guarantee email delivery
- **Replay Attacks**: Without expiration (x= tag), replay attacks are possible
- **Key Management**: Private key compromise enables forging messages
- **Forwarding**: DKIM signatures may break when messages are forwarded
- **Partial Signing**: Only specified headers are signed; modified headers remain undetected

### 9.3 Attack Vectors

- **Private Key Compromise**: Attacker obtains the domain's private key
- **DNS Hijacking**: Attacker manipulates DNS records to provide fake public keys
- **Canonicalization Attacks**: Exploiting differences between canonicalization methods
- **Header Injection**: Adding unsigned headers that appear authenticated

## 10. Best Practices for Implementation

### 10.1 Key Management

- Use RSA-2048 or ECDSA P-256 keys minimum
- Rotate keys periodically (recommended: every 6-12 months)
- Use secure key storage (HSM or secure key management services)
- Monitor for key compromise

### 10.2 Configuration Recommendations

- Use relaxed canonicalization for both headers and body
- Sign essential headers: From, To, Subject, Date, Message-ID
- Use long key sizes (RSA-2048 or higher)
- Set appropriate expiration times (x= tag)

### 10.3 Deployment Strategy

- Begin with testing mode (s=y flag in key record)
- Monitor authentication results
- Implement DMARC policy progressively
- Coordinate with SPF and DKIM configuration

## 11. Conclusion

DKIM represents a fundamental advancement in email security, providing cryptographic verification of message authenticity and integrity through digital signatures. By understanding DKIM's theoretical foundations—including canonicalization algorithms, the selector mechanism, and the cryptographic signing/verification processes—security professionals can effectively implement and manage email authentication systems. The integration of DKIM with SPF and DMARC creates a robust email security framework essential for combating phishing, spoofing, and spam in modern communication systems.
