# Subnetting and Routing Algorithms

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

### 1.1 What is Subnetting?

**Subnetting** is the process of dividing a single IP network into multiple smaller subnetworks (subnets). This fundamental networking technique allows network administrators to create efficient, secure, and manageable network architectures. In today's interconnected world, where organizations ranging from small businesses to global enterprises rely on computer networks, subnetting plays a crucial role in optimizing network performance and security.

### 1.2 Why This Topic Matters

For students at Delhi University studying under the NEP 2024 UGCF curriculum, understanding subnetting and routing algorithms forms the backbone of computer networking knowledge. These concepts are essential for:

- **Network Design**: Creating scalable and efficient network infrastructures
- **IP Address Management**: Conserving address space and reducing broadcast domains
- **Security Implementation**: Isolating sensitive network segments
- **Troubleshooting**: Diagnosing and resolving network connectivity issues
- **Industry Relevance**: Skills required for network administrator, system administrator, and DevOps roles

---

## 2. Subnetting Fundamentals

### 2.1 IP Address Structure

An IPv4 address is a 32-bit number expressed in dotted decimal notation (e.g., 192.168.1.1). Each address consists of two parts:

```
┌─────────────────────────────────────────────────────────┐
│              Network ID (Network Portion)               │
├─────────────────────────────────────────────────────────┤
│              Host ID (Host Portion)                     │
└─────────────────────────────────────────────────────────┘
32 bits
```

### 2.2 IP Address Classes

| Class | First Octet Range | Default Subnet Mask | CIDR Notation | Max Hosts per Network |
|-------|-------------------|---------------------|---------------|----------------------|
| A     | 1 – 126           | 255.0.0.0           | /8            | 16,777,214           |
| B     | 128 – 191         | 255.255.0.0         | /16           | 65,534               |
| C     | 192 – 223         | 255.255.255.0       | /24           | 254                  |
| D     | 224 – 239         | Not applicable      | Not applicable| Multicast            |
| E     | 240 – 255         | Not applicable      | Not applicable| Reserved             |

**Important Notes:**
- **127.x.x.x** is reserved for loopback testing (localhost)
- **0.0.0.0** represents the default route
- Private IP ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16

### 2.3 Subnet Mask

A subnet mask is a 32-bit number that divides the IP address into network and host portions. The bits set to "1" represent the network portion, and bits set to "0" represent the host portion.

**Common Subnet Masks:**

| Subnet Mask      | CIDR | Binary Representation          | Number of Hosts |
|------------------|------|--------------------------------|-----------------|
| 255.255.255.0    | /24  | 11111111.11111111.11111111.00000000 | 254         |
| 255.255.255.128  | /25  | 11111111.11111111.11111111.10000000 | 126         |
| 255.255.255.192  | /26  | 11111111.11111111.11111111.11000000 | 62          |
| 255.255.255.224  | /27  | 11111111.11111111.11111111.11100000 | 30          |
| 255.255.255.240  | /28  | 11111111.11111111.11111111.11110000 | 14          |
| 255.255.255.248  | /29  | 11111111.11111111.11111111.11111000 | 6           |
| 255.255.255.252  | /30  | 11111111.11111111.11111111.11111100 | 2           |

### 2.4 CIDR (Classless Inter-Domain Routing)

CIDR is a method of allocating IP addresses and routing prefixes that replaces the classful addressing system. CIDR notation represents IP addresses and their associated network prefix as a suffix (e.g., 192.168.1.0/24).

**CIDR Block Size Calculation:**
```
Number of IP addresses = 2^(32 - CIDR prefix)
Number of usable hosts = 2^(32 - CIDR prefix) - 2
```

---

## 3. The Subnetting Process: Step-by-Step

### 3.1 Subnetting Formula

To effectively subnet a network, you need to understand these key formulas:

```
Number of subnets = 2^n  (where n = number of borrowed bits)
Number of hosts per subnet = 2^h - 2  (where h = remaining host bits)
```

**Note:** We subtract 2 because the first address is the network address and the last is the broadcast address.

### 3.2 Example 1: Subnetting a Class C Network

**Problem:** Subnet the network 192.168.10.0/24 into 4 equal subnets.

**Solution:**

