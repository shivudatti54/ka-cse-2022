# Riding Your Waves: Demand Management - Summary

## Key Definitions and Concepts

- **Demand Waves**: Fluctuations in user demand for IT services over time, representing peaks and troughs in workload
- **Demand Management**: Strategies to influence when and how users consume IT services
- **Capacity Scaling**: Adjusting IT resources to match demand levels
- **Wave Riding**: Effectively managing demand variations without service degradation or excessive costs

## Important Formulas and Theorems

- **Scaling Factor** = Peak Demand / Base Demand
- **Cost Optimization**: Minimum cost = f(capacity × time) while meeting SLA requirements
- **Auto-scaling Trigger**: Scale-up when metric > threshold, scale-down when metric < threshold

## Key Points

- Demand waves occur in patterns: daily, weekly, seasonal, and event-driven
- Demand shaping influences user behavior to align with capacity
- Demand forecasting uses historical data to predict future requirements
- Vertical scaling adds power to existing resources; horizontal scaling adds more resources
- Elastic scaling automatically adjusts capacity based on real-time demand
- Buffer management maintains reserve capacity for unexpected surges
- Load balancing distributes workloads to prevent individual resource overload
- Throttling controls request rates to protect system integrity during peaks

## Common Mistakes to Avoid

- Confusing demand management with capacity management
- Over-provisioning due to fear of performance issues (leads to unnecessary costs)
- Under-provisioning during planning (results in service failures)
- Ignoring historical data when forecasting demand
- Setting auto-scaling thresholds too aggressively (causes oscillation)

## Revision Tips

- Create a comparison table of scaling approaches (vertical, horizontal, elastic)
- Practice with scenario-based questions involving demand pattern analysis
- Remember that the goal is balancing cost and service quality
- Review cloud provider auto-scaling configurations as practical examples
- Focus on understanding the relationship between demand waves and capacity responses
