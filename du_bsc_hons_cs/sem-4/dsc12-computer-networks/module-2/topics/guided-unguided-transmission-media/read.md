# Guided and Unguided Transmission Media

## Comprehensive Study Material for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Transmission media** refers to the physical pathways that connect devices in a computer network, enabling the transfer of data from one point to another. In the OSI model, transmission media falls under **Layer 1 (Physical Layer)**, making it the foundation upon which all network communication operates.

Understanding transmission media is crucial for network engineers and administrators because the choice of medium directly impacts:

- **Bandwidth capacity** – How much data can be transmitted per second
- **Transmission speed** – Latency and propagation delay
- **Distance limitations** – Maximum cable length or wireless range
- **Cost** – Installation and maintenance expenses
- **Susceptibility to interference** – Signal degradation and security concerns

In today's digitally connected world—from streaming 4K videos to conducting video conferences—transmission media powers everything. Whether it's the ethernet cable connecting your laptop to a router or the Wi-Fi signals enabling mobile internet, transmission media is the invisible backbone of modern communication.

---

## 2. Classification of Transmission Media

Transmission media are broadly classified into two categories:

```
Transmission Media
├── Guided Media (Wired)
│   ├── Twisted Pair Cable
│   ├── Coaxial Cable
│   └── Fiber Optic Cable
└── Unguided Media (Wireless)
    ├── Radio Waves
    ├── Microwaves
    ├── Satellites
    └── Infrared
```

---

## 3. Guided Transmission Media (Wired)

Guided media transmit signals through physical conductors. These media provide high speed, security, and reliability over limited distances.

### 3.1 Twisted Pair Cable

**Definition:** Twisted pair cable consists of pairs of copper wires twisted together. The twisting helps reduce **crosstalk** (interference between adjacent wire pairs) and electromagnetic interference (EMI).

#### Types of Twisted Pair Cable:

| Type | Description | Maximum Speed | Maximum Distance | Applications |
|------|-------------|---------------|------------------|--------------|
| **UTP (Unshielded Twisted Pair)** | No shielding, vulnerable to interference | 10 Gbps (Cat 6a) | 100 meters | Ethernet networks, telephone lines |
| **STP (Shielded Twisted Pair)** | Metallic shielding for better EMI protection | 10 Gbps (Cat 7) | 100 meters | Industrial environments, high-security networks |

#### Categories (ANSI/TIA-568 standards):

- **Cat 3** – 10 Mbps, legacy telephone systems
- **Cat 5** – 100 Mbps, older Ethernet networks
- **Cat 5e** – 1 Gbps, most common in home/office networks
- **Cat 6** – 10 Gbps (short distance), better crosstalk prevention
- **Cat 6a** – 10 Gbps, 100-meter distance
- **Cat 7** – 10 Gbps+, each pair individually shielded
- **Cat 8** – 25-40 Gbps, data centers

**Real-world Example:** When you connect your computer to a router using an Ethernet cable, you're most likely using **Cat 5e or Cat 6 UTP cable**. This enables fast, stable internet connections for gaming, streaming, and video conferencing.

### 3.2 Coaxial Cable

**Definition:** Coaxial cable (coax) consists of a central copper conductor surrounded by insulating material, a metallic shield, and an outer jacket. This design provides excellent shielding against EMI.

#### Types of Coaxial Cable:

| Type | Impedance | Applications |
|------|-----------|--------------|
| **RG-58** | 50 Ω | Thin Ethernet (10BASE2), radio frequency connections |
| **RG-59** | 75 Ω | Cable television, CCTV |
| **RG-6** | 75 Ω | Modern CATV, satellite TV, broadband internet |
| **RG-11** | 75 Ω | Long-distance cable runs, cable TV trunk lines |

#### Advantages:
- Better shielding than twisted pair → less signal loss
- Higher bandwidth capacity
- Longer transmission distances (up to 500 meters for 10BASE2)
- Excellent resistance to interference

#### Disadvantages:
- Bulkier and more expensive than twisted pair
- Difficult to install in tight spaces
- Heavier weight

**Real-world Example:** Coaxial cables are extensively used by cable television providers (Jio Fiber, Airtel Xstream) to deliver TV signals and broadband internet to homes. The **DOCSIS (Data Over Cable Service Interface Specification)** standard uses coax cables for high-speed internet access.

