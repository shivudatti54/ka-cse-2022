# Disk Structure - Summary

## Key Definitions

- **Platter**: A circular magnetic disk plate that stores data on its surfaces; multiple platters are stacked on a common spindle in hard disk drives.

- **Track**: A concentric circle on a disk surface where data is magnetically recorded; tracks are numbered from the outer edge inward.

- **Sector**: The smallest addressable unit on a disk, typically containing 512 or 4,096 bytes of data, including synchronization marks, address information, and error-correcting code.

- **Cylinder**: The set of all tracks with the same track number on all surfaces of a multi-platter disk; data on the same cylinder can be accessed without head movement.

- **CHS Addressing**: Cylinder-Head-Sector addressing mode that specifies exact physical locations using three coordinates.

- **LBA (Logical Block Addressing)**: A linear addressing scheme that treats the disk as an array of numbered sectors from 0 onward.

- **Zone Bit Recording (ZBR)**: A technique dividing the disk into zones with varying sectors per track to maximize capacity.

## Important Formulas

- **Total Sectors** = Number of Surfaces × Tracks per Surface × Sectors per Track

- **Disk Capacity** = Total Sectors × Bytes per Sector

- **LBA Calculation**: LBA = (Cylinder × Heads + Head) × Sectors per Track + (Sector - 1)

- **Access Time** = Seek Time + Rotational Latency + Transfer Time

- **Rotational Latency** = (1/2) × (60 / RPM) × 1000 ms

## Key Points

- Magnetic disks consist of one or more platters rotating at constant angular velocity, with data accessed by moving read/write heads radially and waiting for sectors to rotate under the head.

- The cylinder concept is fundamental to disk performance because accessing data within the same cylinder eliminates seek time.

- Modern disks use LBA addressing exclusively, with the disk controller translating logical addresses to physical CHS coordinates internally.

- Zone Bit Recording increases disk capacity by utilizing the larger circumference of outer tracks for more sectors per track.

- Average seek time, rotational latency, and data transfer rate are the three primary components determining disk performance.

- Disk geometry parameters (cylinders, heads, sectors) are now largely abstract concepts due to LBA and disk geometry translation.

- Sequential access within the same cylinder provides the highest data transfer rates; random access across different cylinders incurs significant seek overhead.

## Common Mistakes

1. **Confusing cylinders with tracks**: A cylinder includes all tracks at the same radial position across ALL surfaces, while a track exists on only ONE surface.

2. **Ignoring rotational latency**: Many students focus only on seek time and forget that waiting for the correct sector to rotate under the head adds significant delay.

3. **Misunderstanding sector numbering**: LBA starts at 0, while traditional sector numbering starts at 1; this off-by-one error is common in calculations.

4. **Conflating GB and GiB**: Disk manufacturers use decimal units (1 GB = 10^9 bytes), while operating systems often report binary units (1 GiB = 2^30 bytes), causing apparent capacity discrepancies.

5. **Assuming constant transfer rate**: With Zone Bit Recording, transfer rates vary across the disk, being higher in outer zones than inner zones.