# Python Data Types and Data Structures

## Introduction

Python, as a high-level, interpreted programming language, provides a rich set of built-in data types and data structures that form the foundation for developing IoT applications. In the context of the Internet of Things, where devices generate and process vast amounts of sensor data, actuator commands, and configuration parameters, understanding Python's data types becomes essential for efficient data handling, storage, and transmission. This topic examines Python's fundamental data types—numeric, string, boolean—and composite data structures including lists, tuples, dictionaries, and sets, with particular emphasis on their applications in IoT scenarios such as sensor data buffering, device configuration management, and telemetry parsing.

The selection of appropriate data structures in IoT applications directly impacts memory consumption, processing latency, and network efficiency. Python's dynamic typing and built-in data structures provide flexibility but require careful consideration when designing systems for resource-constrained embedded devices or high-throughput data aggregation platforms. This chapter provides a comprehensive analysis of each data type, their properties (mutability, ordering), internal implementations, and practical examples relevant to IoT system development.

## Key Concepts

### Primitive Data Types

Python's primitive data types represent the most fundamental units of data in any Python program. These include integers (`int`), floating-point numbers (`float`), strings (`str`), and boolean values (`bool`). Each type has distinct characteristics regarding memory allocation, precision, and applicable operations.

**Integer Type (int):** Integers in Python represent whole numbers without any fractional component. In IoT applications, integers are extensively used for sensor readings that represent discrete quantities—temperature readings in Celsius (e.g., 25), humidity percentages (e.g., 60), or device counts. Python integers have arbitrary precision, meaning they can represent numbers of any size limited only by available memory. However, for embedded IoT devices, this flexibility may introduce unnecessary memory overhead. The `sys.getsizeof()` function reveals that a simple integer in CPython occupies at least 28 bytes, prompting developers to consider more compact representations when processing large volumes of sensor data.

```python
# IoT Example: Processing temperature sensor data
temperature_reading = 23 # Integer representing temperature in Celsius
humidity_percentage = 65 # Integer representing humidity percentage
packet_count = 1024 # Total packets received
```

**Floating-Point Type (float):** Floating-point numbers represent real numbers with decimal precision. They are essential for IoT applications requiring fractional measurements such as voltage levels (e.g., 3.3V), GPS coordinates (e.g., 40.7128° N), or pressure readings (e.g., 1013.25 hPa). Python floats follow the IEEE 754 double-precision standard, providing approximately 15-17 decimal digits of precision. When working with sensor data that requires high precision, developers must be aware of floating-point arithmetic limitations and potential rounding errors in cumulative calculations.

```python
# IoT Example: GPS coordinates and voltage readings
latitude = 40.7128
longitude = -74.0060
voltage = 3.3 # Operating voltage for Raspberry Pi GPIO
current_draw = 0.125 # Current draw in amperes
```

**String Type (str):** Strings in Python are immutable sequences of Unicode characters, denoted by single quotes, double quotes, or triple quotes. In IoT contexts, strings are ubiquitous for device identifiers, JSON payloads, MAC addresses, and status messages. The immutability of strings ensures thread safety and allows Python's string interning optimization to conserve memory when identical strings are used repeatedly. For IoT applications involving network communication, string encoding (UTF-8) becomes critical for proper interpretation of data across different device platforms.

```python
# IoT Example: Device identification and messaging
device_id = "SENSOR-001"
mac_address = "B8:27:EB:5C:8A:2D"
json_payload = '{"temperature": 25, "humidity": 60}'
status_message = "Device connected successfully"
```

**Boolean Type (bool):** Boolean values represent truth values (`True` and `False`) and are fundamental for conditional logic in IoT applications. Booleans are frequently used for device state monitoring (e.g., is the motion sensor triggered?), feature flags for configuration, and return values from validation functions. In Python, booleans are subclasses of integers, with `True` equivalent to 1 and `False` equivalent to 0, which enables arithmetic operations but requires careful attention in conditional contexts.

```python
# IoT Example: Device state monitoring
motion_detected = True
device_online = False
threshold_exceeded = (temperature_reading > 30)
```

### Composite Data Structures

