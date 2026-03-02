# Test-Driven Development

## Introduction
Test-Driven Development (TDD) is a software development methodology that emphasizes writing tests before writing production code. Originating from Agile practices, TDD flips traditional development by making tests the primary driver of design and implementation. This approach ensures code correctness, improves maintainability, and reduces defect rates by 40-90% according to industry studies.

In modern software engineering, TDD is critical for building robust systems in CI/CD pipelines. Companies like Google, Amazon, and Spotify use TDD to maintain code quality at scale. For DU MCA students, mastering TDD is essential for industry readiness, as it demonstrates professional discipline and aligns with India's growing emphasis on quality-driven software exports.

The paradigm shift in TDD forces developers to think through requirements first, resulting in better-defined interfaces and modular architectures. This is particularly valuable in complex systems like banking software or IoT platforms where regression errors can be catastrophic.

## Key Concepts
1. **Red-Green-Refactor Cycle**: 
   - **Red**: Write a failing test for a specific requirement
   - **Green**: Write minimal code to pass the test
   - **Refactor**: Improve code structure without changing behavior

2. **Unit Testing Frameworks**: 
   - JUnit (Java), pytest (Python), RSpec (Ruby)
   - Assertion methods (`assertEquals`, `assertTrue`)
   - Test fixtures and setup/teardown methods

3. **Mocking and Stubbing**:
   - Isolate units using tools like Mockito or unittest.mock
   - Replace dependencies with controlled substitutes
   - Verify interactions between components

4. **Regression Testing**:
   - Automated test suites prevent reintroduction of bugs
   - Continuous Integration systems (Jenkins, GitHub Actions) run tests on every commit

5. **Code Coverage**:
   - Metrics: Line coverage, branch coverage
   - Tools: JaCoCo, Coverage.py
   - Industry standard: 80%+ coverage for critical systems

## Examples

**Example 1: String Reversal Function**
```python
# Step 1: Red (Write failing test)
def test_reverse_string():
    assert reverse_string("hello") == "olleh"

# Step 2: Green (Implement minimal code)
def reverse_string(s):
    return s[::-1]

# Step 3: Refactor (Improve readability)
def reverse_string(s):
    return ''.join(reversed(s))
```

**Example 2: Shopping Cart Total**
```java
// Step 1: Red
@Test
public void testCalculateTotal() {
    Cart cart = new Cart();
    cart.addItem(new Item("Book", 299));
    assertEquals(299, cart.calculateTotal());
}

// Step 2: Green
public class Cart {
    private List<Item> items = new ArrayList<>();
    
    public int calculateTotal() {
        return items.stream().mapToInt(Item::getPrice).sum();
    }
}

// Step 3: Refactor - Extract lambda to method reference
```

## Exam Tips
1. Always mention the Red-Green-Refactor cycle with context-specific examples
2. Compare TDD with traditional testing: TDD writes tests first vs. tests after implementation
3. Memorize key metrics: Ideal code coverage percentages (70-90%) and defect reduction rates
4. For diagram questions, practice drawing CI/CD pipelines with TDD integration
5. When asked about limitations, discuss scenarios where TDD isn't ideal (UI testing, exploratory programming)
6. Use industry case studies: NASA's mission-critical systems, e-commerce payment gateways
7. Explain mocking with concrete examples like database abstraction in web applications