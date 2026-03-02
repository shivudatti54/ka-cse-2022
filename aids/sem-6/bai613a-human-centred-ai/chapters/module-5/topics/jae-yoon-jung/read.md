Of course. Here is a comprehensive educational module on Jae-Yoon Jung's work in Human-Centred AI, tailored for  engineering students.

***

### **Module 5: Human-Centred AI - The Work of Jae-Yoon Jung**

#### **1. Introduction: Why Focus on the Human?**

In the race to develop increasingly powerful AI, a critical question often emerges: are we building systems *for* people, or are we forcing people to adapt *to* the systems? **Human-Centred AI (HCAI)** is a framework that insists on the former. It advocates for AI that amplifies human capabilities, respects human autonomy, and is understandable and trustworthy.

A leading thinker in this domain is **Jae-Yoon Jung**, a Professor at Seoul National University. His research provides a crucial bridge between raw AI capabilities and practical, usable human-AI collaboration. For engineers, understanding his work is essential for moving beyond technical performance metrics (like accuracy or F1-score) to designing systems that are truly effective in real-world scenarios.

---

#### **2. Core Concepts: From Automation to Amplification**

Jung's work often centers on moving AI from a role of pure **automation** to one of **amplification**. He argues that the goal should not be to replace human intelligence but to augment it. His research can be broken down into three key pillars:

**a) Mixed-Initiative User Interfaces (MIUI)**
This is a core concept in Jung's work. In a traditional system, the initiative is one-sided: either the user commands the computer (user-initiative) or the computer automates a task completely (system-initiative).

*   **Mixed-Initiative** systems create a fluid dialogue where both the human and the AI can start, interrupt, and complete tasks collaboratively.
*   **How it works:** The AI might suggest a next step (e.g., "Would you like to filter these results by date?"), but the human retains ultimate control, able to accept, modify, or ignore the suggestion.
*   **Engineering Implication:** This requires designing AI not just as a black-box solver, but as a cooperative agent that can explain its suggestions and reason about the user's goals.

**b) Explainable AI (XAI) and Interpretable Systems**
Jung emphasizes that for humans to trust and collaborate effectively with AI, they must understand its reasoning. This is not about showing the complex math of a deep learning model but providing **interpretable explanations** tailored to the context.

*   **Example:** A medical AI diagnosing a tumor shouldn't just output "Malignant, 92% confidence." Following Jung's principles, it should highlight the specific regions in the scan that contributed most to the decision (e.g., "The spiculated margins and irregular shape of this region are strong indicators of malignancy"). This allows the radiologist to validate the AI's reasoning using their own expertise.

**c) Proactive and Task-Based Support**
Jung's research explores how AI can be **proactive**—anticipating user needs based on context—without being intrusive. This is often framed around supporting high-level user tasks rather than just low-level functions.

*   **Example:** Consider a design software.
    *   *Reactive AI:* You use a blur tool, and the AI helps you adjust the blur radius perfectly.
    *   *Proactive AI (Jung's approach):* The AI analyzes the image you're working on and your current task (e.g., creating a background). It might proactively suggest: "Based on your composition, applying a depth-of-field blur to these layers might help the subject pop. Would you like to try it?" The user can then accept or refine this high-level suggestion.

---

#### **3. A Practical Example: AI-Assisted Document Editing**

Let's design a feature using Jung's principles for a tool like Google Docs or Microsoft Word.

1.  **Automation (The Old Way):** A grammar AI automatically corrects all perceived errors. The user is confused when their intentionally informal language is "fixed," and they feel a loss of control.
2.  **Amplification (Jung's Way):**
    *   **Mixed-Initiative:** The AI underlines a potentially awkward phrase and adds a comment: "This sentence is in the passive voice. It could be stronger in the active voice. [See suggestion]". The user clicks to see the suggested edit and can **choose to accept, ignore, or edit the suggestion further.**
    *   **Explainable:** The explanation is clear and task-oriented ("stronger writing"), not technical ("passive voice construction detected").
    *   **Proactive:** The AI might analyze the document's structure and suggest: "Your second section lacks a topic sentence. Would you like help generating one based on the content below?" This supports the user's high-level task of writing a coherent document, not just fixing spelling.

---

#### **4. Key Takeaways & Summary**

| Key Concept | Description | Engineering Goal |
| :--- | :--- | :--- |
| **Amplification over Automation** | Design AI to augment human skills, not replace them. | Create collaborative tools, not autonomous replacements. |
| **Mixed-Initiative Interaction** | Enable a fluid dialogue where both human and AI can make suggestions. | Build systems that can propose, explain, and defer to the user. |
| **Explainability (XAI)** | Provide understandable reasons for AI outputs tailored to the user's context. | Move beyond accuracy metrics to design for trust and understanding. |
| **Proactive Task-Support** | Anticipate user needs based on their high-level goals and current context. | Develop AI that understands user intent, not just executes commands. |

**For the  Engineer:** Jung's work teaches us that the most "intelligent" system is not the one with the highest accuracy on a benchmark dataset, but the one that most effectively empowers its human user. As you design AI systems, always ask: "How does this increase the user's capability? How does it ensure they remain in control and understand what is happening?" This is the essence of Human-Centred AI.