# Raspberry Pi - About the Board

## Introduction

The Raspberry Pi represents a paradigm shift in embedded computing, bridging the gap between traditional microcontrollers and full-fledged desktop computers within the IoT ecosystem. Developed by the Raspberry Pi Foundation in the United Kingdom, this single-board computer (SBC) was initially conceived in 2006 and first released in 2012 to address declining computer science enrollment in universities. The platform has since evolved into a versatile embedded computing platform powering millions of IoT applications worldwide, from simple sensor nodes to complex industrial automation systems.

Fundamentally, the Raspberry Pi distinguishes itself from microcontroller platforms (such as Arduino) by executing a complete operating system—typically Raspberry Pi OS (formerly Raspbian), a Debian-based Linux distribution. This architectural difference enables the execution of complex software stacks, including networking protocols, web servers, database management systems, and high-level programming environments like Python, Node.js, and Java. The presence of a General Purpose Input/Output (GPIO) header preserves hardware interfacing capabilities, allowing direct connection to sensors, actuators, and communication peripherals while leveraging the computational power of an ARM-based processor.

## System Architecture

### System-on-Chip (SoC) Design

The Raspberry Pi utilizes Broadcom system-on-chip (SoC) processors that integrate multiple computational components onto a single silicon die. The latest Raspberry Pi 4 Model B employs the Broadcom BCM2711 SoC, fabricated on a 28nm process node, featuring a quad-core ARM Cortex-A72 (ARMv8-A architecture) processor operating at 1.5 GHz with 1MB shared L2 cache. Each Cortex-A72 core implements out-of-order execution, branch prediction, and speculative execution, delivering approximately 3-4× the performance per clock cycle compared to the earlier Cortex-A53 cores found in Raspberry Pi 3.

The VideoCore VI GPU integrated within the BCM2711 supports OpenGL ES 3.0 and hardware-accelerated video decoding for H.265 (4Kp60), H.264 (1080p60), and VP9 codecs. For IoT applications involving edge computing with machine learning workloads, the GPU can be leveraged for parallel processing tasks, though the newer Raspberry Pi 5 incorporates the Raspberry Pi Chip (RP1) for enhanced I/O handling.

### Memory Architecture

The Raspberry Pi 4 introduced significant memory improvements over its predecessors, offering LPDDR4 SDRAM in 2GB, 4GB, or 8GB configurations with a bus width of 32 bits operating at 3200 MT/s. The memory architecture employs a unified memory system where the CPU and GPU share the same physical memory pool, requiring dynamic memory allocation between processing resources. This shared memory design eliminates the need for separate video memory but requires careful memory management in resource-constrained IoT deployments.

Earlier models utilized LPDDR2 or LPDDR3 memory with lower bandwidth characteristics. The Raspberry Pi 3 Model B+ features 1GB LPDDR2 RAM operating at 900 MHz, demonstrating the evolution of memory technology across generations.

### Storage Configuration

Unlike conventional computing platforms, Raspberry Pi boards lack internal storage devices, relying exclusively on microSD cards for boot storage and persistent data. This design philosophy supports rapid operating system switching, portable configurations, and cost reduction. The boot process initiates from the onboard bootloader stored in OTP (One-Time Programmable) memory, which subsequently loads the firmware from the microSD card's boot partition. For enterprise IoT deployments requiring enhanced reliability, the Raspberry Pi 4 supports USB 3.0 boot from external SSDs, providing substantially higher I/O throughput and improved durability compared to microSD media.

## GPIO Interface and Pinout

### 40-Pin Header Configuration

The GPIO (General Purpose Input/Output) header constitutes the primary hardware interfacing mechanism for IoT applications. The standard 40-pin header present on Raspberry Pi models from Model B+ onward provides the following functional groups:

**Power Supply Pins**: The header supplies two voltage rails—3.3V (limited to 50mA total) and 5V (drawn directly from input supply, limited by USB power rating). These rails provide power to sensors and peripherals, though high-current devices require external power supplies.

