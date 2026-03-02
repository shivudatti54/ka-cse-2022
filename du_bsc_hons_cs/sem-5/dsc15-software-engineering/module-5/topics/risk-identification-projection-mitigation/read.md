# Risk Identification, Projection, and Mitigation in Software Engineering

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

Software projects are inherently complex endeavors where success depends on navigating numerous uncertainties. According to the Standish Group's Chaos Report, only about 31% of software projects succeed—meaning they are completed on time, on budget, and with all planned features. The remaining projects either fail completely or are challenged, primarily due to inadequate risk management.

In the context of Delhi University's BSc (Hons) Computer Science curriculum under NEP 2024 UGCF, understanding risk management is crucial for producing industry-ready software engineers. Real-world software failures like the healthcare.gov rollout ($93.7 million spent before launch with critical failures), the Knight Capital Group's $440 million trading loss due to a software bug, and numerous data breaches highlight the catastrophic consequences of ignoring software engineering risks.

This study material provides comprehensive coverage of the three pillars of software risk management: **Identification**, **Projection** (also called Estimation/Analysis), and **Mitigation**.

---

## 2. Understanding Risk in Software Engineering

### 2.1 Definition of Risk

A **risk** is an uncertain event or condition that, if it occurs, has a positive or negative effect on at least one project objective (schedule, cost, scope, or quality).

- **Positive Risk (Opportunity)**: An uncertain event that can have favorable outcomes
- **Negative Risk (Threat)**: An uncertain event that can cause harm to the project

### 2.2 Risk vs. Issue

| Aspect | Risk | Issue |
|--------|------|-------|
| **Timing** | Future uncertain event | Current problem |
| **Nature** | May or may not occur | Has occurred |
| **Management** | Mitigation strategies | Resolution actions |

---

## 3. Risk Identification

Risk identification is the process of determining which risks may affect the project and documenting their characteristics.

### 3.1 Risk Identification Techniques

#### 3.1.1 Brainstorming
A group creativity technique where team members generate ideas about potential risks in an open, non-judgmental environment.

**Example Application**: In a team meeting for an e-commerce website development project:
- "Server crashes during high traffic"
- "Payment gateway integration failures"
- "User data privacy violations"

#### 3.1.2 Delphi Technique
An anonymous survey process where experts provide risk estimates iteratively until consensus is reached. Eliminates group bias and influence.

#### 3.1.3 SWOT Analysis
Analyzing the project from four perspectives:
- **S**trengths: Internal capabilities that mitigate risks
- **W**eaknesses: Internal vulnerabilities
- **O**pportunities: External positive possibilities
- **T**hreats: External negative possibilities

#### 3.1.4 Risk Checklists
Pre-defined lists based on historical project data and industry standards.

### 3.2 Software-Specific Risks Categories

#### 3.2.1 Project Risks (Internal)
- Schedule delays
- Budget overruns
- Resource unavailability
- Scope creep

#### 3.2.2 Product Risks (Technical)
- Technology obsolescence
- Security vulnerabilities
- Performance degradation
- Integration failures
- Scalability limitations

#### 3.2.3 Business Risks (External)
- Market changes
- Regulatory compliance (GDPR, IT Act)
- Vendor reliability
- Stakeholder conflicts

### 3.3 Software-Specific Critical Risks

#### 3.3.1 Security Risks
```python
# Example: Inadequate input validation leading to SQL Injection
# RISK: User input directly concatenated in SQL query
user_input = request.GET['username']
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
# This allows attackers to inject malicious SQL code

# MITIGATION: Use parameterized queries
cursor.execute("SELECT * FROM users WHERE username = ?", (user_input,))
```

#### 3.3.2 Technology Obsolescence Risk
```
Risk: Using deprecated technologies (e.g., Python 2.7 discontinued in 2020)
Impact: Security vulnerabilities, lack of community support, hiring difficulties
Mitigation: 
  - Regular technology assessment
  - Planning for migration
  - Using LTS (Long Term Support) versions
```

#### 3.3.3 Requirement Volatility Risk
```
Risk: Frequent requirement changes during development
Impact: Schedule overruns, cost escalation, quality degradation
Mitigation:
  - Agile methodology with iterative sprints
  - Change control board
  - Clear scope definition with signed-off SRS
```

---

## 4. Risk Projection (Estimation/Analysis)

Risk projection involves analyzing the probability and impact of identified risks to determine their overall risk rating.

### 4.1 Probability-Impact Matrix

A visual tool that plots risks based on their probability of occurrence and potential impact.

| Impact ↓ / Probability → | Low (0.2) | Medium (0.5) | High (0.8) |
|--------------------------|-----------|--------------|------------|
| **High ($100K)**         | Medium    | High         | Critical   |
| **Medium ($50K)**        | Low       | Medium       | High       |
| **Low ($10K)**           | Low       | Low          | Medium     |

**Risk Rating Formula**: `Risk Rating = Probability × Impact`

**Example Calculation**:
- Risk: "Key developer leaves project"
- Probability: 0.3 (30% chance)
- Impact: $80,000 (cost of recruitment + retraining + delays)
- Risk Rating: 0.3 × 80,000 = **$24,000**