**Step 1:** Determine the number of bits to borrow
- Need 4 subnets: 2^n ≥ 4, so n = 2 (borrow 2 bits)
- Original host bits: 8
- Remaining host bits: 8 - 2 = 6

**Step 2:** Determine the new subnet mask
- Original: /24
- New: /26 (24 + 2 = 26)
- Subnet mask: 255.255.255.192

**Step 3:** Calculate subnets
```
Subnet 1: 192.168.10.0/26
  - Network: 192.168.10.0
  - First usable: 192.168.10.1
  - Last usable: 192.168.10.62
  - Broadcast: 192.168.10.63

Subnet 2: 192.168.10.64/26
  - Network: 192.168.10.64
  - First usable: 192.168.10.65
  - Last usable: 192.168.10.126
  - Broadcast: 192.168.10.127

Subnet 3: 192.168.10.128/26
  - Network: 192.168.10.128
  - First usable: 192.168.10.129
  - Last usable: 192.168.10.190
  - Broadcast: 192.168.10.191

Subnet 4: 192.168.10.192/26
  - Network: 192.168.10.192
  - First usable: 192.168.10.193
  - Last usable: 192.168.10.254
  - Broadcast: 192.168.10.255
```

**Step 4:** Verify
- Hosts per subnet: 2^6 - 2 = 64 - 2 = 62 ✓
- Total subnets: 4 ✓

### 3.3 Example 2: Variable Length Subnet Masking (VLSM)

**Problem:** Given the network 192.168.10.0/24, design a network with the following requirements:
- Subnet A: 100 hosts
- Subnet B: 50 hosts
- Subnet C: 25 hosts
- Subnet D: 10 hosts
- Subnet E: 2 hosts

**Solution using VLSM:**

**Step 1:** Sort requirements from largest to smallest
- Subnet A: 100 hosts → needs /25 (126 hosts)
- Subnet B: 50 hosts → needs /26 (62 hosts)
- Subnet C: 25 hosts → needs /27 (30 hosts)
- Subnet D: 10 hosts → needs /28 (14 hosts)
- Subnet E: 2 hosts → needs /30 (2 hosts)

**Step 2:** Allocate address space

```
Subnet A (100 hosts): 192.168.10.0/25
  - Network: 192.168.10.0
  - Range: 192.168.10.1 - 192.168.10.126
  - Broadcast: 192.168.10.127

Subnet B (50 hosts): 192.168.10.128/26
  - Network: 192.168.10.128
  - Range: 192.168.10.129 - 192.168.10.190
  - Broadcast: 192.168.10.191

Subnet C (25 hosts): 192.168.10.192/27
  - Network: 192.168.10.192
  - Range: 192.168.10.193 - 192.168.10.222
  - Broadcast: 192.168.10.223

Subnet D (10 hosts): 192.168.10.224/28
  - Network: 192.168.10.224
  - Range: 192.168.10.225 - 192.168.10.238
  - Broadcast: 192.168.10.239

Subnet E (2 hosts): 192.168.10.240/30
  - Network: 192.168.10.240
  - Range: 192.168.10.241 - 192.168.10.242
  - Broadcast: 192.168.10.243
```

### 3.4 Python Code for Subnet Calculation

Here's a practical Python program to perform subnet calculations:

```python
import ipaddress

def calculate_subnet(network_cidr, num_subnets=None, hosts_per_subnet=None):
    """
    Calculate subnet details based on network and requirements.
    
    Args:
        network_cidr: Network in CIDR notation (e.g., '192.168.1.0/24')
        num_subnets: Number of subnets required
        hosts_per_subnet: Number of hosts per subnet
    
    Returns:
        Dictionary with subnet details
    """
    network = ipaddress.ip_network(network_cidr, strict=False)
    
    if num_subnets:
        # Find minimum prefix length for required subnets
        current_prefix = network.prefixlen
        required_prefix = current_prefix
        
        while (2 ** (required_prefix - current_prefix)) < num_subnets:
            required_prefix += 1
            
        subnets = list(network.subnets(new_prefix=required_prefix))
        return {
            'original_network': str(network),
            'new_prefix_length': required_prefix,
            'subnet_mask': str(ipaddress.IPv4Network(f'0.0.0.0/{required_prefix}', strict=False).netmask),
            'number_of_subnets': len(subnets),
            'hosts_per_subnet': subnets[0].num_addresses - 2,
            'subnets': [(str(s), str(s[1]), str(s[-1])) for s in subnets]
        }
    
    if hosts_per_subnet:
        # Find minimum prefix length for required hosts
        required_bits = (hosts_per_subnet + 2).bit_length()
        required_prefix = 32 - required_bits
        
        if required_prefix < network.prefixlen:
            return {"error": "Cannot subnet to required host count"}
            
        subnets = list(network.subnets(new_prefix=required_prefix))
        return {
            'original_network': str(network),
            'new_prefix_length': required_prefix,
            'subnet_mask': str(ipaddress.IPv4Network(f'0.0.0.0/{required_prefix}', strict=False).netmask),
            'number_of_subnets': len(subnets),
            'hosts_per_subnet': subnets[0].num_addresses - 2,
            'subnets': [(str(s), str(s[1]), str(s[-2]), str(s[-1])) for s in subnets]
        }

# Example usage
print("=" * 60)
print("Example 1: Subnet 192.168.10.0/24 into 4 subnets")
print("=" * 60)
result = calculate_subnet('192.168.10.0/24', num_subnets=4)
print(f"New Prefix Length: /{result['new_prefix_length']}")
print(f"Subnet Mask: {result['subnet_mask']}")
print(f"Hosts per Subnet: {result['hosts_per_subnet']}")
print(f"Number of Subnets: {result['number_of_subnets']}")
print("\nSubnet Details:")
for subnet in result['subnets']:
    print(f"  Network: {subnet[0]}")

print("\n" + "=" * 60)
print("Example 2: Create subnet with 50 hosts")
print("=" * 60)
result = calculate_subnet('192.168.10.0/24', hosts_per_subnet=50)
print(f"New Prefix Length: /{result['new_prefix_length']}")
print(f"Subnet Mask: {result['subnet_mask']}")
print(f"Hosts per Subnet: {result['hosts_per_subnet']}")
```

---

## 4. Routing Algorithms

### 4.1 Introduction to Routing

Routing is the process of forwarding packets from source to destination across interconnected networks. Routing algorithms determine the optimal path for data transmission. These algorithms are fundamental to how the internet functions.

### 4.2 Types of Routing

#### 4.2.1 Static Routing

- Routes are manually configured by network administrators
- Suitable for small networks with consistent traffic patterns
- Advantages: Predictable, low overhead, secure
- Disadvantages: No adaptability, time-consuming for large networks

#### 4.2.2 Dynamic Routing

- Routes are automatically determined by routing protocols
- Adapts to network changes automatically
- Suitable for large, complex networks
- Advantages: Adaptive, scalable, self-healing
- Disadvantages: More complex, uses bandwidth, potential for suboptimal paths

### 4.3 Distance Vector Routing

**Distance Vector** routing protocols use the Bellman-Ford algorithm to determine the best path. Each router maintains a table (vector) of distances to all known destinations.

#### 4.3.1 Routing Information Protocol (RIP)

RIP is one of the oldest distance vector protocols.

**Characteristics:**
- Uses hop count as the metric (maximum hop count = 15)
- Updates routing tables every 30 seconds
- Maximum hop count of 16 (unreachable)
- Suitable for small networks (< 15 routers)

**RIP Versions:**
| Feature | RIP v1 | RIP v2 |
|---------|--------|--------|
| Classful | Yes | No |
| Subnet Mask | No | Yes |
| Authentication | No | Yes |
| Multicast | No | Yes (224.0.0.9) |

#### 4.3.2 How Distance Vector Works

```
Example: Network Topology
         
    [R1]----1----[R2]----1----[R3]
     |            |            |
     1            1            1
    [A]          [B]          [C]

Initial routing table at R1 for destination C:
- Via R2: Cost = 1 (to R2) + 1 (R2 to R3) = 2 hops
- Via direct: Not possible (not directly connected)

After R2 updates:
- R1 learns new route: R1 → R2 → R3 = 2 hops
```

### 4.4 Link State Routing

**Link State** protocols build a complete map of the network topology. Each router has a complete understanding of the network topology.

#### 4.4.1 Open Shortest Path First (OSPF)

OSPF is a widely used link state protocol.

