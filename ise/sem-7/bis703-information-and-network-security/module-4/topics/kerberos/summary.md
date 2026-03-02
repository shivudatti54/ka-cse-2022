# Kerberos Authentication Protocol

=====================================

### Overview

Kerberos is a network authentication protocol developed at MIT that uses symmetric-key cryptography and a trusted third party (Key Distribution Center) to authenticate clients to servers without transmitting passwords over the network. It uses a ticket-based system with three exchanges: AS, TGS, and AP.

### Key Points

- **Key Distribution Center (KDC):** Trusted third party consisting of the Authentication Server (AS) and Ticket Granting Server (TGS)
- **Ticket Granting Ticket (TGT):** Issued by AS after initial authentication; used to request service tickets from TGS
- **Service Ticket:** Issued by TGS; presented to the target server to gain access
- **Authenticator:** Token proving the ticket presenter is the legitimate owner; encrypted with session key
- **Session Key:** Temporary encryption key generated for a specific communication session
- **Three Exchanges:** AS Exchange (get TGT), TGS Exchange (get service ticket), AP Exchange (access service)
- **Single Sign-On:** Users authenticate once and can access multiple services without re-entering passwords
- **Realm:** A logical authentication domain with its own KDC; cross-realm authentication uses inter-realm keys
- **Kerberos v5 Improvements:** Multiple encryption algorithms, ticket forwarding/delegation, renewable tickets, ASN.1 encoding

### Important Concepts

- AS Exchange: Client sends AS-REQ -> AS returns TGT (encrypted with TGS key) + session key (encrypted with client key)
- TGS Exchange: Client sends TGT + authenticator -> TGS returns service ticket + server session key
- AP Exchange: Client sends service ticket + authenticator -> Server validates and grants access
- Replay protection: Timestamps (5-minute tolerance) and nonces ensure freshness
- Tickets encrypted with target service's secret key; authenticators encrypted with session keys

### Notes

- Memorize all three exchanges (AS, TGS, AP) and what keys encrypt which components
- KDC is a single point of failure -- if it goes down, no new authentication is possible
- Synchronized clocks are critical; Kerberos fails if clock skew exceeds the tolerance window
- Compare Kerberos (symmetric-key, ticket-based) with certificate-based authentication (PKI/SSL)