**Ground Pins**: Eight ground pins provide common reference for all digital circuits connected to the GPIO header.

**Digital I/O Pins**: Pins GPIO 0-26 (BCM numbering) serve as bidirectional digital lines configurable as inputs or outputs. Each pin can source or sink maximum 16mA with a total limit of 50mA across all GPIO pins, necessitating current-limiting resistors for LED and similar loads.

**Special Function Pins**: The header includes dedicated interfaces for I2C (GPIO 2=SDA, GPIO 3=SCL), SPI (MOSI=MOSI, MISO=MISO, SCLK=SCLK, CE0/CE1=chip enables), and UART (GPIO 14=TXD, GPIO 15=RXD).

**PWM Channels**: Hardware PWM is available on GPIO 12, 13, 18, and 19, providing 8-bit resolution PWM at frequencies up to 125 MHz divided by the selected divisor.

### Pin Numbering Schemes

Two distinct numbering schemes govern GPIO access in software. The **BCM numbering** (Broadcom channel numbering) references the pin mapping to the processor's GPIO controller, while **Physical/BOARD numbering** references the sequential position on the 40-pin header. Code using RPi.GPIO library must explicitly declare the mode via `GPIO.setmode(GPIO.BCM)` or `GPIO.setmode(GPIO.BOARD)`. Misconfiguration between schemes represents a common source of hardware damage when incorrect pins are toggled.

## Power Management and Requirements

### Voltage Regulation Circuitry

The Raspberry Pi employs onboard switching voltage regulators to derive necessary supply voltages from the 5V input. The BCM2711 requires multiple voltage rails: 3.3V for I/O and GPIO, 1.8V for core logic, and 1.2V for CPU/L3 cache. The Raspberry Pi 4 implements a more efficient regulator design compared to earlier models, though power consumption remains a critical consideration for battery-powered IoT deployments.

### Power Budget Calculation

For a Raspberry Pi 4 connected to sensors and peripherals, total power consumption must be carefully calculated. The board itself draws approximately 2.5W at idle, rising to 6-7W under computational load. When selecting power supplies, the formula P_total = P_board + ΣP_peripherals applies, where P_board includes CPU consumption plus regulator losses (approximately 85% efficiency). A 5V/3A power supply provides 15W, leaving approximately 8-10W for connected peripherals—a constraint frequently exceeded in multi-sensor IoT installations, necessitating external power distribution.

## Boot Process

The Raspberry Pi boot sequence proceeds through defined stages: Stage 1 (bootcode.bin) initializes SDRAM from OTP memory, Stage 2 (start.elf) configures GPU and loads kernel, and Stage 3 transfers control to the ARM CPU for Linux kernel initialization. This multi-stage boot process supports network boot (PXE) and USB mass storage boot on Raspberry Pi 3 and later models, enabling centralized IoT device management without physical access.

## Model Comparison

| Model | Processor | RAM | Key IoT Features | Release |
|-------|-----------|-----|------------------|---------|
| Pi 4 B | Cortex-A72 @ 1.5GHz | 2/4/8GB LPDDR4 | USB 3.0, Gigabit Ethernet, dual-band WiFi | 2019 |
| Pi 3 B+ | Cortex-A53 @ 1.4GHz | 1GB LPDDR2 | Dual-band WiFi, PoE header | 2018 |
| Pi 3 B | Cortex-A53 @ 1.2GHz | 1GB LPDDR2 | Built-in WiFi/BT | 2016 |
| Pi Zero W | ARM11 @ 1GHz | 512MB | Compact form, WiFi/BT | 2017 |
| Pi 5 | Cortex-A76 @ 2.4GHz | 4/8GB LPDDR4X | RP1 chip, PCIe | 2023 |

## Raspberry Pi vs Microcontroller IoT Nodes

