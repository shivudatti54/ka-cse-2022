# Motor Control with Microcontrollers

## Introduction to Motor Control
Motor control is a fundamental application of microcontrollers in embedded systems, enabling precise movement in robotics, industrial automation, consumer electronics, and automotive systems. This module explores how microcontrollers interface with and control various types of motors using their built-in peripherals.

## Types of Motors
Different motors require different control strategies. The main types include:

### DC Motors
DC motors are the simplest type, operating on direct current. They provide continuous rotation and are controlled by varying voltage.

```
+12V ------ [Motor] ------ GND
```

**Key Characteristics:**
- Simple control (voltage = speed)
- Bidirectional operation (reverse polarity)
- High torque at low speeds

### Stepper Motors
Stepper motors move in discrete steps, offering precise positional control without feedback systems.

```
         +----+
Pulse -->|    |--> Motor Movement (Step)
         +----+
```

**Key Characteristics:**
- Precise positional control
- Open-loop operation (no feedback needed)
- Lower torque compared to DC motors

### Servo Motors
Servo motors incorporate feedback mechanisms (usually potentiometers or encoders) for closed-loop control of position, velocity, or torque.

```
+---------------------+
| Setpoint --> Controller --> Motor --> Output
|                     |                   |
|                     <-- Feedback <------+
+---------------------+
```

**Key Characteristics:**
- Closed-loop control
- High precision positioning
- Built-in control circuitry

## Motor Control Techniques

### PWM (Pulse Width Modulation) Control
PWM is the primary method for controlling motor speed and direction. It works by rapidly switching power on and off, with the ratio of on-time to off-time (duty cycle) determining the average voltage.

```
Duty Cycle = 25%
+-----+     +-----+     +-----+
|     |     |     |     |     |
|     |     |     |     |     |
+     +-----+     +-----+     +-----

Duty Cycle = 50%
+---------+     +---------+     +-----
|         |     |         |     |
|         |     |         |     |
+         +-----+         +-----+

Duty Cycle = 75%
+-------------+     +-------------+ 
|             |     |             |
|             |     |             |
+             +-----+             +---
```

**PWM Parameters:**
- Frequency: How often the pulse repeats (typically 1-20 kHz for motors)
- Duty Cycle: Percentage of time the signal is high (0-100%)
- Resolution: Number of discrete duty cycle values (8-bit = 256, 16-bit = 65536)

### H-Bridge Circuitry
For bidirectional control of DC motors, H-bridges are essential. They allow current to flow through the motor in both directions.

```
       +12V
         |
    Q1       Q2
     |       |
A ---+--[M]--+--- B
     |       |
    Q3       Q4
         |
        GND
```

**Control Logic:**
```
Q1-Q4: Q2-Q3: Forward
Q1-Q4: Q1-Q4: Brake
Q2-Q3: Q2-Q3: Reverse
Q2-Q3: Q1-Q4: Brake
```

## Microcontroller Interfacing

### GPIO Configuration
Microcontrollers use General Purpose Input/Output pins to interface with motor drivers:

```c
// Example AVR code for motor control
DDRB |= (1 << PB1);  // Set PB1 as output (PWM)
DDRD |= (1 << PD2) | (1 << PD3);  // Set direction pins as output
```

### Timer Peripherals for PWM Generation
Most microcontrollers have dedicated timer peripherals that generate hardware PWM:

**8051 Example:**
```assembly
MOV TMOD, #01H  ; Timer 0 in mode 1
SETB TR0        ; Start timer
```

**AVR Example:**
```c
// Fast PWM mode, 8-bit
TCCR0A |= (1 << COM0A1) | (1 << WGM01) | (1 << WGM00);
TCCR0B |= (1 << CS00);   // No prescaling
OCR0A = 128;             // 50% duty cycle
```

**ARM Cortex-M Example:**
```c
// Using STM32 HAL library
TIM_HandleTypeDef htim;
htim.Instance = TIM2;
htim.Init.Prescaler = 0;
htim.Init.CounterMode = TIM_COUNTERMODE_UP;
htim.Init.Period = 255;
htim.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
HAL_TIM_PWM_Init(&htim);

TIM_OC_InitTypeDef sConfigOC;
sConfigOC.OCMode = TIM_OCMODE_PWM1;
sConfigOC.Pulse = 127;
sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
HAL_TIM_PWM_ConfigChannel(&htim, &sConfigOC, TIM_CHANNEL_1);
HAL_TIM_PWM_Start(&htim, TIM_CHANNEL_1);
```

## Motor Driver ICs
Microcontrollers typically don't drive motors directly due to current limitations. Instead, they interface with motor driver ICs:

### Common Motor Driver ICs
| IC | Motor Type | Max Current | Interface | Features |
|----|------------|-------------|-----------|----------|
| L293D | DC, Stepper | 600mA | Parallel | Dual H-bridge |
| L298N | DC, Stepper | 2A | Parallel | Dual H-bridge |
| TB6612FNG | DC | 1.2A | Parallel | Dual, low voltage |
| DRV8833 | DC | 1.5A | Parallel | Dual H-bridge |
| A4988 | Stepper | 2A | Step/Dir | Stepper driver with microstepping |
| DRV8825 | Stepper | 2.5A | Step/Dir | Stepper driver with microstepping |

### Interfacing Example with L293D
```
Microcontroller            L293D              Motor
PB0 (PWM)    ----------> Enable 1
PD0 (DIR1)   ----------> Input 1
PD1 (DIR2)   ----------> Input 2
                          Output1 ----------> Motor Terminal A
                          Output2 ----------> Motor Terminal B
```

## Stepper Motor Control
Stepper motors require precise sequencing of coils:

### Stepper Motor Sequencing
**Full Step Sequence (4-step):**
```
Step  Coil A  Coil B  Coil C  Coil D
1     High    Low     Low     Low
2     Low     High    Low     Low
3     Low     Low     High    Low
4     Low     Low     Low     High
```

**Wave Drive Sequence:**
```
Step  A  B  C  D
1     1  0  0  0
2     0  1  0  0
3     0  0  1  0
4     0  0  0  1
```

### Microstepping
Microstepping divides steps into smaller increments for smoother motion by controlling current through coils with varying PWM signals.

## Servo Motor Control
Servo motors use a specific PWM signal for position control:

**Servo PWM Signal:**
- Frequency: 50Hz (20ms period)
- Pulse Width: 1ms (0°) to 2ms (180°)
- Neutral: 1.5ms (90°)

```
0° Position (1ms pulse):
+---+
|   |
|   |                   (19ms off)
+   +-----------------------------------

180° Position (2ms pulse):
+------+
|      |
|      |                (18ms off)
+      +--------------------------------
```

## Feedback Systems
Advanced motor control often incorporates feedback for closed-loop operation:

### Encoders
Optical or magnetic encoders provide position and velocity feedback:

```
         +-----+-----+-----+
Channel A|     |     |     |
         |     |     |     |
         +     +     +     +
         
         +-----+-----+-----+
Channel B|   |   |   |   |
         |   |   |   |   |
         +   +   +   +   +
```

### PID Control
Proportional-Integral-Derivative controllers maintain precise control:

```
         +---------------------------------+
Setpoint -->| Proportional |--> Sum --> Output --> Motor
            | Integral     |      ^         |
            | Derivative   |      |         |
            +--------------+      |         |
                 ^                |         |
                 |                |         |
                 +--- Feedback <--+         |
                                            |
                                            +--> System
```

## Practical Implementation Considerations

### Power Supply Decoupling
Motors generate electrical noise that can disrupt microcontroller operation:

```
+5V ----||-------+---- MCU
      100nF      |
                 |
                ===
                 |
                GND
```

### Current Sensing
Monitoring motor current helps detect stalls and overloads:

```
+12V ----[R_sense]----[Motor]---- GND
                  |
                  +---[Amplifier]--- ADC input
```

### Thermal Protection
Motor drivers can overheat; temperature monitoring is essential:

```c
// Read temperature sensor
adc_value = read_adc(TEMP_SENSOR_CHANNEL);
if (adc_value > OVERHEAT_THRESHOLD) {
    disable_motor();
}
```

## Real-World Applications

### Robotics
- Precise joint control using servos
- Wheel drive using DC motors with encoders
- Arm positioning using stepper motors

### Automotive Systems
- Window lift motors
- Seat adjustment
- Wiper control
- Electric power steering

### Industrial Automation
- Conveyor belt control
- CNC machines
- Robotic arms
- Packaging equipment

## Comparison of Motor Types
| Parameter | DC Motor | Stepper Motor | Servo Motor |
|-----------|----------|---------------|-------------|
| Control Complexity | Low | Medium | High |
| Position Feedback | Not inherent | Not needed | Built-in |
| Cost | Low | Medium | High |
| Torque | High at low speed | Good holding torque | High |
| Speed Range | Wide | Limited | Medium |
| Precision | Low | High | Very High |

## Exam Tips
1. **Remember PWM parameters**: Frequency affects motor noise, duty cycle controls speed, resolution affects smoothness.
2. **H-bridge operation**: Understand the four switching states (forward, reverse, brake, coast).
3. **Stepper sequencing**: Be able to write the sequence for different step modes.
4. **Servo timing**: Memorize the pulse widths for 0°, 90°, and 180° positions.
5. **Current calculations**: Know how to calculate appropriate current-limiting resistors.
6. **Noise considerations**: Always mention decoupling capacitors in design questions.
7. **Interface protocols**: Differentiate between parallel (L293D) and step/dir (A4988) interfaces.