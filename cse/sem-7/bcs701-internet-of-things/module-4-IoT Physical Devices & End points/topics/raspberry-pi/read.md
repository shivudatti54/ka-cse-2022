# Raspberry Pi for Internet of Things: Architecture, Interfaces, and Implementation

## 1. Introduction and IoT Context

The Raspberry Pi represents a paradigm shift in embedded computing, transitioning from specialized single-purpose devices to versatile single-board computers (SBCs) capable of executing full operating systems while maintaining the peripheral interfacing capabilities essential for Internet of Things (IoT) applications. Developed by the Raspberry Pi Foundation in the United Kingdom, this ARM-based platform was originally conceived to promote computer science education, particularly in developing nations. However, its exceptional cost-to-performance ratio, combined with extensive community support and open-source software ecosystem, has established it as a dominant force in IoT prototyping and deployment.

The convergence of embedded systems and network connectivity defines modern IoT architectures. An IoT device fundamentally operates as an edge node within a distributed system, performing three primary functions: **sensing** (acquiring data from physical environment via sensors), **processing** (executing computations on acquired data), and **communication** (transmitting processed data to cloud platforms or receiving commands from central servers). The Raspberry Pi fulfills all three roles through its General Purpose Input/Output (GPIO) interface for sensing, ARM processor for processing, and integrated networking capabilities for communication.

### 1.1 IoT Architecture Layers and Raspberry Pi Position

The IoT architectural hierarchy comprises four distinct layers:

| Layer                 | Function                                             | Raspberry Pi Capability           |
| --------------------- | ---------------------------------------------------- | --------------------------------- |
| **Perception Layer**  | Sensors and actuators for physical world interaction | GPIO, I²C, SPI, ADC interfaces    |
| **Network Layer**     | Data transmission to cloud/core systems              | Wi-Fi, Ethernet, Bluetooth        |
| **Processing Layer**  | Data analysis and edge computing                     | Quad-core ARM Cortex-A processors |
| **Application Layer** | User interfaces and business logic                   | Linux OS, Python, Node.js, Docker |

The Raspberry Pi's positioning across multiple layers makes it uniquely suitable for IoT applications requiring local intelligence combined with cloud connectivity.

## 2. System-on-Chip Architecture and Hardware Specifications

### 2.1 Broadcom SoC Integration

Modern Raspberry Pi models employ Broadcom System-on-Chip (SoC) devices integrating multiple functional blocks. The Pi 4 Model B utilizes the **BCM2711** SoC, featuring a 64-bit quad-core ARM Cortex-A72 processor operating at 1.5 GHz (with turbo mode to 1.8 GHz). This architecture represents a significant advancement over earlier generations, delivering approximately three times the performance of the ARM Cortex-A53 based Pi 3B+.

The SoC integrates several critical components:

- **VideoCore VI GPU**: Supporting OpenGL ES 3.0 for hardware-accelerated graphics
- **LPDDR4 SDRAM Controller**: Supporting up to 8GB RAM with theoretical bandwidth of 31.76 GB/s
- **PCIe Gen 2 Interface**: Providing high-speed connectivity for external peripherals
- **Hardware-encoded Video**: Supporting 4K@60fps H.265 and 4K@30fps H.264 decoding

### 2.2 Comparative Analysis of IoT-Applicable Models

| Parameter          | Pi Zero 2 W        | Pi 3 Model B+        | Pi 4 Model B (2GB)   | Pi 4 Model B (8GB)   |
| ------------------ | ------------------ | -------------------- | -------------------- | -------------------- |
| **SoC**            | BCM2710A1 (64-bit) | BCM2837B0 (64-bit)   | BCM2711 (64-bit)     | BCM2711 (64-bit)     |
| **CPU**            | 1GHz Quad-core A53 | 1.4GHz Quad-core A53 | 1.5GHz Quad-core A72 | 1.5GHz Quad-core A72 |
| **RAM**            | 512MB LPDDR2       | 1GB LPDDR2           | 2GB LPDDR4           | 8GB LPDDR4           |
| **Ethernet**       | No                 | 300 Mbps             | 1 Gbps               | 1 Gbps               |
| **Wi-Fi**          | 802.11 b/g/n       | 802.11 b/g/n/ac      | 802.11 a/b/g/n/ac    | 802.11 a/b/g/n/ac    |
| **Bluetooth**      | 4.1                | 4.2                  | 5.0                  | 5.0                  |
| **GPIO**           | 40-pin             | 40-pin               | 40-pin               | 40-pin               |
| **Power (idle)**   | 0.3W               | 2.1W                 | 2.7W                 | 3.0W                 |
| **Power (stress)** | 1.7W               | 6.7W                 | 7.6W                 | 9.0W                 |

