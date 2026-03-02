# Key Management

## What is Key Management?

Key management is the administration of cryptographic keys throughout their lifecycle: generation, storage, distribution, usage, rotation, and destruction. Proper key management is critical - encryption is only as strong as key protection.

## Key Lifecycle

### 1. Generation

- Use cryptographically secure random number generators
- Adequate key length (AES-256, RSA-2048+)
- Hardware Security Modules (HSM) for high-security keys

### 2. Storage

- Never store keys with encrypted data
- Use dedicated key management services
- HSM-backed storage for sensitive keys

### 3. Distribution

- Encrypt keys in transit
- Minimum exposure principle
- Secure key exchange protocols

### 4. Usage

- Access controls on key usage
- Audit logging of key operations
- Separation of duties

### 5. Rotation

- Regular automatic rotation
- Rotate on suspected compromise
- Maintain backward compatibility during rotation

### 6. Destruction

- Cryptographic erasure
- Secure deletion procedures
- Documented destruction process

## Cloud Key Management Services

### AWS KMS

- **Managed Keys**: AWS-managed CMKs
- **Customer Keys**: Customer-managed CMKs
- **Imported Keys**: Bring your own key (BYOK)
- **HSM**: CloudHSM for dedicated hardware

### Azure Key Vault

- **Secrets**: Passwords, connection strings
- **Keys**: Cryptographic keys
- **Certificates**: SSL/TLS certificates
- **HSM-backed**: Premium tier with HSM

### GCP Cloud KMS

- **Software Keys**: Google-managed protection
- **HSM Keys**: Cloud HSM protection
- **External Keys**: External key manager
- **Customer-managed encryption keys (CMEK)**

## Envelope Encryption

Envelope encryption uses a hierarchy of keys:

```
Master Key (in KMS)
    |
    v
Data Encryption Key (DEK)
    |
    v
Encrypted Data
```

**Benefits:**

- Master key never leaves KMS
- DEK can be rotated without re-encrypting data
- Efficient for large datasets

## Best Practices

1. **Use managed KMS** - Don't roll your own
2. **Enable automatic rotation** - At least annually
3. **Implement least privilege** - Restrict key access
4. **Audit key usage** - Log all key operations
5. **Separate key from data** - Different access controls
6. **Have recovery plans** - Key backup and recovery
7. **Use HSM for sensitive keys** - Hardware protection

## Summary

- Key management covers entire key lifecycle
- Cloud KMS services provide managed key storage
- Envelope encryption separates master and data keys
- Automatic rotation is essential
- HSMs provide hardware-level protection