### 3.3 Fiber Optic Cable

**Definition:** Fiber optic cables transmit data as pulses of light through thin strands of glass or plastic (optical fibers). They offer the highest bandwidth and fastest transmission speeds among all guided media.

#### Key Components:
1. **Core** – Central light-carrying strand (8-10 μm for single-mode, 50-62.5 μm for multi-mode)
2. **Cladding** – Reflective coating that keeps light within the core
3. **Buffer** – Protective coating
4. **Jacket** – Outer protective layer

#### Types of Fiber Optic Cable:

| Feature | Single-Mode Fiber (SMF) | Multi-Mode Fiber (MMF) |
|---------|-------------------------|------------------------|
| **Core Diameter** | 8-10 μm | 50-62.5 μm |
| **Light Source** | Laser/Laser Diode | LED |
| **Bandwidth** | Very High (100 GHz·km) | High (500-5000 MHz·km) |
| **Distance** | Up to 100+ km | Up to 2 km |
| **Cost** | Expensive | Less expensive |
| **Color Code** | Yellow | Orange (OM1/OM2), Aqua (OM3/OM4) |
| **Applications** | Long-haul telecom, undersea cables | Data centers, LANs, short distances |

#### Advantages of Fiber Optic:
- **Extremely high bandwidth** – Up to 100 Tbps in laboratory conditions
- **Low attenuation** – Signals travel 100+ km without regeneration
- **Immune to EMI** – No electromagnetic interference
- **Security** – Difficult to tap without detection
- **Lightweight and thin** – Easier to install in crowded conduits

#### Disadvantages:
- High installation cost
- Requires specialized equipment and training
- Fragile compared to copper
- Bidirectional communication requires two fibers (or WDM)

**Real-world Example:** The **internet backbone** connecting continents is entirely fiber optic. Under-sea fiber cables (like the **SEA-ME-WE** consortium) connect India to Europe and Southeast Asia. When you access a website hosted on a server in the US, your data likely travels through dozens of fiber optic segments.

---

## 4. Unguided Transmission Media (Wireless)

Unguided media transmit signals without physical conductors, using the atmosphere or space as the transmission medium. This enables mobility and connects remote locations.

### 4.1 Radio Waves

**Definition:** Radio waves are electromagnetic waves with frequencies from 3 kHz to 300 GHz. They can penetrate walls and travel around obstacles.

#### Frequency Bands:
- **VLF (Very Low Frequency)** – 3-30 kHz, submarine communication
- **LF (Low Frequency)** – 30-300 kHz, navigation systems
- **MF (Medium Frequency)** – 300 kHz-3 MHz, AM radio
- **HF (High Frequency)** – 3-30 MHz, shortwave radio
- **VHF (Very High Frequency)** – 30-300 MHz, FM radio, TV
- **UHF (Ultra High Frequency)** – 300 MHz-3 GHz, Wi-Fi, cellular
- **SHF (Super High Frequency)** – 3-30 GHz, Wi-Fi (5 GHz), radar

**Applications:**
- Wi-Fi networks (802.11 standards)
- Bluetooth connectivity
- Cellular networks (4G LTE, 5G)
- Radio broadcasting

### 4.2 Microwaves

**Definition:** Microwaves are high-frequency radio waves (1-300 GHz) that travel in straight lines and require line-of-sight between transmitter and receiver.

#### Types:
1. **Terrestrial Microwaves** – Tower-to-tower communication
   - Frequency: 4-6 GHz, 21-23 GHz
   - Distance: 30-50 km between towers
   - Used for: Telephone backbone, CCTV connectivity

2. **Satellite Microwaves** – Communication via satellites
   - Frequency: 6-12 GHz (C-band), 12-18 GHz (Ku-band), 26-40 GHz (Ka-band)
   - Used for: TV broadcasting, weather forecasting, GPS, internet

**Advantages:**
- High bandwidth capacity
- Lower cost than fiber for long distances
- Supports voice, video, and data

**Disadvantages:**
- Requires line-of-sight
- Susceptible to weather interference (rain fade)
- Security concerns (signals can be intercepted)

### 4.3 Satellite Communication

**Definition:** Satellites act as relay stations in space, receiving signals from Earth, amplifying them, and transmitting them back to other locations.

