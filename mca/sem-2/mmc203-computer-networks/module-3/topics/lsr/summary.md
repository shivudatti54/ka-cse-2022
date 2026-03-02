# Label Switched Router (LSR) - Summary

## Key Definitions and Concepts

- **Label Switched Router (LSR)**: A network device in MPLS that performs label-based packet forwarding by examining and manipulating labels attached to packets rather than analyzing IP headers at each hop.

- **Label Switching**: A technique where short, fixed-length labels are used to make forwarding decisions, enabling faster packet processing compared to traditional IP routing.

- **Forwarding Equivalence Class (FEC)**: A group of packets that are forwarded in the same manner, typically based on destination address, service class, or tunnel identifier.

- **Label-Switched Path (LSP)**: The end-to-end path through which labeled packets travel in an MPLS network, established by label distribution protocols.

## Important Formulas and Concepts

- **Label Operations**: Push (add label at ingress), Swap (replace label at intermediate), Pop (remove label at egress)
- **LDP Messages**: Discovery, Adjacency, Session, and Notification messages
- **PHP (Penultimate Hop Popping)**: Optimization technique where the second-to-last LSR removes the label

## Key Points

- LSR operates at layer 2.5 of the OSI model, between data link and network layers.
- The three functional components are: control plane (routing and label distribution), forwarding plane (actual packet switching), and management plane (configuration).
- The Label Information Base (LIB) stores mappings between incoming labels, outgoing labels, and next-hop information.
- LDP is the standard protocol for distributing label bindings between adjacent LSRs.
- There are three types of LSR: Ingress (LER at entry), Intermediate (performs label swapping), and Egress (LER at exit).
- Penultimate Hop Popping reduces processing burden on egress LSR by removing labels at the previous hop.
- LSR enables faster forwarding through simple label lookup instead of complex IP prefix matching.
- MPLS with LSR supports advanced features including traffic engineering, QoS, and layer 3 VPNs.

## Common Mistakes to Avoid

- Confusing LER (Label Edge Router) with LSR - LERs are special LSRs at network boundaries that perform additional functions.
- Believing that MPLS replaces IP routing - MPLS operates in conjunction with IP routing protocols.
- Forgetting that labels are swapped at each hop except at penultimate hop (with PHP) or egress.
- Not understanding that LIB is built from LDP information, not directly from routing protocols.

## Revision Tips

- Practice drawing the MPLS packet format with label headers to understand the label stack operations.
- Remember the label operation sequence: Push → Swap → Pop (at egress) or Swap → Swap → PHP → Pop.
- Review the functions of each plane in LSR architecture and be able to list them from memory.
- Understand how LDP establishes sessions and exchanges label bindings between neighboring LSRs.
- Focus on the advantages of LSR-based forwarding over traditional IP forwarding for exam preparation.
