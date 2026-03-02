# Network Types: An Introduction

**Subject:** COMPUTER NETWORKS
**Semester:** V
**Module:** Module 1

## Introduction

A computer network is a fundamental system that connects computing devices to share resources and exchange data. However, not all networks are created equal. They are built to serve different purposes, cover varying geographical areas, and use distinct technologies. Classifying networks into types helps us understand their design principles, capabilities, and limitations. For  engineering students, grasping these types is the first step toward designing and implementing efficient network solutions.

## Core Concepts of Network Types

Networks are primarily categorized based on their geographical span and the design philosophy used to construct them.

### 1. Based on Geographical Area

This is the most common classification, ranging from a network in a single room to one that spans the globe.

#### a) Personal Area Network (PAN)
A PAN is the most basic and smallest type of network, designed for personal use, typically within a range of 10 meters.
*   **Purpose:** To connect devices owned by a single person.
*   **Technology:** Uses wireless technologies like **Bluetooth** (e.g., connecting a wireless mouse to a laptop) or Infrared (IR). Wired PANs can be created using USB cables.
*   **Example:** Syncing your smartphone with your laptop via Bluetooth, or connecting a wireless headset to your PC.

#### b) Local Area Network (LAN)
A LAN connects devices within a limited geographical area such as a home, school, office building, or a cluster of buildings.
*   **Purpose:** To share resources like printers, files, and internet access efficiently.
*   **Technology:** Traditionally uses wired technologies like **Ethernet** (with twisted-pair cables) or wireless technologies like **Wi-Fi (IEEE 802.11)**. LANs are characterized by high data transfer rates (high bandwidth) and low latency.
*   **Example:** The Wi-Fi network in your college campus or the wired network connecting all computers in a  lab.

#### c) Metropolitan Area Network (MAN)
A MAN spans a city or a large campus. It is essentially a larger version of a LAN.
*   **Purpose:** To provide network connectivity to a larger geographical area, often connecting multiple LANs.
*   **Technology:** Uses technologies like **Microwave transmission**, **radio waves**, or **fiber-optic cables**. A common example of MAN technology is the **IEEE 802.16 standard (WiMAX)**.
*   **Example:** The network connecting all the branches of a bank within a city, or a cable TV network serving an entire metropolitan area.

#### d) Wide Area Network (WAN)
A WAN covers a very large geographical area, such as a country, a continent, or even the entire world.
*   **Purpose:** To connect smaller networks (like LANs and MANs) across long distances.
*   **Technology:** Utilizes leased **telecommunication lines**, satellite links, and undersea cables. The most prominent example of a WAN is the **Internet**. Routers are the key devices used to connect these vast networks.
*   **Example:** A multinational corporation connecting its office networks in Bangalore, London, and New York over the internet using secure VPN tunnels.

### 2. Based on Design Architecture

This classification defines how the network is structured and managed.

#### a) Client-Server Network
In this centralized architecture, powerful computers called **servers** provide services and resources (like files, databases, web pages) to less powerful computers called **clients**, which request these services.
*   **Characteristics:** Centralized management, more secure, easier to back up, but the server is a single point of failure.
*   **Example:** Accessing a website (e.g., .ac.in). Your browser (the client) requests the webpage from 's web server.

#### b) Peer-to-Peer (P2P) Network
In a decentralized P2P architecture, all devices (peers) have equal capabilities and can act as both clients and servers. There is no central authority.
*   **Characteristics:** Easy to set up, less expensive, but lacks centralized security and is harder to manage as it scales.
*   **Example:** File-sharing networks like BitTorrent, where each peer shares and downloads files directly from other peers.

## Key Points / Summary

| Network Type | Acronym | Span | Key Technology | Example |
| :--- | :--- | :--- | :--- | :--- |
| Personal Area Network | PAN | ~10 meters | Bluetooth, USB | Wireless mouse |
| Local Area Network | LAN | Building/Campus | Ethernet, Wi-Fi | College Lab Network |
| Metropolitan Area Network | MAN | City | WiMAX, Fiber optics | City-wide Cable TV |
| Wide Area Network | WAN | Country/Globe | Leased Lines, Internet | The Internet |
| **Architecture** | | | | |
| Client-Server | | Centralized | Dedicated Servers | Web Browsing |
| Peer-to-Peer | P2P | Decentralized | Equal Peers | BitTorrent |

Understanding these network types provides the foundational context for delving deeper into the protocols, topologies, and technologies that make modern communication possible.