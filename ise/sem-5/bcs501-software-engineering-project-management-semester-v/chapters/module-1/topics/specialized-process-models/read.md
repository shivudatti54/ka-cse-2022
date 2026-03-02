# Specialized and Modern Process Models

## Specialized Process Models

### Component-Based Development

Focuses on building software from pre-existing components.

**Process Steps:**

1. Identify candidate components
2. Search for components in library
3. Extract if available, build if not
4. Construct new components as needed
5. Integrate components into system

**Benefits:**

- Reduced development time
- Reusability across projects
- Proven, tested components
- Cost effective

### Formal Methods Model

Uses mathematical specification for software development.

**Characteristics:**

- Rigorous mathematical notation
- Enables formal verification
- Ambiguity-free specifications
- Primarily used in safety-critical systems

**Limitations:**

- Time-consuming and expensive
- Requires specialized training
- Limited tool support
- Communication barrier with non-technical stakeholders

### Aspect-Oriented Software Development (AOSD)

Addresses cross-cutting concerns separately.

**Cross-cutting Concerns:**

- Logging
- Security
- Error handling
- Transaction management

**Benefits:**

- Improved modularity
- Reduced code duplication
- Easier maintenance

## Unified Process (UP)

Iterative, incremental framework that uses UML.

### UP Phases

| Phase            | Purpose                 | Key Activities                       |
| ---------------- | ----------------------- | ------------------------------------ |
| **Inception**    | Establish business case | Scope, vision, risk assessment       |
| **Elaboration**  | Develop understanding   | Architecture, requirements, planning |
| **Construction** | Build the system        | Design, implementation, testing      |
| **Transition**   | Deploy to users         | Beta testing, deployment, training   |

### UP Characteristics

```
            Inception → Elaboration → Construction → Transition
                │           │              │             │
Iterations:    1-2         2-3           3-5           1-2
Focus:        Vision    Architecture    Build        Deploy
```

**Key Principles:**

- **Use-Case Driven** - Requirements as use cases
- **Architecture-Centric** - Early architecture focus
- **Iterative and Incremental** - Multiple iterations
- **Risk-Focused** - Address risks early

### UP Workflows

**Engineering Workflows:**

1. Business Modeling
2. Requirements
3. Analysis and Design
4. Implementation
5. Test
6. Deployment

**Supporting Workflows:**

1. Configuration Management
2. Project Management
3. Environment

## Personal Software Process (PSP)

Developed by Watts Humphrey at SEI.

### PSP Levels

| Level  | Name     | Focus                              |
| ------ | -------- | ---------------------------------- |
| PSP0   | Baseline | Basic process, measurement         |
| PSP0.1 | Enhanced | Coding standards, size measurement |
| PSP1   | Planning | Size estimation, test planning     |
| PSP1.1 | Enhanced | Schedule planning                  |
| PSP2   | Quality  | Code reviews, design reviews       |
| PSP2.1 | Enhanced | Design templates                   |
| PSP3   | Cyclic   | Scaled for large programs          |

### PSP Objectives

- Improve estimation accuracy
- Improve scheduling and planning
- Reduce defects
- Improve individual productivity

### PSP Activities

1. **Planning** - Estimate size and resources
2. **High-Level Design** - Design specifications
3. **Design Review** - Verify design
4. **Development** - Code and compile
5. **Code Review** - Find defects
6. **Compile** - Compile and fix errors
7. **Test** - Unit testing
8. **Postmortem** - Analyze performance

## Team Software Process (TSP)

Extends PSP concepts to team level.

### TSP Goals

- Build self-directed teams
- Improve product quality
- Accelerate software improvement
- Provide guidance for high-maturity organizations

### TSP Team Roles

| Role                    | Responsibility                  |
| ----------------------- | ------------------------------- |
| Team Leader             | Motivate, coordinate, report    |
| Development Manager     | Lead development activities     |
| Planning Manager        | Maintain plans, schedules       |
| Quality/Process Manager | Process adherence, quality      |
| Support Manager         | Tools, configuration management |

### TSP Launch Process

```
Strategy → Planning → Requirements → Design →
Implementation → Test → Postmortem
```

**TSP Meetings:**

- Weekly team meetings
- Regular management reviews
- Periodic checkpoints

## Comparison Summary

| Model           | Focus        | Best For                                   |
| --------------- | ------------ | ------------------------------------------ |
| Component-Based | Reuse        | Rapid development with existing components |
| Formal Methods  | Correctness  | Safety-critical systems                    |
| Unified Process | Architecture | Large OO projects                          |
| PSP             | Individual   | Personal improvement                       |
| TSP             | Team         | Team-based development                     |

## Key Takeaways

1. **Unified Process** - Iterative, use-case driven, architecture-centric
2. **UP Phases** - Inception, Elaboration, Construction, Transition
3. **PSP** - Personal process for individual improvement
4. **TSP** - Team process building on PSP
5. **Component-based** - Focuses on reuse for efficiency
