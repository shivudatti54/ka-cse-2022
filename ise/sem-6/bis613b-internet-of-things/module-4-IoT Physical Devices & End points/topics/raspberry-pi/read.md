# Raspberry Pi Overview for IoT


## Table of Contents

- [Raspberry Pi Overview for IoT](#raspberry-pi-overview-for-iot)
- [Introduction to Raspberry Pi](#introduction-to-raspberry-pi)
- [Key Hardware Specifications](#key-hardware-specifications)
- [Linux on Raspberry Pi](#linux-on-raspberry-pi)
- [Raspberry Pi Interfaces for IoT](#raspberry-pi-interfaces-for-iot)
- [Programming with Python](#programming-with-python)
- [Using RPi.GPIO](#using-rpigpio)
- [Using gpiozero (simpler)](#using-gpiozero-simpler)
- [Case Study: Simple IoT Weather Station](#case-study-simple-iot-weather-station)
- [Sensor setup](#sensor-setup)
- [Cloud API endpoint](#cloud-api-endpoint)
- [Read sensor data](#read-sensor-data)
- [Send data to cloud](#send-data-to-cloud)
- [Wait for 5 minutes before next reading](#wait-for-5-minutes-before-next-reading)
- [Exam Tips](#exam-tips)

## Introduction to Raspberry Pi

The Raspberry Pi is a series of small, affordable, single-board computers developed in the United Kingdom by the Raspberry Pi Foundation. Its primary purpose is to promote the teaching of basic computer science in schools and in developing countries. However, due to its low cost, modularity, and open design, it has become immensely popular in the hobbyist market and for prototyping Internet of Things (IoT) applications.

An IoT device is a piece of hardware that can transmit data over a network without requiring human-to-human or human-to-computer interaction. The Raspberry Pi fits this definition perfectly as it can sense its environment (via attached sensors), process data, and communicate with other devices or a central server.

## Key Hardware Specifications

Different models of Raspberry Pi offer varying capabilities. Here is a comparison of some popular models relevant to IoT:

| Model             | CPU                     | RAM     | Networking                              | GPIO Pins | Power Consumption | Typical IoT Use Case                           |
| :---------------- | :---------------------- | :------ | :-------------------------------------- | :-------- | :---------------- | :--------------------------------------------- |
| **Pi Zero W**     | 1GHz Single-core        | 512MB   | Wi-Fi, Bluetooth                        | 40        | ~0.5W             | Ultra-low power, space-constrained sensor node |
| **Pi 3 Model B+** | 1.4GHz Quad-core        | 1GB     | Gigabit Ethernet, Wi-Fi, Bluetooth      | 40        | ~3-4W (idle)      | Gateway device, local data processing hub      |
| **Pi 4 Model B**  | 1.5GHz-1.8GHz Quad-core | 2GB-8GB | Gigabit Ethernet (x2), Wi-Fi, Bluetooth | 40        | ~3-7W (idle)      | High-performance edge computing, media server  |

**General Purpose Input/Output (GPIO) Header:** This is arguably the most important feature for IoT. The 40-pin header allows you to connect a vast array of sensors, actuators, LEDs, and other electronic components directly to the Pi, enabling it to interact with the physical world.

```
+-----+-----+---------+------+---+---Pi 4B--+---+------+---------+-----+-----+
| BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
|     |     |    3.3V |      |   |  1 || 2  |   |      | 5V      |     |     |
|   2 |   8 |   SDA.1 | ALT0 | 1 |  3 || 4  |   |      | 5V      |     |     |
|   3 |   9 |   SCL.1 | ALT0 | 1 |  5 || 6  |   |      | GND     |     |     |
|   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
|     |     |     GND |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
|  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
|  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | GND     |     |     |
|  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
|     |     |    3.3V |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
|  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | GND     |     |     |
|   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
|  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
|     |     |     GND |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
|   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
|   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | GND     |     |     |
|   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
|  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | GND     |     |     |
|  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
|  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
|     |     |     GND |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
+-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
```

_Simplified GPIO pinout diagram for Raspberry Pi (BCM numbering)_

## Linux on Raspberry Pi

The Raspberry Pi typically runs a Linux-based operating system. The most common and officially supported OS is **Raspberry Pi OS** (formerly Raspbian), which is a Debian-based distribution optimized for the Pi's hardware.

**Key Linux Concepts for IoT:**

- **Kernel:** The core of the OS that manages hardware resources.
- **Shell:** The command-line interface (CLI) used to interact with the system (e.g., Bash).
- **Packages:** Software bundles managed by a package manager like `apt` (Advanced Package Tool).
- **Daemons:** Background processes that provide services (e.g., a web server daemon).
- **Permissions:** A security model where users and processes have specific rights (crucial for system security).

Basic interaction is done through a terminal. Common commands include:

- `ls` - List directory contents
- `cd` - Change directory
- `sudo` - Execute a command with superuser privileges
- `apt-get update && apt-get upgrade` - Update the package list and upgrade installed packages
- `python3 --version` - Check the installed Python version

## Raspberry Pi Interfaces for IoT

The Pi offers several hardware interfaces to connect with the external world, making it a versatile IoT device.

**1. GPIO (General Purpose Input/Output):** As shown in the pinout, these are programmable pins that can be set to read digital input (e.g., from a button) or write digital output (e.g., to an LED).

**2. Protocols over GPIO:**

- **I²C (Inter-Integrated Circuit):** A multi-device, two-wire serial protocol for connecting low-speed peripherals (sensors, AD converters). Uses SDA (data) and SCL (clock) lines.
  ```
  Master (Pi) ------- SDA -------> Slave Device 1
        |             SCL -------> Slave Device 2
        |             SCL -------> Slave Device 3
        |_____________SDA -------> Slave Device 4
  ```
- **SPI (Serial Peripheral Interface):** A faster, full-duplex serial protocol for communication between a master and one or more slave devices. Uses MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Clock), and CE (Chip Enable) lines.
- **UART (Universal Asynchronous Receiver/Transmitter):** A serial protocol for point-to-point communication, often used for GPS modules or to communicate with Arduino boards. Uses Tx (transmit) and Rx (receive) pins.

**3. USB Ports:** Used to connect Wi-Fi dongles (on older models), keyboards, mice, webcams, and external storage. A USB webcam turns a Pi into a powerful vision-based IoT device.

**4. Camera Serial Interface (CSI):** A dedicated port for connecting the official Raspberry Pi Camera Module, enabling high-quality image and video capture.

**5. Display Serial Interface (DSI):** A port for connecting an official Raspberry Pi touchscreen display.

## Programming with Python

Python is the recommended and most popular language for programming the Raspberry Pi, especially for IoT prototypes, due to its simplicity, readability, and vast ecosystem of libraries.

**Key Python Libraries for Raspberry Pi IoT:**

- **RPi.GPIO:** The fundamental library for controlling GPIO pins. It allows you to set pin modes, read inputs, and write outputs.
- **gpiozero:** A higher-level, beginner-friendly library that provides objects for components (e.g., LED, Button, MotionSensor) instead of dealing with raw pins.
- **smbus2:** A library for communicating with I²C devices.
- **spidev:** A library for SPI communication.
- **Pillow (PIL):** For image processing, often used with the camera module.
- **Requests:** For making HTTP calls to send sensor data to web APIs or cloud platforms.

**Basic Example: Blinking an LED**

```python
# Using RPi.GPIO
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait 1 second
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C exit

# Using gpiozero (simpler)
from gpiozero import LED
from time import sleep

led = LED(17)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

## Case Study: Simple IoT Weather Station

A common IoT project is a weather station that logs data to the cloud.

**Components:**

1.  **Raspberry Pi** (e.g., Model 3B+)
2.  **BME280 Sensor** (connected via I²C) - measures temperature, humidity, and pressure.
3.  **Internet Connection** (via Wi-Fi/Ethernet)

**Workflow:**

```
+----------------+    +-------------+    +-----------------+    +-------------+
| BME280 Sensor  | -> | Raspberry Pi| -> | Internet / WiFi| -> | Cloud API   |
| (I²C Bus)      |    | (Python App)|    |                 |    | (e.g., AWS, |
+----------------+    +-------------+    +-----------------+    +-------------+
                                                                    |
                                                                    v
                                                            +---------------+
                                                            | Database/Dash-|
                                                            | board for Log-|
                                                            | ging & Viewing|
                                                            +---------------+
```

**Python Code Snippet:**

```python
import smbus2
import bme280
import requests
import time

# Sensor setup
port = 1
address = 0x76  # BME280 address
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

# Cloud API endpoint
url = 'https://your-cloud-api.com/data'

try:
    while True:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)
        payload = {
            'temperature': data.temperature,
            'humidity': data.humidity,
            'pressure': data.pressure,
            'timestamp': data.timestamp.isoformat()
        }

        # Send data to cloud
        response = requests.post(url, json=payload)
        print(f"Data sent. Status: {response.status_code}")

        # Wait for 5 minutes before next reading
        time.sleep(300)

except KeyboardInterrupt:
    print("Script stopped by user.")
```

## Exam Tips

1.  **Focus on GPIO:** Be sure to understand the purpose of the GPIO header and the differences between key protocols (I²C vs. SPI vs. UART). You may be asked to choose a protocol for a given scenario.
2.  **Know the Models:** Understand the rough specifications and target use cases for different Pi models (Zero vs. 3 vs. 4). This is a common MCQ topic.
3.  **Python Code Reading:** You will likely be given a short Python code snippet using `RPi.GPIO` or `gpiozero` and asked to predict its output or find an error. Practice reading basic GPIO control code.
4.  **Linux Commands:** Memorize a handful of essential Linux commands (`ls`, `cd`, `sudo`, `apt-get`, `nano`) and their basic usage.
5.  **Define IoT Device:** Be prepared to define what an IoT device is and explain why the Raspberry Pi is a suitable platform, citing its key features (cost, connectivity, GPIO).
