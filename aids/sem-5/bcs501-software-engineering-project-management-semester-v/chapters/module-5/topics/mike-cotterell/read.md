# Mike Cohn: An Introduction to Agile Estimation and Planning

## Introduction

While the name "Mike Cotterell" appears in your request, it is likely a misspelling or misattribution. The seminal figure in Agile estimation and planning, particularly for Scrum, is **Mike Cohn**. He is a highly influential author, consultant, and one of the founders of the Scrum Alliance and the Agile Alliance. For  engineering students, understanding Cohn's contributions is fundamental to mastering the practical application of Agile project management, a cornerstone of modern software engineering. His work provides a structured yet flexible approach to answering the critical project questions: "What will we build?" and "When will it be done?"

## Core Concepts

Mike Cohn's methodologies primarily revolve around making software estimation more accurate and less burdensome. His key concepts include:

### 1. Planning Poker®

This is a consensus-based technique for estimating the effort or relative size of user stories.

*   **How it works:** The development team gathers, and each member is given a deck of cards with numbers representing story points (often using a modified Fibonacci sequence: 1, 2, 3, 5, 8, 13...). For each user story (e.g., "As a user, I can reset my password"), the product owner explains the feature. Each team member then privately selects a card representing their estimate. Cards are revealed simultaneously. If estimates differ significantly, the high and low estimators discuss their reasoning. The process repeats until a consensus is reached.
*   **Why it works:** It leverages collective wisdom, mitigates anchoring bias (where the first number spoken influences others), and fosters team discussion and shared understanding of the work.

### 2. Story Points and Velocity

Cohn championed the use of abstract, relative units called **Story Points** instead of absolute time-based estimates (e.g., hours or days).

*   **Story Points:** Represent the overall effort involved in developing a user story, considering complexity, amount of work, and risk/uncertainty. A story assigned 8 points is roughly twice as "big" as one assigned 4 points.
*   **Velocity:** This is the sum of story points a team completes in a single sprint. It is a measure of the team's rate of progress. For example, if a team completes stories totaling 24 points in Sprint 1 and 26 points in Sprint 2, their average velocity is ~25.
*   **Benefit:** This allows for more accurate long-term planning. If the product backlog contains 250 story points and the team's average velocity is 25, they can forecast completing the work in approximately 10 sprints.

### 3. The Product Backlog and Release Planning

Cohn's techniques are integral to managing the product backlog and planning releases.

*   **Prioritized Backlog:** The product owner maintains a list of desired features (user stories) ordered by priority.
*   **Release Planning:** Using the team's known velocity, the product owner can forecast which features (from the top of the backlog) will be included in a future release. This shifts the question from "When will *every* feature be done?" to "Which features will be done by this date?"

### Example: Building a Login Feature

1.  **Backlog Items:**
    *   "As a user, I can log in with email and password" (Story A)
    *   "As a user, I can log in with Google OAuth" (Story B)
    *   "As a user, I can request a password reset" (Story C)

2.  **Planning Poker:** The team discusses and estimates:
    *   Story A: 3 points (straightforward)
    *   Story B: 8 points (more complex due to third-party integration)
    *   Story C: 5 points (medium complexity)

3.  **Sprint Planning:** The team, with a velocity of 13, decides they can commit to Story A (3 pts) and Story C (5 pts) in the upcoming sprint, totaling 8 points. Story B (8 pts) is too large for this sprint and is deferred.

4.  **Forecasting:** With a velocity of 13, the product owner knows that the 50-point "Minimum Viable Product (MVP)" backlog will take approximately 4 sprints to complete.

## Key Points / Summary

*   **Who:** Mike Cohn is a foundational Agile thinker, not Mike Cotterell. His work is essential for Software Project Management.
*   **Core Techniques:** He popularized **Planning Poker®** for collaborative estimation and championed the use of **Story Points** over hours.
*   **Key Metric:** **Velocity** (story points per sprint) is used to measure a team's capacity and forecast future work.
*   **Practical Outcome:** His methods enable evidence-based **release planning**, moving from vague guesses to data-driven forecasts on what can be delivered and when.
*   **Philosophy:** Estimation should be a quick, team-oriented activity that fosters discussion and shared understanding, not a lengthy, individual burden.

**Reference:** Cohn's book, *"Agile Estimating and Planning,"* is considered the definitive guide on the subject.