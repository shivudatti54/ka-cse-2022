# Linux on Raspberry Pi for IoT Applications

## Introduction

The Raspberry Pi, a series of ARM-based single-board computers, has emerged as a foundational platform for Internet of Things (IoT) development. The Linux operating system, particularly Raspberry Pi OS (formerly Raspbian), serves as the software backbone for approximately 70% of production IoT deployments utilizing Raspberry Pi hardware. This chapter examines the Linux kernel architecture, system-level programming interfaces, and deployment strategies essential for building robust IoT solutions on embedded platforms.

## Linux Kernel Architecture for Embedded Systems

### Kernel Subsystems Relevant to IoT

The Linux kernel comprises several interconnected subsystems that directly impact IoT application performance on resource-constrained devices:

**Process Scheduler (CFS - Completely Fair Scheduler)**: The Linux kernel employs the CFS algorithm, implementing fair CPU time distribution among processes. For IoT applications executing concurrent sensor data acquisition tasks, understanding scheduler latency is critical. The scheduler maintains a red-black tree of runnable processes, achieving O(log n) complexity for process selection.

**Memory Management**: Raspberry Pi devices typically feature 2-8GB RAM, necessitating efficient memory utilization. The kernel's page allocator and SLUB allocator manage memory pages and small objects respectively. IoT applications must consider memory pressure when buffering sensor data streams.

**Device Driver Framework**: Linux provides unified interfaces for hardware access through:

- **Character devices**: Used for GPIO, serial communication, and sensors
- **Block devices**: SD cards, USB storage
- **Network devices**: Ethernet, WiFi adapters

### Real-Time Considerations for IoT

Standard Linux kernels exhibit interrupt latency ranging from microseconds to milliseconds, which may be inadequate for time-critical IoT applications. The PREEMPT_RT patch set transforms Linux into a real-time operating system by:

1. Converting interrupt handlers into kernel threads
2. Implementing priority inheritance for mutexes
3. Reducing worst-case latency to single-digit microseconds

```bash
# Check current kernel preempt configuration
zcat /proc/config.gz | grep CONFIG_PREEMPT
```

## Systemd Service Management for IoT Daemons

### Creating IoT Application Services

Systemd provides robust service management essential for production IoT deployments. A well-designed systemd unit file ensures automatic restart on failure, proper dependency ordering, and controlled startup sequences.

**Example: Sensor Data Collection Service**

```ini
[Unit]
Description=IoT Temperature Sensor Daemon
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/local/bin/sensor_collector.py
Restart=on-failure
RestartSec=5
User=pi
Environment=PYTHONPATH=/opt/sensors/lib

# Hardening for IoT security
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadOnlyPaths=/boot

[Install]
WantedBy=multi-user.target
```

**Service Management Commands**:

```bash
# Reload systemd after unit file modification
sudo systemctl daemon-reload

# Enable service to start at boot
sudo systemctl enable sensor_collector

# View real-time logs for debugging
journalctl -u sensor_collector -f

# Analyze service failure
systemctl status sensor_collector
journalctl -u sensor_collector -n 50 --no-pager
```

## Shell Scripting for IoT Automation

### Sensor Data Aggregation Scripts

Shell scripting provides efficient automation for IoT data collection, preprocessing, and transmission pipelines.

```bash
#!/bin/bash
# sensor_aggregator.sh - Collect and aggregate sensor data

SENSOR_ID="TEMP_001"
COLLECTION_INTERVAL=60
DATA_DIR="/var/log/sensor_data"
API_ENDPOINT="https://iot.example.com/api/v1/data"

# Create timestamped log entry
log_data() {
 local timestamp=$(date +%Y-%m-%dT%H:%M:%SZ)
 local temp=$(python3 /opt/sensors/read_temp.py)
 local humidity=$(python3 /opt/sensors/read_humidity.py)

 # Validate sensor readings
 if [[ -z "$temp" ]] || [[ ! "$temp" =~ ^-?[0-9]+\.?[0-9]*$ ]]; then
 logger -t sensor_aggregator "Invalid temperature reading: $temp"
 return 1
 fi

 # Write to local buffer
 echo "$timestamp,$SENSOR_ID,$temp,$humidity" >> "$DATA_DIR/buffer.csv"
}

# Main collection loop
while true; do
 log_data

 # Rotate buffer if exceeding size threshold
 if [[ $(stat -f%z "$DATA_DIR/buffer.csv" 2>/dev/null || stat -c%s "$DATA_DIR/buffer.csv") -gt 10485760 ]]; then
 mv "$DATA_DIR/buffer.csv" "$DATA_DIR/buffer_$(date +%Y%m%d_%H%M%S).csv"
 gzip "$DATA_DIR/buffer_"*.csv &
 fi

 sleep $COLLECTION_INTERVAL
done
```

