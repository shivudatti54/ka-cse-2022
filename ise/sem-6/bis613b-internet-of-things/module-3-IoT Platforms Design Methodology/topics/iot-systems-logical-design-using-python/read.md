# IoT Systems - Logical Design using Python


## Table of Contents

- [IoT Systems - Logical Design using Python](#iot-systems---logical-design-using-python)
- [Introduction](#introduction)
- [What is Logical Design in IoT?](#what-is-logical-design-in-iot)
- [Python's Role in IoT Logical Design](#pythons-role-in-iot-logical-design)
- [State Machines in IoT](#state-machines-in-iot)
  - [Basic State Machine Structure](#basic-state-machine-structure)
- [Example: Traffic Light System](#example-traffic-light-system)
  - [State Definitions](#state-definitions)
  - [Event-Driven Logic](#event-driven-logic)
- [Wait for timer expiration](#wait-for-timer-expiration)
- [Trigger state transition](#trigger-state-transition)
- [Check safety properties](#check-safety-properties)
- [Safety: light should always be in a valid state](#safety-light-should-always-be-in-a-valid-state)
  - [Temporal Logic Properties](#temporal-logic-properties)
- [Example: IoT Sensor Data Pipeline](#example-iot-sensor-data-pipeline)
  - [Data Flow Architecture](#data-flow-architecture)
- [Apply filters](#apply-filters)
- [Apply processors](#apply-processors)
- [Send to outputs](#send-to-outputs)
  - [Example Pipeline Usage](#example-pipeline-usage)
- [Create pipeline](#create-pipeline)
- [Add filters](#add-filters)
- [Add processors](#add-processors)
- [Add outputs](#add-outputs)
- [Simulate sending to cloud](#simulate-sending-to-cloud)
- [Process sensor reading](#process-sensor-reading)
- [Event-Driven Design Pattern](#event-driven-design-pattern)
- [Example: Smart Home System](#example-smart-home-system)
- [Design Patterns for IoT in Python](#design-patterns-for-iot-in-python)
  - [Observer Pattern](#observer-pattern)
- [Usage](#usage)
- [Best Practices for IoT Logical Design](#best-practices-for-iot-logical-design)
- [Verification and Validation](#verification-and-validation)
  - [Unit Testing Example](#unit-testing-example)
- [Conclusion](#conclusion)

## Introduction

Logical design in IoT systems focuses on defining the abstract functional components and their interactions, independent of hardware implementation. Python has emerged as a powerful language for IoT logical design due to its simplicity, extensive libraries, and ability to prototype complex systems quickly.

## What is Logical Design in IoT?

Logical design represents the abstract flow of data and control in an IoT system. It includes:

- **Data Flow Models**: How data moves from sensors to processing units to actuators
- **State Machines**: Defining system states and transitions
- **Event-Driven Architecture**: Responding to events like sensor readings or user inputs
- **Communication Protocols**: Abstract representation of message exchange patterns
- **Processing Logic**: Algorithms for data transformation and decision-making

## Python's Role in IoT Logical Design

Python offers several advantages for IoT logical design:

1. **Rapid Prototyping**: Quick iteration on system logic before hardware implementation
2. **Readability**: Clear syntax that maps well to design specifications
3. **Rich Libraries**: Extensive ecosystem for networking, data processing, and hardware interfacing
4. **Cross-Platform**: Same logic can run on various platforms (Raspberry Pi, PC, cloud servers)
5. **Simulation**: Test logical design without physical hardware

## State Machines in IoT

State machines are fundamental to IoT logical design. They model systems that exist in distinct states and transition based on events.

### Basic State Machine Structure

```python
class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name, handler):
        self.states[state_name] = handler

    def set_start(self, state_name):
        self.current_state = state_name

    def transition(self, event):
        if self.current_state in self.states:
            new_state = self.states[self.current_state](event)
            if new_state:
                self.current_state = new_state

    def get_state(self):
        return self.current_state
```

## Example: Traffic Light System

A traffic light is a classic example of a state-based IoT system. Let's design its logical structure:

### State Definitions

```python
import time

class TrafficLight:
    def __init__(self):
        self.states = ["red", "yellow", "green"]
        self.current_state = "red"
        self.cycle_times = {
            "red": 30,      # 30 seconds
            "yellow": 5,    # 5 seconds
            "green": 25     # 25 seconds
        }

    def get_state(self):
        return self.current_state

    def transition(self, event):
        """Handle state transitions based on events"""
        if event == "timer_expiration":
            if self.current_state == "red":
                self.current_state = "green"
            elif self.current_state == "green":
                self.current_state = "yellow"
            elif self.current_state == "yellow":
                self.current_state = "red"

    def get_cycle_time(self):
        """Return the duration for current state"""
        return self.cycle_times[self.current_state]
```

### Event-Driven Logic

```python
class TrafficController:
    def __init__(self):
        self.traffic_light = TrafficLight()

    def run(self):
        """Main event loop"""
        while True:
            state = self.traffic_light.get_state()
            duration = self.traffic_light.get_cycle_time()

            print(f"Light is {state.upper()}")

            # Wait for timer expiration
            time.sleep(duration)

            # Trigger state transition
            self.traffic_light.transition("timer_expiration")

            # Check safety properties
            if not self.check_safety():
                print("Safety violation detected!")
                break

    def check_safety(self):
        """Verify safety properties"""
        state = self.traffic_light.get_state()
        # Safety: light should always be in a valid state
        return state in ["red", "yellow", "green"]
```

### Temporal Logic Properties

```python
def safety_property(traffic_light):
    """
    Safety Property: The light should never skip a state
    (e.g., cannot go from red directly to yellow)
    """
    return traffic_light.get_state() in ["red", "yellow", "green"]

def liveness_property(traffic_light, history):
    """
    Liveness Property: All states should be visited eventually
    """
    return all(state in history for state in ["red", "yellow", "green"])
```

## Example: IoT Sensor Data Pipeline

Let's design a logical pipeline for processing sensor data:

### Data Flow Architecture

```python
class SensorDataPipeline:
    def __init__(self):
        self.filters = []
        self.processors = []
        self.outputs = []

    def add_filter(self, filter_func):
        """Add a data filter to the pipeline"""
        self.filters.append(filter_func)

    def add_processor(self, processor_func):
        """Add a data processor to the pipeline"""
        self.processors.append(processor_func)

    def add_output(self, output_func):
        """Add an output handler"""
        self.outputs.append(output_func)

    def process(self, data):
        """Process data through the pipeline"""
        # Apply filters
        for filter_func in self.filters:
            if not filter_func(data):
                return None  # Data filtered out

        # Apply processors
        processed_data = data
        for processor_func in self.processors:
            processed_data = processor_func(processed_data)

        # Send to outputs
        for output_func in self.outputs:
            output_func(processed_data)

        return processed_data
```

### Example Pipeline Usage

```python
# Create pipeline
pipeline = SensorDataPipeline()

# Add filters
def valid_temperature(data):
    """Filter out invalid temperature readings"""
    return -50 <= data['temperature'] <= 100

pipeline.add_filter(valid_temperature)

# Add processors
def convert_to_fahrenheit(data):
    """Convert celsius to fahrenheit"""
    data['temperature_f'] = (data['temperature'] * 9/5) + 32
    return data

def add_timestamp(data):
    """Add timestamp to data"""
    import datetime
    data['timestamp'] = datetime.datetime.now().isoformat()
    return data

pipeline.add_processor(convert_to_fahrenheit)
pipeline.add_processor(add_timestamp)

# Add outputs
def log_to_console(data):
    print(f"Temperature: {data['temperature']}°C ({data['temperature_f']}°F)")

def send_to_cloud(data):
    # Simulate sending to cloud
    print(f"Sending to cloud: {data}")

pipeline.add_output(log_to_console)
pipeline.add_output(send_to_cloud)

# Process sensor reading
sensor_reading = {'temperature': 25.5}
pipeline.process(sensor_reading)
```

## Event-Driven Design Pattern

Event-driven architecture is crucial for responsive IoT systems:

```python
class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        """Subscribe a listener to an event type"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def publish(self, event_type, data=None):
        """Publish an event to all listeners"""
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)

# Example: Smart Home System
class SmartHomeSystem:
    def __init__(self):
        self.event_manager = EventManager()
        self.setup_listeners()

    def setup_listeners(self):
        """Setup event listeners"""
        self.event_manager.subscribe('motion_detected', self.on_motion)
        self.event_manager.subscribe('temperature_high', self.on_high_temp)
        self.event_manager.subscribe('door_opened', self.on_door_open)

    def on_motion(self, data):
        print(f"Motion detected in {data['location']}")
        print("Turning on lights...")

    def on_high_temp(self, data):
        print(f"High temperature: {data['temperature']}°C")
        print("Activating air conditioning...")

    def on_door_open(self, data):
        print(f"Door opened: {data['door_id']}")
        print("Sending notification...")

    def simulate(self):
        """Simulate various events"""
        self.event_manager.publish('motion_detected',
                                   {'location': 'living room'})
        self.event_manager.publish('temperature_high',
                                   {'temperature': 30})
        self.event_manager.publish('door_opened',
                                   {'door_id': 'front_door'})
```

## Design Patterns for IoT in Python

### Observer Pattern

```python
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, data):
        for observer in self._observers:
            observer.update(data)

class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 0

    def set_temperature(self, temp):
        self.temperature = temp
        self.notify(temp)

class Display:
    def update(self, temperature):
        print(f"Display: Temperature is {temperature}°C")

class Logger:
    def update(self, temperature):
        print(f"Logger: Recording temperature {temperature}°C")

# Usage
sensor = TemperatureSensor()
display = Display()
logger = Logger()

sensor.attach(display)
sensor.attach(logger)

sensor.set_temperature(25.5)
```

## Best Practices for IoT Logical Design

1. **Separation of Concerns**: Keep sensing, processing, and actuation logic separate
2. **State Management**: Use clear state machines for systems with distinct states
3. **Error Handling**: Design for sensor failures and communication errors
4. **Modularity**: Create reusable components that can be composed
5. **Testing**: Write unit tests for logical components before hardware integration
6. **Documentation**: Document state transitions and event flows clearly

## Verification and Validation

### Unit Testing Example

```python
import unittest

class TestTrafficLight(unittest.TestCase):
    def setUp(self):
        self.traffic_light = TrafficLight()

    def test_initial_state(self):
        self.assertEqual(self.traffic_light.get_state(), "red")

    def test_red_to_green_transition(self):
        self.traffic_light.transition("timer_expiration")
        self.assertEqual(self.traffic_light.get_state(), "green")

    def test_complete_cycle(self):
        states = []
        for _ in range(3):
            states.append(self.traffic_light.get_state())
            self.traffic_light.transition("timer_expiration")
        self.assertEqual(states, ["red", "green", "yellow"])

if __name__ == '__main__':
    unittest.main()
```

## Conclusion

Logical design using Python provides a powerful framework for developing IoT systems. By focusing on abstract data flows, state machines, and event-driven patterns, developers can create robust, maintainable IoT applications that are easy to test and validate before hardware deployment. Python's expressiveness and extensive library ecosystem make it an ideal choice for rapid prototyping and implementation of IoT logical designs.
