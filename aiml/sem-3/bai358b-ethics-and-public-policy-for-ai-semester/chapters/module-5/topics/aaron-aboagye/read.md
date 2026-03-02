Of course. Here is comprehensive educational content on Aaron Aboagye, tailored for  engineering students.

***

# Module 5: Case Study - Aaron Aboagye: Algorithmic Bias in Criminal Justice

**Subject:** Ethics and Public Policy for AI
**Semester:** As per your curriculum

## Introduction

For engineers building AI systems, understanding real-world consequences is paramount. The case of Aaron Aboagye is a stark, real-life example of how algorithmic bias can directly impact human lives, particularly within the U.S. criminal justice system. This case study moves beyond abstract ethical principles and demonstrates the tangible harm that can occur when predictive algorithms are trained on biased historical data. It serves as a critical lesson for engineers on the importance of fairness, transparency, and accountability in AI design and deployment.

## Core Concepts Explained

### 1. The COMPAS Algorithm

At the heart of this case is the Correctional Offender Management Profiling for Alternative Sanctions (COMPAS) algorithm. Developed by Northpointe (now Equivant), COMPAS is a risk assessment tool designed to predict the likelihood of a defendant **recidivating**—that is, committing another crime in the future.

*   **How it works:** The algorithm uses a questionnaire with over 100 factors, including criminal history, social background, and behavioral questions, to generate a "risk score" on a scale of 1 to 10.
*   **Its intended use:** To assist judges in making more informed decisions about bail, sentencing, and parole by providing a data-driven assessment of risk.

### 2. Algorithmic Bias and Disparate Impact

The central ethical issue in Aboagye's case is **algorithmic bias**. This occurs when a system produces systematically unfair outcomes that disadvantage a particular group. Importantly, this bias is often not a result of malicious intent but is embedded in the data itself.

*   **Historical Data Bias:** COMPAS was trained on historical crime data. If this data reflects existing societal biases (e.g., over-policing in certain neighborhoods, racial disparities in arrest rates), the algorithm will learn and perpetuate these patterns.
*   **Disparate Impact:** A 2016 investigation by ProPublica found that COMPAS was twice as likely to falsely label Black defendants as high-risk compared to White defendants. Conversely, it was more likely to falsely label White defendants as low-risk. This is a classic example of **disparate impact**—where a seemingly neutral procedure (an algorithm) has a disproportionately adverse effect on a protected group (Black defendants).

### 3. The Case of Aaron Aboagye

Aaron Aboagye, a Black man in Broward County, Florida, was arrested in 2013 for allegedly stealing a chainsaw and grill from a home depot, worth less than $1,100. Despite having no prior criminal convictions, the COMPAS algorithm scored him a 8 out of 10 for "recidivism risk" and a 6 out of 10 for "violence risk." These high-risk scores likely influenced the judge's decision to set his bail at an unaffordable $5,500. Unable to pay, Aboagye spent **88 days in jail** awaiting trial for a non-violent, low-level offense. The charges were eventually dropped.

This case highlights a critical failure:
*   **Lack of Transparency (The "Black Box" Problem):** The proprietary nature of COMPAS meant neither Aboagye nor his lawyers could effectively challenge the algorithm's score or understand how it was derived.
*   **Conflation of Prediction with Punishment:** A prediction about *future behavior* was used to justify a *current punishment* (pretrial detention), violating the presumption of innocence.

## Example: How Bias Manifests

Imagine two defendants, both 20-year-old males arrested for the same non-violent theft.
*   **Defendant A (White):** Lives in a well-off suburb, has a friend who was arrested once. COMPAS score: **3 (Low Risk)**.
*   **Defendant B (Black):** Lives in an under-policed urban area, has several neighbors who have been arrested. COMPAS score: **8 (High Risk)**.

The algorithm uses zip code and social circles as proxies. Because historical data shows higher arrest rates in Defendant B's zip code, the algorithm infers higher risk, perpetuating the cycle of disadvantage. Defendant A gets released on low bail, while Defendant B sits in jail, potentially losing his job and family stability, which ironically may *increase* his actual future risk.

## Key Points & Summary

| Key Point | Explanation | Engineering Implication |
| :--- | :--- | :--- |
| **Bias in, Bias out** | AI systems amplify biases present in their training data. | Engineers must critically audit and preprocess training datasets for historical bias. |
| **Transparency is Crucial** | "Black box" algorithms undermine justice and due process. | Prioritize explainable AI (XAI) and demand transparency, especially in high-stakes domains. |
| **Context Matters** | A tool designed for "assistance" can easily become a tool for "automation" of bias. | Understand the socio-political context of deployment. Build systems for human oversight, not replacement. |
| **Real-World Harm** | Algorithmic bias is not an academic concern; it leads to unjust incarceration, loss of liberty, and reinforced inequality. | Ethical design is a non-negotiable part of the engineering process. |

**Summary:** The Aaron Aboagye case is a foundational lesson in AI ethics. It demonstrates that technical proficiency alone is insufficient. Engineers have a profound responsibility to ensure their creations are fair, transparent, and just. Building ethical AI requires proactive measures—diverse training data, rigorous bias testing, and explainable models—to prevent powerful algorithms from automating and scaling historical injustices.