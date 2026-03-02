# Disk Structure


## Table of Contents

- [Disk Structure](#disk-structure)
- [Introduction](#introduction)
- [Physical Structure of a Hard Disk](#physical-structure-of-a-hard-disk)
  - [Key Terminology](#key-terminology)
- [Logical Block Addressing (LBA)](#logical-block-addressing-lba)
  - [Why LBA?](#why-lba)
- [Mapping Logical Blocks to Physical Sectors](#mapping-logical-blocks-to-physical-sectors)
  - [Mapping Formula](#mapping-formula)
  - [Sector Numbering](#sector-numbering)
- [Constant Linear Velocity vs Constant Angular Velocity](#constant-linear-velocity-vs-constant-angular-velocity)
  - [Constant Angular Velocity (CAV)](#constant-angular-velocity-cav)
  - [Constant Linear Velocity (CLV)](#constant-linear-velocity-clv)
  - [Comparison](#comparison)
- [Solid-State Drives (SSDs)](#solid-state-drives-ssds)
- [Disk Capacity Calculation](#disk-capacity-calculation)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

Modern disk drives are addressed as large **one-dimensional arrays of logical blocks**, where the logical block is the smallest unit of transfer. The OS and the disk controller must map these logical block numbers to the physical geometry of the disk — cylinders, tracks (heads), and sectors. Understanding this mapping is essential for grasping how the OS interacts with storage hardware.

This topic corresponds to **Section 10.2** of Silberschatz (Operating System Concepts).

## Physical Structure of a Hard Disk

A hard disk drive (HDD) consists of one or more **platters** mounted on a **spindle** that spins at high speed (typically 5400–15000 RPM). Each platter has two surfaces, and each surface has a **read-write head**.

```
Physical Disk Structure (side view):

 Read-Write Heads
 |
 =========|========= ← Platter 1 (top surface)
 =========|========= ← Platter 1 (bottom surface)
 |
 =========|========= ← Platter 2 (top surface)
 =========|========= ← Platter 2 (bottom surface)
 |
 Spindle (rotates all platters together)


Top view of a single platter surface:

 +---------------------------+
 | Track 0 (outermost) |
 | +---------------------+ |
 | | Track 1 | |
 | | +-----------------+ | |
 | | | Track 2 | | |
 | | | +----+ | | |
 | | | | | Spindle | | |
 | | | +----+ | | |
 | | +-----------------+ | |
 | +---------------------+ |
 +---------------------------+

Each track is divided into sectors:

 Track: [Sector 0][Sector 1][Sector 2][Sector 3]...[Sector N]
```

### Key Terminology

| Term         | Definition                                                                                 |
| :----------- | :----------------------------------------------------------------------------------------- |
| **Platter**  | A circular disk coated with magnetic material; data is stored on its surfaces              |
| **Surface**  | Each platter has a top and bottom surface, each with its own read-write head               |
| **Track**    | A concentric circle on a platter surface                                                   |
| **Sector**   | A subdivision of a track; the smallest physical storage unit (typically 512 bytes or 4 KB) |
| **Cylinder** | The set of all tracks at the same position across all platter surfaces                     |
| **Head**     | The read-write mechanism; one per surface. Head number identifies which surface            |
| **Arm**      | Holds the read-write head; all arms move together (they share an actuator)                 |

```
Cylinder concept (3 platters = 6 surfaces):

Surface 0: ---[Track 5]---
Surface 1: ---[Track 5]---
Surface 2: ---[Track 5]--- ← All these tracks together
Surface 3: ---[Track 5]--- form Cylinder 5
Surface 4: ---[Track 5]---
Surface 5: ---[Track 5]---
```

## Logical Block Addressing (LBA)

The disk is abstracted as a **one-dimensional array of logical blocks**, numbered 0, 1, 2, ..., N-1. The OS doesn't need to know the physical geometry — it simply requests "read block 1547" and the disk controller handles the mapping.

```
Logical view (what the OS sees):

Block: [0] [1] [2] [3] [4] [5] ... [N-1]

Each logical block maps to a physical (cylinder, head, sector) location.
```

### Why LBA?

| Aspect          | CHS Addressing                 | LBA                                |
| :-------------- | :----------------------------- | :--------------------------------- |
| **Format**      | (Cylinder, Head, Sector)       | Single block number (0, 1, 2, ...) |
| **Complexity**  | OS must know disk geometry     | OS just uses block numbers         |
| **Portability** | Tied to specific disk geometry | Works with any disk                |
| **Limits**      | Original CHS limited to 8.4 GB | LBA supports very large disks      |
| **Used by**     | Old BIOS (pre-1990s)           | All modern systems                 |

## Mapping Logical Blocks to Physical Sectors

The disk controller maps logical block numbers to physical (cylinder, head, sector) addresses. The mapping typically proceeds in this order:

```
Mapping Order:

Logical Block 0 → Cylinder 0, Head 0, Sector 0
Logical Block 1 → Cylinder 0, Head 0, Sector 1
...
(all sectors on track 0 of surface 0)
...
Next → Cylinder 0, Head 1, Sector 0
...
(all sectors on track 0 of surface 1)
...
(continue through all heads at cylinder 0)
...
Next → Cylinder 1, Head 0, Sector 0
...
(and so on, cylinder by cylinder)
```

### Mapping Formula

Given:

- **S** = sectors per track
- **H** = number of heads (surfaces)
- **Logical block number** = B

```
Cylinder = B / (S × H)
Head = (B / S) mod H
Sector = B mod S

Example:
 S = 63 sectors/track, H = 16 heads
 Logical block B = 2000

 Cylinder = 2000 / (63 × 16) = 2000 / 1008 = 1
 Head = (2000 / 63) mod 16 = 31 mod 16 = 15
 Sector = 2000 mod 63 = 56

 So block 2000 → Cylinder 1, Head 15, Sector 56
```

### Sector Numbering

Within a track, sectors are not always numbered sequentially around the platter:

- **Sector interleaving** — Sectors may be numbered with gaps (e.g., 0, 3, 6, 1, 4, 7, 2, 5, 8) so the controller has time to process one sector before the next one rotates under the head
- **Track skew** — The first sector of adjacent tracks is offset so the head doesn't miss sector 0 when switching tracks

```
Without track skew: With track skew:
Track 0: [0][1][2][3] Track 0: [0][1][2][3]
Track 1: [0][1][2][3] Track 1: [3][0][1][2] ← offset by 1
 (head arrives after track switch
 and catches sector 0 on time)
```

## Constant Linear Velocity vs Constant Angular Velocity

Disks can spin in two modes, affecting how data is distributed:

### Constant Angular Velocity (CAV)

The disk rotates at the **same speed** regardless of which track the head is on. This means:

- Outer tracks are physically longer but have the **same number of sectors** as inner tracks
- Sectors on outer tracks are larger (lower density)
- Simpler design — most HDDs use CAV

```
CAV: Same RPM everywhere

Outer track: [---S0---][---S1---][---S2---][---S3---] (wider sectors)
Inner track: [-S0-][-S1-][-S2-][-S3-] (narrower sectors)

Both tracks have same number of sectors, same rotation speed.
Outer track wastes potential capacity.
```

### Constant Linear Velocity (CLV)

The density of data is **uniform** across the disk. This means:

- Outer tracks have **more sectors** than inner tracks (because they are longer)
- The disk spins **slower** for outer tracks and **faster** for inner tracks to maintain constant data rate
- Used by CD-ROMs, DVDs, and Blu-ray drives

```
CLV: Variable RPM

Outer track: [S0][S1][S2][S3][S4][S5][S6][S7] (more sectors)
Inner track: [S0][S1][S2][S3] (fewer sectors)

Rotation speed adjusts so data passes the head at a constant rate.
More efficient use of disk surface area.
```

### Comparison

| Aspect                | CAV                                 | CLV                                 |
| :-------------------- | :---------------------------------- | :---------------------------------- |
| **Rotation speed**    | Constant (same RPM)                 | Variable (changes per track)        |
| **Sectors per track** | Same for all tracks                 | More on outer, fewer on inner       |
| **Data density**      | Lower on outer tracks               | Uniform across disk                 |
| **Space efficiency**  | Lower (wastes outer track capacity) | Higher (uses full surface)          |
| **Complexity**        | Simpler                             | More complex (variable speed motor) |
| **Used by**           | HDDs                                | CD-ROMs, DVDs, Blu-ray              |

**Zone Bit Recording (ZBR):** Modern HDDs use a hybrid approach — the disk is divided into zones, and outer zones have more sectors per track than inner zones, but within a zone, the RPM is constant. This gets many benefits of CLV while keeping CAV simplicity.

## Solid-State Drives (SSDs)

SSDs have no platters, heads, or mechanical parts. They use **NAND flash memory**.

```
SSD Structure:

+----------------------------------+
| SSD Controller |
| +-----------+ +-----------+ |
| | Flash | | Flash | |
| | Chip 0 | | Chip 1 | |
| | +-------+ | | +-------+ | |
| | | Block | | | | Block | | |
| | | +---+ | | | | +---+ | | |
| | | |Pg | | | | | |Pg | | | |
| | | +---+ | | | | +---+ | | |
| | +-------+ | | +-------+ | |
| +-----------+ +-----------+ |
+----------------------------------+

Page: smallest read/write unit (~4-16 KB)
Block: smallest erase unit (~256-512 KB, contains many pages)
```

| Aspect                | HDD                              | SSD                                |
| :-------------------- | :------------------------------- | :--------------------------------- |
| **Medium**            | Magnetic platters                | NAND flash memory                  |
| **Moving parts**      | Yes (heads, spindle)             | None                               |
| **Random access**     | Slow (seek + rotation)           | Fast (no mechanical delay)         |
| **Sequential access** | Good                             | Excellent                          |
| **Seek time**         | 3-15 ms                          | ~0.1 ms (electronic, no seek)      |
| **Wear**              | Mechanical wear                  | Limited write cycles per cell      |
| **Special concern**   | Bad sectors from physical damage | Wear leveling to distribute writes |

Because SSDs have no seek time or rotational latency, disk scheduling algorithms (FCFS, SSTF, SCAN) are largely irrelevant for SSDs.

## Disk Capacity Calculation

```
Disk Capacity = number_of_cylinders × heads_per_cylinder × sectors_per_track × bytes_per_sector

Example:
 Cylinders = 10,000
 Heads = 8
 Sectors per track = 200
 Bytes per sector = 512

 Capacity = 10,000 × 8 × 200 × 512
 = 8,192,000,000 bytes
 ≈ 7.63 GB
```

## Summary

| Concept                  | Key Point                                                                         |
| :----------------------- | :-------------------------------------------------------------------------------- |
| Physical structure       | Platters → surfaces → tracks → sectors; cylinder = same track across all surfaces |
| Logical Block Addressing | Disk seen as 1D array of blocks (0 to N-1); OS doesn't need physical geometry     |
| CHS to LBA mapping       | Block B → Cylinder = B/(S×H), Head = (B/S) mod H, Sector = B mod S                |
| CAV                      | Constant rotation speed; same sectors per track; used by HDDs                     |
| CLV                      | Variable rotation speed; more sectors on outer tracks; used by optical drives     |
| Zone Bit Recording       | Hybrid: zones with varying sectors/track but constant RPM within zones            |
| SSD                      | No moving parts; no seek time; limited write cycles; wear leveling needed         |

## Exam Tips

1. **CHS to LBA mapping formula** — frequently asks: "Given a disk with C cylinders, H heads, S sectors per track, map logical block B to its physical address." Practice the formula with numbers.
2. **CAV vs CLV** — Know the difference and which devices use each. This is a common 5-mark comparison question.
3. **Draw the physical disk structure** — Be able to draw platters, tracks, sectors, and cylinders. Label all parts clearly.
4. **Disk capacity calculation** — Practice: Cylinders × Heads × Sectors/track × Bytes/sector. Watch for unit conversions (bytes to GB).
5. **HDD vs SSD comparison** — Know why disk scheduling doesn't apply to SSDs (no seek time). This shows modern understanding.
6. **Sector interleaving and track skew** — Know why these exist (give controller processing time). May appear as a short-answer question.