**Lists:** Lists are mutable, ordered sequences that can hold elements of different types. They support zero-based indexing, negative indexing, slicing, and various methods for manipulation. In IoT applications, lists serve as the primary data structure for storing time-series sensor readings, managing device queues, and implementing circular buffers for streaming data. The dynamic array implementation provides O(1) indexed access but O(n) insertion and deletion at arbitrary positions.

```python
# IoT Example: Sensor data buffer
temperature_readings = [22, 23, 24, 23, 25, 26]
temperature_readings.append(27) # Add new reading
average_temp = sum(temperature_readings) / len(temperature_readings)
```

**Tuples:** Tuples are immutable, ordered sequences that differ from lists in their immutability property. This immutability makes tuples suitable for representing fixed collections such as coordinate pairs (latitude, longitude), device configuration parameters, and database records. The immutability guarantee ensures data integrity and allows tuples to be used as dictionary keys—a capability unavailable with lists. In IoT applications, tuples frequently appear in function return values and when parsing structured data formats.

```python
# IoT Example: GPS coordinate and device configuration
gps_coordinates = (40.7128, -74.0060) # (latitude, longitude)
device_config = ("192.168.1.100", 8883, "device_topic", 60) # (host, port, topic, timeout)
```

**Dictionaries:** Dictionaries are mutable, unordered collections of key-value pairs, implemented as hash tables providing O(1) average-case lookup, insertion, and deletion. In IoT contexts, dictionaries are indispensable for representing device metadata, JSON parsing results, and configuration mappings. The flexibility of dictionary keys (requiring hashable types) and values (any Python object) enables complex nested structures for representing device hierarchies and sensor networks.

```python
# IoT Example: Device metadata and telemetry
device_metadata = {
 "device_id": "SENSOR-001",
 "type": "temperature_humidity",
 "location": "Building-A-Floor-2",
 "battery_level": 85
}

telemetry = {
 "temperature": 25.5,
 "humidity": 60,
 "timestamp": "2024-01-15T10:30:00Z"
}
```

**Sets:** Sets are unordered collections of unique hashable elements, implemented using hash tables without storing values. They provide O(1) membership testing, making them ideal for tracking unique device identifiers, detecting duplicate sensor readings, and performing set operations (union, intersection, difference) on groups of devices or data points. The mutable nature of sets allows addition and removal of elements, though elements themselves must be immutable.

```python
# IoT Example: Unique device tracking and duplicate detection
active_device_ids = {"device_001", "device_002", "device_003"}
new_device_id = "device_004"

# Add new device
active_device_ids.add(new_device_id)

# Check if device has been seen
if new_device_id not in active_device_ids:
 active_device_ids.add(new_device_id)
```

### Mutability and Memory Implications

The distinction between mutable and immutable data types has significant implications for IoT application design. Mutable objects (lists, dictionaries, sets) can be modified in place, while immutable objects (integers, floats, strings, tuples) cannot be modified after creation. This distinction affects memory management, as immutable objects may be subject to string interning and integer caching, while mutable objects require careful reference management to avoid unintended side effects.

In resource-constrained IoT environments, understanding mutability helps developers choose appropriate data structures. For instance, using tuples instead of lists for configuration data ensures that parameters remain constant throughout the application lifecycle, preventing accidental modification and enabling certain optimization opportunities.

### Specialized Data Structures for IoT

**Circular Buffers (Ring Buffers):** For continuous sensor data streaming applications, circular buffers provide efficient fixed-size storage that overwrites oldest data when full. While Python's built-in collections do not include a native circular buffer, the `collections.deque` class provides O(1) append and pop operations from both ends, making it suitable for implementing ring buffer behavior.

```python
from collections import deque
import time

class SensorBuffer:
 def __init__(self, max_size=100):
 self.buffer = deque(maxlen=max_size)

 def add_reading(self, value, timestamp=None):
 if timestamp is None:
 timestamp = time.time()
 self.buffer.append((timestamp, value))

 def get_recent(self, n=10):
 return list(self.buffer)[-n:]

# Usage for streaming temperature data
temp_buffer = SensorBuffer(max_size=60) # Store 1 minute of readings at 1Hz
```

