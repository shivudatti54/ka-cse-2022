# Unit, Integration, and Validation Testing - Summary

## Key Definitions and Concepts

- **Unit Testing:** Testing individual software components in isolation to verify correct functioning of each unit
- **Integration Testing:** Testing combined components to ensure they work together correctly
- **Validation Testing:** Final testing phase verifying the complete system meets user requirements (acceptance testing)
- **Stub:** Dummy module used in top-down integration to simulate lower-level components
- **Driver:** Dummy module used in bottom-up integration to simulate higher-level components
- **Test-Driven Development (TDD):** Development methodology where tests are written before code following Red-Green-Refactor cycle

## Important Formulas and Theorems

- **Test Coverage Formula:** Coverage = (Executed Code Lines / Total Code Lines) × 100%
- **Cyclomatic Complexity:** V(G) = E - N + 2P (used to determine path coverage requirements)
- **No single testing approach guarantees defect-free software** - multiple levels are essential

## Key Points

1. Unit tests form the foundation of the testing pyramid - they are most numerous and execute fastest
2. Stubs are used in top-down integration; drivers are used in bottom-up integration
3. Big-Bang integration is simple but risky; Sandwich integration combines advantages of top-down and bottom-up
4. Validation testing determines if "we are building the right product" while verification checks "we are building the product right"
5. Alpha testing occurs at developer's site; beta testing occurs at user's location
6. Test-Driven Development follows Red (write failing test) → Green (write code to pass) → Refactor cycle
7. Code coverage metrics (line, branch, path) measure test thoroughness but don't guarantee quality
8. Equivalence partitioning and boundary value analysis are fundamental black-box test design techniques

## Common Mistakes to Avoid

- Confusing stubs with drivers in integration testing contexts
- Treating unit testing and integration testing as interchangeable
- Assuming 100% code coverage means the software is defect-free
- Mixing up alpha testing (in-house) with beta testing (external users)
- Writing tests after code instead of following TDD principles when applicable
- Skipping validation testing assuming unit and integration tests are sufficient

## Revision Tips

1. Create comparison tables for different testing levels and integration approaches
2. Practice identifying whether a scenario describes unit, integration, or validation testing
3. Memorize the TDD Red-Green-Refactor cycle sequence
4. Remember the testing pyramid structure: Unit → Integration → Validation
5. Review previous DU question papers to understand the exam pattern and frequently tested concepts