### Cron Jobs for Periodic IoT Tasks

```bash
# Edit crontab for scheduled tasks
crontab -e

# Example entries for IoT maintenance:
# Collect sensor data every minute
* * * * * /usr/local/bin/sensor_aggregator.sh >> /var/log/sensor_collect.log 2>&1

# Daily system maintenance at 3 AM
0 3 * * * sudo apt update && sudo apt upgrade -y >> /var/log/apt_upgrade.log 2>&1

# Hourly network connectivity check
0 * * * * ping -c 3 8.8.8.8 || /usr/local/bin/net_restart.sh
```

## GPIO Programming via Linux Interfaces

### Accessing GPIO Through sysfs

The Linux filesystem interface (sysfs) provides standardized GPIO access without requiring kernel module development:

```bash
# Export GPIO pin (BCM numbering)
echo "17" | sudo tee /sys/class/gpio/export

# Configure as output
echo "out" | sudo tee /sys/class/gpio/gpio17/direction

# Write output value (1 = HIGH, 0 = LOW)
echo "1" | sudo tee /sys/class/gpio/gpio17/value

# Configure as input
echo "in" | sudo tee /sys/class/gpio/gpio17/direction

# Read input value
cat /sys/class/gpio/gpio17/value
```

### Python Interface for GPIO Operations

```python
#!/usr/bin/env python3
# gpio_controller.py - GPIO control for IoT actuators

import RPi.GPIO as GPIO
import time
import threading
from collections import deque

class ActuatorController:
 def __init__(self, pin_config):
 GPIO.setmode(GPIO.BCM)
 self.pins = pin_config
 self.state = {pin: False for pin in pin_config.values()}
 self.command_queue = deque()

 for name, pin in pin_config.items():
 GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

 def set_actuator(self, name, state):
 """Thread-safe actuator control"""
 if name not in self.pins:
 raise ValueError(f"Unknown actuator: {name}")

 pin = self.pins[name]
 GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)
 self.state[name] = state

 def emergency_shutdown(self):
 """Kill all actuators on critical error"""
 for pin in self.pins.values():
 GPIO.output(pin, GPIO.LOW)
 self.state = {name: False for name in self.state}

# Usage example
controller = ActuatorController({
 'pump': 17,
 'valve': 27,
 'fan': 22
})
controller.set_actuator('pump', True)
```

## Network Configuration for IoT Deployments

### Static IP Configuration via systemd-networkd

For reliable IoT connectivity, static IP addressing eliminates DHCP dependency:

```bash
# /etc/systemd/network/05-eth0.network
[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8 8.8.4.4
```

### Firewall Configuration for IoT Security

```bash
# Configure iptables for IoT device
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -s 192.168.1.0/24 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 8883 -j ACCEPT # MQTT over TLS
sudo iptables -A INPUT -j DROP

# Persist rules
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

## IoT Project: Environmental Monitoring System

### System Architecture

A complete Linux-based IoT solution comprises multiple integrated components:

1. **Sensor Layer**: Temperature, humidity, and pressure sensors accessed via I2C/SPI
2. **Processing Layer**: Python applications processing raw data
3. **Storage Layer**: SQLite database for local buffering
4. **Communication Layer**: MQTT client publishing to cloud broker

### Implementation

```python
#!/usr/bin/env python3
# environment_monitor.py - Complete IoT monitoring system

import sqlite3
import paho.mqtt.client as mqtt
import json
import logging
from datetime import datetime
from threading import Thread, Event
import bme680

