# Internet Key Exchange

## Summary

Internet Key Exchange (IKE) is a protocol used to establish and manage Security Associations (SAs) in IPsec. It operates in two phases: Main Mode and Quick Mode. IKE negotiates the parameters of the SA, establishes a secure channel, and authenticates the parties.

### Important Formulas, Definitions, and Theorems

- IKE: Internet Key Exchange
- SA: Security Association
- Main Mode: A mode of operation in IKE that establishes a secure channel and negotiates the parameters of the SA.
- Quick Mode: A mode of operation in IKE that establishes the IPsec SA using the secure channel established in Main Mode.
- Diffie-Hellman key exchange: A key exchange algorithm used in IKE to establish a shared secret key.

### Key Points

- IKE is a hybrid protocol that combines the Internet Security Association and Key Management Protocol (ISAKMP) with the Oakley Key Determination Protocol.
- Main Mode is a more secure mode of operation than Aggressive Mode.
- IKE can use preshared keys instead of public key authentication.
- Authentication and identity protection are critical components of IKE.
- Diffie-Hellman key exchange is used in IKE to establish a shared secret key.
- IKE is used to establish IPsec SAs in a real-world scenario.

### Revision Tips

- Review the basics of IKE and its modes of operation.
- Practice configuring IKE to use preshared keys instead of public key authentication.
- Apply IKE to establish IPsec SAs in a real-world scenario.
- Focus on the security implications of using IKE to establish IPsec SAs.
