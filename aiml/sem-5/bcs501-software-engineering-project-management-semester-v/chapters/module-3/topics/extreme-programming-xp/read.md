# Extreme Programming (XP)

## What is Extreme Programming?

Extreme Programming (XP) is an agile software development methodology that emphasizes customer satisfaction, teamwork, and delivering high-quality software through a set of engineering practices.

### Origins

- Created by **Kent Beck** in the late 1990s
- First used on the Chrysler C3 payroll project
- Named "Extreme" because it takes proven practices to extreme levels

## XP Values

### Five Core Values

1. **Communication**
   - Face-to-face conversation
   - Customer on-site
   - Daily standups

2. **Simplicity**
   - YAGNI (You Aren't Gonna Need It)
   - Do the simplest thing that works
   - Avoid over-engineering

3. **Feedback**
   - Unit tests provide immediate feedback
   - Customer reviews iterations
   - Continuous integration

4. **Courage**
   - Refactor when needed
   - Throw away code that doesn't work
   - Accept that requirements change

5. **Respect**
   - Team members respect each other
   - Respect the customer
   - Respect the process

## XP Practices

### Primary Practices

| Practice | Description |
|----------|-------------|
| **Planning Game** | Release and iteration planning |
| **Small Releases** | Frequent, incremental releases |
| **Customer On-site** | Customer available for questions |
| **Simple Design** | No unnecessary complexity |
| **Pair Programming** | Two programmers, one computer |
| **Test-Driven Development** | Write tests before code |
| **Refactoring** | Improve code without changing behavior |
| **Continuous Integration** | Integrate and test frequently |
| **Collective Code Ownership** | Anyone can change any code |
| **Coding Standards** | Consistent code style |
| **Sustainable Pace** | 40-hour work weeks |
| **Metaphor** | Shared vocabulary and understanding |

### Pair Programming

Two programmers working at one workstation:
- **Driver** - Types the code
- **Navigator** - Reviews and thinks ahead

**Benefits:**
- Continuous code review
- Knowledge sharing
- Better design decisions
- Fewer defects

**Challenges:**
- Requires collaboration skills
- Can be tiring
- May not suit all personalities

### Test-Driven Development (TDD)

```
Write Failing Test → Write Minimal Code → Refactor → Repeat
     (Red)              (Green)           (Refactor)
```

**TDD Cycle:**
1. **Red** - Write a test that fails
2. **Green** - Write just enough code to pass
3. **Refactor** - Improve the code

### Continuous Integration

**Practices:**
- Commit code frequently (multiple times daily)
- Automated build on every commit
- Automated test execution
- Fix broken builds immediately
- Keep build fast

### Refactoring

Restructuring code without changing external behavior.

**Common Refactorings:**
- Extract Method
- Rename Variable
- Move Method
- Replace Conditional with Polymorphism

**When to Refactor:**
- Before adding new features
- When code smells are detected
- During code reviews

## XP Framework Activities

### Four Framework Activities

```
Planning → Design → Coding → Testing
    ↑                           │
    └───────────────────────────┘
           (Continuous)
```

1. **Planning**
   - User stories written
   - Stories estimated (story points)
   - Release planning
   - Iteration planning

2. **Design**
   - Simple design
   - CRC cards
   - Spike solutions for risks
   - Refactoring

3. **Coding**
   - Pair programming
   - Collective ownership
   - Coding standards
   - Customer on-site

4. **Testing**
   - Unit tests (TDD)
   - Acceptance tests
   - Continuous integration

## XP Roles

| Role | Responsibility |
|------|----------------|
| **Customer** | Defines requirements, priorities, acceptance tests |
| **Developer** | Designs, codes, tests, integrates |
| **Tracker** | Monitors progress, identifies problems |
| **Coach** | Guides team, teaches XP practices |

## User Stories

### Story Card Format

```
+----------------------------------+
| As a [user type]                 |
| I want [goal]                    |
| So that [benefit]                |
+----------------------------------+
| Acceptance Criteria:             |
| - Criterion 1                    |
| - Criterion 2                    |
+----------------------------------+
| Estimate: 3 points               |
+----------------------------------+
```

### INVEST Criteria for Good Stories

- **I**ndependent
- **N**egotiable
- **V**aluable
- **E**stimable
- **S**mall
- **T**estable

## When to Use XP

**Good For:**
- Small to medium teams (2-12 developers)
- Projects with changing requirements
- Greenfield development
- Technically challenging projects

**Not Ideal For:**
- Large distributed teams
- Fixed-price contracts
- Highly regulated environments
- Legacy system maintenance

## Key Takeaways

1. XP emphasizes **engineering practices** for quality
2. **Five values**: Communication, Simplicity, Feedback, Courage, Respect
3. **Key practices**: TDD, Pair Programming, Continuous Integration
4. **Customer involvement** is essential
5. **Small releases** and **frequent feedback** reduce risk
