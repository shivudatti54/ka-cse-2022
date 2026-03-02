# Test-Driven Development (TDD) - Summary

## Key Definitions and Concepts

- **Test-Driven Development (TDD)**: A software development methodology where developers write automated tests before writing the actual implementation code, following a short iterative cycle.

- **Red-Green-Refactor**: The three-phase TDD cycle where developers first write a failing test (Red), then write minimal code to pass the test (Green), and finally refactor the code while keeping tests passing.

- **Unit Test**: A test that verifies the behavior of the smallest testable units of code (typically functions or methods) in isolation from the rest of the system.

- **Mock Object**: A test double that simulates the behavior of real objects, used to isolate the unit under test from its dependencies.

- **Test Fixture**: The setup of fixed state or resources required for tests to run, typically implemented through setup and teardown methods.

## Important Formulas and Principles

- **F.I.R.S.T. Principles for Unit Tests**:
  - **F**ast: Tests should run quickly
  - **I**ndependent: Tests should not depend on each other
  - **R**epeatable: Tests should produce consistent results
  - **S**elf-Validating: Tests should automatically determine pass/fail
  - **T**imely: Tests should be written at the right time (before code)

- **TDD Cycle**: Red → Green → Refactor (repeat for each piece of functionality)

## Key Points

- TDD shifts the development mindset from "how to build" to "what should this do"
- Writing tests first forces clear thinking about requirements and interface design
- The Green phase requires writing only enough code to pass tests, not perfect code
- Comprehensive test suites enable confident refactoring without fear of breaking functionality
- Mock objects replace external dependencies (databases, APIs, file systems) for faster, isolated testing
- TDD naturally produces high test coverage focused on behavior, not arbitrary metrics
- Test names should describe the behavior being tested, not the implementation
- TDD serves as living documentation that always stays current with the code

## Common Mistakes to Avoid

- **Writing too many tests at once**: TDD works best with one test (one failing test) at a time
- **Skipping the refactor phase**: Refactoring is essential for code quality and must not be neglected
- **Testing implementation details**: Focus on behavior, not internal state, to avoid brittle tests
- **Writing tests that depend on each other**: Each test must be independent and able to run in any order
- **Making tests slow**: Unit tests must be fast to maintain the TDD feedback loop

## Revision Tips

1. Practice writing the complete TDD cycle for simple functions—start with an empty test, implement minimally, then refactor
2. Memorize the Red-Green-Refactor sequence and ensure you can explain each phase
3. Understand when mocking is necessary: replace slow or non-deterministic dependencies
4. Review the F.I.R.S.T. principles and be able to explain each characteristic with examples
5. Be prepared to write actual test code in exams—practice syntax for common assertions and test structures