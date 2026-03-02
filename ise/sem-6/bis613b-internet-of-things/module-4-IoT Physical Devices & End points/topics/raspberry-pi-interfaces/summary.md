# Raspberry Pi Interfaces

=====================================

### Overview

The Raspberry Pi provides multiple hardware interfaces including GPIO, I2C, SPI, UART, USB, Ethernet, Wi-Fi, Bluetooth, HDMI, CSI, and DSI that enable it to communicate with sensors, actuators, displays, networks, and peripherals for IoT applications.

### Key Points

- **GPIO (General Purpose I/O):** 40-pin header with power pins (3.3V, 5V, GND), digital I/O pins, and special function pins; programmed using RPi.GPIO or gpiozero libraries in Python.
- **I2C Protocol:** Two-wire serial protocol using SDA (data) and SCL (clock) lines, supports multiple devices with 7-bit addresses, operates at 100-400 kHz; ideal for connecting multiple low-speed sensors.
- **SPI Protocol:** Four-wire, full-duplex serial protocol (MOSI, MISO, SCLK, CE) operating at speeds up to tens of MHz; used for high-speed communication with sensors, displays, and ADCs.
- **UART Protocol:** Asynchronous two-wire serial communication (TX, RX) with configurable baud rates and no clock signal; commonly used for GPS modules and console access.
- **Network Interfaces:** Ethernet (100Mbps/1Gbps with PoE support), Wi-Fi (2.4/5 GHz, 802.11 b/g/n/ac), and Bluetooth (4.2/5.0 with BLE support).
- **Display/Camera Interfaces:** HDMI (up to 4K), DSI for official touchscreen display, and CSI for Raspberry Pi Camera Module with direct GPU access.
- **Power Management:** Requires 5V DC input via USB-C/Micro-USB (minimum 2.5A for Pi 4); GPIO provides 3.3V and 5V output with limited current (50mA per pin).

### Important Concepts

- Protocol comparison: I2C (2 wires, multi-device, moderate speed) vs SPI (4 wires, high speed, full-duplex) vs UART (2 wires, point-to-point, asynchronous)
- Interface selection criteria: data rate, number of devices, distance, power consumption, and complexity
- PWM (Pulse Width Modulation) on GPIO for analog-like control (e.g., LED brightness)
- Security considerations: physical security of GPIO, network encryption, data validation, access control

### Notes

- Exam questions frequently ask to compare I2C, SPI, and UART protocols and recommend the best protocol for a given IoT scenario.
- Memorize the pin functions: SDA/SCL for I2C, MOSI/MISO/SCLK/CE for SPI, and TX/RX for UART.
- Know the speed and use-case trade-offs: SPI for high-speed data, I2C for multiple sensors on same bus, UART for serial devices like GPS.
