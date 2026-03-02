# **Synchronizing Physical Clocks**

## **Key Definitions and Formulas**

- **Global Time**: The time measured by a reference clock (e.g., an atomic clock)
- **Local Time**: The time measured by a physical clock
- **Clock Skew**: The difference between a physical clock and the global time
- **Clock Synchronization**: The process of adjusting a physical clock to match the global time

## **Theories and Algorithms**

- **NTP (Network Time Protocol)**: A widely used protocol for synchronizing clocks over networks
  - **Equation 1**: `delta_t = (k \* delta_t_{prev} + \* delta_t_{ref}) / (k + 1)`
    - Where:
      - `delta_t`: The estimated clock skew
      - `delta_t_{prev}`: The previous estimated clock skew
      - `delta_t_{ref}`: The reference clock skew
      - `k`: The number of iterations
- **Pendulum Clock Synchronization**: A method for synchronizing two pendulum clocks
  - **Theorem 1**: "The two clocks will eventually converge to the same time if they are started within 10 seconds of each other"

## **Other Important Points**

- **Clock drift**: The gradual change in clock time due to aging or other factors
- **Clock jitter**: The random variation in clock time due to thermal noise or other sources
- **Synchronization intervals**: The frequency at which clocks are synchronized (e.g., every hour, every 10 minutes)
