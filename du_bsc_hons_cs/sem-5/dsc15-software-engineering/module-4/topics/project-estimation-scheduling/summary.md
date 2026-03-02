# Project Estimation & Scheduling — Quick Revision Notes

## BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

### Introduction

Project Estimation and Scheduling are critical phases in software project management that determine a project's feasibility, resource requirements, and delivery timeline. Accurate estimation and effective scheduling are essential for successful software development, helping teams deliver projects on time and within budget.

---

### Key Concepts

#### **Project Estimation**
- **Purpose**: Predict the effort (person-months), time, and cost required to complete a software project
- **Types of Estimates**:
  - Preliminary/Order of Magnitude ( ±50%)
  - Budgetary (±25%)
  - Definitive (±10%)

#### **Estimation Techniques**

- **Expert Judgment**: Based on experience of senior team members
- **Delphi Technique**: Iterative consensus among experts; reduces bias
- **Analogy-Based Estimation**: Comparing with similar past projects
- **Parametric Models**: Use mathematical formulas (e.g., COCOMO)
- **Function Point (FP) Analysis**: Measures software size based on functionality
- **Use Case Points (UCP)**: Estimates from use case specifications
- **COCOMO Model** (Basic/Intermediate/Detailed):
  - **Effort = a × (KLOC)^b × Product Factor**
  - **Time = c × (Effort)^d**
  - Constants a,b,c,d vary by project type (organic, semi-detached, embedded)

#### **Project Scheduling**

- **Purpose**: Define when project activities will be performed and who will perform them
- **Milestones**: Key deliverables or events with zero duration
- **Task Dependencies**:
  - Finish-to-Start (most common)
  - Start-to-Start
  - Finish-to-Finish
  - Start-to-Finish

#### **Scheduling Techniques**

- **Gantt Chart**: Bar chart showing tasks vs. time; simple visualization
- **PERT (Program Evaluation & Review Technique)**:
  - **Optimistic (O) + 4×Most Likely (M) + Pessimistic (P) / 6**
  - Used for uncertain task durations
- **Critical Path Method (CPM)**:
  - Identifies longest path of dependent tasks
  - Determines minimum project duration
  - Critical activities have zero float/slack

#### **Resource Allocation**
- Assigning personnel, equipment, and budget to project tasks
- Resource leveling balances workload
- Over-allocation must be avoided

#### **Estimation vs Scheduling**
- **Estimation**: "How much?" (effort, cost, size)
- **Scheduling**: "When?" (timeline, milestones)

---

### Important Formulas

- **Productivity**: Effort / Person-Months
- **Schedule Variance**: Planned Progress - Actual Progress
- **Cost Variance**: Earned Value - Actual Cost

---

### Conclusion

Project estimation and scheduling are foundational to software engineering project success. Students should master techniques like COCOMO, Function Points, PERT, and CPM for accurate predictions. Effective scheduling ensures timely delivery, resource optimization, and project control—essential skills for professional software development.

---

*Reference: Delhi University BSc (Hons) CS Syllabus — Software Engineering (NEP 2024 UGCF)*