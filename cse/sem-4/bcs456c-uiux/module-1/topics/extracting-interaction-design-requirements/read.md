# Extracting Interaction Design Requirements

## Table of Contents

- [Extracting Interaction Design Requirements](#extracting-interaction-design-requirements)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Understanding Interaction Design Requirements](#understanding-interaction-design-requirements)
  - [User Research Methods](#user-research-methods)
  - [Persona Creation](#persona-creation)
  - [User Scenarios and User Stories](#user-scenarios-and-user-stories)
  - [Task Analysis](#task-analysis)
  - [Use Case Development](#use-case-development)
  - [User Journey Mapping](#user-journey-mapping)
- [Examples](#examples)
  - [Example 1: E-Commerce Checkout Redesign](#example-1-e-commerce-checkout-redesign)
  - [Example 2: Healthcare Appointment App](#example-2-healthcare-appointment-app)
  - [Example 3: Banking Application Redesign](#example-3-banking-application-redesign)
- [Exam Tips](#exam-tips)

## Introduction

Extracting interaction design requirements is a fundamental phase in the user-centered design process that bridges the gap between user needs and technical implementation. In the context of UI/UX design, this process involves systematically gathering, analyzing, and documenting the specific requirements that define how users will interact with a digital product. This phase precedes the actual design and development work and serves as the foundation upon which all subsequent design decisions are made.

The importance of properly extracting interaction design requirements cannot be overstated. According to industry research, nearly 50% of software projects fail due to poorly defined requirements, leading to expensive redesigns, user dissatisfaction, and project delays. For interaction design specifically, understanding user behaviors, motivations, and pain points through structured requirements extraction ensures that the final product meets actual user needs rather than assumed requirements. This is particularly critical in today's digital landscape where users expect intuitive, seamless interactions across all platforms.

In the the syllabus for BCS456C (UI/UX), this topic forms the critical first step in the design thinking process. Students must understand that requirements extraction is not merely a checklist activity but a comprehensive research endeavor that combines qualitative and quantitative methods to build a complete picture of the target users and their interaction needs. The deliverables from this phase—including user personas, scenarios, use cases, and requirement specifications—directly inform the design solutions that follow.

## Key Concepts

### Understanding Interaction Design Requirements

Interaction design requirements encompass all the specifications that define how a system should behave from the user's perspective. These requirements typically include functional requirements (what the system should do), non-functional requirements (performance, usability, reliability), and interaction requirements (how users accomplish tasks). The key distinction in interaction design is that requirements are always viewed through the lens of user goals and tasks rather than technical capabilities alone.

Requirements in interaction design can be categorized into three main types: user requirements (what users need to achieve), system requirements (how the system should respond to user actions), and design requirements (constraints and guidelines for the interface). Each category requires different extraction techniques and yields different deliverables. Understanding this categorization helps designers approach requirements gathering with the right mindset and methodology.

### User Research Methods

The primary methods for extracting interaction design requirements include user interviews, surveys, observation (contextual inquiry), focus groups, and document analysis. Each method has its strengths and limitations, and experienced designers typically employ multiple methods in combination to ensure comprehensive requirements gathering.

**User Interviews** are one-on-one conversations with potential users that provide deep insights into user needs, motivations, and pain points. Conducting effective interviews requires careful planning, including defining interview objectives, creating an interview guide, selecting appropriate participants, and analyzing the collected data systematically. Interviews are particularly valuable for understanding the "why" behind user behaviors and uncovering requirements that users themselves may not consciously recognize.

**Surveys** enable gathering quantitative data from large user samples, making them ideal for identifying patterns and trends across a broad user base. Well-designed surveys include both closed-ended questions (for quantitative analysis) and open-ended questions (for qualitative insights). The key to effective survey design is ensuring questions are clear, unbiased, and directly tied to design objectives.

**Contextual Inquiry and Observation** involve observing users in their natural environment as they perform relevant tasks. This method reveals the actual context of use, including environmental factors, workarounds users have developed, and real-world pain points that users might not mention in interviews. This ethnographic approach provides rich, contextual data that purely retrospective methods cannot capture.

**Focus Groups** bring together 6-10 users to discuss specific topics, generating ideas and revealing consensus or disagreement among user groups. While valuable for generating ideas and understanding social dynamics, focus groups require skilled moderation to prevent groupthink and ensure all participants contribute.

### Persona Creation

Personas are fictional representations of target users created based on research data. They synthesize user research findings into concrete, relatable characters that keep design teams focused on real user needs throughout the development process. A well-crafted persona includes demographic information, goals, motivations, frustrations, and behavioral patterns.

Creating effective personas requires analyzing user research data to identify distinct user groups (segmentation), then developing representative profiles for each segment. The key is to create personas that are specific enough to guide design decisions but not so detailed that they become unrealistic. Best practices include giving personas names and photos to make them memorable, limiting the number of personas to 3-5 per product, and ensuring personas are based on actual research data rather than assumptions.

### User Scenarios and User Stories

User scenarios describe specific situations in which users interact with the product to achieve their goals. They provide narrative descriptions that help designers understand the context, user actions, and system responses. A well-written scenario includes the user persona, the context or situation, the user's goal, and the steps taken to achieve that goal.

User stories, derived from Agile methodologies, follow the format: "As a [type of user], I want [goal] so that [benefit]." This format keeps the focus on user needs while clearly articulating the value delivered. User stories are particularly useful for prioritizing requirements and ensuring that development efforts align with user value.

### Task Analysis

Task analysis is a systematic examination of how users accomplish specific goals, breaking down tasks into their component steps, decisions, and information needs. This technique helps designers understand the cognitive and physical processes involved in user interactions, enabling them to design interfaces that support natural user workflows.

There are several approaches to task analysis, including hierarchical task analysis (breaking tasks into subtasks), cognitive task analysis (understanding mental processes), and entity-based task analysis (identifying objects and actions). The choice of approach depends on the nature of the tasks and the design questions being addressed.

### Use Case Development

Use cases describe system interactions from the user's perspective, specifying what happens when users interact with the system to accomplish specific goals. A use case typically includes the actor (user), the system, the trigger event, the main flow of events, alternative flows, and postconditions.

Use cases serve as a bridge between user requirements and technical specifications, helping translate abstract user needs into concrete system behaviors. They are particularly valuable for identifying edge cases, error conditions, and system boundaries early in the design process.

### User Journey Mapping

User journey maps visualize the sequence of interactions a user has with a product over time, from initial awareness through ongoing use. These maps capture the user's emotions, pain points, and opportunities at each stage of the journey, providing a holistic view of the user experience.

Creating effective journey maps requires defining the scope (which stages to include), gathering data about user behaviors and emotions at each stage, and synthesizing this information into a visual format that reveals patterns and opportunities for improvement.

## Examples

### Example 1: E-Commerce Checkout Redesign

Consider a scenario where a design team is tasked with improving the checkout process for an e-commerce website. The requirements extraction phase would proceed as follows:

**Step 1: User Interviews** - The team conducts 15 interviews with users who have abandoned carts in the past. Key findings include: users abandon when forced to create accounts (12/15), users want multiple payment options (14/15), users are concerned about security (11/15), and users find shipping costs at the end frustrating (13/15).

**Step 2: Survey** - A survey of 500 users confirms these patterns quantitatively and reveals additional insights: 67% prefer guest checkout, 82% consider trust badges important, and mobile users abandon at 1.5x the rate of desktop users.

**Step 3: Persona Creation** - Based on this research, the team creates two primary personas: "Quick Shopper Karen" (values speed, prefers guest checkout, price-sensitive) and "Researcher Raj" (thorough, wants detailed product info, loyalty program member).

**Step 4: Task Analysis** - The team breaks down the checkout task into steps: browse → add to cart → review cart → enter shipping → select payment → confirm order → receive confirmation. Analysis reveals that "review cart" and "enter shipping" have the highest abandonment rates.

**Step 5: Use Cases** - Primary use cases include "Guest Checkout," "Returning Customer Login," "Save Cart for Later," and "Apply Discount Code."

These extracted requirements directly inform design decisions: implement guest checkout, show shipping costs early, add trust badges, optimize for mobile, and provide multiple payment options.

### Example 2: Healthcare Appointment App

For a healthcare appointment booking application, requirements extraction might involve:

**User Interviews with Patients**: Understanding that elderly patients prefer larger buttons and simpler navigation, while younger patients want appointment reminders and integration with calendar apps.

**Contextual Inquiry**: Observing patients at clinic reception reveals pain points: long wait times, confusion about which department to visit, difficulty reaching the clinic by phone.

**Persona Development**: Creating personas like "Tech-Savvy Tina" (35, prefers app booking) and "Traditional Tom" (70, prefers phone booking or in-person visits).

**User Journey Mapping**: Mapping the patient journey from "feeling unwell" → "searching for care" → "booking appointment" → "attending appointment" → "follow-up care," identifying opportunities at each touchpoint.

The extracted requirements include: accessibility features (WCAG compliance), phone booking option as alternative, integration with health insurance systems, appointment reminder notifications, and simplified department navigation.

### Example 3: Banking Application Redesign

**Research Methods**: The team combines analytics data review (identifying where users drop off), competitive analysis (examining other banking apps), and user interviews.

**Key Findings**: Users find the current interface cluttered (78%), cannot easily locate transaction history (65%), and want better bill payment features (82%).

**Requirements Specification**: The team documents specific requirements:

- Requirement 1: Implement cardless ATM withdrawal feature
- Requirement 2: Add spending categorization and visualization
- Requirement 3: One-tap bill payment with scheduled payments
- Requirement 4: Simplified navigation with maximum 3 taps to any feature
- Requirement 5: Biometric authentication option

These requirements are prioritized using MoSCoW method (Must have, Should have, Could have, Won't have) and form the basis for the redesign specification.

## Exam Tips

1. **Remember the distinction between user research methods**: Be clear about when to use each method—interviews for depth, surveys for breadth, observation for context, and focus groups for group dynamics and idea generation.

2. **Know the components of a persona**: A complete persona includes name, photo, demographic details, goals, motivations, frustrations, behavioral traits, and a brief narrative description. Understand how to create effective personas from research data.

3. **Understand user story format**: Remember the "As a [user], I want [goal], so that [benefit]" format. This is frequently tested in university exams and is essential for requirements documentation.

4. **Task analysis is about breaking down user tasks**: Know that task analysis involves identifying goals, subgoals, actions, and decisions. Be familiar with hierarchical task analysis and cognitive task analysis approaches.

5. **Requirements should be user-centered**: Always emphasize that interaction design requirements are derived from user needs, not technical capabilities. This is a key principle that distinguishes interaction design from traditional software engineering requirements.

6. **MoSCoW prioritization method**: Understand how to categorize requirements as Must have, Should have, Could have, and Won't have (this time). This is a common requirement prioritization technique.

7. **Connection between research and design**: Understand that all deliverables from requirements extraction (personas, scenarios, journey maps, use cases) directly inform design decisions. The exam may ask you to explain this connection.

8. **Know the difference between quantitative and qualitative methods**: Surveys yield quantitative data (numbers, statistics), while interviews and observations yield qualitative data (insights, themes). Both are valuable and often used together.
