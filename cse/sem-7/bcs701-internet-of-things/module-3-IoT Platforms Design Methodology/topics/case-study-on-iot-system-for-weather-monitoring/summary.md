# Case Study: IoT System for Weather Monitoring - Summary

## Key Definitions

- **MQTT (Message Queuing Telemetry Transport)**: A lightweight publish-subscribe messaging protocol designed for constrained devices with limited bandwidth, operating over TCP/IP.
- **Quality of Service (QoS)**: MQTT parameter determining message delivery guarantees—QoS 0 (at most once), QoS 1 (at least once), QoS 2 (exactly once).
- **Edge Computing**: Processing data at the network edge rather than centralized cloud, reducing latency and bandwidth requirements.
- **ThingSpeak**: IoT analytics platform service for storing and visualizing sensor data in the cloud.

## Important Formulas

- **Weighted Sensor Fusion**: $V_{final} = \frac{\sum_{i=1}^{n} w_i \cdot V_i}{\sum_{i=1}^{n} w_i}$
- **Power Consumption**: $E_{total} = (P_{active} \times t_{active}) + (P_{sleep} \times t_{sleep})$
- **Battery Lifetime (hours)**: $\frac{Battery Capacity (mAh)}{Average Current Draw (mA)}$

## Key Points

1. The three-tier IoT architecture comprises Sensing Layer (sensors), Processing Layer (microcontrollers/Raspberry Pi), and Communication Layer (MQTT/HTTP).

2. Python packages `Paho-MQTT`, `Adafruit_DHT`, `adafruit_bmp180`, and `requests` form the core implementation toolkit.

3. MQTT's lightweight 2-byte header makes it superior to HTTP for bandwidth-constrained sensor networks.

4. JSON serves as the standard data serialization format due to interoperability and human-readable structure.

5. DHT22 sensor provides temperature (±0.5°C accuracy) and humidity (±2% RH accuracy); BMP180 delivers barometric pressure measurements.

6. TLS/SSL encryption, OAuth authentication, and certificate-based device verification ensure IoT system security.

7. Cloud platforms like ThingSpeak enable real-time data visualization without custom backend development.

8. Exponential backoff algorithms provide resilience against network instabilities in IoT deployments.

## Common Mistakes

1. **Confusing MQTT QoS levels**: Students often incorrectly assume higher QoS always improves performance—QoS 2 adds significant latency unsuitable for real-time sensor streams.

2. **Ignoring timestamp synchronization**: Without NTP synchronization, multi-sensor data correlation becomes unreliable, especially in distributed deployments.

3. **Neglecting error handling**: Bare exception catching without specific handling leads to silent failures in production IoT systems.

4. **Incorrect unit conversions**: Pressure sensors often output in Pascals; conversion to hPa (1 hPa = 100 Pa) requires attention to units in calculations.

5. **Underestimating power requirements**: Many students calculate only active power consumption, ignoring sleep mode power draw that significantly impacts battery lifetime in intermittent transmission scenarios.