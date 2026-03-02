Of course. Here is a comprehensive educational module on IPv4 Addresses, tailored for  Engineering students.

### Module 3: IPv4 Address

#### **Introduction to IPv4 Address**

An IPv4 (Internet Protocol version 4) address is a unique logical identifier assigned to each device connected to a network that uses the Internet Protocol for communication. It functions much like a postal address, ensuring that data sent from a source device reaches the correct destination device. As the foundational addressing system of the modern internet, understanding its structure and classes is crucial for any network engineer.

---

#### **Core Concepts**

**1. Structure and Notation**
An IPv4 address is a 32-bit binary number, meaning it consists of 32 ones and zeros. To make it human-readable, it is converted into a dotted-decimal notation.

- **Binary Format:** `11000000.10101000.00000001.00000001`
- **Dotted-Decimal Notation:** `192.168.1.1`

The 32 bits are divided into four 8-bit segments called **octets**. Each octet is converted to its decimal equivalent, resulting in four decimal numbers separated by dots. Each octet can range from 0 to 255.

**2. Components: Network ID and Host ID**
An IP address is not just a random string of numbers; it contains two parts:

- **Network ID (Prefix):** The leftmost part of the address that identifies the specific network a device belongs to. All devices on the same physical network share the same network ID.
- **Host ID (Suffix):** The rightmost part that identifies the specific device (host) within that network. This must be unique for each device on the network.

The division between the Network ID and Host ID is not fixed and is defined by the address class or, more commonly today, by a **subnet mask**.

**3. Address Classes**
To accommodate networks of different sizes, IPv4 addresses are categorized into five primary classes: A, B, C, D, and E.

| Class | Leading Bits | Start Range | End Range       | Network/Host ID Split                           | Purpose                                                |
| :---- | :----------- | :---------- | :-------------- | :---------------------------------------------- | :----------------------------------------------------- |
| **A** | `0`          | 1.0.0.0     | 126.255.255.255 | **N.H.H.H** (First octet is Network ID)         | Few large networks (e.g., multinational companies)     |
| **B** | `10`         | 128.0.0.0   | 191.255.255.255 | **N.N.H.H** (First two octets are Network ID)   | Medium-sized networks (e.g., large universities)       |
| **C** | `110`        | 192.0.0.0   | 223.255.255.255 | **N.N.N.H** (First three octets are Network ID) | Small networks (e.g., small offices, departments)      |
| **D** | `1110`       | 224.0.0.0   | 239.255.255.255 | Not applicable                                  | **Multicasting** (Sending data to a group of devices)  |
| **E** | `1111`       | 240.0.0.0   | 255.255.255.255 | Not applicable                                  | **Experimental** (Reserved for future or research use) |

**Example:**

- Address: `150.10.15.20`
  - The first octet is `150`, which falls in the range 128-191. This is a **Class B** address.
  - Therefore, the Network ID is `150.10` and the Host ID is `15.20`.

**4. Subnet Mask**
A subnet mask is a 32-bit number that distinguishes the Network ID from the Host ID in an IP address. It uses the same dotted-decimal notation.

- A `1` bit in the mask corresponds to a network bit in the IP address.
- A `0` bit corresponds to a host bit.

**Default Subnet Masks:**

- **Class A:** `255.0.0.0`
- **Class B:** `255.255.0.0`
- **Class C:** `255.255.255.0`

**5. Special Addresses**

- **Loopback Address (`127.0.0.1`):** Used by a host to test its own network interface (TCP/IP stack) without sending packets onto the network.
- **Private Addresses:** Not routable on the public internet, used inside private networks. Defined in RFC 1918.
  - Class A: `10.0.0.0` to `10.255.255.255`
  - Class B: `172.16.0.0` to `172.31.255.255`
  - Class C: `192.168.0.0` to `192.168.255.255`
- **APIPA (Automatic Private IP Addressing) (`169.254.0.0/16`):** Self-assigned address when a device cannot obtain an IP from a DHCP server.

---

#### **Key Points & Summary**

- **Purpose:** An IPv4 address is a **32-bit logical address** that uniquely identifies a device on a network.
- **Notation:** Represented in **dotted-decimal** form (e.g., `192.168.1.10`), which is a human-friendly version of its 32-bit binary equivalent.
- **Components:** Divided into two parts—**Network ID** (identifies the network) and **Host ID** (identifies the device on that network).
- **Classes:** Divided into classes (A, B, C, D, E) based on the value of the first octet, which determines the default split between network and host bits.
- **Subnet Mask:** A crucial number (e.g., `255.255.255.0`) used to explicitly define which part of the IP address is the Network ID and which is the Host ID.
- **Special Addresses:** Include loopback (`127.0.0.1`), private IP ranges (e.g., `192.168.x.x`), and APIPA for failover addressing.
- **Limitation:** The 32-bit address space allows for only ~4.3 billion unique addresses, which led to its depletion and the development of **IPv6**.

Understanding IPv4 addressing is the first step towards mastering more advanced concepts like subnetting, VLSM, and network design.