When selecting hardware for IoT applications, the choice between SBCs (Raspberry Pi) and microcontrollers (Arduino, ESP32) involves critical trade-offs. Raspberry Pi platforms offer superior processing capability for complex algorithms, operating system-level networking stacks, and multimedia handling, but consume 50-100× more power (1-5W vs 10-50mW) and lack real-time response guarantees. Microcontroller platforms excel in ultra-low-power applications requiring deterministic timing, such as motor control loops with microsecond-level precision. Hybrid approaches frequently employ microcontrollers for real-time sensor acquisition and communication, connected to Raspberry Pi hubs for data aggregation and cloud transmission.

## Worked Examples

**Example 1: GPIO Pin Configuration Analysis**

Consider an LED connected through a 330Ω resistor to GPIO 21 (BCM numbering). Using Physical numbering, this corresponds to pin 40. If the LED has forward voltage drop of 2V at 10mA operating current, the resistor value calculation proceeds as: R = (V_supply - V_LED)/I = (3.3V - 2V)/0.01A = 130Ω. The 330Ω resistor limits current to approximately 4mA, providing adequate brightness while ensuring pin current stays well within the 16mA absolute maximum rating.

**Example 2: Power Budget for Multi-Sensor IoT Node**

A Raspberry Pi 4 operating at 5V draws 600mA under load. Connecting five DHT22 temperature sensors (each requiring 1.5mA at 3.3V), one BME280 sensor (0.3mA), and an USB camera (500mA) yields: P_total = (5×0.0015 + 0.0003) × 3.3 + 5×0.6 + 5×0.5 = 0.0279W + 3W + 2.5W ≈ 5.53W. This remains within the 15W supply capacity, but thermal dissipation requires adequate ventilation in enclosed installations.

## Assessment

### Multiple Choice Questions

**Question 1**: A Raspberry Pi 4 Model B is configured to read data from an I2C temperature sensor at 100 kHz. If the sensor requires a 4.7kΩ pull-up resistor on each I2C line, and the I2C bus operates at 3.3V, what is the approximate current flowing through each pull-up resistor when the line is driven LOW?

A) 0.7 mA
B) 1.4 mA
C) 3.3 mA
D) 7.0 mA

**Answer**: A) 0.7 mA. When the GPIO drives the I2C line LOW, current flows from 3.3V through the 4.7kΩ resistor to ground, following Ohm's Law: I = V/R = 3.3V/4700Ω ≈ 0.7mA.

**Question 2**: For an IoT application requiring continuous data logging from four analog sensors with 12-bit ADC resolution, SPI communication at 10 MHz, and Wi-Fi transmission of logged data every 30 seconds, which Raspberry Pi model provides the most cost-effective solution while meeting performance requirements?

A) Raspberry Pi Zero W
B) Raspberry Pi 3 Model B
C) Raspberry Pi 4 Model B (2GB)
D) Raspberry Pi 4 Model B (8GB)

**Answer**: B) Raspberry Pi 3 Model B. The application does not require the 4K video capabilities or PCIe of Pi 4, and the 1GB RAM suffices for data logging operations. The quad-core Cortex-A53 handles SPI polling and Wi-Fi stack concurrently. Pi Zero W lacks sufficient performance for simultaneous SPI handling and Wi-Fi operations, while Pi 4 incurs unnecessary cost and power consumption for this workload.

**Question 3**: Calculate the minimum microSD card class rating required to achieve a sustained write speed of 20 MB/s for a Raspberry Pi 4 recording video at 1080p resolution using an external USB 3.0 storage enclosure.

A) Class 4 (4 MB/s)
B) Class 10 (10 MB/s)
C) UHS-I U1 (10 MB/s)
D) UHS-I U3 (30 MB/s)

**Answer**: D) UHS-I U3 (30 MB/s). Although video is written to USB storage, the microSD card hosts the operating system and must handle filesystem operations, temporary caching, and system logs. A UHS-I U3 rating guarantees minimum 30 MB/s sequential writes, providing sufficient headroom for the 20 MB/s video stream plus system overhead.