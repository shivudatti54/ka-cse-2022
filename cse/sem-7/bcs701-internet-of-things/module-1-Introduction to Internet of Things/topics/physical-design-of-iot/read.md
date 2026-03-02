# Physical Design of IoT

## 1. Introduction to IoT Physical Design

The physical design of Internet of Things (IoT) systems encompasses the tangible hardware components, their interconnections, and the architectural patterns that enable the bridge between physical phenomena and digital processing. Unlike conventional computing systems that operate exclusively in the digital domain, IoT physical design must address the fundamental challenge of interfacing with heterogeneous physical environments while maintaining constraints on power, form factor, and computational capacity.

The physical layer establishes the definitive boundaries of what an IoT system can perceive and control. The selection of sensors determines the measurable phenomena; the processing architecture defines computational latency; communication protocols dictate bandwidth and reliability; and power infrastructure imposes operational lifespans. Consequently, physical design decisions propagate through all subsequent logical and application layers, making rigorous hardware selection a critical systems engineering task.

## 2. Fundamental Hardware Components

### 2.1 IoT Devices and Edge Nodes

IoT devices constitute the terminal nodes in an IoT architecture, defined as physical artifacts embedded with sensors, actuators, processors, and communication interfaces that enable data acquisition and controlled intervention in physical processes. These devices are classified along a spectrum from highly constrained nodes to compute-capable edge gateways.

**Constrained devices** (Class 1-2 per RFC 7228) operate with limited SRAM (< 64 KB), minimal flash memory, and severe power budgets, often precluding full TCP/IP stack implementation. These typically employ microcontroller-based architectures with duty-cycled operation.

**Edge devices** possess greater computational capacity, capable of executing embedded Linux or similar operating systems, enabling local analytics, data aggregation, and protocol translation between legacy industrial systems and IP-based networks.

### 2.2 Sensors: Transduction Principles

Sensors function as transducers that convert physical quantities into electrical signals. The fundamental transduction mechanisms include:

** resistive sensing**: Thermistors exhibit temperature-dependent resistance (R_T = R_0 exp[B(1/T - 1/T_0)], where B is the beta coefficient), enabling temperature measurement through voltage division.

** capacitive sensing**: Humidity sensors utilize hygroscopic polymer dielectrics whose permittivity varies with moisture content, altering capacitance according to C = ε_r ε_0 A/d.

** inductive sensing**: Proximity sensors employing coil inductance changes induced by eddy currents in conductive targets.

** piezoelectric sensing**: Accelerometers and pressure sensors generate charge proportional to mechanical strain, requiring charge amplification and filtering.

** optical sensing**: LDRs and photodiodes convert incident irradiance to current or resistance changes via semiconductor photoelectric effects.

**Sensor Calibration**: The general linear calibration model follows V_out = V_offset + S × P, where S represents sensitivity and P represents the measured physical quantity. Non-linear sensors require polynomial or lookup-table corrections.

### 2.3 Actuators: Control Output Devices

Actuators perform the inverse transduction, converting electrical signals to physical action:

| Actuator Type       | Driving Method         | Typical Application     | Response Time |
| ------------------- | ---------------------- | ----------------------- | ------------- |
| DC Motors           | PWM voltage            | Propulsion, positioning | < 10 ms       |
| Servo Motors        | PWM position signals   | Angular control         | 50-150 ms     |
| Stepper Motors      | Step/direction signals | Precision positioning   | 1-10 ms       |
| Solenoids           | On/off current         | Valves, locking         | 10-50 ms      |
| Solid-State Relays  | Opto-isolation + TRIAC | Switching AC loads      | < 10 ms       |
| Piezoelectric Stack | High-voltage drive     | Precision positioning   | < 1 ms        |

### 2.4 Processing Units: MCUs and MPUs

**Microcontrollers (MCUs)** integrate processor core, memory, and peripherals on a single chip, optimized for deterministic real-time control:

- **8-bit MCUs**: Atmel ATmega, PIC18F – suitable for simplest sensor nodes
- **32-bit MCUs**: STM32, ESP32, NXP LPC – dominant in commercial IoT
- **MCUs with Wireless**: ESP32, STM32WB, Texas Instruments CC26xx – integrated RF

**Selection Criteria**:

- **Instruction cycle time**: Determines minimum response latency
- **ADC resolution**: 10-bit (Atmega) to 16-bit (STM32) affects measurement precision
- **Peripheral set**: UART, SPI, I2C, PWM, DMA availability
- **Power modes**: Active, Sleep, Deep-Sleep, Stop, Standby

**Microprocessors (MPUs)** provide greater compute capability at higher power consumption:

- **Raspberry Pi Compute Module**: Quad-core ARM Cortex-A72, suitable for gateway applications
- **NVIDIA Jetson Nano**: GPU-accelerated for edge AI inference
- ** BeagleBone AI**: Real-time PRU cores alongside ARM Cortex-A15

## 3. Communication Technologies and Protocols

### 3.1 Physical Layer Comparison

The selection of communication technology involves trade-offs across range, data rate, power consumption, and spectral efficiency:

**Short-Range Technologies (< 100 m)**:

- **Bluetooth Low Energy (BLE)**: 2.4 GHz ISM band, 1 Mbps nominal, adaptive power control (-20 dBm to +10 dBm), suitable for personal area networks. Connectionless advertising and connected modes support diverse topologies.

- **Wi-Fi (IEEE 802.11)**: 2.4/5 GHz bands, 100+ Mbps practical throughput, higher power (100-500 mA TX), appropriate for video streaming and high-bandwidth sensors.

- **Zigbee (IEEE 802.15.4)**: 2.4 GHz, 250 Kbps, mesh networking capability, 10-100 m range, extensively used in home automation and industrial monitoring.

**Long-Range Technologies (> 1 km)**:

- **LoRaWAN**: Chirp spread spectrum modulation, 0.3-50 Kbps, 2-15 km urban range, extremely low power (20-100 mA TX), ideal for battery-operated remote monitoring.

- **NB-IoT**: Cellular LPWAN variant, 200 Kbps, nationwide coverage via existing cellular infrastructure, suitable for utility metering.

- **5G mMTC**: Massive machine-type communications, designed for 10^6 devices/km² density.

### 3.2 Application Layer Protocols

**MQTT (Message Queuing Telemetry Transport)**:

- Publish/subscribe broker pattern
- Three QoS levels: 0 (at most once), 1 (at least once), 2 (exactly once)
- Small packet overhead (2-byte header minimum)
- Retained messages and last-will/testament for state management

**CoAP (Constrained Application Protocol)**:

- RESTful resource model over UDP
- Observe option for subscriptions
- Block-wise transfer for large payloads
- Suitable for resource-constrained devices

**AMQP (Advanced Message Queuing Protocol)**:

- Enterprise messaging with delivery guarantees
- Complex routing (topic exchanges, direct queues)
- Higher overhead, appropriate for cloud integration

## 4. Power Management and Energy Budgeting

Power consumption constitutes the primary design constraint for battery-operated IoT deployments. The total energy budget E_total per operation cycle follows:

**E_total = E_sense + E_process + E_transmit + E_sleep**

Where:

- E_sense = V_supply × I_sense × t_sense
- E_process = V_supply × I_active × t_active
- E_transmit = V_supply × I_tx × t_tx
- E_sleep = V_supply × I_sleep × t_sleep

**Power Reduction Strategies**:

1. **Duty Cycling**: Operating at 1% duty cycle reduces average power by 40-60 dB

- t_active = D × T_cycle, where D is duty cycle ratio
- Average current: I_avg = I_active × D + I_sleep × (1-D)

2. **Dynamic Voltage Scaling (DVS)**: Power scales with V² and f

- P ∝ V² × f (dominant dynamic power component)

3. **Energy Harvesting**: Solar (10-100 μW/cm² indoor), vibrational (100 μW/cm³), thermal gradients (10-100 μW/cm²)

4. **Battery Selection**:

- Li-SOCl2: 3.6 V, 19 Ah, 10-year shelf life, low self-discharge
- LiMnO2: 3.0 V, 500 mAh, wide temperature range
- Supercapacitors: 10^5 cycle life, but lower energy density

## 5. Signal Conditioning and Interface Circuits

Sensors rarely produce signals directly compatible with ADC inputs. Signal conditioning encompasses:

**Amplification**: Instrumentation amplifiers (INA26x) provide high common-mode rejection (CMRR > 100 dB) for differential sensor signals. Gain selection: V_out = G × V_in

**Filtering**: Anti-aliasing filters must satisfy Nyquist criterion. First-order RC filters: f_c = 1/(2πRC)

**Impedance Matching**: High-impedance sensors (> 10 kΩ) require buffer amplifiers to prevent loading errors: V_error = V_source × (R_load / (R_source + R_load))

**ADC Considerations**:

- Resolution: n bits provides 2^n quantization levels
- ENOB (Effective Number of Bits) accounts for noise and linearity
- Sampling rate: f_s ≥ 2 × f_max (Nyquist theorem)

## 6. IoT Device Architecture Patterns

```
┌─────────────────────────────────────────────────────────────────────┐
│ IoT Device Architecture │
├─────────────────────────────────────────────────────────────────────┤
│ Physical │ Sensor │ Signal │ Micro- │ Comms │
│ Phenomena │ Array │ Conditioning │ controller│ Module │
│ │ │ (AMP, Filt) │ (ADC, DMA)│ (RF) │
└──────────────┴─────────────┴───────────────┴────────────┴──────────┘
 │ │
 ▼ ▼
 Data Acquisition Network/Cloud
 (Time-stamped (Protocol
 Samples) Translation)
```

**Device-to-Cloud Direct Architecture**: End devices communicate directly with cloud services via IP-based protocols. Suitable for Wi-Fi/cellular connected devices with reliable power.

**Gateway-Mediated Architecture**: Constrained devices communicate via low-power mesh (Zigbee, Thread) to a gateway that performs protocol translation, local aggregation, and edge analytics.

## 7. Hardware Security Considerations

Physical design must incorporate security from inception:

- **Secure Boot**: Cryptographic verification of firmware integrity at boot
- **Secure Element**: Hardware trust anchor (TPM, ATECC608A) for key storage
- **Tamper Detection**: Hardware interlocks triggering data wipe on physical breach
- **Side-Channel Resistance**: Constant-time cryptographic implementations