### 4.2 Expected Monetary Value (EMV)

EMV is a statistical technique used to quantify risks by calculating the average outcome when uncertain events may or may not occur.

**Formula**: 
```
EMV = Σ (Probability of Outcome_i × Value of Outcome_i)
```

#### EMV Calculation Example

```
Project: Mobile Banking Application Development

Risk 1: Third-party API unavailability
  - Outcome A: API works (60%): $0 impact
  - Outcome B: API fails, need alternative (40%): $50,000 extra cost
  - EMV = (0.6 × 0) + (0.4 × 50,000) = $20,000

Risk 2: Security breach during development
  - Outcome A: No breach (70%): $0 impact
  - Outcome B: Minor breach (25%): $30,000 remediation
  - Outcome C: Major breach (5%): $200,000 remediation + reputational damage
  - EMV = (0.7 × 0) + (0.25 × 30,000) + (0.05 × 200,000) = $17,500

Total Expected Risk Cost = $20,000 + $17,500 = $37,500
```

### 4.3 Risk Urgency Rating

Factors determining urgency:
1. Probability of occurrence in near future
2. Time available to respond
3. Warning indicators present

**Formula for Risk Exposure**:
```
Risk Exposure = Probability × Impact × Detectability Factor
```
(Where detectability factor ranges from 0.1 to 1.0, with 0.1 being easily detectable)

---

## 5. Risk Mitigation Strategies

### 5.1 The Four Main Strategies

| Strategy | Description | Example |
|----------|-------------|---------|
| **Avoid** | Eliminate the threat by eliminating the cause | Change technology stack to avoid unsupported framework |
| **Transfer** | Shift negative impact to a third party | Buy insurance, outsource to vendor |
| **Mitigate** | Reduce probability and/or impact | Add more testing, hire additional developers |
| **Accept** | Acknowledge and prepare contingency | Accept that minor bugs may occur |

### 5.2 Risk Mitigation Plan Example

```python
# Example: Risk Mitigation Plan for "Database Performance Issues"

RISK: Database performance degradation with 100,000+ users

MITIGATION STRATEGIES:
┌─────────────────────────────────────────────────────────────────┐
│ 1. AVOID: Use scalable database architecture (sharding)        │
│    - Implement database partitioning                           │
│    - Design for horizontal scaling                             │
├─────────────────────────────────────────────────────────────────┤
│ 2. TRANSFER: Use managed cloud database service                 │
│    - AWS RDS / Azure SQL with automatic scaling                │
│    - Transfer operational burden to cloud provider             │
├─────────────────────────────────────────────────────────────────┤
│ 3. MITIGATE: Implement performance optimization                │
│    - Add indexing on frequently queried columns                │
│    - Implement caching layer (Redis, Memcached)                │
│    - Database query optimization                               │
│    - Load testing before production                            │
├─────────────────────────────────────────────────────────────────┤
│ 4. ACCEPT & CONTINGENCY:                                       │
│    - Plan for 4-hour recovery time objective (RTO)             │
│    - Document rollback procedures                              │
│    - Set aside 15% budget contingency                          │
└─────────────────────────────────────────────────────────────────┘
```

### 5.3 Risk Monitoring and Control

Continuous activities include:
- Tracking identified risks
- Monitoring residual risks
- Identifying new risks
- Evaluating risk process effectiveness

---

## 6. Risk Register

A risk register is a document listing all identified risks with their details.

### 6.1 Components of a Risk Register

| Field | Description |
|-------|-------------|
| Risk ID | Unique identifier |
| Description | Clear description of risk |
| Category | Project/Product/Business |
| Probability | 0-1 scale |
| Impact | Cost/Schedule/Quality |
| Risk Rating | Priority score |
| Mitigation Strategy | Chosen approach |
| Owner | Responsible person |
| Status | Active/Mitigated/Closed |
| Due Date | Response deadline |

### 6.2 Risk Register Example

```
┌──────────┬────────────────────────────┬──────────┬───────────┬─────────┬──────────┬──────────────┐
│ Risk ID  │ Description               │ Category │ Prob.    │ Impact  │ Rating   │ Strategy     │
├──────────┼────────────────────────────┼──────────┼───────────┼─────────┼──────────┼──────────────┤
│ R-001    │ Key developer attrition   │ Project  │ 0.4      │ High    │ 0.40     │ Transfer     │
│ R-002    │ Security vulnerability    │ Product  │ 0.6      │ High    │ 0.60     │ Mitigate     │
│ R-003    │ Scope creep               │ Project  │ 0.7      │ Medium  │ 0.35     │ Avoid        │
│ R-004    │ Third-party API change    │ Business │ 0.3      │ Medium  │ 0.15     │ Accept       │
│ R-005    │ Technology obsolescence   │ Product  │ 0.5      │ High    │ 0.50     │ Mitigate     │
└──────────┴────────────────────────────┴──────────┴───────────┴─────────┴──────────┴──────────────┘
```

---

## 7. Case Study: Real-World Software Risk Failure

### Case Study: Knight Capital Group Trading Loss (2012)

