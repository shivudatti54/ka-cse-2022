# Public Key Cryptography in Blockchain

## What is Public Key Cryptography?

Public key cryptography (asymmetric cryptography) uses mathematically related key pairs: a private key (secret) and a public key (shareable). Data encrypted with one key can only be decrypted with the other.

## Key Concepts

### Private Key
- Random 256-bit number (blockchain standard)
- Must be kept absolutely secret
- Used to sign transactions
- Losing it means losing funds forever

### Public Key
- Derived mathematically from private key
- Can be shared freely
- Used to verify signatures
- Cannot be used to derive private key

### Address
- Derived from public key (usually hashed)
- Used for receiving funds
- Human-readable identifier
- Shorter than full public key

## Key Generation Flow

```
Random Number -> Private Key -> Public Key -> Address
     |               |              |           |
  256 bits      256 bits       512 bits    160-256 bits
  (secret)      (secret)      (public)     (public)
```

## Elliptic Curve Cryptography (ECC)

### Why ECC?
- Smaller keys than RSA for same security
- 256-bit ECC = ~3072-bit RSA
- Efficient for mobile/embedded devices
- Standard in blockchain

### secp256k1 Curve
- Used by Bitcoin and Ethereum
- Equation: y² = x³ + 7
- Efficient implementation
- Well-analyzed security

## Mathematical Foundation

### Key Generation (Simplified)
1. Choose random private key: d
2. Public key: Q = d × G (elliptic curve multiplication)
3. G is a known generator point on the curve
4. Multiplication is easy; division (finding d from Q) is hard

### Security Basis
- Discrete Logarithm Problem
- Easy: multiply point by scalar
- Hard: find scalar given result (ECDLP)
- Currently requires 2^128 operations to break

## Address Generation

### Bitcoin Address
```
Private Key
    ↓
Public Key (ECDSA secp256k1)
    ↓
SHA-256
    ↓
RIPEMD-160 (Hash160)
    ↓
Version Byte + Checksum
    ↓
Base58 Encoding
    ↓
Bitcoin Address (e.g., 1A1zP1...)
```

### Ethereum Address
```
Private Key
    ↓
Public Key (ECDSA secp256k1)
    ↓
Keccak-256 (last 20 bytes)
    ↓
Add "0x" prefix
    ↓
Ethereum Address (e.g., 0x742d35...)
```

## Security Best Practices

1. **Key Generation**: Use cryptographically secure random source
2. **Storage**: Hardware wallets, encrypted backups
3. **Never Share**: Private key exposure = total loss
4. **Backup**: Multiple secure backups essential
5. **Key Derivation**: Use HD wallets (BIP-32/39/44)

## HD Wallets (Hierarchical Deterministic)

- Generate many keys from single seed phrase
- 12 or 24 word mnemonic backup
- BIP-32/39/44 standards
- Organized key hierarchy

## Summary

- Asymmetric: private (secret) and public (shareable) keys
- ECC provides compact keys with strong security
- secp256k1 curve standard in blockchain
- Addresses derived from public keys via hashing
- HD wallets enable secure key management
