# Cloud Capacity - Use It or Lose It - Summary

## Key Definitions and Concepts

- **Cloud Capacity**: Total computing resources (CPU, RAM, storage, network) available in a cloud environment that can be provisioned and scaled.

- **Reserved Capacity**: Cloud resources committed for a fixed period (typically 1-3 years) with significant discounts but mandatory payment regardless of usage.

- **Use It or Lose It**: Principle where organizations must pay for reserved cloud capacity whether fully utilized or not; unused reserved capacity represents pure financial waste.

- **On-Demand Capacity**: Flexible pay-per-use model with no commitment but higher per-unit costs.

- **Spot/Preemptible Instances**: Discounted excess capacity that can be interrupted with short notice.

## Important Formulas and Theorems

- **Reserved vs On-Demand Savings**: Savings = (On-Demand Annual Cost) - (Reserved Annual Cost)

- **Cost per VM (Reserved)**: Total Reserved Cost ÷ Number of VMs ÷ 12 = Monthly cost per VM

- **Break-even Analysis**: Reserved is beneficial when: (On-Demand Rate × Utilization Hours) > Reserved Rate

- **Capacity Utilization Rate**: (Actual Used Capacity ÷ Reserved Capacity) × 100%

## Key Points

- The "use it or lose it" principle applies specifically to reserved cloud instances, not on-demand resources.

- Reserved capacity offers 40-60% discounts compared to on-demand pricing but requires accurate demand forecasting.

- Over-reservation leads to significant financial waste that cannot be recovered during the commitment period.

- Mixed definitions in cloud capacity include: physical vs virtual, allocated vs consumed, and committed vs uncommitted.

- Steady-state workloads are ideal for reserved capacity; variable workloads suit on-demand; fault-tolerant batch jobs can use spot instances.

- Auto-scaling helps optimize on-demand costs but requires proper configuration to avoid unexpected bills.

- Cloud providers use different terminology: Reserved Instances (AWS), Reserved VM Instances (Azure), Committed Use Discounts (GCP).

## Common Mistakes to Avoid

1. **Over-reserving capacity**: Always forecast accurately; unused reserved instances waste money with no recovery option.

2. **Ignoring utilization tracking**: Not monitoring reserved instance utilization leads to continued waste.

3. **Choosing reserved for highly variable workloads**: Reserved capacity suits predictable, steady workloads only.

4. **Not considering growth projections**: Reservations should account for expected growth during the commitment period.

5. **Forgetting about spot instance limitations**: Spot instances can be terminated with 2-minute notice; never use for critical production workloads.

## Revision Tips

1. Create a comparison table of pricing models covering cost, flexibility, risk, and suitable workload types.

2. Practice numerical problems comparing reserved vs on-demand costs with different utilization scenarios.

3. Remember the key principle: Reserved = Commitment = Discount = Use it or lose it.

4. Review real-world case studies of cloud cost optimization failures due to poor capacity planning.

5. Understand that "mixed definitions" refers to different ways of categorizing cloud capacity - always specify which definition you're using.