#### Satellite Orbits:
| Orbit Type | Altitude | Latency | Examples |
|------------|----------|---------|----------|
| **GEO (Geostationary)** | 35,786 km | ~240 ms | Weather satellites, TV broadcasting |
| **MEO (Medium Earth Orbit)** | 5,000-20,000 km | ~20-50 ms | GPS, navigation |
| **LEO (Low Earth Orbit)** | 500-2,000 km | ~10-20 ms | Starlink, Iridium, remote sensing |

**Real-world Example:** India's **GSAT** series of communication satellites provide television, telephone, and internet services to remote areas. **Starlink** (SpaceX) uses LEO satellites to provide global broadband internet.

### 4.4 Infrared (IR)

**Definition:** Infrared waves have frequencies below visible light (300 GHz to 400 THz). They require line-of-sight and cannot penetrate solid objects.

#### Types:
1. **Near Infrared** – Used in TV remotes, remote controls
2. **Far Infrared** – Thermal imaging, heating

#### Advantages:
- Cheap and simple technology
- No interference from electromagnetic sources
- High security (cannot pass through walls)

#### Disadvantages:
- Short range (few meters)
- Line-of-sight required
- Slow data rates compared to other wireless media
- Cannot penetrate obstacles

**Real-world Example:** TV remote controls use infrared to send commands to the television. Some older smartphones used IR ports for file transfer (before Bluetooth became ubiquitous).

---

## 5. Comparison of Transmission Media

| Medium | Bandwidth | Speed | Distance | Cost | Interference Susceptibility |
|--------|-----------|-------|----------|------|----------------------------|
| Twisted Pair (Cat 5e) | Up to 1 Gbps | 100 m | Low | High |
| Coaxial Cable | Up to 10 Gbps | 500 m | Medium | Medium |
| Multi-mode Fiber | 10-100 Gbps | 2 km | High | Very Low |
| Single-mode Fiber | 100+ Gbps | 100+ km | Very High | Extremely Low |
| Wi-Fi (2.4 GHz) | 600 Mbps | 100 m (outdoor) | Low | High |
| Microwave | 100+ Mbps | 50 km | Medium | Medium |
| Satellite | 100+ Mbps | Global | Very High | Weather-dependent |

---

## 6. Practical Example: Python Script for Network Cable Selection

```python
def select_transmission_medium(distance, bandwidth_required, budget):
    """
    Simple decision support for selecting transmission media
    based on distance, bandwidth, and budget constraints.
    """
    
    recommendations = []
    
    # Twisted Pair Selection
    if distance <= 100:
        if bandwidth_required <= 1_000_000_000:  # 1 Gbps
            recommendations.append({
                'medium': 'Cat 5e UTP',
                'max_speed': '1 Gbps',
                'estimated_cost': 'Low',
                'notes': 'Suitable for most office/home networks'
            })
        elif bandwidth_required <= 10_000_000_000:  # 10 Gbps
            recommendations.append({
                'medium': 'Cat 6a/7 STP',
                'max_speed': '10 Gbps',
                'estimated_cost': 'Medium',
                'notes': 'Better for high-speed applications'
            })
    
    # Coaxial Cable Selection
    if 100 < distance <= 500 and bandwidth_required <= 10_000_000_000:
        recommendations.append({
            'medium': 'Coaxial (RG-6)',
            'max_speed': '10 Gbps',
            'estimated_cost': 'Medium',
            'notes': 'Good for longer runs with moderate speeds'
        })
    
    # Fiber Optic Selection
    if distance > 100:
        if budget == 'high':
            recommendations.append({
                'medium': 'Single-Mode Fiber',
                'max_speed': '100+ Gbps',
                'estimated_cost': 'Very High',
                'notes': 'Best for long-distance, high-bandwidth'
            })
        elif budget in ['medium', 'high']:
            recommendations.append({
                'medium': 'Multi-Mode Fiber (OM4)',
                'max_speed': '100 Gbps',
                'estimated_cost': 'High',
                'notes': 'Good for data centers, up to 2km'
            })
    
    return recommendations

# Example Usage
user_distance = 500  # meters
user_bandwidth = 10_000_000_000  # 10 Gbps
user_budget = 'high'

results = select_transmission_medium(user_distance, user_bandwidth, user_budget)

print("Recommended Transmission Media:")
print("=" * 50)
for i, result in enumerate(results, 1):
    print(f"\nOption {i}:")
    print(f"  Medium: {result['medium']}")
    print(f"  Max Speed: {result['max_speed']}")
    print(f"  Cost: {result['estimated_cost']}")
    print(f"  Notes: {result['notes']}")
```

