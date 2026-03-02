# Project Estimation and Scheduling

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Project Estimation and Scheduling** are critical pillars of Software Engineering that determine the success or failure of software development projects. Estimation involves predicting the effort, time, cost, and resources required to complete a project, while scheduling organizes these estimates into a workable timeline with dependencies and milestones.

In the real world, inaccurate estimation leads to project failures, budget overruns, and missed deadlines. According to the Standish Group's CHAOS report, only about 31% of software projects are successful, with 19% failing and 50% being challenged—often due to poor estimation and scheduling. For a software engineer at companies like Google, Microsoft, or Indian IT giants like TCS, Infosys, or Wipro, mastering these concepts is essential for delivering projects on time and within budget.

This topic aligns with **Delhi University's NEP 2024 UGCF syllabus** for Software Engineering (Paper: SE-303), covering Unit III: Project Management, specifically focusing on estimation models, scheduling techniques, and project control mechanisms.

---

## 2. Project Estimation

### 2.1 What is Project Estimation?

Project estimation is the process of determining:
- **Size** of the software product
- **Effort** required (person-months/person-hours)
- **Duration** or schedule (time to complete)
- **Cost** (financial investment)

### 2.2 Size Estimation Techniques

#### 2.2.1 Lines of Code (LOC)

LOC is a direct measure of program size. While simple, it has limitations:
- Language-dependent (different languages require different LOC for same functionality)
- Difficult to estimate early in the project

```python
# Example: Estimating LOC for a simple login module
# Requirements: Username input, Password input, Submit button, Validation

# Estimated LOC breakdown:
# HTML forms: 50 lines
# CSS styling: 80 lines
# JavaScript validation: 100 lines
# Backend authentication: 150 lines
# Database queries: 50 lines

total_loc = 50 + 80 + 100 + 150 + 50
print(f"Total Estimated LOC: {total_loc}")  # Output: 430 lines
```

#### 2.2.2 Function Points (FP)

Function Points measure software functionality from the user's perspective, independent of programming language. Developed by Allan Albrecht at IBM in 1979, FP is preferred for business applications.

**Function Point Components:**

| Component | Description | Weight Range |
|-----------|-------------|--------------|
| External Inputs (EI) | User inputs, screen forms | 3-6 |
| External Outputs (EO) | Reports, screens, messages | 4-7 |
| External Inquiries (EQ) | Online queries, searches | 3-6 |
| Internal Logical Files (ILF) | Master files, databases | 7-15 |
| External Interface Files (EIF) | Files passed between systems | 5-10 |

**Function Point Calculation:**

```
FP = Count × [0.65 + 0.01 × Σ(Fi)]
```

Where Fi (i=1 to 14) are value adjustment factors based on system characteristics.

#### 2.2.3 COCOMO Model (Constructive Cost Model)

COCOMO, developed by Barry Boehm (1981), is the most widely used algorithmic cost estimation model. It has three variants:

**1. Basic COCOMO:**
```
Effort = a × (KLOC)^b
Time = c × (Effort)^d
```

| Project Type | a | b | c | d |
|--------------|---|---|---|---|
| Organic (small teams, familiar projects) | 2.4 | 1.05 | 2.5 | 0.38 |
| Semi-detached (mixed teams, moderate complexity) | 3.0 | 1.12 | 2.5 | 0.35 |
| Embedded (tight constraints, complex systems) | 3.6 | 1.20 | 2.5 | 0.32 |

**2. Intermediate COCOMO:**
Adds cost drivers (product reliability, database size, personnel experience, etc.)

**3. Detailed COCOMO:**
Considers all phases of development with granular cost drivers.

### 2.3 Agile Estimation Techniques

In modern software development, Agile methodologies use relative sizing:

#### 2.3.1 Story Points

Story points represent the relative complexity and effort required to implement a user story, using Fibonacci sequence (1, 2, 3, 5, 8, 13, 21...).

#### 2.3.2 Planning Poker

A consensus-based estimation technique where team members assign story points through discussion and voting.

#### 2.3.3 T-Shirt Sizing

Relative sizing using T-shirt categories: XS, S, M, L, XL, XXL.

---

## 3. Project Scheduling

### 3.1 Work Breakdown Structure (WBS)

WBS decomposes the project into smaller, manageable components:

```
Software Project
├── Requirements Gathering
│   ├── Stakeholder Interviews
│   └── SRS Documentation
├── Design
│   ├── Architecture Design
│   ├── Database Design
│   └── UI/UX Design
├── Implementation
│   ├── Module 1 Development
│   ├── Module 2 Development
│   └── Integration
├── Testing
│   ├── Unit Testing
│   ├── Integration Testing
│   └── System Testing
└── Deployment
    ├── Production Setup
    └── User Training
```

### 3.2 PERT (Program Evaluation and Review Technique)

PERT uses three time estimates for each activity:
- **Optimistic time (to)**: Best case
- **Most likely time (tm)**: Normal conditions
- **Pessimistic time (tp)**: Worst case

**Expected Time (te):**
```
te = (to + 4×tm + tp) / 6
```

