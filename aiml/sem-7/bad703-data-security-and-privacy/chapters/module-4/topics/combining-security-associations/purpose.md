# Learning Purpose: Combining Security Associations

**1. Importance**
This topic is crucial because modern secure communication, such as a VPN connection, rarely relies on a single cryptographic protocol. Instead, it uses multiple, layered security associations (SAs) in combination to provide confidentiality, integrity, and authenticity. Understanding how to correctly combine these SAs is fundamental to building robust and comprehensive security architectures that protect data in transit against a wide array of threats.

**2. Learning Outcomes**
Students will learn the purpose and structure of security associations. They will explore how different SAs (e.g., for IPsec AH and ESP) are bundled together to form layered security policies within a single system (SA bundling) and how they are sequenced across multiple systems to create secure end-to-end channels (SA sequencing). This includes understanding the logical order of application and the resultant security properties.

**3. Connection to Other Concepts**
This knowledge directly builds upon understanding individual security protocols like IPsec (AH/ESP/IKE) and TLS from previous modules. It is a practical application of cryptographic concepts (encryption, hashing) and is essential for implementing complex network security designs, including VPNs and secure gateways, which will be covered in subsequent topics.

**4. Real-World Applications**
The principle of combining SAs is applied whenever a VPN tunnel is established, ensuring both the payload is encrypted and the packet itself is authenticated. It is also used in secure web browsing (TLS over TCP), where a transport-layer SA is layered over a network-layer connection, providing end-to-end security between a client and a server across potentially insecure networks.