**Characteristics:**
- Uses cost as metric (based on bandwidth)
- Supports VLSM and CIDR
- Uses Dijkstra's algorithm for path calculation
- Sends updates only when changes occur (not periodic)
- Forms adjacencies using Hello packets
- Supports area-based hierarchy

**OSPF Areas:**
- **Area 0 (Backbone Area)**: All other areas connect here
- **Stub Area**: Blocks external routes
- **NSSA (Not So Stubby Area)**: Allows limited external routes

**OSPF States:**
1. **Down**: No Hello received
2. **Init**: Hello received, not bidirectional
3. **Two-Way**: Bidirectional communication established
4. **ExStart**: Master/Slave relationship established
5. **Exchange**: DBD packets exchanged
6. **Loading**: LSAs requested and received
7. **Full**: Adjacency formed

### 4.5 Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path between nodes in a weighted graph. It's used by OSPF and other protocols to calculate optimal routes.

#### 4.5.1 Algorithm Steps

```
1. Set distance to source = 0, all other nodes = ∞
2. Add all nodes to unvisited set
3. While unvisited set is not empty:
   a. Select node with minimum distance value
   b. Mark it as visited
   c. For each unvisited neighbor:
      - Calculate new distance = current distance + edge weight
      - If new distance < existing distance, update it
```

#### 4.5.2 Example: Dijkstra's Algorithm

**Network Topology:**

```
        2
    A ------- B
    |        /|\
   1|       / | \4
    |      /  |  \
    |     /   |   \
    |    /    |    \
   4|   /     |     \3
    |  /      |      \
    | /       |       \
    C---------D-------E
        2        1
    
Goal: Find shortest path from A to E
```

**Step-by-Step Solution:**

**Initial State:**
```
Node | Distance from A | Previous Node | Visited
A    | 0               | None          | Yes
B    | ∞               | None          | No
C    | ∞               | None          | No
D    | ∞               | None          | No
E    | ∞               | None          | No
```

**Iteration 1:** Check neighbors of A
```
- A → B: Distance = 0 + 2 = 2 (update B)
- A → C: Distance = 0 + 1 = 1 (update C)
```
```
Node | Distance | Previous | Visited
A    | 0        | None     | Yes
B    | 2        | A        | No
C    | 1        | A        | No
D    | ∞        | None     | No
E    | ∞        | None     | No
```

**Iteration 2:** Select unvisited node with minimum distance (C = 1)
```
Neighbors of C:
- C → D: Distance = 1 + 2 = 3 (update D)
```
```
Node | Distance | Previous | Visited
A    | 0        | None     | Yes
B    | 2        | A        | No
C    | 1        | A        | Yes
D    | 3        | C        | No
E    | ∞        | None     | No
```

**Iteration 3:** Select unvisited node with minimum distance (B = 2)
```
Neighbors of B:
- B → D: Distance = 2 + 4 = 6 (keep existing 3)
- B → D: Distance = 2 + 4 = 6 (not better than 3)
```
```
Node | Distance | Previous | Visited
A    | 0        | None     | Yes
B    | 2        | A        | Yes
C    | 1        | A        | Yes
D    | 3        | C        | No
E    | ∞        | None     | No
```

**Iteration 4:** Select unvisited node with minimum distance (D = 3)
```
Neighbors of D:
- D → B: Distance = 3 + 4 = 7 (not better)
- D → E: Distance = 3 + 1 = 4 (update E)
```
```
Node | Distance | Previous | Visited
A    | 0        | None     | Yes
B    | 2        | A        | Yes
C    | 1        | A        | Yes
D    | 3        | C        | Yes
E    | 4        | D        | No
```

**Iteration 5:** Select unvisited node with minimum distance (E = 4)

**Result:**
- Shortest path from A to E: A → C → D → E
- Total cost: 1 + 2 + 1 = 4

#### 4.5.3 Python Implementation of Dijkstra's Algorithm

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start, end):
    """
    Implementation of Dijkstra's algorithm to find shortest path.
    
    Args:
        graph: Dictionary representing adjacency list
               {node: [(neighbor, weight), ...]}
        start: Starting node
        end: Destination node
    
    Returns:
        Tuple of (shortest_distance, path)
    """
    # Distance dictionary
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Track the path
    previous = {node: None for node in graph}
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    
    # Set of visited nodes
    visited = set()
    
    while pq:
        # Get node with minimum distance
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Check if we reached the destination
        if current_node == end:
            break
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
                
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distances[end], path