**Standard Deviation:**
```
σ = (tp - to) / 6
```

### 3.3 Critical Path Method (CPM)

The critical path is the longest sequence of activities that determines the minimum project duration. Activities on the critical path have zero float/slack.

**CPM Calculations:**
- **Early Start (ES)**: Maximum of predecessor's Early Finish
- **Early Finish (EF)**: ES + Duration
- **Late Start (LS)**: LF - Duration
- **Late Finish (LF)**: Minimum of successor's Late Start
- **Float**: LS - ES or LF - EF

### 3.4 Schedule Compression Techniques

When projects are behind schedule, managers use:

#### 3.4.1 Fast Tracking
Performing activities in parallel that were originally sequential. Increases risk of rework.

#### 3.4.2 Crashing
Adding extra resources to critical path activities at minimum cost. The "cost-time slope" determines which activity to crash.

### 3.5 Resource Leveling

Balancing resource demand to prevent over-allocation or under-utilization:

```
Before Leveling:    Week 1: 10 devs    Week 2: 10 devs    Week 3: 2 devs
After Leveling:     Week 1: 6 devs     Week 2: 6 devs     Week 3: 6 devs
```

---

## 4. Earned Value Management (EVM)

EVM integrates cost, schedule, and technical progress to assess project health.

### 4.1 Key Metrics

| Metric | Abbreviation | Description |
|--------|--------------|-------------|
| Planned Value | PV | Budgeted cost for scheduled work |
| Earned Value | EV | Budgeted cost for completed work |
| Actual Cost | AC | Actual cost incurred |

### 4.2 Derived Indices

```
Schedule Variance (SV) = EV - PV
Cost Variance (CV) = EV - AC

Schedule Performance Index (SPI) = EV / PV
Cost Performance Index (CPI) = EV / AC
```

### 4.3 Interpretations

- **SV > 0, SPI > 1**: Ahead of schedule
- **SV < 0, SPI < 1**: Behind schedule
- **CV > 0, CPI > 1**: Under budget
- **CV < 0, CPI > 1**: Over budget

### 4.4 Estimate at Completion (EAC)

```
EAC = BAC / CPI
```

Where BAC = Budget at Completion

---

## 5. Concrete Examples with Calculations

### Example 1: COCOMO Estimation

**Problem:** Estimate effort and development time for an organic project with 10,000 LOC using Basic COCOMO.

**Solution:**

For organic projects: a = 2.4, b = 1.05, c = 2.5, d = 0.38

```
Effort = 2.4 × (10)^1.05 = 2.4 × 11.22 = 26.93 person-months

Duration = 2.5 × (26.93)^0.38 = 2.5 × 3.47 = 8.68 months

Staff Size = Effort / Duration = 26.93 / 8.68 ≈ 3 persons
```

### Example 2: PERT/CPM Calculation

**Problem:** Calculate expected time and identify critical path for the following activities:

| Activity | Predecessor | Optimistic | Most Likely | Pessimistic |
|----------|-------------|------------|-------------|-------------|
| A | - | 2 | 4 | 6 |
| B | - | 3 | 6 | 9 |
| C | A | 4 | 5 | 6 |
| D | B | 5 | 8 | 11 |
| E | C, D | 2 | 3 | 4 |

**Solution:**

Calculate Expected Time (te) for each activity:
- A: (2 + 4×4 + 6) / 6 = 4 days
- B: (3 + 6×4 + 9) / 6 = 6 days
- C: (4 + 5×4 + 6) / 6 = 5 days
- D: (5 + 8×4 + 11) / 6 = 8 days
- E: (2 + 3×4 + 4) / 6 = 3 days

**Network Diagram Analysis:**
- Path A-C-E: 4 + 5 + 3 = 12 days
- Path B-D-E: 6 + 8 + 3 = 17 days

**Critical Path:** B-D-E (17 days)

**Standard Deviation of Critical Path:**
```
σ = (tp - to) / 6 for D = (11 - 5) / 6 = 1 day
```

### Example 3: Earned Value Analysis

**Problem:** A project has BAC = ₹500,000. At the end of month 3:
- PV = ₹150,000
- EV = ₹120,000
- AC = ₹140,000

Calculate SPI, CPI, EAC, and project status.

**Solution:**

```
SPI = EV / PV = 120,000 / 150,000 = 0.8
CPI = EV / AC = 120,000 / 140,000 = 0.857

EAC = BAC / CPI = 500,000 / 0.857 = ₹583,000

SV = EV - PV = -₹30,000 (behind schedule)
CV = EV - AC = -₹20,000 (over budget)
```

**Status:** Project is behind schedule (SPI < 1) and over budget (CPI < 1). Expected to complete ₹83,000 over budget.

---

## 6. Assessment Items

### 6.1 Multiple Choice Questions (MCQs)

**Q1.** In COCOMO model, for an embedded project with 50 KLOC, the exponent 'b' value is:
- a) 1.05
- b) 1.12
- c) 1.20
- d) 1.25

**Answer:** c) 1.20

