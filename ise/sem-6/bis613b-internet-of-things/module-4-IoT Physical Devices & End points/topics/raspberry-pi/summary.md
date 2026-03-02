# Raspberry Pi

=====================================

### Overview

The Raspberry Pi is a small, affordable single-board computer developed by the Raspberry Pi Foundation, widely used in IoT applications due to its low cost, modularity, GPIO header, and ability to run a full Linux operating system. It serves as both a sensor node and a gateway device in IoT ecosystems.

### Key Points

- **GPIO Header:** The 40-pin General Purpose Input/Output header is the most important feature for IoT, enabling connection to sensors, actuators, LEDs, and other electronic components.
- **Model Variants:** Pi Zero W (ultra-low power, 512MB RAM), Pi 3B+ (1GB RAM, gateway use), and Pi 4B (up to 8GB RAM, edge computing) serve different IoT use cases.
- **Operating System:** Runs Raspberry Pi OS (Debian-based Linux) with kernel, shell (Bash), package manager (apt), daemons, and permission-based security.
- **Communication Protocols:** Supports I2C (two-wire, multi-device), SPI (high-speed, full-duplex), and UART (point-to-point serial) over GPIO pins.
- **Python Programming:** RPi.GPIO (low-level pin control) and gpiozero (high-level component objects) are the primary libraries for IoT development.
- **Connectivity:** Built-in Wi-Fi, Bluetooth, Gigabit Ethernet, USB ports, CSI camera interface, and DSI display interface.
- **IoT Workflow:** Sensors connect to Pi via GPIO/I2C/SPI, Python processes data, and results are sent to cloud APIs via Wi-Fi/Ethernet.

### Important Concepts

- BCM vs Physical pin numbering schemes for GPIO
- I2C uses SDA and SCL lines; SPI uses MOSI, MISO, SCLK, CE lines; UART uses Tx and Rx
- IoT weather station example: BME280 sensor over I2C, Python for processing, HTTP POST to cloud
- GPIO.setmode(), GPIO.setup(), GPIO.output(), and GPIO.cleanup() workflow

### Notes

- Exam MCQs commonly test differences between Pi models (Zero vs 3 vs 4) and their target use cases based on specifications.
- Be prepared to read and interpret short Python GPIO code snippets using RPi.GPIO or gpiozero libraries.
- Always define what makes Raspberry Pi an IoT device: sensing capability (via sensors), processing, and network connectivity.
