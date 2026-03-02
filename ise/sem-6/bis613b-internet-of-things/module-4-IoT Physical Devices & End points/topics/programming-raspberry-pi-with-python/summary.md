# Programming Raspberry Pi with Python

=====================================

### Overview

Python is the recommended programming language for Raspberry Pi IoT development due to its simplicity, readability, and vast ecosystem of libraries. The Raspberry Pi comes with Python pre-installed, enabling rapid prototyping of IoT applications involving sensor reading, hardware control, and data communication.

### Key Points

- **Setup Requirements:** Install Raspberry Pi OS on a microSD card, connect to monitor/keyboard/power, configure network settings, and use Python IDEs like IDLE or Thonious.
- **Python Basics:** Variables and data types (int, float, str, bool), control structures (if/else, for/while loops), functions (def), and module imports are foundational for IoT scripts.
- **GPIO Control with RPi.GPIO:** Use GPIO.setmode(GPIO.BCM) for pin numbering, GPIO.setup() for pin direction, GPIO.output() for writing, and GPIO.input() for reading pin states.
- **Hardware Interfacing:** LEDs are controlled via GPIO output pins, buttons are read via GPIO input pins, and sensors like DHT11 use dedicated libraries (Adafruit_DHT).
- **Key Libraries:** RPi.GPIO (low-level GPIO control), gpiozero (high-level component abstraction), Adafruit_DHT (temperature/humidity sensors), smbus2 (I2C devices), and requests (HTTP API calls).
- **Temperature Monitoring Example:** Connect DHT11 sensor to GPIO, use Adafruit_DHT.read() to get humidity and temperature, and display or transmit the readings.

### Important Concepts

- GPIO.BCM vs GPIO.BOARD numbering: BCM uses Broadcom chip pin numbers, BOARD uses physical header pin numbers
- GPIO.cleanup() must be called to reset pins and prevent warnings on next run
- Python modules like time (delays), serial (UART), and requests (HTTP) extend IoT functionality
- Event-driven programming: reading sensor inputs, processing data, triggering actuator outputs

### Notes

- Exam questions may provide a short Python GPIO code snippet and ask you to predict output or identify errors -- practice reading RPi.GPIO code.
- Always remember the sequence: setmode, setup, output/input, and cleanup when writing GPIO programs.
- The combination of sensor reading (input), processing logic (Python), and actuator control (output) forms the core IoT programming pattern on Raspberry Pi.