# Example graph from the topology above
graph = defaultdict(list)
graph['A'] = [('B', 2), ('C', 1)]
graph['B'] = [('A', 2), ('C', 2), ('D', 4)]
graph['C'] = [('A', 1), ('B', 2), ('D', 2)]
graph['D'] = [('B', 4), ('C', 2), ('E', 1)]
graph['E'] = [('D', 1), ('B', 3)]

# Find shortest path from A to E
distance, path = dijkstra(graph, 'A', 'E')
print(f"Shortest path from A to E: {' → '.join(path)}")
print(f"Total distance: {distance}")

# Output:
# Shortest path from A to E: A → C → D → E
# Total distance: 4
```

### 4.6 Comparison of Routing Protocols

| Feature | RIP (v2) | OSPF | EIGRP |
|---------|----------|------|-------|
| Type | Distance Vector | Link State | Advanced Distance Vector |
| Metric | Hop Count | Cost (Bandwidth) | Composite (Bandwidth, Delay, etc.) |
| Max Hops | 15 | Unlimited | 224 |
| Convergence | Slow | Fast | Very Fast |
| Scalability | Small | Large | Very Large |
| VLSM Support | No | Yes | Yes |
| Administrative Distance | 120 | 110 | 90 |
| Updates | Periodic (30s) | Triggered | Triggered |

### 4.7 Routing vs. Routed Protocols

- **Routed Protocols**: Protocols that carry user data (IP, IPX, AppleTalk)
- **Routing Protocols**: Protocols that determine paths and update routing tables (RIP, OSPF, EIGRP, BGP)

---

## 5. Key Takeaways

### 5.1 Subnetting

1. **Subnetting divides a larger network into smaller, manageable subnets**
   - Reduces broadcast domains
   - Improves security through network isolation
   - Optimizes IP address utilization

2. **Understanding binary and CIDR notation is essential**
   - Subnet mask determines network/host portion
   - Formula: 2^n subnets, 2^h - 2 hosts per subnet

3. **VLSM allows efficient IP address allocation**
   - Assign subnets based on actual host requirements
   - Minimizes wasted address space

4. **Key formulas to remember:**
   - Number of subnets = 2^borrowed_bits
   - Usable hosts = 2^remaining_host_bits - 2
   - New prefix length = original_prefix + borrowed_bits

### 5.2 Routing Algorithms

1. **Static vs. Dynamic Routing**
   - Static: Manual configuration, predictable, for simple networks
   - Dynamic: Automated, adaptive, for complex networks

2. **Distance Vector Protocols (RIP)**
   - Simple implementation
   - Uses hop count metric
   - Limited scalability (16 hops maximum)

3. **Link State Protocols (OSPF)**
   - Complete network topology knowledge
   - Uses Dijkstra's algorithm
   - Fast convergence, highly scalable

4. **Dijkstra's Algorithm**
   - Finds shortest path in weighted graphs
   - Used by OSPF for route calculation
   - Core concept for understanding modern routing

5. **Protocol Selection Criteria**
   - Network size and complexity
   - Convergence requirements
   - Vendor support and compatibility

---

## 6. Assessment Section

### 6.1 Comprehensive Multiple Choice Questions

**Question 1:** What is the default subnet mask for a Class B IP address?
- A) 255.0.0.0
- B) 255.255.0.0
- C) 255.255.255.0
- D) 255.255.255.255

**Question 2:** How many usable host addresses are there in a /26 subnet?
- A) 30
- B) 62
- C) 126
- D) 254

**Question 3:** Which routing protocol uses Dijkstra's algorithm?
- A) RIP
- B) EIGRP
- C) OSPF
- D) BGP

**Question 4:** What is the maximum hop count in RIP?
- A) 15
- B) 16
- C) 255
- D) Unlimited

**Question 5:** Which IP address class is used for multicast?
- A) Class A
- B) Class B
- C) Class C
- D) Class D

**Question 6:** In VLSM, what is the primary advantage?
- A) All subnets must be the same size
- B) Subnets can be different sizes based on needs
- C) Reduces number of routing entries
- D) Eliminates need for routing protocols

**Question 7:** What is the network address of 192.168.10.35/26?
- A) 192.168.10.0
- B) 192.168.10.32
- C) 192.168.10.64
- D) 192.168.10.128

**Question 8:** Which protocol supports VLSM and CIDR?
- A) RIP v1
- B) RIP v2
- C) Both A and B
- D) Neither

**Question 9:** What is the broadcast address for 10.0.15.0/23?
- A) 10.0.15.255
- B) 10.0.16.255
- C) 10.0.17.255
- D) 10.0.14.255

**Question 10:** In OSPF, what is the backbone area called?
- Area 0
- Area 1
- Area 10
- Area 255

**Question 11:** What type of routing protocol is EIGRP?
- A) Pure Distance Vector
- B) Pure Link State
- C) Advanced Distance Vector
- D) Path Vector

**Question 12:** How many bits are borrowed when creating 8 subnets from a Class C network?
- A) 2
- B) 3
- C) 4
- D) 5

**Question 13:** What is the primary metric used by OSPF?
- A) Hop count
- B) Bandwidth (Cost)
- C) Delay
- D) Load

**Question 14:** Which of the following is a private IP address range?
- A) 172.16.0.0/12
- B) 169.254.0.0/16
- C) 127.0.0.0/8
- D) 224.0.0.0/4

**Question 15:** What does the "/30" subnet mask provide?
- A) 2 usable hosts
- B) 6 usable hosts
- C) 14 usable hosts
- D) 30 usable hosts

### Answer Key

| Q | Answer | Q | Answer |
|---|--------|---|--------|
| 1 | B | 9 | A |
| 2 | B | 10 | Area 0 |
| 3 | C | 11 | C |
| 4 | A | 12 | B |
| 5 | D | 13 | B |
| 6 | B | 14 | A |
| 7 | B | 15 | A |
| 8 | B |   |   |

### 6.2 Flashcards for Quick Review

**Flashcard 1:**
- **Term:** Subnetting
- **Definition:** The process of dividing a larger IP network into smaller subnetworks

**Flashcard 2:**
- **Term:** CIDR Notation
- **Definition:** A method of representing IP addresses and network prefixes (e.g., 192.168.1.0/24)

**Flashcard 3:**
- **Term:** Default Gateway
- **Definition:** The router interface that connects a local network to other networks

**Flashcard 4:**
- **Term:** Broadcast Address
- **Definition:** The highest address in a network range, used to send to all hosts

**Flashcard 5:**
- **Term:** VLSM
- **Definition:** Variable Length Subnet Masking - allows subnets of different sizes

**Flashcard 6:**
- **Term:** Routing Protocol
- **Definition:** A protocol that determines optimal paths and updates routing tables

**Flashcard 7:**
- **Term:** Dijkstra's Algorithm
- **Definition:** A shortest path algorithm used in link-state routing protocols

**Flashcard 8:**
- **Term:** Administrative Distance
- **Definition:** A measure of trust for routing information; lower values are preferred

**Flashcard 9:**
- **Term:** OSPF
- **Definition:** Open Shortest Path First - a link-state interior gateway protocol

**Flashcard 10:**
- **Term:** RIP
- **Definition:** Routing Information Protocol - a distance-vector routing protocol

**Flashcard 11:**
- **Term:** Network Address
- **Definition:** The first address in an IP network range, identifies the network itself

**Flashcard 12:**
- **Term:** Subnet Mask
- **Definition:** A 32-bit number that divides an IP address into network and host portions

---

## 7. References and Further Reading

### Delhi University NEP 2024 UGCF Syllabus Alignment

This study material covers the following units as per the Delhi University BSc (Hons) Computer Science syllabus:

- Unit I: Introduction to Networking and IP Addressing
- Unit II: Subnetting and CIDR
- Unit III: Routing Concepts and Protocols
- Unit IV: Advanced Routing Algorithms

### Recommended Textbooks

1. **Computer Networking: A Top-Down Approach** - Kurose & Ross
2. **Data Communications and Networking** - Behrouz A. Forouzan
3. **CCNA Routing and Switching** - Cisco Press

### Online Resources

- Cisco Networking Academy
- RFC 2453 (RIP Version 2)
- RFC 2328 (OSPF Version 2)

---

*This comprehensive study material has been prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. For better retention, practice subnetting problems regularly and implement routing algorithms in a lab environment.*