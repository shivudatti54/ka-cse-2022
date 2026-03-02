# Data Communications - Summary

## Key Definitions and Concepts

- **Data Communication**: The process of exchanging data between devices through a communication channel using standardized protocols.

- **Protocol**: A set of rules governing data exchange between devices in a network.

- **Bandwidth**: The range of frequencies a transmission medium can carry, measured in Hertz (Hz).

- **Data Rate**: The number of bits transmitted per second, measured in bits per second (bps).

- **Attenuation**: The gradual loss of signal strength during transmission.

- **Signal-to-Noise Ratio (SNR)**: The ratio of signal power to noise power, determining communication quality.

## Important Formulas and Theorems

- **Nyquist Theorem (Noiseless Channel)**: Maximum Data Rate = 2B × log₂M
  - B = bandwidth in Hz, M = number of signal levels

- **Shannon's Capacity Theorem (Noisy Channel)**: Maximum Capacity = B × log₂(1 + S/N)
  - B = bandwidth in Hz, S/N = signal-to-noise ratio

## Key Points

1. A data communication system has five components: Message, Sender, Receiver, Medium, and Protocol.

2. Transmission modes: Simplex (one-way), Half-Duplex (two-way alternately), Full-Duplex (simultaneous two-way).

3. Serial transmission sends bits sequentially (long distance); parallel transmission sends multiple bits simultaneously (short distance).

4. Guided media: Twisted Pair, Coaxial Cable, Fiber Optic. Unguided media: Radio Waves, Microwaves, Infrared.

5. Fiber optic cables offer highest bandwidth, lowest attenuation, and immunity to electromagnetic interference.

6. Digital signals are more noise-resistant than analog signals and can be regenerated without distortion.

7. Higher bandwidth allows higher data rates according to Nyquist and Shannon theorems.

8. Twisted pair cables use Category ratings (CAT 5e supports 1 Gbps, CAT 6 supports 10 Gbps).

9. Analog signals are continuous; digital signals are discrete (binary: 0s and 1s).

10. Signal-to-noise ratio directly affects the achievable data rate in practical communication systems.

## Common Mistakes to Avoid

1. Confusing bandwidth with data rate - bandwidth is capacity (Hz), data rate is speed (bps).

2. Misremembering transmission modes - full-duplex allows simultaneous communication, half-duplex does not.

3. Believing higher bandwidth always means higher data rate - noise levels also limit the actual data rate.

4. Mixing up analog and digital - analog is continuous wave, digital is discrete pulses.

5. Forgetting that parallel transmission, while faster, is limited to short distances due to synchronization issues.

## Revision Tips

1. Create a comparison table for all transmission media with columns for type, bandwidth, distance, advantages, and applications.

2. Practice numerical problems on Nyquist and Shannon formulas from previous question papers.

3. Draw diagrams of different transmission modes to visualize data flow directions.

4. Memorize the five components of data communication system - this is a frequently asked 5-mark question.

5. Review advantages and disadvantages of fiber optic over copper cables for exam preparation.
