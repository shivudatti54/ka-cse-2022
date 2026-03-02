# UX Metrics

## Table of Contents

- [UX Metrics](#ux-metrics)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Categories of UX Metrics](#categories-of-ux-metrics)
  - [Key UX Metrics and Frameworks](#key-ux-metrics-and-frameworks)
  - [Engagement and Business Metrics](#engagement-and-business-metrics)
  - [Qualitative Research Metrics](#qualitative-research-metrics)
  - [Accessibility Metrics](#accessibility-metrics)
- [Examples](#examples)
  - [Example 1: Calculating SUS Score](#example-1-calculating-sus-score)
  - [Example 2: NPS Calculation for Mobile App](#example-2-nps-calculation-for-mobile-app)
  - [Example 3: Task Completion Analysis for E-commerce Checkout](#example-3-task-completion-analysis-for-e-commerce-checkout)
- [Exam Tips](#exam-tips)

## Introduction

User Experience (UX) Metrics are quantifiable measures used to evaluate the quality of a user's interaction with a product, system, or service. In the context of UI/UX design, measuring user experience is crucial for understanding how well a design meets user needs and business objectives. Without metrics, designers rely solely on intuition and qualitative feedback, which may not capture the true performance of a design in real-world scenarios.

UX metrics provide objective, data-driven insights that help stakeholders make informed decisions about design improvements, feature prioritization, and resource allocation. These metrics bridge the gap between subjective user perceptions and measurable design outcomes. As organizations increasingly focus on user-centered design, understanding and implementing appropriate UX metrics has become an essential skill for designers, product managers, and researchers alike.

The field of UX metrics evolved from traditional usability engineering, where metrics like task success rates and error counts were used to evaluate system performance. Today, UX metrics encompass a broader range of measures including user satisfaction, engagement, accessibility, and business-impact metrics. This comprehensive approach ensures that design decisions are backed by concrete evidence rather than assumptions.

## Key Concepts

### Categories of UX Metrics

**Behavioral Metrics** measure user actions and behaviors while interacting with a product. These include task completion rates, time on task, click-through rates, navigation patterns, and conversion rates. Behavioral metrics are typically captured through analytics tools and provide objective data about how users actually use the product. Examples include tracking which buttons users click, how long they spend on specific pages, and where they encounter difficulties.

**Attitudinal Metrics** capture user perceptions, attitudes, and subjective experiences. These are collected through surveys, interviews, and feedback forms. Common attitudinal metrics include satisfaction scores, perceived ease of use, trust levels, and emotional responses. Techniques like the System Usability Scale (SUS) and Net Promoter Score (NPS) fall into this category. Attitudinal metrics help understand the "why" behind user behaviors.

**Composite Metrics** combine multiple measurements to provide a comprehensive view of user experience. The System Usability Scale (SUS) is a prime example, combining ten Likert-scale questions into a single score ranging from 0 to 100. These metrics offer quick benchmarks for comparing different designs or tracking improvements over time.

### Key UX Metrics and Frameworks

**System Usability Scale (SUS)** is one of the most widely used standardized questionnaires for measuring perceived usability. Developed by John Brooke in 1986, SUS consists of ten questions with five response options each. The final score is calculated by summing the responses and multiplying by 2.5 to get a value out of 100. A score above 68 is considered above average, while scores above 80 indicate excellent usability. SUS is valuable because it is quick to administer, technology-agnostic, and provides reliable results.

**Net Promoter Score (NPS)** measures user loyalty by asking a single question: "How likely are you to recommend this product to a friend or colleague?" Users respond on a 0-10 scale, and responses are categorized as Promoters (9-10), Passives (7-8), or Detractors (0-6). The NPS is calculated by subtracting the percentage of Detractors from the percentage of Promoters, resulting in a score between -100 and +100. NPS is particularly useful for measuring overall customer satisfaction and loyalty.

**Customer Satisfaction Score (CSAT)** measures user satisfaction with a specific interaction, feature, or overall experience. Typically measured on a 1-5 or 1-7 scale, CSAT provides immediate feedback about particular aspects of the product. Unlike NPS which measures loyalty, CSAT focuses on immediate satisfaction and is often used after specific interactions like customer support or completed tasks.

**TIME Metrics** evaluate task-based performance through four dimensions: Time (how long it takes to complete a task), Errors (number of mistakes made), Efficiency (resources consumed), and Memorability (how easily users can re-learn the system). These metrics are particularly useful for evaluating productivity-focused applications and identifying specific pain points in the user journey.

**Heuristic Evaluation Metrics** assess how well a design adheres to established usability heuristics. Nielsen's ten heuristics include visibility of system status, match between system and real world, user control and freedom, consistency and standards, error prevention, recognition rather than recall, flexibility and efficiency of use, aesthetic and minimalist design, help users recognize errors, and help and documentation. Metrics derived from heuristic evaluations include severity ratings for identified issues and compliance scores.

### Engagement and Business Metrics

**Conversion Rate** measures the percentage of users who complete a desired action, such as making a purchase, signing up for a newsletter, or completing a registration. Conversion rate optimization (CRO) is critical for business success and directly connects UX decisions to business outcomes. Low conversion rates often indicate usability issues that prevent users from completing tasks.

**Bounce Rate** indicates the percentage of users who leave a website after viewing only one page. High bounce rates may suggest problems with content relevance, page load times, or first impressions. However, bounce rate interpretation varies by context—for some sites, a high bounce rate may be expected and acceptable.

**Task Completion Rate** measures the percentage of users who successfully complete a given task. This fundamental metric provides direct insight into the usability of a system. Low completion rates indicate significant usability barriers that require immediate attention. Tracking completion rates across different user segments helps identify accessibility and usability issues for specific audiences.

**Churn Rate** measures the percentage of users who stop using a product over a specific period. In UX context, high churn often correlates with poor user experience, unmet needs, or frustrating interactions. Understanding churn patterns helps identify critical touchpoints where users abandon the product.

### Qualitative Research Metrics

**Think-Aloud Protocol Metrics** involve users verbalizing their thoughts while completing tasks. Metrics include time to first comment, frequency of positive versus negative comments, and identification of confusion points. This method provides rich qualitative data about user mental models and decision-making processes.

**Card Sorting Metrics** measure information architecture effectiveness through metrics like open/closed card sort analysis, dendrograms showing user mental models, and agreement indices. These help understand how users expect content to be organized, informing navigation and content structure decisions.

### Accessibility Metrics

**Web Content Accessibility Guidelines (WCAG) Compliance** provides measurable criteria for evaluating accessibility. Metrics include conformance levels (A, AA, AAA), number of accessibility violations, and automated testing scores. Accessibility metrics ensure products are usable by people with diverse abilities and are often required by regulations.

## Examples

### Example 1: Calculating SUS Score

A usability test was conducted with 5 participants who completed the SUS questionnaire. Their responses (odd-numbered questions positively worded, even-numbered negatively worded) are converted to a 0-4 scale where:

- For odd questions: Response minus 1
- For even questions: 5 minus Response

**Participant responses (on 1-5 scale):**

- P1: Q1=4, Q2=2, Q3=4, Q4=1, Q5=4, Q6=2, Q7=5, Q8=2, Q9=4, Q10=2
- P2: Q1=3, Q2=3, Q3=3, Q4=2, Q5=4, Q6=3, Q7=4, Q8=2, Q9=3, Q10=3
- P3: Q1=5, Q2=1, Q3=4, Q4=2, Q5=5, Q6=1, Q7=5, Q8=2, Q9=4, Q10=1
- P4: Q1=4, Q2=2, Q3=3, Q4=3, Q5=4, Q6=2, Q7=4, Q8=3, Q9=3, Q10=2
- P5: Q1=3, Q2=2, Q3=4, Q4=2, Q5=3, Q6=3, Q7=4, Q8=2, Q9=4, Q10=2

**Calculation for Participant 1:**

- Odd questions (Q1,Q3,Q5,Q7,Q9): 4-1=3, 4-1=3, 4-1=3, 5-1=4, 4-1=3 → Sum = 16
- Even questions (Q2,Q4,Q6,Q8,Q10): 5-2=3, 5-1=4, 5-2=3, 5-2=3, 5-2=3 → Sum = 16
- Total = 32, Multiply by 2.5 = 80

**SUS Scores:** P1=80, P2=67.5, P3=90, P4=67.5, P5=75
**Average SUS Score:** (80+67.5+90+67.5+75)/5 = 76

**Interpretation:** The average score of 76 indicates above-average usability (above 68), suggesting the system is relatively easy to use. However, there's variability among users, indicating potential inconsistencies that might need investigation.

### Example 2: NPS Calculation for Mobile App

A mobile banking app conducted a survey with 200 users. The responses to "How likely are you to recommend our app?" were:

- Promoters (9-10): 80 users
- Passives (7-8): 70 users
- Detractors (0-6): 50 users

**Calculation:**

- Percentage of Promoters = (80/200) × 100 = 40%
- Percentage of Detractors = (50/200) × 100 = 25%
- NPS = 40 - 25 = +15

**Interpretation:** An NPS of +15 is moderate. While there are more promoters than detractors, the score indicates room for improvement. The company should analyze detractor feedback to identify pain points and improve the user experience to increase loyalty.

### Example 3: Task Completion Analysis for E-commerce Checkout

An e-commerce website conducted usability testing for their checkout process with 20 users.

**Task:** Complete a purchase of a product priced at ₹999

**Results:**

- Successfully completed: 14 users
- Abandoned checkout: 4 users
- Completed with errors: 2 users (corrected during process)

**Calculations:**

- Task Completion Rate = (14/20) × 100 = 70%
- Error Rate = (2/20) × 100 = 10%
- Abandonment Rate = (4/20) × 100 = 20%

**Analysis:** The 70% completion rate is below industry benchmarks (typically 75-85%). Common issues identified through observation included:

- Confusing payment options (encountered by 6 users)
- Unexpected shipping costs (encountered by 8 users)
- Lengthy form fields (encountered by 5 users)

**Recommendations:** The UX team should focus on reducing form fields, displaying shipping costs earlier in the process, and simplifying payment option selection. These improvements aim to increase the task completion rate to at least 80%.

## Exam Tips

1. **Know the difference between behavioral and attitudinal metrics**: Behavioral metrics measure actual user actions (clicks, time, completion), while attitudinal metrics measure user perceptions and feelings (satisfaction, trust, loyalty).

2. **Remember SUS scoring interpretation**: SUS scores above 68 are above average; above 80 indicates excellent usability. The maximum score is 100.

3. **NPS calculation formula**: NPS = % Promoters (9-10) - % Detractors (0-6). The score ranges from -100 to +100, not 0-100.

4. **TIME metrics components**: Time (task duration), Errors (mistakes made), Efficiency (resources used), and Memorability (re-learning ability).

5. **Understand when to use each metric**: CSAT for immediate post-interaction feedback, NPS for overall loyalty measurement, SUS for comprehensive usability assessment.

6. **Know Nielsen's heuristics**: The ten usability heuristics are frequently tested. Be able to identify examples of each heuristic in interface design.

7. **Key accessibility standards**: Remember WCAG has three conformance levels (A, AA, AAA) and is the primary standard for web accessibility.

8. **Conversion rate importance**: This metric directly connects UX decisions to business outcomes and is critical for demonstrating ROI of UX investments.
