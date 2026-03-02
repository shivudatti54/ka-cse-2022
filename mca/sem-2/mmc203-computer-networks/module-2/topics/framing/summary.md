# Data Link Layer Framing - Summary

## Key Definitions and Concepts

- **Framing:** The process of grouping bits from the physical layer into identifiable frames with clear boundaries
- **Frame:** A data link layer protocol data unit consisting of header, payload (network layer packet), and trailer
- **Bit Stuffing:** Inserting a '0' after five consecutive '1's in the data to prevent flag sequences from appearing naturally
- **Byte Stuffing:** Using escape characters to handle special characters (flags) that appear in the data payload
- **Frame Synchronization:** The receiver's ability to identify correct frame boundaries in the incoming bit stream
- **Transparency:** The ability to transmit any arbitrary data pattern without it being mistaken for control sequences

## Important Formulas and Theorems

- **Bit Stuffing Rule:** After five consecutive 1s in data, insert a 0 (transmitter); remove any 0 following five 1s (receiver)
- **Byte Stuffing Rule:** Replace flag (0x7E) with escape+flag (0x7D 0x5E); replace escape (0x7D) with escape+escape (0x7D 0x5D)
- **Ethernet Frame Size:** Minimum 64 bytes, Maximum 1518 bytes (including FCS)
- **FCS Calculation:** Uses CRC-32 (Ethernet) or CRC-16/CRC-32 (other protocols) for error detection

## Key Points

- Framing is essential because the physical layer only transmits raw bits without any structure
- The data link layer adds addressing (MAC addresses), error detection codes, and control information
- Bit stuffing provides better bandwidth efficiency than byte stuffing as it works at bit granularity
- Ethernet uses physical layer coding violations and preamble/SFD for frame synchronization, not stuffing
- The flag sequence (0x7E) marks frame boundaries in both bit-oriented and character-oriented protocols
- Frame Check Sequence (FCS) in the trailer enables detection of transmission errors
- Proper destuffing must occur before FCS calculation at the receiver
- Different protocols implement framing differently based on their requirements and operating environments

## Common Mistakes to Avoid

1. **Confusing stuffing and destuffing rules:** Remember that the receiver performs the reverse operation - removing stuffed bits/bytes to restore original data
2. **Forgetting that Ethernet does not use stuffing:** This is a common misconception; Ethernet relies on physical layer mechanisms
3. **Applying stuffing to the flag sequence itself:** The delimiters are never stuffed; only the data between flags undergoes stuffing
4. **Ignoring minimum frame size requirements:** Ethernet's 64-byte minimum exists to ensure collision detection, not just for framing

## Revision Tips

1. Practice bit stuffing with various data patterns, including edge cases with consecutive 1s
2. Memorize the standard flag value (0x7E) and escape character (0x7D) for byte stuffing
3. Remember that HDLC is the foundation for many modern bit-oriented protocols
4. Know the difference between synchronous (HDLC) and asynchronous (PPP async) framing
5. Review sample hex dumps of Ethernet frames to identify source/destination addresses
