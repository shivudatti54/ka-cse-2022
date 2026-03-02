# Image Formation and Sensing - Summary

## Key Definitions and Concepts
- **GSD**: Smallest object size resolvable in an image
- **Full Well Capacity**: Maximum electrons a pixel can hold before saturation
- **Photon Transfer Curve**: Relates sensor output variance to signal level
- **Quantum Efficiency**: Percentage of photons converted to electrons

## Important Formulas and Theorems
- \( \text{SNR} = \frac{N}{\sqrt{N + \sigma_{read}^2}} \) (Photon Transfer Equation)
- \( \text{MTF}(f) = \text{sinc}(\pi f \Delta x) \) (Modulation Transfer Function)
- Nyquist Frequency: \( f_N = \frac{1}{2\Delta x} \)
- Radiometric Response: \( E = \int L(\lambda)S(\lambda)R(\lambda)d\lambda \)

## Key Points
- CCD sensors offer better global shutter performance but higher power consumption
- Spatial aliasing occurs when sampling below Nyquist rate
- 14-bit ADCs are becoming standard in scientific imaging
- Dark current doubles every 5-6°C temperature increase
- Quad Bayer filters (e.g., 48MP smartphone cameras) use pixel binning
- Event cameras respond to logarithmic intensity changes with microsecond latency
- Quantum image sensors achieve sub-electron read noise via avalanche multiplication

## Common Mistakes to Avoid
- Confusing irradiance (W/m²) with radiance (W/sr·m²)
- Assuming all noise sources are Gaussian-distributed
- Neglecting PSF effects when calculating optical resolution
- Overlooking temperature's impact on dark current in long exposures

## Revision Tips
1. Create comparative tables: CCD vs CMOS, Bayer vs Foveon sensors
2. Solve GSD and SNR problems using DU's past exam papers
3. Study IEEE ISSCC papers (2020-2023) for sensor technology trends
4. Implement a basic noise simulator in Python (Poisson + Gaussian noise)

Length: 650 words