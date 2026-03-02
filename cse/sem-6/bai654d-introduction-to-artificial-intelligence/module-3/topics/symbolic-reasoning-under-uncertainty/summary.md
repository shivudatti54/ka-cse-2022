# Symbolic Reasoning Under Uncertainty

## Overview

Symbolic reasoning under uncertainty extends traditional symbolic AI approaches to handle incomplete, unreliable, or ambiguous information. It maintains structured knowledge representation while incorporating mechanisms like non-monotonic reasoning, default logic, fuzzy logic, and truth maintenance to quantify and reason with uncertainty.

## Key Points

- **Non-Monotonic Reasoning**: Allows retracting conclusions when new evidence emerges (unlike monotonic classical logic)
- **Default Reasoning**: Makes assumptions about typical cases when specific information is lacking using "normally" statements
- **Truth Maintenance Systems**: Track dependencies between beliefs and maintain consistency when adding new information
- **Fuzzy Logic**: Handles uncertainty using degrees of truth between 0 and 1 rather than binary true/false
- **Justification-based TMS**: Records reasons for beliefs to enable retraction when justifications fail
- **Membership Functions**: Define degree of membership in fuzzy sets for vague concepts like "hot temperature"

## Important Concepts

- Classic example: "Birds typically fly, but penguins are exceptions" demonstrates non-monotonic reasoning
- Default reasoning uses rules like "If bird(X) and consistent that flies(X), then assume flies(X)"
- Fuzzy logic naturally represents linguistic variables and vague concepts using continuous membership values
- Symbolic approaches maintain explainability while handling uncertainty, unlike pure statistical methods

## Notes

- Understand difference between symbolic (rules, logic) and statistical (probabilities) uncertainty handling
- Practice tracing through default reasoning examples showing belief retraction
- Know when each approach is suitable: non-monotonic for exceptions, fuzzy for vagueness
- Compare approaches: non-monotonic handles exceptions, default makes assumptions, fuzzy handles degrees
- Real applications include expert systems, robotic control, NLP, and legal reasoning