**Byte Arrays and Struct Module:** IoT devices frequently transmit binary data representing sensor readings, timestamps, or compressed information. The `bytearray` type provides mutable byte sequences suitable for constructing network packets, while the `struct` module enables packing and unpacking binary data according to specified format strings—essential for parsing protocols like MQTT or custom serial communications.

```python
import struct

# Pack sensor data into binary format
sensor_id = 1
temperature = 23.5
humidity = 60

# Format: uint8, float, uint8 (total 10 bytes)
binary_data = struct.pack('!B f B', sensor_id, temperature, humidity)

# Unpack received binary data
unpacked = struct.unpack('!B f B', binary_data)
device_id, temp, hum = unpacked
print(f"Device {device_id}: {temp}°C, {humidity}%")
```

**JSON Processing:** JavaScript Object Notation (JSON) remains the predominant data interchange format in IoT applications. Python's built-in `json` module provides `json.dumps()` and `json.loads()` functions for serialization and deserialization, enabling seamless integration between IoT devices and cloud platforms.

```python
import json

# Serialize IoT telemetry to JSON
telemetry_data = {
 "device_id": "SENSOR-001",
 "readings": [
 {"type": "temperature", "value": 25.5, "unit": "C"},
 {"type": "humidity", "value": 60, "unit": "%"}
 ],
 "timestamp": "2024-01-15T10:30:00Z"
}

json_string = json.dumps(telemetry_data)
# Result: '{"device_id": "SENSOR-001", "readings": [...], "timestamp": "..."}'

# Deserialize JSON from IoT device
received_json = '{"status": "ok", "battery": 85}'
data = json.loads(received_json)
print(f"Battery level: {data['battery']}%")
```

## Examples

### Example 1: Temperature Monitoring System

Consider a weather monitoring IoT system that collects temperature readings from multiple sensors. The system must store recent readings, compute statistics, and detect anomalies.

```python
from collections import deque
import statistics

class TemperatureMonitor:
 def __init__(self, sensor_id, buffer_size=10, threshold=30.0):
 self.sensor_id = sensor_id
 self.buffer = deque(maxlen=buffer_size)
 self.threshold = threshold

 def add_reading(self, temperature):
 """Add a new temperature reading to the buffer."""
 self.buffer.append(temperature)

 # Check for threshold exceedance
 if temperature > self.threshold:
 return {"alert": "high_temperature", "value": temperature}
 return None

 def get_statistics(self):
 """Calculate statistics for buffered readings."""
 if not self.buffer:
 return None

 readings = list(self.buffer)
 return {
 "current": readings[-1],
 "average": statistics.mean(readings),
 "max": max(readings),
 "min": min(readings),
 "std_dev": statistics.stdev(readings) if len(readings) > 1 else 0
 }

# Demonstration
monitor = TemperatureMonitor(sensor_id="TEMP-001", buffer_size=5, threshold=28.0)

readings = [22.5, 23.0, 24.5, 27.0, 29.5, 31.0, 28.0]
for temp in readings:
 alert = monitor.add_reading(temp)
 if alert:
 print(f"ALERT from {monitor.sensor_id}: {alert}")

stats = monitor.get_statistics()
print(f"Statistics: Current={stats['current']}°C, Avg={stats['average']:.2f}°C")
# Output: ALERT from TEMP-001: {'alert': 'high_temperature', 'value': 31.0}
# Output: Statistics: Current=28.0°C, Avg=26.5°C
```

### Example 2: Device Configuration Management

This example demonstrates the use of dictionaries and nested data structures for managing heterogeneous IoT device configurations.