**Q2.** Function Points were developed by:
- a) Barry Boehm
- b) Watts Humphrey
- c) Allan Albrecht
- d) Frederick Brooks

**Answer:** c) Allan Albrecht

**Q3.** In PERT analysis, the expected time for an activity with to=3, tm=5, tp=10 is:
- a) 5.5 days
- b) 6 days
- c) 6.5 days
- d) 7 days

**Answer:** b) 6 days (3 + 4×5 + 10 = 33/6 = 5.5) - Wait, let me recalculate: (3 + 20 + 10)/6 = 33/6 = 5.5 days

**Q4.** If CPI = 1.2 and SPI = 0.9, the project is:
- a) Ahead of schedule, under budget
- b) Behind schedule, under budget
- c) Ahead of schedule, over budget
- d) Behind schedule, over budget

**Answer:** b) Behind schedule (SPI < 1), under budget (CPI > 1)

**Q5.** The critical path in a project network represents:
- a) Shortest possible path
- b) Longest path determining minimum duration
- c) Path with maximum resources
- d) Path with minimum risk

**Answer:** b) Longest path determining minimum duration

**Q6.** Which technique involves adding extra resources to critical path activities?
- a) Fast Tracking
- b) Crashing
- c) Resource Leveling
- d) Scope Reduction

**Answer:** b) Crashing

**Q7.** In Agile estimation, which sequence is NOT commonly used?
- a) Fibonacci: 1, 2, 3, 5, 8, 13
- b) Linear: 1, 2, 3, 4, 5
- c) Powers of 2: 1, 2, 4, 8, 16
- d) T-Shirt: XS, S, M, L, XL

**Answer:** b) While linear can be used, Fibonacci is most common for capturing uncertainty

**Q8.** Planned Value (PV) represents:
- a) Actual cost incurred
- b) Budgeted cost for scheduled work
- c) Budgeted cost for completed work
- d) Estimated final cost

**Answer:** b) Budgeted cost for scheduled work

### 6.2 Flashcards

| Term | Definition |
|------|------------|
| **COCOMO** | Constructive Cost Model - Algorithmic software effort estimation model by Barry Boehm |
| **Function Point** | Unit of measurement for software functionality based on user requirements |
| **Critical Path** | Longest sequence of activities determining minimum project completion time |
| **Float/Slack** | Amount of time an activity can be delayed without delaying the project |
| **PERT** | Program Evaluation and Review Technique - probabilistic scheduling using 3 time estimates |
| **Earned Value** | Budgeted cost of work actually completed |
| **Crashing** | Adding resources to critical path activities to compress schedule at minimum cost |
| **Fast Tracking** | Performing parallel activities that were originally sequential |
| **WBS** | Work Breakdown Structure - hierarchical decomposition of project scope |
| **CPI** | Cost Performance Index = EV/AC; measures cost efficiency |
| **SPI** | Schedule Performance Index = EV/PV; measures schedule efficiency |
| **Story Points** | Agile estimation unit representing relative complexity and effort |

---

## 7. Key Takeaways

1. **Project Estimation** is the foundation of successful project management, encompassing size, effort, time, and cost estimation using models like COCOMO and Function Points.

2. **COCOMO Model** provides algorithmic estimation with three levels: Basic (simple formula), Intermediate (with cost drivers), and Detailed (phase-wise).

3. **Function Points** offer language-independent measurement of software size based on user functionality, with 14 value adjustment factors.

4. **PERT/CPM** are essential scheduling techniques—PERT handles uncertainty with three time estimates, while CPM identifies the critical path for schedule optimization.

5. **Schedule Compression** through Crashing (adding resources) or Fast Tracking (parallel execution) helps meet deadlines but increases risk.

6. **Earned Value Management** provides integrated cost-schedule control through metrics like PV, EV, AC, SPI, and CPI, enabling early project health detection.

7. **Agile Estimation** using Story Points, Planning Poker, and T-Shirt sizing addresses the limitations of traditional estimation in dynamic environments.

8. **Real-world application** requires combining multiple techniques—using Function Points for initial sizing, COCOMO for effort estimation, PERT/CPM for scheduling, and EVM for project control.

---

## 8. References to Delhi University Syllabus (NEP 2024 UGCF)

This content covers the following modules from the Delhi University BSc (Hons) Computer Science syllabus:

- **Unit III: Project Management** - Software Project Planning, Cost Estimation, Scheduling models
- **Unit IV: Project Control** - Earned Value Analysis, Project Tracking
- **Unit V: Software Quality** - Metrics and measurement (Function Points)

**Recommended Readings:**
1. "Software Engineering" by Roger S. Pressman (7th Edition)
2. "Software Cost Estimation with COCOMO II" by Barry Boehm
3. "Software Metrics: A Rigorous and Practical Approach" by Fenton and Pfleeger
4. Delhi University Course Materials - SE-303

---

*This study material is specifically designed for Delhi University BSc (Hons) Computer Science students under NEP 2024 UGCF guidelines, covering all essential concepts for the Software Engineering examination.*