# Controlled Access Protocols - Summary

## Key Definitions and Concepts

- **Controlled Access Protocols**: MAC protocols where stations must obtain explicit permission before transmitting data on a shared channel, eliminating collisions entirely.

- **Reservation Protocol**: Divides channel time into a reservation period (for claiming slots) and a data transmission period (for actual data transfer).

- **Polling Protocol**: Master-slave protocol where a controller station systematically polls each secondary station using POLL and SELECT commands to grant transmission permission.

- **Token Passing Protocol**: Uses a special control frame (token) that circulates among stations; only the token holder can transmit data.

- **Token**: A special control frame that grants exclusive right to transmit; passes from station to station in a logical ring.

## Important Formulas and Theorems

- **Polling Efficiency**: Average polling time = n × (Polling overhead + Probability of data × Transmission time)
- **Reservation Efficiency**: Efficiency = Total data transmission time / Total frame time
- **Token Passing Cycle**: Each station gets one transmission opportunity per complete token rotation

## Key Points

1. Controlled access protocols eliminate collisions by requiring explicit permission before transmission.

2. The three main types are: Reservation, Polling, and Token Passing.

3. Reservation protocols divide time into reservation and data transmission periods; efficient when traffic is predictable.

4. Polling uses a central controller (primary) that polls each secondary station sequentially; uses SELECT and POLL commands.

5. Token passing uses a circulating token—only the holder can transmit; implements logical ring topology.

6. Token Ring (IEEE 802.5) and Token Bus (IEEE 802.4) are standard implementations of token passing.

7. Token passing offers highest efficiency under heavy load among controlled access methods.

8. Controlled access provides deterministic latency and guarantees fair access (no starvation).

## Common Mistakes to Avoid

1. Confusing controlled access with random access—controlled access requires permission, random access does not.

2. Incomplete understanding of token passing: Remember that the token must be "released" after transmission, not lost.

3. Assuming polling is always efficient—polling overhead can be significant with many stations or sparse traffic.

4. Forgetting that reservation protocols can be inefficient when number of reservation slots far exceeds active stations.

5. Not understanding that token loss requires recovery procedures—this is critical for network reliability.

## Revision Tips

1. Draw the token passing process for 3-4 stations to reinforce understanding of token circulation.

2. Memorize the difference between SELECT and POLL commands in polling protocols.

3. Remember the efficiency comparison: Token Passing > Reservation > Polling under heavy load.

4. Practice numerical problems involving polling time calculations and reservation efficiency.

5. Review the IEEE standards: 802.5 for Token Ring, 802.4 for Token Bus (token passing variants).