**Background**: Knight Capital, a financial services firm, deployed new trading software on August 1, 2012.

**Risk Identification Failure**:
- No proper code review for the new feature
- Legacy code with dead paths was not removed
- Insufficient testing in production-like environment

**What Went Wrong**:
```python
# Simplified illustration of the bug
def execute_trade(flag):
    if flag == 1:
        # New functionality - buy
        buy()
    elif flag == 2:
        # New functionality - sell  
        sell()
    # BUG: When flag = 0 (default), old code paths executed
    # These were meant for internal testing, not production
    # Result: Massive unintended trades
```

**Consequence**:
- $440 million loss in 45 minutes
- Company bankruptcy (acquired for $40 million)
- 8 employees terminated

**Risk Mitigation Lessons**:
1. Always remove dead/unused code
2. Comprehensive code review mandatory
3. Gradual rollout with kill switches
4. Real-time monitoring and alerting
5. Proper testing including edge cases

---

## 8. Key Takeaways

1. **Risk is Inevitable**: Every software project faces uncertainties; proactive management determines success
2. **Identification First**: You cannot manage risks you haven't identified—use multiple techniques
3. **Software-Specific Risks**: Security, technology obsolescence, and requirement volatility are critical in modern software development
4. **Quantify When Possible**: Use EMV and probability-impact matrices for objective prioritization
5. **Four-Pronged Strategy**: Avoid, Transfer, Mitigate, or Accept—choose based on risk characteristics
6. **Risk Register is Essential**: Document all risks, their analysis, and responses systematically
7. **Continuous Process**: Risk management is iterative throughout the project lifecycle
8. **Real-World Impact**: Inadequate risk management leads to project failures, financial losses, and reputational damage

---

## 9. Assessment Questions

### Multiple Choice Questions

**Q1. In the Expected Monetary Value (EMV) calculation, if a risk has a 30% chance of causing $50,000 loss and a 70% chance of causing no loss, what is the EMV?**
- (a) $15,000
- (b) $50,000
- (c) $35,000
- (d) $0

**Q2. Which risk response strategy involves shifting the negative impact to a third party?**
- (a) Avoidance
- (b) Mitigation
- (c) Transfer
- (d) Acceptance

**Q3. In a Probability-Impact Matrix, a risk with High probability (0.8) and Low impact ($10,000) falls in which category?**
- (a) Critical
- (b) High
- (c) Medium
- (d) Low

**Q4. Which of the following is NOT a software-specific risk category?**
- (a) Security vulnerabilities
- (b) Technology obsolescence
- (c) Market competition
- (d) Scope creep

**Q5. The Knight Capital incident (2012) was primarily caused by:**
- (a) Insufficient budget
- (b) Unremoved legacy code causing unintended trades
- (c) Hardware failure
- (d) Employee strikes

**Q6. What is the formula for Risk Exposure?**
- (a) Probability + Impact
- (b) Probability - Impact
- (c) Probability × Impact × Detectability
- (d) Impact / Probability

**Q7. A risk register typically does NOT include:**
- (a) Risk description
- (b) Probability and impact
- (c) Final solution code
- (d) Mitigation strategy

**Q8. Which technique uses anonymous surveys to reach consensus on risks?**
- (a) Brainstorming
- (b) Delphi Technique
- (c) SWOT Analysis
- (d) Checklists

**Q9. Requirement volatility risk is BEST managed using:**
- (a) Waterfall methodology
- (b) Change control board and Agile iterations
- (c) Hiring more developers
- (d) Ignoring changes

**Q10. The primary purpose of risk monitoring is to:**
- (a) Identify new risks only
- (b) Track identified risks and identify new ones
- (c) Close all risks immediately
- (d) Transfer all risks to stakeholders

### Answers
1. (a) $15,000 | 2. (c) Transfer | 3. (c) Medium | 4. (c) Market competition | 5. (b) Unremoved legacy code | 6. (c) Probability × Impact × Detectability | 7. (c) Final solution code | 8. (b) Delphi Technique | 9. (b) Change control board and Agile iterations | 10. (b) Track identified risks and identify new ones

---

## 10. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **Risk** | An uncertain event that may positively or negatively affect project objectives |
| **EMV** | Expected Monetary Value = Σ(Probability × Impact) |
| **Risk Avoidance** | Eliminating the threat by removing the cause entirely |
| **Risk Transfer** | Shifting negative impact to a third party (e.g., insurance, outsourcing) |
| **Risk Mitigation** | Reducing probability and/or impact of a risk |
| **Risk Acceptance** | Acknowledging risk without active response; preparing contingency |
| **Risk Register** | Document containing all identified risks and their characteristics |
| **Probability-Impact Matrix** | Tool plotting risks by likelihood and consequence severity |
| **Scope Creep** | Uncontrolled expansion of project requirements |
| **Technology Obsolescence** | Risk of using outdated/deprecated technologies |

---

*This study material aligns with the Delhi University BSc (Hons) Computer Science NEP 2024 UGCF syllabus for Software Engineering, covering all essential aspects of Risk Identification, Projection, and Mitigation for examination preparation and practical application.*