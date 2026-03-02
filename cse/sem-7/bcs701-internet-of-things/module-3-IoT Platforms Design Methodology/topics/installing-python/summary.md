# Installing Python for IoT - Summary

## Key Definitions
- **Python 3 (CPython)**: The reference implementation of Python, required for modern IoT development
- **Virtual Environment (venv)**: An isolated Python installation that prevents dependency conflicts between projects
- **pip**: The package installer for Python, essential for installing IoT libraries
- **Raspberry Pi OS**: The official operating system for Raspberry Pi, pre-installed with Python 3
- **GPIO (General Purpose Input/Output)**: Pins on Raspberry Pi for hardware interaction
- **I2C/SPI**: Communication protocols for interfacing sensors and actuators in IoT systems
- **PlatformIO**: An open-source ecosystem for embedded IoT development

## Important Formulas
- Python version check: `python3 --version`
- Pip version check: `pip3 --version`
- Virtual environment creation: `python3 -m venv <env-name>`
- Virtual environment activation (Linux/macOS): `source <env-name>/bin/activate`
- Virtual environment activation (Windows): `<env-name>\Scripts\activate`
- MQTT library installation: `pip install paho-mqtt`
- GPIO library installation: `pip install RPi.GPIO`
- Conda environment creation: `conda create -n <env-name> python=3.12`

## Key Points
1. Python 3.10+ is required for modern IoT development; Python 2.7 is deprecated
2. Always enable "Add Python to PATH" during Windows installation
3. Raspberry Pi OS comes with Python 3 pre-installed; verify with `python3 --version`
4. Virtual environments are mandatory for IoT projects to manage dependencies
5. Essential IoT libraries include paho-mqtt (MQTT), RPi.GPIO/gpiozero (hardware), and Adafruit libraries (sensors)
6. VS Code with Python extension provides comprehensive IoT development features
7. PlatformIO supports Arduino, ESP32, and other embedded platforms
8. Raspberry Pi requires interface enablement via `raspi-config` for I2C/SPI
9. GPIO permission errors on Raspberry Pi are resolved by adding user to gpio group
10. Package managers (Homebrew for macOS, apt for Ubuntu, winget for Windows) provide streamlined installation

## Common Mistakes
1. **Forgetting to add Python to PATH on Windows**: Causes "python is not recognized" errors
2. **Installing packages globally instead of in virtual environments**: Leads to version conflicts
3. **Skipping virtual environment activation**: Results in packages installed to system Python
4. **Not enabling I2C/SPI interfaces on Raspberry Pi**: Causes sensor communication failures
5. **Using sudo with pip on Linux**: Creates permission issues and system Python conflicts
6. **Installing Python 2 instead of Python 3**: Many IoT libraries require Python 3
7. **Not restarting terminal after PATH changes**: New paths not loaded in current session
8. **Ignoring hardware permissions on Raspberry Pi**: GPIO access requires proper group membership
===SUMMARY_MD===