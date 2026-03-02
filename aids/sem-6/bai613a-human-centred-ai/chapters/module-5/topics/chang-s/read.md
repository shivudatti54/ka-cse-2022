Of course. Here is a comprehensive educational note on "Chang S" for  Engineering students, tailored for the subject of Human-Centred AI.

# Module 5: Human-Centred AI - The Chang S. Framework

## Introduction to Chang S.

In the development of Human-Centred AI (HCAI), a critical challenge is ensuring that AI systems are not just technically proficient but also genuinely beneficial, trustworthy, and aligned with human values. The framework proposed by **Chang S.** (often cited in literature, with seminal work by researchers like **Chih-Hong Cheng** and colleagues) provides a structured, three-pillar approach to achieving this. It moves beyond mere performance metrics to focus on the entire human-AI interaction lifecycle. This framework is essential for engineers to design systems that are safe, reliable, and acceptable to users.

## Core Concepts: The Three Pillars of Chang S.

The Chang S. framework is built upon three interconnected pillars: **Sanctioning**, **Sensemaking**, and **Socialization**. These pillars address the lifecycle of an AI system from its initial design and validation to its deployment and long-term integration into society.

### 1. Sanctioning
**Sanctioning** refers to the formal process of **verification, validation, and certification** that an AI system must undergo before it is deployed. It's about obtaining official or societal "permission" for the AI to operate.

*   **Objective:** To ensure the AI system is **safe, reliable, and compliant** with predefined regulations, standards, and ethical guidelines.
*   **Engineering Focus:** This involves rigorous testing methodologies.
    *   **Verification:** "Did we build the system right?" Checking that the AI's implementation correctly matches its design specifications (e.g., testing code for bugs).
    *   **Validation:** "Did we build the right system?" Ensuring the AI model meets the intended user needs and requirements in real-world scenarios (e.g., achieving high accuracy on unseen data).
    *   **Certification:** Formally attesting that the system meets specific industry or legal standards (e.g., a safety standard for a medical AI device).

**Example:** Before an autonomous vehicle (AV) is allowed on public roads, it must be **sanctioned**. This involves millions of miles of simulated and real-world testing (verification/validation) to prove its decision-making is safe and finally receiving approval from a government transportation authority (certification).

### 2. Sensemaking
**Sensemaking** focuses on the human's ability to **understand, interpret, and trust** the AI's outputs and behavior. It deals with the explainability and transparency of AI systems.

*   **Objective:** To bridge the gap between the AI's complex internal processes and the human user's cognitive model. It empowers users to comprehend *why* an AI made a certain decision.
*   **Engineering Focus:** This involves implementing techniques like:
    *   **Explainable AI (XAI):** Methods such as LIME (Local Interpretable Model-agnostic Explanations) or SHAP (SHapley Additive exPlanations) that provide insights into model predictions.
    *   **User-Centric Design:** Creating interfaces that present explanations in an intuitive and actionable way for the end-user (e.g., a doctor using a diagnostic AI).

**Example:** A loan application is rejected by an AI. Instead of just a "rejected" message, the **sensemaking** pillar would require the system to provide a clear explanation: "Application denied due to high debt-to-income ratio (85%) and short credit history (2 years)." This allows the applicant to understand the reason and take corrective action.

### 3. Socialization
**Socialization** is the process of an AI system **integrating into society and adapting to its evolving norms, values, and rules** over its long-term operational lifespan. It acknowledges that context and societal acceptance are not static.

*   **Objective:** To ensure the AI remains relevant, fair, and trusted as societal values and regulations change. It involves continuous monitoring and learning.
*   **Engineering Focus:** This involves building systems capable of:
    *   **Continuous Learning & Adaptation:** Safely updating the model with new data to reflect changing real-world conditions (e.g., an AI moderating content must adapt to new slang and cultural contexts).
    *   **Feedback Loops:** Creating mechanisms for users and stakeholders to report issues, biases, or unexpected behaviors.
    *   **Auditing and Monitoring:** Continuously checking for performance drift, emerging biases, or compliance with new laws (e.g., new data privacy regulations).

**Example:** A facial recognition system initially deployed for building access might face **socialization** challenges as societal concerns about privacy grow. The engineering team must then adapt the system—perhaps by implementing stricter data governance, adding opt-out features, or shifting to a less invasive technology—to maintain its social license to operate.

## Interconnection of the Pillars

These pillars are not sequential but highly interdependent. A flaw in **Sanctioning** (e.g., an undiscovered bias) will cripple **Sensemaking** (as explanations will be based on a flawed model) and ultimately lead to a failure in **Socialization** (as society rejects the biased system). Effective HCAI requires a holistic approach that addresses all three pillars throughout the AI lifecycle.

## Key Points / Summary

| Pillar | Key Question | Engineering Focus |
| :--- | :--- | :--- |
| **Sanctioning** | Is this AI system safe and approved for use? | Verification, Validation, Certification (Pre-deployment) |
| **Sensemaking** | Can the user understand and trust the AI's output? | Explainability (XAI), Transparency, User Interface Design |
| **Socialization** | Does the AI continue to align with societal values over time? | Continuous Learning, Feedback Loops, Monitoring & Auditing |

*   The **Chang S. framework** provides a holistic structure for developing **Human-Centred AI**.
*   It emphasizes that technical excellence alone is insufficient; AI must be **verified**, **understandable**, and **socially adaptable**.
*   For engineers, this means designing systems with built-in capabilities for testing, explanation, and continuous adaptation based on human feedback.
*   Mastering this framework is crucial for building AI that is not only powerful but also responsible, ethical, and beneficial for humanity.