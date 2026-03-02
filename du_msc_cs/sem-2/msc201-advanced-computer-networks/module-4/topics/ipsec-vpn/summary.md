# IPSec VPN - Summary

## Key Definitions and Concepts

- **IPSec (Internet Protocol Security):** A suite of protocols operating at Layer 3 (Network Layer) of the OSI model that provides confidentiality, integrity, and authentication for IP communications.

- **Security Association (SA):** A unidirectional logical connection defining security parameters between IPSec peers, identified by SPI, destination IP address, and security protocol.

- **AH (Authentication Header):** IPSec protocol providing integrity and authentication but not encryption (RFC 4302).

- **ESP (Encapsulating Security Payload):** IPSec protocol providing encryption and optional authentication (RFC 4303).

- **IKE (Internet Key Exchange):** Protocol for automated key management, establishing SAs between peers (RFC 7296).

- **SPI (Security Parameter Index):** A unique identifier in the IPSec header that helps identify the SA for incoming packets.

## Important Formulas and Theorems

- **IPSec Modes:**
  - Transport Mode: Original IP header preserved, AH/ESP inserted between header and payload
  - Tunnel Mode: Entire original packet encapsulated, new IP header added

- **SA Requirements:** Minimum 2 SAs needed for bidirectional communication (one inbound, one outbound)

- **IKE Phase 1 Modes:**
  - Main Mode: 6 messages, full identity protection
  - Aggressive Mode: 3 messages, faster but exposes identities

## Key Points

- IPSec operates at Layer 3, making it transparent to applications unlike SSL/TLS at Layer 4+

- AH provides integrity and authentication but NOT encryption

- ESP provides encryption and optionally authentication; recommended for modern deployments

- Tunnel mode is essential for site-to-site VPNs; transport mode for host-to-host

- IKEv2 has replaced IKEv1 in modern implementations due to improved security and reliability

- NAT-T (UDP port 4500) enables IPSec traversal through NAT devices

- Common deployment scenarios: Site-to-site (gateway-to-gateway) and Remote-access (client-to-gateway)

## Common Mistakes to Avoid

- Confusing transport mode with tunnel mode—transport preserves original IP header, tunnel does not

- Assuming AH provides encryption—it only provides integrity and authentication

- Forgetting that SAs are unidirectional—bidirectional communication requires two SAs

- Not matching IKE Phase 1 and Phase 2 parameters on both ends (most common VPN failure cause)

## Revision Tips

1. Draw the packet structure for ESP in tunnel mode with both original and new IP headers

2. Create a comparison table of AH vs. ESP vs. SSL VPN with security properties

3. Memorize the IKE Phase 1 and Phase 2 message exchange sequence

4. Practice troubleshooting scenarios: if Phase 1 fails, check PSK/authentication; if Phase 2 fails, check transform sets

5. Review current RFCs (7296 for IKEv2, 4302/4303 for IPSec) for the latest specifications