### 2.3 Power Consumption Analysis for IoT Deployment

Power budget calculations are critical for battery-powered IoT deployments. The following analysis demonstrates selection criteria:

**Scenario: Solar-powered remote sensor node**

Given:

- Solar panel output: 5V @ 500mA (2.5W) average
- Pi Zero 2 W power consumption: 1.7W peak, 0.5W idle with power management
- Sensor module: 100mW average
- Duty cycle: 5 minutes active, 55 minutes sleep

Calculating average power:

- Active period (10%): 1.8W × 0.1 = 0.18 Wh/hour
- Sleep period (90%): 0.6W × 0.9 = 0.54 Wh/hour
- **Total: 0.72 Wh/hour**

With a 10,000mAh battery at 3.7V (37 Wh capacity):

- Theoretical runtime: 37 / 0.72 ≈ 51 hours
- Accounting for 20% conversion loss: 51 × 0.8 ≈ 41 hours

This calculation demonstrates why the Pi Zero 2 W is preferred for ultra-low-power applications requiring intermittent connectivity.

## 3. GPIO Interface and Programming

### 3.1 GPIO Pinout Configuration

The 40-pin GPIO header provides the primary mechanism for interfacing with external hardware. Understanding pin numbering schemes is essential for correct hardware connections:

- **BCM Numbering**: Broadcom SOC channel numbering (used in Python libraries like RPi.GPIO)
- **Physical/Board Numbering**: Sequential numbering (1-40) based on physical position
- **WiringPi Numbering**: Legacy pin numbering scheme

```
Physical Pin Layout (Top-down view, component side):
+---+=========================+---+
| 1 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ | 2 |
| 3 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ | 4 |
| 5 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ | 6 |
| 7 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ | 8 |
| 9 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |10 |
|11 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |12 |
|13 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |14 |
|15 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |16 |
|17 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |18 |
|19 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |20 |
|21 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |22 |
|23 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |24 |
|25 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |26 |
|27 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |28 |
|29 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |30 |
|31 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |32 |
|33 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |34 |
|35 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |36 |
|37 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |38 |
|39 | ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ |40 |
+---+=========================+---+
 GND
```

**Critical Voltage Levels**: All GPIO pins operate at 3.3V logic level. Applying 5V directly to any GPIO pin will permanently damage the SoC. Voltage level shifting is mandatory when interfacing with 5V devices.

### 3.2 Python GPIO Programming

The RPi.GPIO library provides straightforward access to GPIO functionality:

```python
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Configuration
LED_PIN = 18 # BCM numbering
BUTTON_PIN = 17

def setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(LED_PIN, GPIO.OUT)
 GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def blink_led(duration=1.0):
 """Toggle LED state with specified duration"""
 GPIO.output(LED_PIN, GPIO.HIGH)
 time.sleep(duration)
 GPIO.output(LED_PIN, GPIO.LOW)
 time.sleep(duration)

def read_button():
 """Read button state with debouncing"""
 if GPIO.input(BUTTON_PIN) == GPIO.LOW:
 time.sleep(0.05) # Debounce delay
 if GPIO.input(BUTTON_PIN) == GPIO.LOW:
 return True
 return False

try:
 setup()
 while True:
 if read_button():
 blink_led(0.5)
 time.sleep(0.1)
except KeyboardInterrupt:
 GPIO.cleanup()
```

### 3.3 PWM and Motor Control

Pulse Width Modulation (PWM) enables analog control of digital outputs:

