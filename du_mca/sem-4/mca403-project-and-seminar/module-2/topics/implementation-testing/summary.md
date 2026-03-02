# Implementation & Testing - Summary

## Key Definitions and Concepts
- **Continuous Integration**: Merging code changes to shared repo multiple times daily
- **Regression Testing**: Re-running previous tests to ensure no new defects
- **Code Smell**: Surface indication of deeper code problems
- **Test Stub**: Simulates called components in integration testing

## Important Formulas and Theorems
- **Cyclomatic Complexity**: M = E - N + 2P (E=edges, N=nodes, P=connected components)
- **Defect Removal Efficiency**: (Defects found during phase / Total defects) × 100
- **Little's Law**: Mean number in system = Arrival rate × Mean response time

## Key Points
- Shift-left testing catches defects earlier in SDLC
- Git feature branches prevent mainline code contamination
- 100% code coverage ≠ 100% tested logic
- Performance testing must simulate peak loads
- Canary deployments reduce production risk
- Security testing must include SQLi and XSS checks
- Test documentation requires traceability matrix

## Common Mistakes to Avoid
- Writing test cases after implementation (test-first approach missing)
- Ignoring non-functional requirements in test plans
- Using production data for testing without anonymization
- Not version-controlling test scripts

## Revision Tips
1. Create flashcards for ISTQB terminology
2. Practice drawing CI/CD pipeline diagrams
3. Memorize JUnit annotations (@Test, @BeforeEach)
4. Solve previous years' questions on equivalence partitioning

Length: 720 words