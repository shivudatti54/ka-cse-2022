# System Testing - Summary

## Key Definitions and Concepts

- **System Testing**: A high-level testing phase that evaluates the complete and integrated software system against specified requirements to ensure it meets functional and non-functional specifications.

- **Functional Testing**: Validates that all specified system functions work correctly according to requirements.

- **Non-Functional Testing**: Evaluates system performance characteristics including speed, scalability, security, and usability.

- **Test Environment**: A production-like setup with appropriate hardware, software, and network configurations for testing.

- **Defect Lifecycle**: The sequence of states a defect goes through - New → Assigned → Open → Fixed → Verified → Closed.

## Important Formulas and Techniques

- **Requirements Traceability Matrix (RTM)**: Maps requirements to test cases to ensure complete coverage
  - Coverage = (Number of requirements with test cases / Total requirements) × 100%

- **Test Case Effectiveness**: Measures how well test cases identify defects
  - Effectiveness = (Defects found / Total defects) × 100%

## Key Points

- System testing is performed after integration testing and before acceptance testing in the SDLC.

- It uses black-box testing techniques where internal code structure is not considered.

- Test environment should closely mirror the production environment for accurate results.

- Both positive (valid inputs) and negative (invalid inputs) test cases must be designed.

- Performance testing includes load testing, stress testing, endurance testing, and spike testing.

- Regression testing ensures new changes don't break existing functionality.

- Critical defects must be resolved before proceeding to acceptance testing.

- Test documentation includes test plans, test cases, test data, and defect reports.

## Common Mistakes to Avoid

- Testing in development environment instead of production-like test environment
- Insufficient test data coverage, especially for edge cases
- Focusing only on functional testing and ignoring non-functional requirements
- Inadequate regression testing after bug fixes
- Not documenting test results systematically for audit purposes

## Revision Tips

1. Create a comparison chart between unit testing, integration testing, system testing, and acceptance testing to understand their distinct purposes.

2. Memorize the different types of performance testing (load, stress, endurance, spike) with real-world examples.

3. Practice writing sample test cases for common scenarios like login, search, and transaction processing.

4. Review defect lifecycle states and understand severity vs priority classification.

5. Remember that system testing validates against the Software Requirements Specification (SRS), while acceptance testing validates against user requirements.