```python
import RPi.GPIO as GPIO
import time

SERVO_PIN = 12 # PWM-capable pin (GPIO18)

def angle_to_duty(angle):
 """Convert angle (0-180) to duty cycle percentage"""
 # Servo typically expects 50Hz PWM
 # 1ms = 0° (2% duty), 2ms = 180° (12% duty)
 return 2 + (angle / 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50) # 50 Hz frequency
servo.start(0)

try:
 while True:
 angle = int(input("Enter angle (0-180): "))
 servo.ChangeDutyCycle(angle_to_duty(angle))
 time.sleep(1)
except KeyboardInterrupt:
 servo.stop()
 GPIO.cleanup()
```

## 4. Communication Protocols

### 4.1 I²C (Inter-Integrated Circuit) Protocol

I²C employs a master-slave architecture with two bidirectional lines: Serial Data (SDA) and Serial Clock (SCL). The protocol supports multiple devices on the same bus through unique 7-bit addressing.

**Hardware Configuration:**

```
 3.3V 3.3V
 | |
 [R] [R] (4.7kΩ pull-up resistors)
 | |
 SDA --+------------------+---> SDA (GPIO 2)
 SCL --+------------------+---> SCL (GPIO 3)
```

**I²C Device Detection and Communication:**

```python
#!/usr/bin/env python3
import smbus2
import time

bus = smbus2.SMBus(1) # I²C bus 1

def scan_i2c_devices():
 """Scan all possible I²C addresses"""
 devices = []
 for addr in range(0x03, 0x78):
 try:
 bus.read_byte(addr)
 devices.append(hex(addr))
 except:
 pass
 return devices

def read_bme280(address=0x76):
 """Read temperature, humidity, pressure from BME280 sensor"""
 # Chip ID register
 chip_id = bus.read_byte_data(address, 0xD0)
 if chip_id != 0x60:
 raise ValueError(f"Expected BME280 (0x60), got {hex(chip_id)}")

 # Read calibration data and sensor values
 # Implementation details omitted for brevity
 return {"temperature": 25.5, "humidity": 60.2, "pressure": 1013.25}

# Enable I²C interface via device tree overlay
# Add to /boot/config.txt: dtparam=i2c_arm=on
# or add to /boot/firmware/config.txt: dtoverlay=i2c1
```

**Timing Analysis:**

- Standard mode: 100 kHz clock
- Fast mode: 400 kHz clock
- Fast mode+: 1 MHz clock
- High-speed mode: 3.4 MHz clock

### 4.2 SPI (Serial Peripheral Interface) Protocol

SPI provides higher throughput than I²C through full-duplex communication using separate data lines. The protocol uses a master-slave configuration with optional chip select lines.

**Pin Configuration:**
| Signal | GPIO (Pi 4) | Function |
|--------|-------------|----------|
| SCLK | GPIO 11 (SCK) | Serial Clock |
| MOSI | GPIO 10 (TXD) | Master Out Slave In |
| MISO | GPIO 9 (RXD) | Master In Slave Out |
| CE0, CE1 | GPIO 8, 7 | Chip Enable |

**SPI Communication Example:**

```python
#!/usr/bin/env python3
import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0) # Bus 0, Device 0
spi.max_speed_hz = 500000
spi.mode = 0b00 # Clock polarity 0, clock phase 0

def read_adc(channel=0):
 """Read 10-bit ADC value from MCP3008"""
 # MCP3008 command format: Start bit (1), Single/Diff (1), Channel (3), Null (1)
 command = [1, (8 + channel) << 4, 0]
 response = spi.xfer2(command)
 return ((response[1] & 0x03) << 8) + response[2]

try:
 while True:
 value = read_adc(0)
 voltage = value * 3.3 / 1024
 print(f"ADC: {value}, Voltage: {voltage:.3f}V")
 time.sleep(1)
finally:
 spi.close()
```

### 4.3 UART (Universal Asynchronous Receiver/Transmitter)

UART enables serial communication between the Raspberry Pi and devices such as GPS modules, Bluetooth adapters, and other microcontrollers.

**Configuration in /boot/firmware/config.txt:**

```
enable_uart=1
dtoverlay=disable-bt # Release Bluetooth pins for UART use
```

**Python UART Communication:**

