# Python Modules for IoT Development


## Table of Contents

- [Python Modules for IoT Development](#python-modules-for-iot-development)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Module Creation and Structure](#1-module-creation-and-structure)
- [sensors.py (Module for sensor operations)](#sensorspy-module-for-sensor-operations)
- [Sensor reading logic](#sensor-reading-logic)
  - [2. Module Import Mechanisms](#2-module-import-mechanisms)
  - [3. Module Search Path](#3-module-search-path)
  - [4. Special Module Attributes](#4-special-module-attributes)
- [In module_usage.py](#in-moduleusagepy)
  - [5. Standard Library Modules for IoT](#5-standard-library-modules-for-iot)
  - [6. The `__name__` Variable](#6-the-name-variable)
- [communication.py](#communicationpy)
- [Implementation](#implementation)
- [Test code when run directly](#test-code-when-run-directly)
- [Module Architecture in IoT Systems](#module-architecture-in-iot-systems)
- [Examples](#examples)
  - [Example 1: Sensor Data Module](#example-1-sensor-data-module)
- [Test sensor reading](#test-sensor-reading)
  - [Example 2: Configuration Module](#example-2-configuration-module)
- [IoT Device Configuration](#iot-device-configuration)
- [Module Dependency Diagram](#module-dependency-diagram)
- [Exam Tips](#exam-tips)
- [Real-World IoT Application](#real-world-iot-application)

## Introduction

Python modules are essential building blocks for creating maintainable IoT systems. A module is a file containing Python code that defines functions, classes, and variables, which can be reused across multiple projects. In IoT applications, modules help organize complex systems into logical components like sensor interfaces, communication protocols, and data processors.

The importance of modules grows exponentially with project complexity. A typical weather monitoring IoT system might require separate modules for:

- Sensor communication (DHT11 temperature/humidity)
- Data encryption
- MQTT message publishing
- Error logging

Modules enable team collaboration by allowing parallel development and prevent code duplication through reusable components. The Python Standard Library provides over 200 built-in modules that form the foundation for IoT development.

## Key Concepts

### 1. Module Creation and Structure

Create a module by saving Python code in a `.py` file:

```python
# sensors.py (Module for sensor operations)
DHT_GPIO_PIN = 4  # Module-level variable

def read_temperature():
    """Returns temperature in Celsius"""
    # Sensor reading logic
    return 25.6

def calculate_dew_point(temp, humidity):
    """Magnus formula for dew point"""
    return temp - ((100 - humidity)/5)
```

### 2. Module Import Mechanisms

**Basic Import:**

```python
import sensors
print(sensors.read_temperature())
```

**Selective Import:**

```python
from sensors import calculate_dew_point
print(calculate_dew_point(25, 60))
```

**Alias Import:**

```python
import sensors as iot_sensors
print(iot_sensors.DHT_GPIO_PIN)
```

### 3. Module Search Path

Python searches for modules in this order:

1. Current directory
2. PYTHONPATH environment variable directories
3. Standard library directories
4. Site-packages directory

View the search path:

```python
import sys
print(sys.path)
```

### 4. Special Module Attributes

```python
# In module_usage.py
import json

print(json.__name__)      # Output: 'json'
print(json.__file__)      # Path to json module
print(json.__doc__)       # Documentation string
```

### 5. Standard Library Modules for IoT

| Module     | IoT Application               |
| ---------- | ----------------------------- |
| `json`     | Data serialization for MQTT   |
| `time`     | Sensor polling intervals      |
| `datetime` | Timestamping sensor data      |
| `os`       | File system operations        |
| `sys`      | System parameters and exit    |
| `socket`   | Network communication         |
| `logging`  | Error tracking in deployments |

### 6. The `__name__` Variable

Control module execution context:

```python
# communication.py
def send_mqtt(data):
    # Implementation
    pass

if __name__ == "__main__":
    # Test code when run directly
    send_mqtt({"temp": 25})
```

## Module Architecture in IoT Systems

**Typical IoT Module Structure:**

```
weather_system/
├── sensors/              # Sub-package
│   ├── __init__.py
│   ├── temperature.py
│   └── humidity.py
├── communication/
│   ├── mqtt_client.py
│   └── http_api.py
└── utils/
    ├── data_processing.py
    └── logger.py
```

## Examples

### Example 1: Sensor Data Module

**File: environmental.py**

```python
"""Module for environmental sensors"""
import time
import random

SENSOR_ID = "DHT22_01"

def read_sensor():
    """Simulate sensor reading with random values"""
    return {
        'timestamp': time.time(),
        'temperature': random.uniform(18.0, 32.0),
        'humidity': random.uniform(40.0, 80.0)
    }

def format_json(data):
    """Convert to IoT JSON format"""
    return {
        "sensor": SENSOR_ID,
        "values": data
    }

if __name__ == "__main__":
    # Test sensor reading
    print(format_json(read_sensor()))
```

**Usage in Main Program:**

```python
from environmental import read_sensor, format_json
import json

sensor_data = read_sensor()
mqtt_payload = json.dumps(format_json(sensor_data))
print(f"Publishing: {mqtt_payload}")
```

### Example 2: Configuration Module

**File: config.py**

```python
# IoT Device Configuration
MQTT_BROKER = "iot.eclipse.org"
MQTT_PORT = 1883
SENSOR_INTERVAL = 5  # Seconds
ALLOWED_TEMP_RANGE = (-40, 85)
```

**Usage Across Modules:**

```python
import config
from time import sleep

def sensor_loop():
    while True:
        read_sensors()
        sleep(config.SENSOR_INTERVAL)
```

## Module Dependency Diagram

```
[Main Program] --> [sensor_module]
                --> [communication_module]
                --> [config]

[sensor_module] --> [time]
                 --> [random]

[communication_module] --> [paho.mqtt.client]
                        --> [json]
```

## Exam Tips

1. **Import Syntax Variations:**
   - `import module` vs `from module import function`
   - Understand `import *` risks (namespace pollution)

2. **Module Search Path:**
   - Remember search order: current dir → PYTHONPATH → stdlib
   - Adding custom paths: `sys.path.append('/custom/path')`

3. **`__name__` Usage:**
   - `if __name__ == "__main__":` allows dual use (module vs script)
   - Test code isolation technique

4. **Standard Library Knowledge:**
   - Memorize 5 IoT-relevant stdlib modules and their uses
   - Example: `json` for MQTT data serialization

5. **Module Design Best Practices:**
   - Cohesive module responsibility
   - Avoid circular imports
   - Use **init**.py for package initialization

6. **Error Diagnosis:**
   - Recognize `ModuleNotFoundError` causes
   - Handle version conflicts between modules

7. **Memory Management:**
   - Modules are loaded once per interpreter session
   - Use `reload()` from importlib for development

## Real-World IoT Application

In a smart agriculture system, modules would be organized as:

- `soil_sensor.py`: Moisture and pH readings
- `irrigation_control.py`: Valve control logic
- `weather_api.py`: External weather data integration
- `alert_system.py`: SMS/email notifications

This modular approach allows updating the SMS gateway without affecting sensor logic, demonstrating maintainability in IoT deployments.
