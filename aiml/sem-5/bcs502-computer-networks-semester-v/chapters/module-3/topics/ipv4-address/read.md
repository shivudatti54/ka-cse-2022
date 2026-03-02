Of course. Here is a comprehensive educational module on IPv4 addressing, tailored for  engineering students.

***

### **Module 3: Network Layer - IPv4 Addressing**

**Subject:** Computer Networks (Semester V)

---

#### **1. Introduction**

The Internet Protocol version 4 (IPv4) is the fundamental communication protocol that enables devices to connect and exchange data across networks and the global internet. At the heart of this protocol is the **IPv4 address**—a unique logical identifier assigned to every device on a network. Think of it as a postal address for your computer; without it, data packets wouldn't know where to go or where they came from. Understanding IPv4 addressing is crucial for network design, troubleshooting, and administration.

---

#### **2. Core Concepts of IPv4 Addressing**

An IPv4 address is a 32-bit numeric address, written in a human-readable notation called **dotted-decimal**. This 32-bit binary number is divided into four 8-bit segments called **octets**.

*   **Structure:** `XXXXXXXX.XXXXXXXX.XXXXXXXX.XXXXXXXX` (in binary) becomes `192.168.1.1` (in dotted-decimal).
*   **Total Address Space:** 2³² = **4,294,967,296 possible addresses**.

##### **2.1. The Network-Host Dichotomy**

An IPv4 address is not just a random string of numbers; it contains two pieces of information:
1.  **Network Portion (Prefix):** Identifies the specific network a device belongs to. All devices on the same local network share the same network portion.
2.  **Host Portion (Suffix):** Identifies the specific device (host) within that network. This part must be unique for every device on the same network.

The boundary between these two portions is defined by the **subnet mask**.

##### **2.2. Subnet Mask**

A subnet mask is another 32-bit number that "masks" the network portion of the IP address. It uses consecutive `1`s for the network bits and `0`s for the host bits.

*   **Example:** The common subnet mask `255.255.255.0` (or `/24` in CIDR notation) in binary is:
    `11111111.11111111.11111111.00000000`
    This indicates that the first 24 bits are the network address, and the last 8 bits are for hosts.

##### **2.3. Address Classes (Classful Addressing)**

Historically, IPv4 addresses were divided into five classes to simplify assignment. While largely replaced by CIDR (Classless Inter-Domain Routing), understanding classes is foundational.

| Class | Leading Bits | Address Range | Default Subnet Mask | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **A** | `0` | 1.0.0.0 to 126.255.255.255 | 255.0.0.0 (/8) | Few large networks |
| **B** | `10` | 128.0.0.0 to 191.255.255.255 | 255.255.0.0 (/16) | Medium-sized networks |
| **C** | `110` | 192.0.0.0 to 223.255.255.255 | 255.255.255.0 (/24) | Small networks (LANs) |
| **D** | `1110` | 224.0.0.0 to 239.255.255.255 | N/A | Multicasting |
| **E** | `1111` | 240.0.0.0 to 255.255.255.255 | N/A | Experimental |

##### **2.4. Private vs. Public Addresses**

*   **Public IP Addresses:** Globally routable addresses assigned by ISPs, unique across the entire internet. Used for communication between different networks.
*   **Private IP Addresses:** Reserved for use within private networks (e.g., your home Wi-Fi, college lab). They are not routable on the public internet. Network Address Translation (NAT) is used to allow these devices to access the internet.
    *   Class A: `10.0.0.0/8`
    *   Class B: `172.16.0.0/12`
    *   Class C: `192.168.0.0/16`

**Example:** Your personal laptop likely has a private address like `192.168.29.75`, while your home router has a public IP assigned by your ISP.

##### **2.5. Special Addresses**

*   **Loopback Address:** `127.0.0.1` (or the entire `127.0.0.0/8` block). Used by a host to test its own TCP/IP stack (e.g., pinging `127.0.0.1`).
*   **Network Address:** The address where the host bits are all `0` (e.g., `192.168.1.0`). It represents the network itself and cannot be assigned to a host.
*   **Broadcast Address:** The address where the host bits are all `1` (e.g., `192.168.1.255`). Packets sent to this address are delivered to all hosts on that local network.

---

#### **3. Key Points & Summary**

*   An **IPv4 address** is a 32-bit logical identifier for a device on a network.
*   It is represented in **dotted-decimal notation** (e.g., `192.168.1.10`).
*   The address is split into a **Network portion** and a **Host portion**.
*   The **Subnet Mask** defines the split between the network and host bits.
*   **Classful addressing** (A, B, C, D, E) is a historical method for allocating address space.
*   **Private Addresses** (like `192.168.x.x`) are used within local networks, while **Public Addresses** are used on the internet.
*   Special addresses like **Network** (host bits all 0), **Broadcast** (host bits all 1), and **Loopback** (`127.0.0.1`) serve specific operational functions.

***Understanding IPv4 addressing is the first step towards grasping more advanced topics like subnetting, supernetting (CIDR), and the transition to IPv6.***

***