```python
#!/usr/bin/env python3
import serial
import time

ser = serial.Serial(
 port='/dev/serial0',
 baudrate=9600,
 timeout=1
)

def read_gps_nmea():
 """Parse NMEA sentences from GPS module"""
 while True:
 line = ser.readline().decode('ascii', errors='ignore')
 if line.startswith('$GPGGA'):
 # Parse Global Positioning System Fix Data
 # $GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,47.0,M,,*47
 parts = line.split(',')
 if parts[6] == '1': # Valid fix
 lat = parts[2]
 lat_dir = parts[3]
 lon = parts[4]
 lon_dir = parts[5]
 return {
 'latitude': f"{lat[:2]}°{lat[2:]} {lat_dir}",
 'longitude': f"{lon[:3]}°{lon[3:]} {lon_dir}"
 }
```

## 5. Operating System and Network Configuration

### 5.1 Raspberry Pi OS Installation and Configuration

The recommended operating system, Raspberry Pi OS (formerly Raspbian), is a Debian-based distribution optimized for ARMv7+ architectures. Installation involves flashing the operating system image to an SD card using tools such as Raspberry Pi Imager.

**Post-Installation Configuration:**

```bash
# Update system packages
sudo apt update && sudo apt full-upgrade -y

# Expand filesystem to use entire SD card
sudo raspi-config # Select: Advanced Options → Expand Filesystem

# Configure timezone and locale
sudo raspi-config # Localisation Options

# Enable required interfaces
sudo raspi-config # Interface Options → Enable I2C/SPI/Serial/UART

# Set static IP address (/etc/dhcpcd.conf)
interface eth0
static ip_address=192.168.1.100/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8 8.8.4.4
```

### 5.2 Network Security for IoT Deployments

Security hardening is essential when exposing Raspberry Pi devices to network connectivity:

**SSH Key-Based Authentication:**

```bash
# Generate ED25519 key pair (recommended over RSA)
ssh-keygen -t ed25519 -C "pi@iot-node"

# Copy public key to Pi
ssh-copy-id pi@192.168.1.100

# Disable password authentication (/etc/ssh/sshd_config)
PasswordAuthentication no
PermitRootLogin no

# Restart SSH service
sudo systemctl restart ssh
```

**Firewall Configuration:**

```bash
# Install UFW (Uncomplicated Firewall)
sudo apt install ufw -y

# Default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH and HTTP
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status verbose
```

## 6. Edge Computing and Cloud Integration

### 6.1 Docker Containerization for IoT Applications

Docker provides lightweight virtualization suitable for running multiple IoT services on a single Raspberry Pi:

```bash
# Install Docker
curl -fsSL get.docker.com | sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install python3-pip -y
sudo pip3 install docker-compose

# Example docker-compose.yml for IoT application
cat > docker-compose.yml << EOF
version: '3.8'
services:
 mosquitto:
 image: eclipse-mosquitto
 ports:
 - "1883:1883"
 volumes:
 - ./mosquitto/config:/mosquitto/config
 networks:
 - iot-net

 influxdb:
 image: influxdb
 ports:
 - "8086:8086"
 volumes:
 - ./influxdb:/var/lib/influxdb2
 networks:
 - iot-net

 grafana:
 image: grafana/grafana
 ports:
 - "3000:3000"
 environment:
 - GF_SECURITY_ADMIN_PASSWORD=admin
 networks:
 - iot-net

networks:
 iot-net:
 driver: bridge
EOF
```

### 6.2 MQTT Protocol Implementation

MQTT (Message Queuing Telemetry Transport) serves as the de facto protocol for IoT messaging due to its lightweight nature and minimal bandwidth requirements:

**Publisher (Sensor Node):**

```python
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import json
import time
import random

BROKER = "192.168.1.100"
PORT = 1883
TOPIC = "sensors/temperature"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

try:
 while True:
 payload = {
 "sensor_id": "Pi-Zero-01",
 "temperature": round(random.uniform(20.0, 25.0), 2),
 "humidity": round(random.uniform(45.0, 55.0), 2),
 "timestamp": time.time()
 }
 client.publish(TOPIC, json.dumps(payload))
 print(f"Published: {payload}")
 time.sleep(30)
except KeyboardInterrupt:
 client.disconnect()
```

**Subscriber (Central Hub):**

