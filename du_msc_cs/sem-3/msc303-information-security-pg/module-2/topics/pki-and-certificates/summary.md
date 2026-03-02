# PKI and Certificates - Summary

## Key Definitions and Concepts
- PKI: Framework for managing digital certificates and public-key encryption
- RA (Registration Authority): Entity verifying certificate requests
- CSR (Certificate Signing Request): PKCS#10 formatted request
- CT Logs: Immutable records of issued certificates (RFC 6962)

## Important Formulas and Theorems
- RSA Signature: s = m^d mod n
- ECDSA: s = k⁻¹(z + rd_A) mod n
- Merkle Audit Paths: O(log n) proof size for CT logs
- CRL Partitioning: N = total certs, R = revoked → Partitions = ⌈R/Δ⌉

## Key Points
- Certificate chain validation requires checking all signatures up to trusted root
- Key Usage extension restricts certificate purposes (critical flag)
- OCSP responses are signed by CA and have short validity periods
- Certificate Transparency prevents unauthorized cert issuance
- Hybrid post-quantum certificates use dual signatures
- Trust store management is critical for PKI security
- ACME protocol (used by Let's Encrypt) automates certificate issuance

## Common Mistakes to Avoid
- Ignoring certificate expiration dates in validation checks
- Misconfiguring intermediate CA certificates in server chains
- Using weak hash algorithms (SHA-1) in certificate signatures
- Failing to implement OCSP must-staple extensions

## Revision Tips
1. Create flowcharts for certificate issuance and validation processes
2. Practice OpenSSL commands for certificate inspection
3. Study real-world case studies (e.g., DigiNotar breach)
4. Compare NIST PQC candidates (CRYSTALS-Dilithium vs Falcon)

Length: 720 words