# The Effects of Social Websites and Open APIs - Summary

## Key Definitions and Concepts

- **Flash Crowd**: A sudden, extreme increase in website traffic, typically caused by viral content being shared on social media platforms, creating demand that can exceed normal levels by orders of magnitude.

- **Open API (Application Programming Interface)**: A publicly accessible interface that allows third-party developers to build applications on top of an existing platform, enabling system interoperability and integration.

- **Rate Limiting**: A technique used to control the number of requests a client can make to an API within a specified time period, protecting backend systems from overload.

- **API Throttling**: Similar to rate limiting, but often refers to temporarily reducing request processing speed rather than outright rejecting excess requests.

- **Horizontal Scaling**: Adding more servers or instances to handle increased load, as opposed to upgrading existing server resources (vertical scaling).

## Important Formulas and Calculations

- **Scaling Factor**: Required Servers = Peak Requests ÷ Single Server Capacity
- **Cached Requests**: Effective Origin Requests = Total Requests × (1 - Cache Hit Rate)
- **API Rate Limit per Client**: Available Capacity ÷ Number of Clients
- **Cascading API Requests**: Downstream Requests = Upstream Requests × Dependency Probability

## Key Points

1. Social media traffic is highly unpredictable due to viral content, requiring auto-scaling and flexible infrastructure.

2. Flash crowds can cause traffic increases of 50x or more within minutes, overwhelming unprepared systems.

3. Open APIs create interconnected ecosystems where failures can cascade through multiple dependent systems.

4. Effective rate limiting balances accessibility for developers with protection of backend resources.

5. Caching strategies can reduce origin server load by 80% or more during traffic spikes.

6. Geographic distribution through CDNs is essential for global social media audiences.

7. Graph databases are preferred for social networks due to their efficiency in managing relationship data.

8. Micro-service architectures require capacity planning at each service level, accounting for dependency chains.

## Common Mistakes to Avoid

- Ignoring the cascading effect when calculating capacity for API-dependent systems
- Setting fixed rate limits without considering burst allowances for legitimate traffic
- Underestimating the impact of viral content on infrastructure requirements
- Failing to account for both internal and external API consumers in capacity calculations

## Revision Tips

1. Practice calculating rate limits with different numbers of consumer tiers and capacity allocations.

2. Review micro-service dependency examples to understand how request volumes propagate through systems.

3. Remember that social media capacity planning requires both quantitative analysis and qualitative understanding of user behavior patterns.

4. Focus on understanding the relationship between caching, auto-scaling, and cost optimization in variable traffic scenarios.
