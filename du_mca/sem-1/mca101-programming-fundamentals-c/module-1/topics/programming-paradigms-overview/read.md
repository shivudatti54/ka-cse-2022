# Programming Paradigms Overview

## Introduction
Programming paradigms represent fundamental styles of building software systems. In computer science education, understanding paradigms equips developers with diverse problem-solving approaches. The University of Delhi's MCA program emphasizes multi-paradigm proficiency as modern systems often combine imperative, object-oriented, and functional approaches.

Contemporary software development requires paradigm awareness. For instance, Android development uses OOP (Java/Kotlin), AI projects employ functional programming (Python/Haskell), and system programming relies on procedural paradigms (C). According to 2023 Stack Overflow data, 75% of professional projects use 2+ paradigms simultaneously.

This topic forms the foundation for advanced courses like Distributed Systems (MCA303) and Machine Learning (MCA402). Paradigm mastery helps students choose optimal approaches for problems like concurrency (actor model in functional) or data encapsulation (OOP).

## Key Concepts
1. **Imperative Programming**
   - Based on explicit state changes through statements
   - Includes procedural (C) and structured programming
   - Memory model: Von Neumann architecture
   - Example construct: `for(int i=0;i<10;i++) {...}`

2. **Object-Oriented Programming (OOP)**
   - Four pillars: Encapsulation, Abstraction, Inheritance, Polymorphism
   - Class-based (Java) vs prototype-based (JavaScript)
   - Design patterns: Singleton, Factory, Observer
   - SOLID principles for maintainable code

3. **Functional Programming**
   - First-class functions, pure functions, immutability
   - Lambda calculus foundation
   - Higher-order functions (map, filter, reduce)
   - Recursion instead of loops
   - Example languages: Haskell, Scala, F#

4. **Declarative Paradigms**
   - SQL (declarative queries)
   - Logic programming (Prolog)
   - React.js UI as declarative components
   - Focus on "what" rather than "how"

5. **Event-Driven Programming**
   - Callbacks and event loops
   - Node.js architecture
   - Observer pattern implementation
   - GUI programming fundamentals

## Examples

**Example 1: Sum of Squares Comparison**
```python
# Imperative
total = 0
for num in range(1,11):
    total += num**2

# Functional
sum(map(lambda x: x**2, range(1,11)))

# Declarative (SQL-like)
SELECT SUM(num^2) FROM generate_series(1,10) AS num
```

**Example 2: OOP vs Functional Data Processing**
```java
// Java (OOP)
List<Integer> squares = new ArrayList<>();
for(int i : Arrays.asList(1,2,3)) {
    squares.add(i*i);
}

// Scala (Functional)
val squares = List(1,2,3).map(x => x*x)
```

**Example 3: React Declarative UI**
```jsx
// Declarative component
function UserList({users}) {
  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  )
}
```

## Exam Tips
1. Always compare paradigms using criteria: state management, code structure, and typical use cases
2. Memorize 2+ language examples for each paradigm
3. Understand how JavaScript supports multiple paradigms (OOP + functional)
4. For 10-mark questions, discuss paradigm evolution (from procedural to FP in big data)
5. Relate design patterns to their native paradigms (Factory → OOP, Monad → FP)
6. Prepare real-world case studies: OOP for banking systems, FP for ML pipelines
7. Practice converting imperative code to functional style (loops → recursion/map)