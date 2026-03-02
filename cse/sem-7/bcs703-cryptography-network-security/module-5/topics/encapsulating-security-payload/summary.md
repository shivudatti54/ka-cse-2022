# Encapsulating Security Payload - Summary

## Key Definitions and Concepts

- **ESP**: IPsec protocol providing confidentiality (encryption), data integrity, authentication, and anti-replay protection
- **Security Association (SA)**: One-way logical connection identified by SPI + Destination IP + Protocol (ESP)
- **Transport Mode**: Encrypts only payload (used for end-to-end security between devices)
- **Tunnel Mode**: Encrypts entire IP packet (used in VPNs between gateways)
- **SPI (Security Parameters Index)**: 32-bit identifier for SA database lookup
- **Anti-Replay Protection**: Uses sequence numbers to detect duplicate packets

## Important Formulas and Theorems

```markdown
1. Padding Calculation:
   Padding Length = (Block Size - (Payload Length % Block Size)) % Block Size

2. HMAC Computation:
   Authentication Data = HMAC(Shared_Key, ESP_Header || Encrypted_Payload || ESP_Trailer)

3. ESP Packet Length:
   Total Length = Original_IP_Length + ESP_Header_Length + IV_Length + Pad_Length + Auth_Data_Length
```

## Key Points

- Operates at OSI Layer 3 (Network Layer) as part of IPsec
- Provides both encryption (AES, 3DES) and authentication (HMAC-SHA1/SHA256)
- Two header components: ESP Header (SPI + Seq No) and ESP Trailer (Padding, Next Header)
- Uses IKE (Internet Key Exchange) for automatic SA establishment
- Packet processing steps: Lookup SA → Check Seq No → Decrypt → Verify Auth Data
- Modes: Transport (protocol 50) for host-to-host, Tunnel (protocol 50) for network-to-network
- Combines with AH (Authentication Header) for enhanced security using Security Associations

## Common Mistakes to Avoid

1. Confusing transport mode (original IP header visible) with tunnel mode (new IP header)
2. Neglecting sequence number checks leading to replay attack vulnerabilities
3. Incorrect padding implementation causing decryption failures
4. Assuming ESP provides routing protection (only tunnel mode hides original IP header)

## Revision Tips

1. Create comparison tables: Transport vs Tunnel Mode | ESP vs AH
2. Practice drawing ESP packet format with header/trailer fields
3. Memorize protocol numbers: ESP=50, IKE=500 (UDP)
4. Focus on SA establishment process (IKE Phase 1 & 2) and SPI usage
