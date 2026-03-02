# Prescriptive Process Models

## A Generic Process Model

Process models provide structure for software development activities. A **generic process model** includes:

- **Process Flow** - How activities are organized
- **Work Products** - Deliverables produced
- **Quality Assurance** - Verification and validation

### Process Flow Types

| Flow Type | Description |
|-----------|-------------|
| **Linear** | Sequential progression |
| **Iterative** | Repeat activities for refinement |
| **Evolutionary** | Circular/spiral progression |
| **Parallel** | Multiple activities simultaneously |

## Waterfall Model

The **classic life cycle model** - sequential, linear approach.

```
Requirements ──► Design ──► Implementation ──► Testing ──► Maintenance
```

### Phases

1. **Requirements Definition** - Complete system requirements documented
2. **System and Software Design** - Architecture and detailed design
3. **Implementation and Unit Testing** - Coding and module testing
4. **Integration and System Testing** - Combine modules, system test
5. **Operation and Maintenance** - Deployment and ongoing support

### Advantages
- Simple, easy to understand
- Well-documented with clear milestones
- Good for well-understood requirements
- Progress easily measured

### Disadvantages
- Assumes requirements are complete upfront
- Difficult to accommodate changes
- Working software delivered late
- High risk for complex projects
- No customer feedback until end

### When to Use
- Requirements are well-understood and stable
- Short projects with clear objectives
- Technology is well-known

## Incremental Process Models

Combines linear and parallel process flows.

### Incremental Model

```
Increment 1: ───►[Core Functions]───►
Increment 2:     ───►[Additional Features]───►
Increment 3:         ───►[Enhanced Features]───►
```

**Characteristics:**
- Software delivered in increments
- First increment is "core product"
- Each increment adds functionality
- Customer evaluates each delivery

### RAD (Rapid Application Development)

High-speed adaptation of incremental model.

**Phases:**
1. Business Modeling
2. Data Modeling
3. Process Modeling
4. Application Generation
5. Testing and Turnover

**Constraints:**
- Requires sufficient resources for parallel teams
- Developers and customers must be committed
- Not suitable for high technical risk projects

## Evolutionary Process Models

Recognize that requirements evolve over time.

### Prototyping

```
Communication → Quick Plan → Modeling (Quick Design) →
Construction (Prototype) → Deployment (Delivery & Feedback) → [Loop]
```

**Purposes:**
- Clarify unclear requirements
- Demonstrate feasibility
- Explore design alternatives

**Drawbacks:**
- Customer may think prototype is finished product
- Developer may make poor implementation choices
- Prototype may be used as final product

### Spiral Model (Boehm)

Risk-driven process combining prototyping with systematic aspects of waterfall.

```
        Planning
           /\
          /  \
Risk     /    \  Customer
Analysis ◄────► Evaluation
          \  /
           \/
      Engineering
```

**Four Quadrants:**
1. **Planning** - Objectives, alternatives, constraints
2. **Risk Analysis** - Analyze and resolve risks
3. **Engineering** - Develop and verify
4. **Customer Evaluation** - Assess results

**Characteristics:**
- Risk-driven iterations
- Each loop is a phase
- Prototype at each iteration
- Suitable for large, complex projects

## Concurrent Models

Activities occur concurrently with different states.

### Concurrent Development Model

**Activity States:**
- None
- Under development
- Awaiting changes
- Under revision
- Under review
- Baselined
- Done

**Characteristics:**
- All activities exist concurrently
- Events trigger state transitions
- Applicable to all types of development
- Good for client/server applications

## Comparison of Models

| Model | Best For | Risk Level | Flexibility |
|-------|----------|------------|-------------|
| Waterfall | Fixed requirements | High | Low |
| Incremental | Partial requirements known | Medium | Medium |
| Prototyping | Unclear requirements | Medium | High |
| Spiral | Large, risky projects | Low | High |
| Concurrent | Complex applications | Medium | High |

## Key Takeaways

1. **Waterfall** - Sequential, works for stable requirements
2. **Incremental** - Delivers software in usable increments
3. **Prototyping** - Clarifies requirements through demonstration
4. **Spiral** - Risk-driven, suitable for large projects
5. **Concurrent** - Activities have states, work in parallel
