# **Synchronizing Physical Clocks**

### Key Points

- **Definition:** Synchronizing physical clocks refers to the process of coordinating the timekeeping of multiple physical clocks to ensure they are accurate and consistent.
- **Importance:** Ensures correct timing in distributed systems, preventing errors and inconsistencies in processing and communication.
- **Challenges:**
  - Clock drift and variations due to environmental factors (e.g., temperature, humidity)
  - Network latency and synchronization overhead

### Key Concepts

- **Clock Skew:** Difference in clock values between two clocks.
- **Clock Synchronization Algorithm:**
  - **Pendulum Clock Algorithm:** Uses a master clock to adjust the time of other clocks.
  - **NTP (Network Time Protocol):** A widely used protocol for synchronizing clocks over networks.
- **Time Synchronization Theorem:** If two clocks are synchronized, any two events that occurred at the same time on one clock will occur at the same time on the other clock.

### Formulas and Definitions

- **Clock Skew Formula:** Δt = t2 - t1, where Δt is the clock skew, and t1 and t2 are the clock values.
- **NTP Algorithm Formula:**
  - `t_new = t_old + (t_master - t_old) / 2`
- **Definition:** A **clock** is a device that measures time, typically using a periodic signal (e.g., pendulum, quartz crystal).

### Important Theorems

- **Arieh E. Baron's Theorem:** If two clocks are synchronized, any two events that occurred at the same time on one clock will occur at the same time on the other clock.
- **Berlin Theorem:** If two clocks are synchronized, the time difference between them will not change over time.

### Revision Tips

- Understand the importance of clock synchronization in distributed systems.
- Familiarize yourself with clock skew, clock synchronization algorithms, and time synchronization theorems.
- Practice calculating clock skew and adjusting clock values using formulas.