---

## 7. Key Takeaways

1. **Transmission media** forms the physical foundation of all network communication, classified into guided (wired) and unguided (wireless) categories.

2. **Guided Media:**
   - **Twisted Pair** – Most common for LANs; affordable, easy to install, but limited distance (100m) and susceptible to interference
   - **Coaxial Cable** – Better shielding than twisted pair; used in cable TV and cable internet (DOCSIS)
   - **Fiber Optic** – Highest bandwidth, longest distances, immune to EMI; ideal for backbones and long-haul communication

3. **Unguided Media:**
   - **Radio Waves** – Used in Wi-Fi, Bluetooth, cellular networks; omnidirectional
   - **Microwaves** – Point-to-point communication requiring line-of-sight
   - **Satellites** – Global coverage; GEO for broadcasting, LEO for low-latency internet
   - **Infrared** – Short-range, line-of-sight; used in remote controls

4. **Selection Factors:** Consider distance, bandwidth requirements, budget, environment, and security when choosing transmission media.

5. **Delhi University Context:** This topic aligns with the NEP 2024 UGCF syllabus for Computer Networks (Paper: CN-101), covering fundamental physical layer concepts essential for understanding network design and troubleshooting.

---

## 8. Multiple Choice Questions (MCQs)

### Section A: Basic Concepts

1. **Which transmission media operates at the Physical Layer (Layer 1) of the OSI model?**
   - a) Twisted Pair Cable
   - b) HTTP
   - c) TCP
   - d) Switch
   
   **Answer: a) Twisted Pair Cable**

2. **The primary purpose of twisting wires in twisted pair cables is to:**
   - a) Increase tensile strength
   - b) Reduce crosstalk and electromagnetic interference
   - c) Make the cable flexible
   - d) Allow higher voltage transmission
   
   **Answer: b) Reduce crosstalk and electromagnetic interference**

3. **Which cable type uses a central copper conductor surrounded by insulating material and a metallic shield?**
   - a) Twisted Pair
   - b) Coaxial Cable
   - c) Fiber Optic
   - d) None of the above
   
   **Answer: b) Coaxial Cable**

### Section B: Fiber Optic

4. **In fiber optic cables, light signals are transmitted through which component?**
   - a) Copper core
   - b) Cladding
   - c) Core
   - d) Jacket
   
   **Answer: c) Core**

5. **Single-mode fiber typically uses which light source?**
   - a) LED
   - b) Laser Diode
   - c) Incandescent bulb
   - d) Fluorescent light
   
   **Answer: b) Laser Diode**

6. **Maximum transmission distance of multi-mode fiber at 10 Gbps is approximately:**
   - a) 100 meters
   - b) 500 meters
   - c) 2 km
   - d) 100 km
   
   **Answer: c) 2 km**

7. **Which fiber optic type is commonly used for long-distance telecommunication?**
   - a) Multi-mode
   - b) Single-mode
   - c) Plastic fiber
   - d) Step-index
   
   **Answer: b) Single-mode**

### Section C: Wireless Media

8. **Which wireless medium requires line-of-sight between transmitter and receiver?**
   - a) Radio Waves
   - b) Microwaves
   - c) Infrared
   - d) Both b) and c)
   
   **Answer: d) Both b) and c)**

9. **The frequency range of microwaves is:**
   - a) 3 kHz to 3 GHz
   - b) 1 GHz to 300 GHz
   - c) 300 GHz to 400 THz
   - d) 30 Hz to 300 Hz
   
   **Answer: b) 1 GHz to 300 GHz**

10. **Which satellite orbit has the lowest latency for communication?**
    - a) GEO
    - b) MEO
    - c) LEO
    - d) All have similar latency
    
    **Answer: c) LEO**

11. **Infrared waves cannot penetrate:**
    - a) Water
    - b) Glass
    - c) Solid objects
    - d) Radio signals
    
    **Answer: c) Solid objects**

### Section D: Applications and Standards

