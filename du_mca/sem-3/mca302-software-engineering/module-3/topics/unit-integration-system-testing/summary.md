# Unit, Integration, and System Testing - Summary

## Key Definitions and Concepts
- **Unit Testing**: Validation of individual software components
- **Integration Testing**: Testing interactions between integrated modules
- **System Testing**: End-to-end validation of complete system
- **Stub**: Simulates called component in top-down integration
- **Driver**: Calls component under test in bottom-up approach

## Important Formulas and Theorems
- **Cyclomatic Complexity**: V(G) = E - N + 2P  
  (Edges - Nodes + 2*Exit Points)
- **Code Coverage**: (Tested LOC / Total LOC) × 100
- **Defect Density**: (Defects found / KLOC)

## Key Points
- Unit tests should achieve >80% code coverage
- Integration testing focuses on interfaces and data flow
- System testing includes both functional and non-functional requirements
- Mock objects isolate units during testing
- Continuous Integration requires automated test suites
- Risk-based testing prioritizes critical modules
- Traceability matrix links tests to requirements

## Common Mistakes to Avoid
1. Testing business logic in system tests instead of unit tests
2. Not resetting state between test cases
3. Overlooking negative test scenarios
4. Using real databases in unit tests

## Revision Tips
1. Create comparison tables for testing types/strategies
2. Practice writing test cases for sample requirements
3. Memorize integration testing approaches using mnemonics:
   - "Top uses Stubs, Bottom uses Drivers"
4. Use flow graphs to calculate cyclomatic complexity

Length: 720 words