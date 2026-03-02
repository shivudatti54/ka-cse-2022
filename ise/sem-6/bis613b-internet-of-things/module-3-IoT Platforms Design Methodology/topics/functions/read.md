# Functions in Python for IoT Development


## Table of Contents

- [Functions in Python for IoT Development](#functions-in-python-for-iot-development)
- [Introduction](#introduction)
- [Key Concepts in Python Functions](#key-concepts-in-python-functions)
  - [1. Function Definition Syntax](#1-function-definition-syntax)
- [Function body](#function-body)
  - [2. Parameter Types](#2-parameter-types)
  - [3. Return Values](#3-return-values)
  - [4. Scope of Variables](#4-scope-of-variables)
  - [5. Recursive Functions](#5-recursive-functions)
  - [6. Lambda Functions](#6-lambda-functions)
- [IoT data filtering](#iot-data-filtering)
  - [7. Function Best Practices for IoT](#7-function-best-practices-for-iot)
- [IoT Function Examples](#iot-function-examples)
  - [Example 1: Sensor Data Aggregation](#example-1-sensor-data-aggregation)
- [Usage](#usage)
  - [Example 2: Threshold Alert System](#example-2-threshold-alert-system)
- [Configuration](#configuration)
- [Execution](#execution)
  - [Example 3: Data Conversion Function](#example-3-data-conversion-function)
- [Usage in IoT system](#usage-in-iot-system)
- [Function Flow in IoT Systems](#function-flow-in-iot-systems)
- [Exam Tips for IoT Exams](#exam-tips-for-iot-exams)

## Introduction

In Python programming for IoT systems, functions serve as fundamental building blocks for creating modular, reusable, and maintainable code. A function is a self-contained block of code that performs a specific task, which becomes crucial in IoT applications where operations like sensor data collection, data processing, and device control need to be executed repeatedly.

Functions enable IoT developers to:

1. Encapsulate complex operations (e.g., sensor calibration)
2. Reduce code duplication
3. Improve system reliability through modular testing
4. Create reusable libraries for common IoT tasks

In weather monitoring systems (a key case study), functions might handle:

- Temperature conversion
- Humidity validation
- Data packet formatting
- Alert threshold checks

```python
def read_temperature(sensor):
    """Read temperature from IoT sensor"""
    raw_data = sensor.read()
    return convert_celsius(raw_data)
```

## Key Concepts in Python Functions

### 1. Function Definition Syntax

```python
def function_name(parameters):
    """Docstring explaining function"""
    # Function body
    return [expression]
```

- `def`: Keyword to declare function
- Parameters: Input variables (positional or keyword)
- Docstring: Documentation string (triple-quoted)
- Return: Optional value to send back

### 2. Parameter Types

#### a. Positional Arguments

```python
def sensor_alert(sensor_type, threshold):
    print(f"Monitoring {sensor_type} above {threshold}°C")

sensor_alert("DHT22", 35)  # Order matters
```

#### b. Keyword Arguments

```python
sensor_alert(threshold=40, sensor_type="BME680")
```

#### c. Default Parameters

```python
def process_data(sensor, precision=2):
    return round(sensor.read(), precision)
```

#### d. Variable-Length Arguments

```python
def average_reading(*readings):
    return sum(readings)/len(readings)
```

### 3. Return Values

- Can return multiple values using tuples
- `return None` if no value specified

```python
def get_sensor_data():
    temp = 25.6
    humidity = 72.4
    return temp, humidity  # Returns tuple (25.6, 72.4)
```

### 4. Scope of Variables

- **Local**: Variables inside function
- **Global**: Declared with `global` keyword

```python
MAX_TEMP = 50  # Global constant

def check_overheating(current_temp):
    global alert_count  # Modify global variable
    if current_temp > MAX_TEMP:
        alert_count += 1
        return True
    return False
```

### 5. Recursive Functions

```python
def binary_search(sensor_data, target, low=0, high=None):
    """Search sorted sensor data recursively"""
    high = high or len(sensor_data)-1
    if low > high:
        return -1
    mid = (low + high) // 2
    if sensor_data[mid] == target:
        return mid
    elif sensor_data[mid] < target:
        return binary_search(sensor_data, target, mid+1, high)
    else:
        return binary_search(sensor_data, target, low, mid-1)
```

### 6. Lambda Functions

Anonymous functions for quick operations:

```python
# IoT data filtering
is_valid = lambda reading: 0 <= reading <= 100
filtered_data = list(filter(is_valid, raw_sensor_data))
```

### 7. Function Best Practices for IoT

1. Single Responsibility Principle: One function per task
2. Type hints for better maintainability

```python
def calibrate_sensor(raw_value: float) -> float:
    return raw_value * 1.05 + 0.2
```

3. Comprehensive error handling

```python
def safe_sensor_read(sensor):
    try:
        return sensor.read()
    except SensorError as e:
        log_error(e)
        return None
```

## IoT Function Examples

### Example 1: Sensor Data Aggregation

```python
def aggregate_sensor_data(sensors, interval=60):
    """Collect data from multiple sensors"""
    readings = {}
    for sensor in sensors:
        try:
            readings[sensor.id] = {
                'temp': sensor.read_temp(),
                'humidity': sensor.read_humidity(),
                'timestamp': time.time()
            }
        except SensorOfflineError:
            continue
    return readings

# Usage
weather_sensors = [sensor1, sensor2, sensor3]
weather_data = aggregate_sensor_data(weather_sensors)
```

### Example 2: Threshold Alert System

```python
def check_thresholds(sensor_data, thresholds):
    """Return dictionary of threshold breaches"""
    alerts = {}
    for sensor_id, data in sensor_data.items():
        if data['temp'] > thresholds['max_temp']:
            alerts[sensor_id] = 'OVERHEATING'
        if data['humidity'] < thresholds['min_humidity']:
            alerts[sensor_id] = 'LOW_HUMIDITY'
    return alerts

# Configuration
SAFE_THRESHOLDS = {'max_temp': 40, 'min_humidity': 30}

# Execution
current_alerts = check_thresholds(weather_data, SAFE_THRESHOLDS)
```

### Example 3: Data Conversion Function

```python
def convert_units(data, target_unit='C'):
    """Convert temperature between Celsius/Fahrenheit"""
    if target_unit == 'C':
        return (data - 32) * 5/9
    elif target_unit == 'F':
        return (data * 9/5) + 32
    else:
        raise ValueError("Invalid unit. Use 'C' or 'F'")

# Usage in IoT system
fahrenheit_readings = [convert_units(c, 'F') for c in celsius_data]
```

## Function Flow in IoT Systems

```
IoT Device Operation Flow:
[Sensor Hardware] --> read_sensor() --> [Raw Data]
                   |
                   v
[Raw Data] --> preprocess_data() --> [Clean Data]
                   |
                   v
[Clean Data] --> analyze_data() --> [Insights]
                   |
                   v
[Insights] --> trigger_actions() --> [Actuators/Cloud]
```

Key components:

1. **Sensor Interface Functions**: Direct hardware interaction
2. **Data Processing Functions**: Filtering and transformation
3. **Analytics Functions**: Pattern recognition and alerts
4. **Communication Functions**: MQTT/HTTP data transmission

## Exam Tips for IoT Exams

1. **Function Definition Syntax**
   - Always include colon `:` after parameter list
   - Indentation (4 spaces) is mandatory for function body
   - Example: 2 marks question on correcting function syntax

2. **Parameter Types**
   - Remember order: positional, \*args, keyword, \*\*kwargs
   - Default parameters must follow non-default parameters
   - Common question: Predict output of nested function calls

3. **Return Values**
   - `return` without value → returns `None`
   - Multiple returns via tuples: `return a, b`
   - Practice questions on function return value tracing

4. **Lambda Functions**
   - Syntax: `lambda args: expression`
   - Used with `map()`, `filter()`, and `sort()`
   - Expect 3-4 marks question on converting regular function to lambda

5. **Scope Resolution**
   - LEGB Rule: Local → Enclosing → Global → Built-in
   - `global` vs `nonlocal` keywords
   - Diagram-based questions on variable scope

6. **IoT Application Questions**
   - Write functions for sensor data processing
   - Implement alert systems with threshold checks
   - Create data conversion utilities

7. **Common Mistakes**
   - Forgetting return statement in value-returning functions
   - Modifying mutable default arguments (e.g., `def func(a=[])`)
   - Confusing function parameters with global variables

8. **Optimization Tips**
   - Use type hints for better code clarity
   - Include docstrings for full marks in documentation
   - Show error handling in IoT functions (try/except blocks)