class EnvironmentalMonitor:
 def __init__(self, db_path, mqtt_config):
 self.db_path = db_path
 self.mqtt_config = mqtt_config
 self.stop_event = Event()
 self.init_database()
 self.setup_mqtt()
 self.setup_sensor()

 def init_database(self):
 """Initialize SQLite schema for sensor data"""
 with sqlite3.connect(self.db_path) as conn:
 conn.execute('''
 CREATE TABLE IF NOT EXISTS readings (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 timestamp TEXT NOT NULL,
 temperature REAL,
 humidity REAL,
 pressure REAL,
 gas_resistance REAL
 )
 ''')
 conn.execute('''
 CREATE INDEX idx_timestamp ON readings(timestamp)
 ''')

 def setup_sensor(self):
 """Initialize BME680 environmental sensor"""
 try:
 self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
 self.sensor.set_temperature_oversample(bme680.OS_8X)
 self.sensor.set_humidity_oversample(bme680.OS_2X)
 self.sensor.set_pressure_oversample(bme680.OS_4X)
 self.sensor.set_gas_heater_temperature(320)
 self.sensor.set_gas_heater_duration(150)
 self.sensor.select_gas()
 except Exception as e:
 logging.error(f"Sensor initialization failed: {e}")
 self.sensor = None

 def read_sensor(self):
 """Read all environmental parameters"""
 if not self.sensor or not self.sensor.get_sensor_data():
 return None

 return {
 'temperature': self.sensor.data.temperature,
 'humidity': self.sensor.data.humidity,
 'pressure': self.sensor.data.pressure,
 'gas_resistance': self.sensor.data.gas_resistance
 }

 def store_reading(self, data):
 """Persist reading to local database"""
 timestamp = datetime.utcnow().isoformat() + 'Z'
 with sqlite3.connect(self.db_path) as conn:
 conn.execute(
 'INSERT INTO readings (timestamp, temperature, humidity, pressure, gas_resistance) VALUES (?, ?, ?, ?, ?)',
 (timestamp, data['temperature'], data['humidity'],
 data['pressure'], data['gas_resistance'])
 )

 def publish_reading(self, data):
 """Transmit reading via MQTT"""
 payload = json.dumps({
 'device': 'rpi-env-001',
 'timestamp': datetime.utcnow().isoformat() + 'Z',
 'sensors': data
 })
 self.client.publish(
 self.mqtt_config['topic'],
 payload,
 qos=1
 )

 def monitoring_loop(self, interval=60):
 """Main monitoring loop"""
 while not self.stop_event.is_set():
 try:
 data = self.read_sensor()
 if data:
 self.store_reading(data)
 self.publish_reading(data)
 logging.info(f"Published: {data}")
 except Exception as e:
 logging.error(f"Monitoring error: {e}")

 self.stop_event.wait(interval)

 def start(self):
 """Start monitoring in background thread"""
 self.thread = Thread(target=self.monitoring_loop)
 self.thread.daemon = True
 self.thread.start()

 def stop(self):
 """Graceful shutdown"""
 self.stop_event.set()
 self.client.loop_stop()
 self.client.disconnect()

# systemd integration point
if __name__ == '__main__':
 logging.basicConfig(level=logging.INFO)
 monitor = EnvironmentalMonitor(
 db_path='/var/lib/iot/env_monitor.db',
 mqtt_config={
 'broker': 'mqtt.example.com',
 'port': 8883,
 'topic': 'home/environment',
 'tls': True
 }
 )
 monitor.start()
 monitor.stop_event.wait()
```

---

## Assessment

### Multiple Choice Questions

**Question 1**: In a production IoT deployment, the sensor collection service fails intermittently. Analysis shows the service starts before network connectivity is established, causing MQTT publish failures. Which systemd configuration modification resolves this issue?

A) Change Type=simple to Type=forking
B) Add After=network-online.target and Wants=network-online.target
C) Increase RestartSec to 60 seconds
D) Remove User=pi and run as root

**Answer**: B) Adding After=network-online.target and Wants=network-online.target ensures the service starts only after network interfaces are fully configured, preventing connection failures during service initialization.

---

**Question 2**: An IoT application running on Raspberry Pi 4 requires consistent interrupt response times below 100 microseconds for motor control. Which Linux kernel configuration is appropriate?

A) CONFIG_PREEMPT_VOLUNTARY
B) CONFIG_PREEMPT=y
C) CONFIG_PREEMPT_RT_FULL
D) CONFIG_NO_HZ=y

**Answer**: C) CONFIG_PREEMPT_RT_FULL provides real-time capabilities by converting interrupt handlers to kernel threads and implementing priority inheritance, achieving single-digit microsecond latency suitable for motor control applications.

---

**Question 3**: The GPIO sysfs interface has been deprecated. Which modern Linux interface should be used for new IoT projects requiring GPIO access?

A) /dev/mem direct memory mapping
B) Character device with ioctl() interface
C) libgpiod library and gpiod tools
D) debugfs GPIO debugging

**Answer**: C) libgpiod provides a character device-based interface (/dev/gpiochip0) with ioctl() commands, supporting multiple GPIO chips, interrupt handling, and line monitoring—essential for modern embedded Linux IoT development.