```python
# Device configuration registry
device_configs = {
 "sensor_001": {
 "type": "temperature",
 "location": "living_room",
 "calibration": {
 "offset": -0.5,
 "scale": 1.02
 },
 "reporting": {
 "interval": 60, # seconds
 "format": "json"
 }
 },
 "sensor_002": {
 "type": "motion",
 "location": "entrance",
 "calibration": {
 "sensitivity": "high"
 },
 "reporting": {
 "interval": 10,
 "format": "json"
 }
 }
}

def update_reporting_interval(device_id, new_interval):
 """Update the reporting interval for a specific device."""
 if device_id in device_configs:
 device_configs[device_id]["reporting"]["interval"] = new_interval
 return True
 return False

def get_devices_by_location(location):
 """Retrieve all devices at a specific location."""
 return [
 {"id": dev_id, "type": config["type"]}
 for dev_id, config in device_configs.items()
 if config.get("location") == location
 ]

# Update interval
update_reporting_interval("sensor_001", 30)

# Query devices
living_room_devices = get_devices_by_location("living_room")
print(f"Living room devices: {living_room_devices}")
# Output: Living room devices: [{'id': 'sensor_001', 'type': 'temperature'}]
```

### Example 3: Binary Sensor Data Processing

This example illustrates parsing binary data from a custom sensor protocol using the `struct` module.

```python
import struct
import datetime

# Define the binary protocol format
# Header (4 bytes): Magic number (0xAA), message type, payload length, checksum
# Payload: Device ID (2 bytes), Temperature (float), Humidity (uint8), Status (uint8)
FORMAT_HEADER = '>BBHB' # Big-endian: uint8, uint8, uint16, uint8
FORMAT_PAYLOAD = '>HfBB' # Device ID (uint16), Temperature (float), Humidity (uint8), Status (uint8)

def parse_sensor_packet(packet_bytes):
 """Parse a binary sensor packet and return structured data."""
 # Parse header
 magic, msg_type, payload_len, checksum = struct.unpack(FORMAT_HEADER, packet_bytes[:6])

 # Validate magic number
 if magic != 0xAA:
 raise ValueError(f"Invalid magic number: {hex(magic)}")

 # Parse payload
 device_id, temperature, humidity, status = struct.unpack(
 FORMAT_PAYLOAD, packet_bytes[6:6+struct.calcsize(FORMAT_PAYLOAD)]
 )

 return {
 "message_type": msg_type,
 "device_id": device_id,
 "temperature": temperature,
 "humidity": humidity,
 "status": status,
 "timestamp": datetime.datetime.now().isoformat()
 }

# Simulate received binary packet
# Header: 0xAA, 0x01, 0x08, 0x2D
# Payload: 0x0001, 23.5, 60, 0x01
header = struct.pack(FORMAT_HEADER, 0xAA, 1, 8, 0x2D)
payload = struct.pack(FORMAT_PAYLOAD, 1, 23.5, 60, 1)
packet = header + payload

# Parse the packet
data = parse_sensor_packet(packet)
print(f"Parsed data: {data}")
# Output: Parsed data: {'message_type': 1, 'device_id': 1, 'temperature': 23.5, 'humidity': 60, 'status': 1, 'timestamp': '...'}
```

## Exam Tips

1. **Understand Mutability Implications:** Be clear about which data types are mutable (list, dict, set, bytearray) and which are immutable (int, float, str, tuple, bool). This affects their use as dictionary keys, function parameter behavior, and memory management in IoT applications.

2. **Choose Appropriate Data Structures:** For IoT sensor data streaming, prefer `deque` with maxlen for O(1) buffer management. For device configuration, use nested dictionaries. For unique device tracking, use sets. Selection impacts both performance and code clarity.

3. **Memory Considerations in IoT:** Remember that Python integers require approximately 28 bytes minimum. For large-scale sensor deployments, consider using array module or numpy for numeric storage to reduce memory footprint.

4. **Binary Protocol Handling:** The `struct` module is essential for parsing binary IoT protocols. Understand format strings (>, <, B, H, f, etc.) for packing and unpacking network data.

5. **JSON vs. Binary:** JSON offers human readability and easy debugging but introduces overhead. Binary formats (using struct) are more efficient for bandwidth-constrained IoT devices.

6. **Time Complexity Awareness:** Dictionary lookups are O(1), list indexing is O(1), but list searching is O(n). For frequent membership testing in IoT device networks, prefer sets over lists.

7. **Data Structure Combinations:** IoT applications frequently combine data structures—for example, a dictionary of lists for time-series data per device, or a list of dictionaries for heterogeneous sensor readings.
