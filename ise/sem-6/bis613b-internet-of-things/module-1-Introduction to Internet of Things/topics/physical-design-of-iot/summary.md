# Physical Design of IoT

=====================================

### Overview

The physical design of IoT encompasses the tangible hardware components -- sensors, actuators, microcontrollers, communication modules, and power systems -- that interact with the physical world to collect data and perform actions. It forms the foundation upon which all IoT applications are built.

### Key Points

- **Sensors:** Input devices detecting physical properties (temperature, humidity, motion, light, pressure, gas) and converting them to electrical signals.
- **Actuators:** Output devices converting electrical signals into physical actions (motors, relays, solenoids, LEDs, buzzers).
- **Microcontrollers (MCUs):** Compact ICs for specific tasks -- Arduino, ESP32, STM32, Raspberry Pi Pico.
- **Microprocessors (MPUs):** More powerful, run full OS for gateways/edge devices -- Raspberry Pi, BeagleBone, NVIDIA Jetson.
- **Communication Modules:** Wireless (BLE, Wi-Fi, Zigbee, LoRaWAN, Cellular, NFC) and wired (Ethernet, RS-485, USB) connectivity options.
- **Power Management:** Sources include batteries, energy harvesting (solar, vibration), mains power, and PoE; techniques include sleep modes, duty cycling, and power gating.
- **Device Categories:** Constrained (simple sensors, RFID tags), Intermediate (smart home devices, wearables), and Gateway (Raspberry Pi, industrial gateways).

### Important Concepts

- IoT device architecture: Sensor reads environment, MCU processes data, Actuator performs action, Communication module connects to network
- Wireless protocol trade-offs: range vs data rate vs power consumption
- Three device categories: Constrained, Intermediate, and Gateway devices
- Design considerations: environmental factors, reliability (MTBF), physical security (tamper-proof, secure boot, HSMs), and cost
- Emerging trends: SoC integration, edge AI/ML, energy harvesting, MEMS miniaturization, flexible/wearable electronics

### Notes

- Always list and describe the five key components (sensors, actuators, MCUs, communication modules, power systems) in exam answers about physical design.
- Compare wireless technologies using a table format with range, data rate, power consumption, and use cases.
- Physical design includes both hardware components and the firmware that controls them -- address both in answers.
