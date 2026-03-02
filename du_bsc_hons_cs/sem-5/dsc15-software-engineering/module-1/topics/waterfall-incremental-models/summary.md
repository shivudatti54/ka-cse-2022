# Waterfall & Incremental Models – Quick Revision (DU BSc Hons CS – NEP 2024 UGCF)

**Introduction**  
The Waterfall and Incremental models are two fundamental software‑process paradigms covered under **Unit III – Software Process Models** of the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus. Both describe how to organise, schedule, and control the activities that transform user requirements into a delivered product, but they differ in approach, flexibility, and risk handling.

---

### Waterfall Model (Linear‑Sequential)

- **Phase‑driven**: Requirements → Design → Implementation → Testing → Deployment → Maintenance.  
- **Documentation‑centric**: Each phase produces formal documents that become the input for the next.  
- **Gate‑based approval**: A phase must be completed and reviewed before the next begins (“gate” concept).  
- **Pros**  
  - Clear milestones; easy to manage and measure progress.  
  - Well‑suited for projects with stable, well‑defined requirements (e.g., regulatory or hardware‑driven software).  
- **Cons**  
  - Inflexible to changes; late discovery of faults can be costly.  
  - Long delivery time; no working software until the final phase.  

---

### Incremental Model (Iterative‑Enhancement)

- **Deliver in small, functional increments**: Each increment adds new functionality on top of a baseline.  
- **Combine waterfall phases within each increment**: Requirements, design, coding, and testing are performed repeatedly.  
- **Key variants**  
  - **Staged Delivery** – each increment is a fully functional sub‑system.  
  - **Prototype‑driven** – early increments are prototypes to refine requirements.  
- **Advantages**  
  - Faster time‑to‑market; user can evaluate early releases.  
  - Easier risk management; defects discovered earlier.  
- **Disadvantages**  
  - Requires careful planning of increment boundaries to avoid integration problems.  
  - May lead to “feature creep” if scope is not controlled.  

---

### Comparison at a Glance

| Aspect               | Waterfall                     | Incremental                   |
|----------------------|-------------------------------|-------------------------------|
| Flexibility          | Low (late changes costly)    | High (mid‑project changes)   |
| Time to First Release| End of project               | After first increment        |
| Risk                 | High (late testing)          | Lower (continuous testing)   |
| Documentation       | Extensive                    | Moderate (updated per increment) |
| Suitable for        | Stable requirements, small‑medium projects | Evolving requirements, large or time‑critical projects |

---

### Exam Tips (DU Syllabus)

- **Remember the顺序**: Waterfall’s linear flow is mirrored by the bullet points in the textbook (e.g., “Software Engineering” by Rajib Mall).  
- **Key phrases**: “document‑driven”, “phase‑gate”, “increments”, “prototype”, “risk‑reduction”.  
- **Short‑answer likely**: “List two advantages of the Incremental model over the Waterfall model.”  
- **Diagram**: Be ready to sketch a simple waterfall diagram and an incremental release timeline.

---

**Conclusion**  
The Waterfall model offers a disciplined, document‑centric pathway for projects with fixed requirements, while the Incremental model provides flexibility and faster user feedback through iterative delivery. Understanding their strengths, limitations, and appropriate contexts is essential for selecting the right process model in software engineering practice—and for scoring well in the DU exam.