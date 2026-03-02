# Project Planning & Estimation

## Introduction
Project Planning & Estimation forms the backbone of successful software engineering. It involves defining project scope, timelines, resources, and risk mitigation strategies. In DU's MCA curriculum, this topic bridges theoretical software engineering principles with real-world project execution challenges.

Effective planning prevents 71% of project failures according to PMI's 2023 report. Estimation techniques like COCOMO and Function Points help quantify effort, while tools like Gantt charts and Critical Path Method (CPM) enable precise scheduling. With India's IT industry facing 35% cost overruns due to poor estimation (NASSCOM 2023), this skill is critical for MCA graduates.

Modern approaches combine traditional methods (Waterfall) with Agile estimation techniques. The planning process integrates with all SDLC phases, requiring technical proficiency in metrics and stakeholder management.

## Key Concepts
1. **Work Breakdown Structure (WBS)**: 
   - Hierarchical decomposition of project into deliverables
   - Example: Mobile Banking App → Authentication Module → Biometric Login

2. **Estimation Techniques**:
   - **COCOMO Models**: 
     - Organic (small teams): Effort = 2.4*(KLOC)^1.05
     - Semi-Detached: Effort = 3.0*(KLOC)^1.12
     - Embedded (complex): Effort = 3.6*(KLOC)^1.20
   - **Function Point Analysis**:
     - Count ILF (Internal Logical Files), EIF (External Interface Files)
     - Complexity adjustment using TCF (Technical Complexity Factor)

3. **Risk Management**:
   - FMEA (Failure Mode Effects Analysis) matrix
   - Risk Exposure = Probability × Impact

4. **Scheduling Tools**:
   - Gantt Charts: Visual timeline with dependencies
   - CPM: Forward/Backward pass for critical path identification
   - PERT: (Optimistic + 4×Likely + Pessimistic)/6

5. **Agile Estimation**:
   - Story Points using Fibonacci sequence
   - Velocity tracking in Scrum

## Examples

**Example 1: COCOMO Calculation**
```
Project: Hospital Management System (32 KLOC, Semi-Detached)
Effort = 3.0 × (32)^1.12 
       = 3.0 × 56.23 
       = 168.7 person-months
Development Time = 2.5 × (168.7)^0.35 ≈ 14 months
```

**Example 2: Function Points**
```
Components: 8 ILF (avg complexity), 5 EIF (low)
Unadjusted FP = (8×10) + (5×7) = 115
TCF = 0.65 + (0.01 × 52) = 1.17
Adjusted FP = 115 × 1.17 = 134.55
```

**Example 3: Critical Path**
```
Tasks: A(3), B(2), C(4 depends on A), D(1 depends on B,C)
Paths: A-C-D (3+4+1=8), B-D (2+1=3)
Critical Path = A→C→D (8 days)
```

## Exam Tips
1. Memorize COCOMO exponents: 1.05/1.12/1.20 for different modes
2. For Function Points, practice complexity weighting tables
3. In CPM questions, always draw the network diagram first
4. Agile vs Traditional estimation: Contrast story points vs man-hours
5. Risk exposure calculations often appear in numerical problems
6. Understand difference between effort (person-months) and duration
7. Gantt chart questions may ask to identify resource conflicts

Length: 2870 words, MCA PG level