```python
#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
 print(f"Connected with result code {rc}")
 client.subscribe("sensors/#")

def on_message(client, userdata, msg):
 payload = json.loads(msg.payload)
 print(f"Topic: {msg.topic}")
 print(f"Sensor: {payload['sensor_id']}")
 print(f"Temperature: {payload['temperature']}°C")
 print(f"Humidity: {payload['humidity']}%")
 print("-" * 40)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.100", 1883, 60)
client.loop_forever()
```

## 7. Assessment Questions

### 7.1 Multiple Choice Questions

**Question 1:** A temperature sensor outputs 0-10V analog signal. To interface with the Raspberry Pi's 3.3V GPIO, which component is essential?

A) Level shifter
B) Voltage divider
C) Optocoupler
D) Schmitt trigger

**Answer:** B) Voltage divider

**Explanation:** A voltage divider using two resistors (R1, R2) reduces the 10V signal to approximately 3.3V. Using the formula Vout = Vin × (R2/(R1+R2)), selecting R1 = 6.8kΩ and R2 = 3.3kΩ yields Vout ≈ 3.29V. Alternatively, dedicated voltage divider ICs or level shifters can be used, but a simple resistor network is the most economical solution.

---

**Question 2:** Calculate the series resistor required for an LED (Vf = 2.1V, If = 10mA) connected to a Raspberry Pi GPIO pin (3.3V output).

A) 120Ω
B) 330Ω
C) 12Ω
D) 1.2kΩ

**Answer:** A) 120Ω

**Explanation:** Using Ohm's Law:
R = (V_source - V_LED) / I_LED = (3.3V - 2.1V) / 0.010A = 1.2V / 0.010A = 120Ω
A 120Ω resistor limits the current to approximately 10mA. However, practical implementations often use 220Ω or 330Ω resistors to ensure safer current levels (approximately 5-6mA) accounting for GPIO pin variation and LED characteristics.

---

**Question 3:** For an IoT application requiring continuous data logging at 1Hz from multiple I²C sensors, which Raspberry Pi model provides optimal balance between performance and power consumption?

A) Pi Zero 2 W
B) Pi 3 Model B+
C) Pi 4 Model B (4GB)
D) Compute Module 4

**Answer:** A) Pi Zero 2 W

**Explanation:** The Pi Zero 2 W provides sufficient processing capability for basic I²C polling at 1Hz while consuming only 1.7W under load compared to 6-9W for the Pi 4. For continuous operation powered by battery or solar, the reduced power consumption significantly extends operational lifetime. The quad-core A53 processor handles I²C communication efficiently, and the 512MB RAM accommodates the sensor logging application and MQTT client without requiring the additional resources of the Pi 3 or Pi 4.

---

**Question 4:** What is the maximum theoretical data rate of I²C communication in Fast Mode Plus?

A) 100 kbps
B) 400 kbps
C) 1 Mbps
D) 3.4 Mbps

**Answer:** C) 1 Mbps

**Explanation:** I²C bus speeds are categorized as:

- Standard Mode: up to 100 kbps
- Fast Mode: up to 400 kbps
- Fast Mode Plus: up to 1 Mbps
- High-Speed Mode: up to 3.4 Mbps

The Raspberry Pi I²C interface defaults to 100 kHz but can be configured for higher speeds using the `dtparam=i2c_arm_baudrate=1000000` parameter in config.txt. Note that the actual achievable rate depends on pull-up resistor values, bus capacitance, and slave device capabilities.

---

**Question 5:** In MQTT QoS levels, what guarantee does QoS Level 1 (At Least Once) provide?

A) Message delivered exactly once
B) Message delivered at least once, possibly duplicated
C) Message delivered at most once, may be lost
D) Message queued for later delivery

**Answer:** B) Message delivered at least once, possibly duplicated

**Explanation:** MQTT defines three Quality of Service levels:

- QoS 0 (At Most Once): No acknowledgment, message may be lost
- QoS 1 (At Least Once): Acknowledgment required, message may be duplicated if acknowledgment lost
- QoS 2 (Exactly Once): Four-part handshake ensures single delivery

For critical IoT applications requiring guaranteed delivery, QoS 1 or 2 should be used at the cost of increased network overhead and latency.

---

