# Installing Python for IoT

=====================================

### Overview

Installing Python is the first step in setting up an IoT development environment. Python is preferred for IoT due to its simple syntax, cross-platform compatibility, and extensive library ecosystem for sensor communication and device control.

### Key Points

- **Why Python for IoT:** Ease of use, cross-platform support (Windows, macOS, Linux), and extensive libraries for IoT development
- **Windows Installation:** Download from official website, run installer, and ensure "Add Python to PATH" is checked
- **macOS Installation:** Install Homebrew first, then use brew install python, verify with python3 --version
- **Linux Installation:** Use package manager with sudo apt update followed by sudo apt install python3
- **PATH Configuration:** Essential to add Python to system PATH for access from any directory in the terminal
- **Package Management:** Use pip (Python's package installer) to install additional IoT libraries like PySerial, PyUSB, and Scapy
- **IoT Libraries:** PySerial for serial communication, PyUSB for USB devices, Scapy for network exploration, RPi.GPIO for Raspberry Pi

### Important Concepts

- Python 3 is the standard version for IoT development
- pip is the primary tool for installing Python packages and dependencies
- Virtual environments help isolate project dependencies
- Cross-platform nature of Python makes it ideal for diverse IoT hardware

### Notes

- Always verify installation with python3 --version after completing the setup
- Adding Python to PATH during installation prevents common command-not-found errors
- Libraries like RPi.GPIO and Adafruit_DHT are specific to hardware platforms and may require additional system-level dependencies
