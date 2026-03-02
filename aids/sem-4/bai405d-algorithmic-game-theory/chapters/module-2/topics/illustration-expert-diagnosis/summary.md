# **Illustration: Expert Diagnosis**

### Definitions and Theorems

- **Expert Diagnosis**: A game-theoretic framework for diagnosis problems where one player (the 'expert') has to diagnose an illness or defect, and the other player (the 'patient') provides information to aid in the diagnosis.
- **Bayes' Theorem**: P(A|B) = P(B|A) \* P(A) / P(B)
- **Mixed Strategy Nash Equilibrium (MSNE)**: A strategy where no player can improve their payoff by unilaterally changing their strategy, assuming the other player's strategy remains unchanged.

### Key Points

- **Expert's Objective**: Maximize probability of correct diagnosis
- **Patient's Objective**: Minimize probability of correct diagnosis (to conceal the defect)
- **Game Setup**:
  - Expert has incomplete information about the patient's state
  - Patient provides information to aid in diagnosis
  - Expert makes a diagnosis based on the information provided
- **Strategies for Expert and Patient**:
  - Expert: Ask questions to gather information
  - Patient: Provide information in a way that misleads the expert
- **Theorems**:
  - **No-Regret Theorem**: An expert can achieve a Nash equilibrium by asking the right questions
  - **Best-Response Theorem**: A patient can achieve a Nash equilibrium by providing the right information