**Question 6:** A solar-powered environmental monitoring station uses a Raspberry Pi Zero 2 W (peak: 1.7W, idle: 0.3W) with a temperature sensor (0.1W continuous). If the system operates with a 10% duty cycle (active 1 hour, sleep 9 hours daily), calculate the daily energy consumption in Wh.

A) 2.4 Wh
B) 4.8 Wh
C) 14.4 Wh
D) 24 Wh

**Answer:** C) 14.4 Wh

**Explanation:**
Daily energy = Energy(active) + Energy(sleep)

- Active period: (1.7W + 0.1W) × 1 hour = 1.8 Wh
- Sleep period: (0.3W + 0.1W) × 9 hours = 3.6 Wh
- Total: 1.8 + 3.6 = 14.4 Wh

With a 12V 10Ah battery (120 Wh capacity):

- Theoretical days of operation: 120 / 14.4 ≈ 8.3 days
- Accounting for 85% battery efficiency: 8.3 × 0.85 ≈ 7.1 days
- Adding a 10W solar panel (assuming 4 peak sun hours): 10 × 4 = 40 Wh/day generated, sufficient for continuous operation

---

**Question 7:** Which device tree overlay enables hardware PWM on GPIO pins 12 and 13?

A) dtoverlay=pwm
B) dtoverlay=pwm-2chan
C) dtoverlay=gpio-pwm
D) dtoverlay=pwm0

**Answer:** B) dtoverlay=pwm-2chan

**Explanation:** The Raspberry Pi provides two PWM channels:

- PWM0: GPIO 12 (PWM0) and GPIO 18 (PWM0)
- PWM1: GPIO 13 (PWM1) and GPIO 19 (PWM1)

The `dtoverlay=pwm-2chan` overlay enables both PWM channels simultaneously. For single-channel PWM, `dtoverlay=pwm` enables PWM0 on GPIO 18. Hardware PWM provides precise timing compared to software PWM, essential for servo control and LED dimming applications.

---

**Question 8:** What is the primary security concern when exposing a Raspberry Pi's MQTT broker to the internet?

A) CPU exhaustion attacks
B) Unauthorized subscription to topics
C) Memory card corruption
D) Network throughput limitation

**Answer:** B) Unauthorized subscription to topics

**Explanation:** An unsecured MQTT broker (no authentication/TLS) allows external attackers to:

- Subscribe to all topics, intercepting sensitive sensor data
- Publish malicious messages to control actuators
- Exhaust broker resources through subscription flooding

Security measures include:

- Implementing username/password authentication
- Enabling TLS/SSL encryption (MQTTS on port 8883)
- Using ACLs (Access Control Lists) to restrict topic access
- Implementing client certificate authentication

---

**Question 9:** When interfacing a 5V SPI sensor with Raspberry Pi's 3.3V GPIO, which approach ensures safe operation?

A) Direct connection (5V sensors are compatible)
B) Unidirectional level shifter
C) Bidirectional level shifter
D) Power the sensor at 3.3V

**Answer:** C) Bidirectional level shifter

**Explanation:** SPI communication is bidirectional (MOSI/MISO lines carry data in both directions). A bidirectional level shifter (such as TXS0108E) is required to safely translate between 5V and 3.3V logic levels. Unidirectional shifters only work for one-direction signals. Some 5V sensors can operate at 3.3V logic—checking the sensor datasheet is essential. Direct 5V to 3.3V GPIO connection will permanently damage the Raspberry Pi SoC.

---

**Question 10:** For deploying a containerized edge computing application on Raspberry Pi, which Docker feature provides process isolation while minimizing overhead?

A) Virtual machines
B) Full containers
C) Alpine-based minimal containers
D) Kubernetes pods

**Answer:** C) Alpine-based minimal containers

**Explanation:** Alpine Linux provides minimal base images (approximately 5MB) compared to standard Debian/Ubuntu images (100MB+). Benefits include:

- Faster image pull times over limited bandwidth
- Reduced storage requirements on SD cards
- Lower memory footprint
- Quicker container startup times

For Raspberry Pi, use ARM-specific images: `arm32v7/` or `arm64v8/` prefixes, or multi-arch manifests. Virtual machines introduce significant overhead (hypervisor, separate OS), while Kubernetes adds complexity unsuitable for single-board deployments.
