# The Digital Camera

## Overview

The digital camera bridges the physical world and digital realm by capturing light and converting it into processable digital images. Understanding the complete pipeline from scene to pixels is essential for effective computer vision algorithm development.

## Key Points

- **Image Formation Pipeline**: Scene → Lens (Aperture) → Image Sensor → Bayer Filter → ADC → Demosaicing → Post-processing → Digital Image
- **CCD vs CMOS Sensors**: CCD has higher quality but more power consumption; CMOS is cheaper, faster, lower power, dominates modern cameras
- **Bayer Filter Pattern**: Red-Green-Green-Blue arrangement with 50% green (matching human eye sensitivity), requires demosaicing
- **Demosaicing**: Interpolation process reconstructing full RGB values at each pixel from mosaic pattern
- **Analog-to-Digital Conversion**: Converts continuous voltage to discrete values; bit depth (8-bit=256 levels, 12-bit=4096 levels) affects quality
- **Post-Processing**: White balance correction, gamma correction (V_out = V_in^γ), noise reduction, compression (JPEG lossy, RAW lossless)
- **Key Parameters**: Resolution (total pixels), dynamic range (brightness ratio), quantization (bit depth), sampling rate

## Important Concepts

- Focal length controls magnification and field of view (longer=telephoto, shorter=wide-angle)
- Aperture (f-stops) controls light amount - lower f-number means larger opening
- Rolling shutter in CMOS can cause skewing with fast motion unlike CCD's global shutter
- Nyquist-Shannon sampling theorem requires sampling at twice the frequency to avoid aliasing
- Camera limitations affect CV: low resolution limits detail, low bit depth causes quantization artifacts, noise interferes with algorithms

## Notes

- Memorize the complete pipeline from lens to digital file
- Understand CCD vs CMOS trade-offs: CCD for quality, CMOS for cost/speed/power
- Draw and explain 2×2 Bayer pattern showing RGGB arrangement
- Explain why demosaicing is necessary and how it interpolates missing color values
- Link camera characteristics to CV task performance (resolution, noise, compression artifacts)
