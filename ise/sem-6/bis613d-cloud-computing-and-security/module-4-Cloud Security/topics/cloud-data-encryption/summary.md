# Cloud Data Encryption

## Overview

Cloud Data Encryption transforms readable data (plaintext) into unreadable format (ciphertext) using cryptographic algorithms and keys. In cloud computing where data resides on third-party infrastructure, encryption serves as the last line of defense, ensuring even unauthorized physical access or interception leaves information confidential and unusable without proper decryption keys.

## Key Points

- **Symmetric Encryption**: Same secret key for encryption and decryption; very fast and efficient for large data volumes (data-at-rest); challenge is secure key distribution; algorithms include AES-256 (common), DES, 3DES
- **Asymmetric Encryption**: Key pair (public and private keys); data encrypted with public key decrypted only with private key; solves key distribution but computationally intensive; used for key exchange (SSL/TLS), digital signatures; algorithms include RSA, ECC, Diffie-Hellman
- **Encryption at Rest**: Protects stored data on persistent media (disks, databases, object storage); implementations include Full Disk Encryption (FDE - BitLocker, LUKS), File-Level Encryption, Database Encryption (TDE, column-level); example: AWS EBS volumes encrypted with AES-256 via KMS
- **Encryption in Transit**: Protects data moving between endpoints using TLS/SSL protocols; combines asymmetric encryption for session establishment and symmetric encryption for data stream efficiency; example: HTTPS for all cloud service traffic
- **Encryption in Use**: Most challenging state - protects data during processing in memory; technologies include Confidential Computing (Intel SGX, AMD SEV TEEs isolating data from hypervisor/host OS) and Homomorphic Encryption (computations directly on ciphertext, experimental)
- **Key Management Service (KMS)**: Managed services (AWS KMS, Azure Key Vault, Google Cloud KMS) for creating, storing, managing, and controlling cryptographic keys
- **Cloud-HSM**: Dedicated FIPS 140-2 Level 3 validated physical device for secure key storage and operations; higher assurance for strict compliance requirements (AWS CloudHSM, Azure Dedicated HSM)

## Important Concepts

- Three data states requiring encryption: At-Rest (stored on persistent media) → In-Transit (moving between endpoints) → In-Use (being processed in memory)
- Customer-Managed Keys (CMK) provide ultimate control where customer generates and manages keys outside provider KMS, then imports for use
- Shared responsibility model: provider secures infrastructure (security of the cloud), customer encrypts data in that infrastructure (security in the cloud)
- Platform-specific encryption: AWS (SSE-S3, SSE-KMS, SSE-C for S3; EBS encryption; AWS KMS), Azure (SSE for Blob Storage, TDE for SQL Database, Azure Key Vault), GCP (default encryption for Cloud Storage, CMEK options, Cloud KMS)
- Best practices: Encrypt by default, classify data by sensitivity, control keys (prefer CMK for sensitive data), secure transit with TLS 1.2+, monitor and audit key usage, rotate keys regularly, plan for key loss recovery

## Notes

- Memorize three data states (at rest, in transit, in use) - favorite exam topic
- Understand symmetric vs. asymmetric differences, advantages, disadvantages, and use cases (TLS uses both)
- Always frame answers within shared responsibility model for data encryption
- Remember that encryption strength is useless without proper key management
- Know cloud-specific services: AWS KMS, Azure Key Vault, Google Cloud KMS for key management
- Confidential Computing is cutting-edge solution for data in use protection using TEEs
- TLS combines asymmetric (session establishment) and symmetric (bulk data encryption) for efficiency
