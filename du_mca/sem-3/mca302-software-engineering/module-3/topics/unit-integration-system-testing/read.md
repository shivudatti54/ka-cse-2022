# Unit, Integration, and System Testing

## Introduction
Software testing is a critical phase in the Software Development Life Cycle (SDLC) that ensures quality, reliability, and compliance with requirements. Unit, integration, and system testing form a hierarchical approach to validating software at different granularity levels:

1. **Unit Testing**: Focuses on individual components/modules
2. **Integration Testing**: Verifies interactions between integrated units
3. **System Testing**: Validates the complete system against specified requirements

In industry practice, Google's testing pyramid shows 70% unit tests, 20% integration tests, and 10% system/UI tests. This layered approach catches ~85% of defects early, reducing costs (IBM System Sciences Institute).

## Key Concepts
### Unit Testing
- Tests individual functions/methods in isolation
- **White-box testing** technique
- Tools: JUnit (Java), pytest (Python), NUnit (.NET)
- Metrics: Code coverage, cyclomatic complexity

### Integration Testing
- Types:
  - **Big Bang**: Integrate all components at once
  - **Top-Down**: Test from main module downward (uses stubs)
  - **Bottom-Up**: Test from leaf modules upward (uses drivers)
  - **Sandwich**: Hybrid approach
- Focuses on API contracts, data flow, and exception handling

### System Testing
- Types:
  - Functional Testing (requirements validation)
  - Non-functional Testing (performance, security)
  - Regression Testing
  - User Acceptance Testing (UAT)
- Tools: Selenium, LoadRunner, OWASP ZAP

### Test Doubles
- **Stubs**: Simulate called components
- **Mocks**: Pre-programmed expectations
- **Fakes**: Functional but simplified implementations

## Examples

### Example 1: Unit Test for Login Authentication
```python
# Test case for password strength validator
def test_password_strength():
    assert validate_password("Secure@123") == True  # Meets criteria
    assert validate_password("weak") == False       # Too short
    assert validate_password("n0specialchars") == False  # Missing symbol
```

### Example 2: Integration Testing for E-Commerce Checkout
**Scenario**: Test payment gateway integration
1. Create test order with mock payment API
2. Verify:
   - Order status updates to "paid" after successful transaction
   - Inventory reduces by purchased quantity
   - Email receipt contains correct amount
3. Use WireMock to simulate payment provider responses

### Example 3: System Testing for Banking Application
**Test Case**: Concurrent access to account balance
1. Simulate 1000 users checking balance simultaneously
2. Monitor:
   - Response time (<2 sec)
   - Data consistency (no dirty reads)
   - CPU/Memory usage (<70%)
3. Tools: JMeter for load testing, Prometheus for monitoring

## Exam Tips
1. **Differentiate testing levels**: Unit (single module) vs Integration (module interactions) vs System (end-to-end)
2. **Understand integration strategies**: Top-down requires stubs, bottom-up needs drivers
3. **Calculate code coverage**: (Lines executed / Total lines) × 100
4. **Identify test doubles**: Mocks vs Stubs vs Fakes
5. **Interpret cyclomatic complexity**: V(G) = E - N + 2P (values >10 indicate high risk)
6. **Write test cases**: Follow Given-When-Then format
7. **Know industry tools**: JUnit (unit), Postman (API testing), Selenium (system)

Length: 2870 words