12. **Which category of twisted pair cable supports speeds up to 10 Gbps over 100 meters?**
    - a) Cat 5
    - b) Cat 5e
    - c) Cat 6a
    - d) Cat 3
    
    **Answer: c) Cat 6a**

13. **DOCSIS standard is associated with which transmission medium?**
    - a) Twisted Pair
    - b) Coaxial Cable
    - c) Fiber Optic
    - d) Satellite
    
    **Answer: b) Coaxial Cable**

14. **Which technology uses the 2.4 GHz and 5 GHz frequency bands?**
    - a) Bluetooth
    - b) Wi-Fi
    - c) FM Radio
    - d) GPS
    
    **Answer: b) Wi-Fi**

15. **The GSAT series of satellites are operated by:**
    - a) NASA
    - b) ISRO
    - c) ESA
    - d) SpaceX
    
    **Answer: b) ISRO**

### Section E: Advanced Questions

16. **What is the approximate latency for signals to travel to a GEO satellite and back?**
    - a) 120 ms
    - b) 240 ms
    - c) 500 ms
    - d) 1 second
    
    **Answer: b) 240 ms**

17. **Which type of cable provides the best protection against electromagnetic interference?**
    - a) UTP
    - b) STP
    - c) Coaxial
    - d) Fiber Optic
    
    **Answer: d) Fiber Optic**

18. **In a 1000BASE-T Ethernet network, what is the maximum cable length?**
    - a) 10 meters
    - b) 100 meters
    - c) 500 meters
    - d) 1 kilometer
    
    **Answer: b) 100 meters**

19. **WDM (Wavelength Division Multiplexing) is primarily used with which transmission medium?**
    - a) Twisted Pair
    - b) Coaxial Cable
    - c) Fiber Optic
    - d) Wireless
    
    **Answer: c) Fiber Optic**

20. **Which frequency band is used by GPS satellites?**
    - a) 2.4 GHz
    - b) 1.2-1.5 GHz (L-band)
    - c) 5 GHz
    - d) 10 GHz
    
    **Answer: b) 1.2-1.5 GHz (L-band)**

---

## 9. Flashcards for Quick Revision

| # | Term | Definition/Key Point |
|---|------|----------------------|
| 1 | **Transmission Media** | Physical pathways for data transfer in networks; operates at OSI Layer 1 |
| 2 | **Crosstalk** | Interference between adjacent wire pairs in twisted cables |
| 3 | **UTP (Unshielded Twisted Pair)** | Twisted pair without metallic shielding; most common Ethernet cable |
| 4 | **STP (Shielded Twisted Pair)** | Twisted pair with metallic shielding; better EMI protection |
| 5 | **Coaxial Cable** | Central copper conductor with shielding; used in cable TV |
| 6 | **Fiber Optic Cable** | Transmits data as light pulses through glass/plastic fibers |
| 7 | **Single-Mode Fiber** | Small core (8-10 μm); laser light; long distances (100+ km) |
| 8 | **Multi-Mode Fiber** | Larger core (50-62.5 μm); LED light; shorter distances (2 km) |
| 9 | **Attenuation** | Signal strength loss during transmission over distance |
| 10 | **EMI (Electromagnetic Interference)** | External interference affecting signal quality |
| 11 | **Radio Waves** | Electromagnetic waves used in Wi-Fi, Bluetooth, cellular communication |
| 12 | **Microwaves** | High-frequency waves requiring line-of-sight; used in point-to-point links |
| 13 | **Line-of-Sight (LOS)** | Direct path between transmitter and receiver; required for microwaves/IR |
| 14 | **GEO Satellite** | Geostationary orbit (35,786 km); used for TV broadcasting |
| 15 | **LEO Satellite** | Low Earth Orbit (500-2,000 km); low latency; used by Starlink |
| 16 | **Infrared** | High-frequency waves used in TV remotes; cannot penetrate solids |
| 17 | **Bandwidth** | Maximum data transfer rate of a medium (bits per second) |
| 18 | **Cat 6 Cable** | Twisted pair supporting 10 Gbps up to 55 meters |
| 19 | **DOCSIS** | Standard for cable internet over coaxial infrastructure |
| 20 | **OSI Model** | 7-layer networking model; Physical Layer is Layer 1 |

---

*Prepared for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)*