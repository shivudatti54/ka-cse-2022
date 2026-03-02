# What is an IoT Device?

=====================================

### Overview

An IoT device is a physical object enhanced with computing power, sensors, software, and network connectivity that can collect and exchange data over a network without human intervention. It bridges the physical and digital worlds by translating real-world phenomena into actionable data.

### Key Points

- **Core Components:** Every IoT device consists of four key parts -- sensors/actuators (perception), microcontroller/microprocessor (processing), connectivity module (communication), and power supply (energy).
- **Sensors vs Actuators:** Sensors are input devices that detect environmental changes (temperature, motion, light, humidity, GPS); actuators are output devices that perform physical actions (relays, servo motors, LEDs, buzzers).
- **MCU vs MPU:** Microcontrollers (Arduino, ESP32) are low-power, single-chip solutions for simple tasks; microprocessors (Raspberry Pi, BeagleBone) are more powerful, run full OS, and handle complex processing.
- **Connectivity Protocols:** Short-range (Wi-Fi, BLE, Zigbee, Z-Wave, NFC), long-range LPWAN (LoRaWAN, NB-IoT, Sigfox), and cellular (4G/LTE, 5G).
- **Key Characteristics:** Sensing, actuation, connectivity, low power, onboard processing, and cost-effectiveness.
- **Device Categories:** General-purpose (Raspberry Pi, Arduino), sensing devices, actuating devices, and gateway devices.
- **IoT Architecture Layers:** Perception/Sensing Layer (devices), Network Layer (communication), Processing Layer (cloud/edge), and Application Layer (dashboards, analytics).

### Important Concepts

- IoT devices reside at the Perception Layer of the 4-layer IoT architecture
- LPWAN protocols (LoRaWAN, NB-IoT) are designed for low power and wide area coverage
- I/O interfaces: GPIO, I2C, SPI, UART connect microcontrollers to peripherals
- Power efficiency is a critical constraint -- devices may use batteries, solar, or energy harvesting

### Notes

- A common short-answer question asks to list and describe the four core components of an IoT device (sensor/actuator, processor, connectivity, power).
- Be prepared to differentiate between MCU and MPU with examples and explain when to use each.
- Always place IoT devices in the context of the larger architecture (Perception Layer) when answering design questions.
