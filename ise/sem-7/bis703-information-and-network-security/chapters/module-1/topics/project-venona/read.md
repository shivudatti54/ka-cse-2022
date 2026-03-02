# Project Evaluation and Risk

## Evaluation of Individual Projects

### Why Evaluate Projects?

- Justify investment decisions
- Compare alternative projects
- Optimize resource allocation
- Track return on investment
- Improve future project selection

### Evaluation Criteria

| Criterion             | Question                        |
| --------------------- | ------------------------------- |
| Strategic alignment   | Does it support business goals? |
| Financial viability   | Is the investment justified?    |
| Technical feasibility | Can we build it?                |
| Resource availability | Do we have the capacity?        |
| Risk level            | What could go wrong?            |
| Dependencies          | What must happen first?         |

## Cost-Benefit Evaluation Techniques

### Net Present Value (NPV)

NPV calculates the present value of future cash flows minus initial investment.

**Formula:**

```
NPV = -C₀ + CF₁/(1+r)¹ + CF₂/(1+r)² + ... + CFₙ/(1+r)ⁿ
```

Where:

- C₀ = Initial investment
- CF = Cash flow in year n
- r = Discount rate
- n = Number of years

**Decision Rule:**

- NPV > 0 → Accept project
- NPV < 0 → Reject project
- Higher NPV = Better project

### Return on Investment (ROI)

**Formula:**

```
ROI = (Net Benefit - Cost) / Cost × 100%
```

**Example:**

- Cost: $100,000
- Benefit: $150,000
- ROI = ($150,000 - $100,000) / $100,000 × 100% = 50%

### Payback Period

Time required to recover the initial investment.

**Formula:**

```
Payback Period = Initial Investment / Annual Cash Flow
```

**Decision Rule:**

- Shorter payback = Lower risk
- Compare to acceptable payback threshold

### Internal Rate of Return (IRR)

The discount rate at which NPV equals zero.

**Decision Rule:**

- IRR > Required rate → Accept
- IRR < Required rate → Reject
- Higher IRR = Better project

### Cost-Benefit Analysis Summary

| Technique | Advantages            | Disadvantages              |
| --------- | --------------------- | -------------------------- |
| NPV       | Time value of money   | Requires discount rate     |
| ROI       | Simple to understand  | Ignores time value         |
| Payback   | Simple, risk-focused  | Ignores cash after payback |
| IRR       | Percentage comparison | Can give multiple values   |

## Risk Evaluation

### What is Project Risk?

Risk is an uncertain event that, if it occurs, has a positive or negative effect on project objectives.

**Risk = Probability × Impact**

### Types of Project Risk

| Category           | Examples                                    |
| ------------------ | ------------------------------------------- |
| **Technical**      | Technology fails, complexity underestimated |
| **Schedule**       | Delays, dependencies slip                   |
| **Cost**           | Budget overruns, inflation                  |
| **Quality**        | Defects, performance issues                 |
| **Resource**       | Key person leaves, skills gap               |
| **External**       | Regulations change, market shifts           |
| **Organizational** | Priority changes, funding cut               |

### Risk Management Process

```
Identify → Analyze → Plan Response → Monitor & Control
```

### Risk Identification

**Techniques:**

- Brainstorming
- Checklists
- Expert interviews
- SWOT analysis
- Historical review

### Risk Analysis

**Qualitative Analysis:**

- Probability assessment (High/Medium/Low)
- Impact assessment (High/Medium/Low)
- Risk ranking

**Risk Matrix:**

```
        │  Low    │ Medium │  High   │
High    │ Medium  │  High  │ Critical│
Impact  ├─────────┼────────┼─────────┤
Medium  │  Low    │ Medium │  High   │
        ├─────────┼────────┼─────────┤
Low     │Very Low │  Low   │ Medium  │
        └─────────┴────────┴─────────┘
           Low     Medium    High
                Probability
```

**Quantitative Analysis:**

- Expected Monetary Value (EMV)
- Monte Carlo simulation
- Decision tree analysis

### Expected Monetary Value (EMV)

**Formula:**

```
EMV = Probability × Impact
```

**Example:**

- Risk: Server failure
- Probability: 20%
- Impact: $50,000 loss
- EMV = 0.20 × $50,000 = $10,000

### Risk Response Strategies

**For Threats (Negative Risks):**

| Strategy     | Description                      |
| ------------ | -------------------------------- |
| **Avoid**    | Eliminate the threat entirely    |
| **Mitigate** | Reduce probability or impact     |
| **Transfer** | Shift to third party (insurance) |
| **Accept**   | Acknowledge and budget for it    |

**For Opportunities (Positive Risks):**

| Strategy    | Description                    |
| ----------- | ------------------------------ |
| **Exploit** | Ensure opportunity occurs      |
| **Enhance** | Increase probability or impact |
| **Share**   | Partner to realize benefit     |
| **Accept**  | Take advantage if it occurs    |

### Risk Register

| Risk ID | Description       | Probability | Impact | EMV  | Response | Owner     |
| ------- | ----------------- | ----------- | ------ | ---- | -------- | --------- |
| R001    | Key dev leaves    | Medium      | High   | $15K | Mitigate | PM        |
| R002    | Tech doesn't work | Low         | High   | $20K | Avoid    | Tech Lead |

### Contingency and Management Reserve

**Contingency Reserve:**

- For known risks (known unknowns)
- Calculated from risk analysis
- Controlled by project manager

**Management Reserve:**

- For unknown risks (unknown unknowns)
- Percentage of total budget (5-10%)
- Controlled by management

## Key Takeaways

1. **NPV, ROI, Payback, IRR** are key financial evaluation techniques
2. **Risk = Probability × Impact**
3. Risk management includes **Identify, Analyze, Plan, Monitor**
4. Use **Risk Matrix** for qualitative analysis
5. Response strategies: **Avoid, Mitigate, Transfer, Accept**
6. **Risk Register** documents all identified risks
