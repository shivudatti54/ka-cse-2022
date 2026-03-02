# File Handling in Python for IoT Applications


## Table of Contents

- [File Handling in Python for IoT Applications](#file-handling-in-python-for-iot-applications)
- [Introduction to File Handling in IoT](#introduction-to-file-handling-in-iot)
- [File Opening and Modes in Python](#file-opening-and-modes-in-python)
  - [File Opening Modes](#file-opening-modes)
  - [Best Practice: Using Context Managers](#best-practice-using-context-managers)
- [Recommended approach](#recommended-approach)
- [File is automatically closed after this block](#file-is-automatically-closed-after-this-block)
- [Not recommended (manual closing required)](#not-recommended-manual-closing-required)
- [Reading Files in IoT Applications](#reading-files-in-iot-applications)
  - [Reading Entire File Content](#reading-entire-file-content)
- [Read complete sensor log file](#read-complete-sensor-log-file)
  - [Reading Line by Line](#reading-line-by-line)
- [Process temperature readings line by line](#process-temperature-readings-line-by-line)
  - [Reading All Lines into a List](#reading-all-lines-into-a-list)
- [Process first 10 readings](#process-first-10-readings)
  - [Reading Specific Number of Characters](#reading-specific-number-of-characters)
- [Writing Files in IoT Applications](#writing-files-in-iot-applications)
  - [Writing Sensor Data to Files](#writing-sensor-data-to-files)
- [Log temperature reading](#log-temperature-reading)
  - [Appending Data (Continuous Logging)](#appending-data-continuous-logging)
- [Example usage](#example-usage)
  - [Writing Multiple Lines](#writing-multiple-lines)
- [Working with CSV Files in IoT](#working-with-csv-files-in-iot)
  - [Writing CSV Data](#writing-csv-data)
- [Log multiple sensor readings to CSV](#log-multiple-sensor-readings-to-csv)
  - [Reading CSV Data](#reading-csv-data)
  - [Using DictReader for Named Access](#using-dictreader-for-named-access)
- [Working with JSON Files in IoT](#working-with-json-files-in-iot)
  - [Writing JSON Configuration](#writing-json-configuration)
  - [Reading JSON Configuration](#reading-json-configuration)
  - [Handling JSON Sensor Data](#handling-json-sensor-data)
- [Example](#example)
- [File Operations for IoT Use Cases](#file-operations-for-iot-use-cases)
  - [Example 1: Data Buffering for Offline IoT Devices](#example-1-data-buffering-for-offline-iot-devices)
- [Usage](#usage)
  - [Example 2: Configuration File Management](#example-2-configuration-file-management)
- [Usage](#usage)
  - [Example 3: Sensor Data Logging System](#example-3-sensor-data-logging-system)
- [Usage](#usage)
- [Exception Handling in File Operations](#exception-handling-in-file-operations)
- [File Management Best Practices for IoT](#file-management-best-practices-for-iot)
  - [Further Reading](#further-reading)

## Introduction to File Handling in IoT

File handling is a fundamental aspect of Python programming that becomes particularly important in Internet of Things (IoT) applications. IoT devices frequently need to read sensor data from files, write logs, store configuration settings, cache data locally, and manage datasets before transmitting them to cloud services. Understanding file operations in Python is essential for building robust IoT systems that can handle data persistence, logging, and local storage efficiently.

In IoT contexts, file handling serves multiple purposes:

- **Data Logging**: Recording sensor readings, events, and system states
- **Configuration Management**: Storing and retrieving device settings
- **Data Buffering**: Temporarily storing data when network connectivity is unavailable
- **Local Processing**: Reading input files for analysis or processing
- **CSV/JSON Data Handling**: Managing structured data formats commonly used in IoT

## File Opening and Modes in Python

Python provides the built-in `open()` function to work with files. The basic syntax is:

```python
file_object = open(filename, mode)
```

### File Opening Modes

| Mode   | Description                              | Use in IoT                                  |
| ------ | ---------------------------------------- | ------------------------------------------- |
| `'r'`  | Read mode (default)                      | Reading sensor data from log files          |
| `'w'`  | Write mode (overwrites existing content) | Creating new configuration files            |
| `'a'`  | Append mode                              | Adding new sensor readings to existing logs |
| `'r+'` | Read and write                           | Updating configuration files                |
| `'w+'` | Write and read (overwrites)              | Creating and immediately reading data       |
| `'a+'` | Append and read                          | Continuous logging with occasional reads    |
| `'rb'` | Read binary                              | Reading image data from cameras             |
| `'wb'` | Write binary                             | Storing binary sensor data                  |

### Best Practice: Using Context Managers

Always use the `with` statement for file operations. It automatically handles file closing, even if exceptions occur:

```python
# Recommended approach
with open('sensor_data.txt', 'r') as file:
    data = file.read()
    # File is automatically closed after this block

# Not recommended (manual closing required)
file = open('sensor_data.txt', 'r')
data = file.read()
file.close()  # Must remember to close
```

## Reading Files in IoT Applications

### Reading Entire File Content

```python
# Read complete sensor log file
with open('temperature_log.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Reading Line by Line

Efficient for processing large sensor data files:

```python
# Process temperature readings line by line
with open('temperature_log.txt', 'r') as file:
    for line in file:
        temp = float(line.strip())
        if temp > 30:
            print(f"Alert: High temperature detected: {temp}°C")
```

### Reading All Lines into a List

```python
with open('sensor_readings.txt', 'r') as file:
    lines = file.readlines()  # Returns list of lines

# Process first 10 readings
for reading in lines[:10]:
    print(reading.strip())
```

### Reading Specific Number of Characters

```python
with open('data.txt', 'r') as file:
    chunk = file.read(100)  # Read first 100 characters
    print(chunk)
```

## Writing Files in IoT Applications

### Writing Sensor Data to Files

```python
# Log temperature reading
temperature = 25.4
with open('temperature_log.txt', 'w') as file:
    file.write(f"Temperature: {temperature}°C\n")
```

### Appending Data (Continuous Logging)

```python
import datetime

def log_sensor_reading(sensor_id, value):
    timestamp = datetime.datetime.now()
    with open('sensor_logs.txt', 'a') as file:
        file.write(f"{timestamp} | Sensor {sensor_id}: {value}\n")

# Example usage
log_sensor_reading("TEMP_01", 24.5)
log_sensor_reading("HUMID_01", 65.2)
```

### Writing Multiple Lines

```python
sensor_readings = [
    "2024-02-09 10:00:00, Temperature, 23.5\n",
    "2024-02-09 10:05:00, Temperature, 24.1\n",
    "2024-02-09 10:10:00, Temperature, 24.8\n"
]

with open('readings.txt', 'w') as file:
    file.writelines(sensor_readings)
```

## Working with CSV Files in IoT

CSV (Comma-Separated Values) files are commonly used for storing structured sensor data.

### Writing CSV Data

```python
import csv

# Log multiple sensor readings to CSV
sensor_data = [
    ['Timestamp', 'Sensor_ID', 'Temperature', 'Humidity'],
    ['2024-02-09 10:00', 'S001', 23.5, 65.2],
    ['2024-02-09 10:05', 'S001', 24.1, 64.8],
    ['2024-02-09 10:10', 'S002', 22.9, 66.1]
]

with open('sensor_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sensor_data)
```

### Reading CSV Data

```python
import csv

with open('sensor_data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header

    for row in reader:
        timestamp, sensor_id, temp, humidity = row
        print(f"Sensor {sensor_id}: Temp={temp}°C, Humidity={humidity}%")
```

### Using DictReader for Named Access

```python
import csv

with open('sensor_data.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        if float(row['Temperature']) > 25:
            print(f"High temperature alert: {row}")
```

## Working with JSON Files in IoT

JSON is the standard format for IoT data exchange and configuration files.

### Writing JSON Configuration

```python
import json

device_config = {
    "device_id": "IOT_SENSOR_001",
    "location": "Building A, Floor 2",
    "sampling_rate": 60,
    "thresholds": {
        "temperature": {"min": 15, "max": 30},
        "humidity": {"min": 40, "max": 70}
    },
    "enabled_sensors": ["temperature", "humidity", "pressure"]
}

with open('device_config.json', 'w') as file:
    json.dump(device_config, file, indent=4)
```

### Reading JSON Configuration

```python
import json

with open('device_config.json', 'r') as file:
    config = json.load(file)

print(f"Device ID: {config['device_id']}")
print(f"Sampling Rate: {config['sampling_rate']} seconds")
print(f"Max Temperature: {config['thresholds']['temperature']['max']}°C")
```

### Handling JSON Sensor Data

```python
import json
import datetime

def save_sensor_reading(sensor_id, readings):
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "sensor_id": sensor_id,
        "readings": readings
    }

    with open(f'{sensor_id}_data.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')  # Each reading on new line

# Example
save_sensor_reading("TEMP_01", {"temperature": 24.5, "humidity": 65.2})
```

## File Operations for IoT Use Cases

### Example 1: Data Buffering for Offline IoT Devices

```python
import json
from datetime import datetime

class DataBuffer:
    def __init__(self, buffer_file='data_buffer.json'):
        self.buffer_file = buffer_file

    def add_reading(self, sensor_data):
        """Add sensor reading to buffer when network is unavailable"""
        try:
            with open(self.buffer_file, 'r') as f:
                buffer = json.load(f)
        except FileNotFoundError:
            buffer = []

        buffer.append({
            'timestamp': datetime.now().isoformat(),
            'data': sensor_data
        })

        with open(self.buffer_file, 'w') as f:
            json.dump(buffer, f)

    def get_buffered_data(self):
        """Retrieve all buffered data for transmission"""
        try:
            with open(self.buffer_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def clear_buffer(self):
        """Clear buffer after successful transmission"""
        with open(self.buffer_file, 'w') as f:
            json.dump([], f)

# Usage
buffer = DataBuffer()
buffer.add_reading({"temperature": 23.5, "humidity": 65})
```

### Example 2: Configuration File Management

```python
import json

class IoTDeviceConfig:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return self.get_default_config()

    def get_default_config(self):
        """Return default configuration"""
        return {
            "sampling_interval": 60,
            "server_url": "http://iot.example.com",
            "enabled": True
        }

    def update_config(self, key, value):
        """Update specific configuration parameter"""
        self.config[key] = value
        self.save_config()

    def save_config(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)

# Usage
config = IoTDeviceConfig()
config.update_config("sampling_interval", 120)
```

### Example 3: Sensor Data Logging System

```python
import csv
from datetime import datetime

class SensorLogger:
    def __init__(self, log_file='sensor_log.csv'):
        self.log_file = log_file
        self.initialize_log()

    def initialize_log(self):
        """Create log file with headers if it doesn't exist"""
        try:
            with open(self.log_file, 'r'):
                pass  # File exists
        except FileNotFoundError:
            with open(self.log_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Timestamp', 'Sensor_ID', 'Value', 'Unit'])

    def log_reading(self, sensor_id, value, unit):
        """Append new sensor reading to log"""
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                sensor_id,
                value,
                unit
            ])

    def get_recent_readings(self, count=10):
        """Get most recent readings"""
        with open(self.log_file, 'r') as f:
            reader = csv.DictReader(f)
            all_readings = list(reader)
            return all_readings[-count:]

# Usage
logger = SensorLogger()
logger.log_reading("TEMP_01", 24.5, "Celsius")
logger.log_reading("HUMID_01", 65.2, "Percent")
```

## Exception Handling in File Operations

Always handle potential file operation errors:

```python
import json

def safe_read_config(filename):
    """Safely read configuration file with error handling"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file {filename} not found. Using defaults.")
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filename}. Using defaults.")
        return {}
    except PermissionError:
        print(f"Permission denied reading {filename}.")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
```

## File Management Best Practices for IoT

1. **Use Context Managers**: Always use `with` statement to ensure proper file closing
2. **Handle Exceptions**: Implement proper error handling for file operations
3. **Choose Appropriate Formats**: Use JSON for configuration, CSV for time-series data
4. **Implement Rotation**: Log rotation for long-running IoT devices to prevent disk full
5. **Validate Data**: Validate data before writing to files
6. **Use Absolute Paths**: Especially important in embedded systems
7. **Consider Storage Limits**: IoT devices often have limited storage; implement cleanup strategies
8. **Atomic Writes**: Write to temporary file then rename for critical data

### Further Reading

Refer to your prescribed textbook and official course materials.
