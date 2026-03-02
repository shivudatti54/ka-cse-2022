# Association Rule Mining - Summary

## Key Definitions and Concepts

- **Association Rule**: An implication of the form X → Y where X and Y are disjoint itemsets (X ∩ Y = ∅)
- **Itemset**: A collection of items; k-itemset contains k items
- **Transaction Database**: Collection of transactions, each containing a set of items
- **Frequent Itemset**: Itemset with support ≥ minimum support threshold
- **Strong Rule**: Rule satisfying both min_sup and min_conf thresholds

## Important Formulas and Theorems

- **Support(A)** = Transactions containing A / Total transactions
- **Confidence(X → Y)** = Support(X ∪ Y) / Support(X)
- **Lift(X → Y)** = Confidence(X → Y) / Support(Y)
- **Leverage(X → Y)** = Support(X ∪ Y) - Support(X) × Support(Y)
- **Apriori Property (Anti-monotone)**: If itemset I is infrequent, all its supersets are infrequent

## Key Points

- Association rule mining discovers interesting relationships in transactional data, originally from market basket analysis
- Support measures itemset frequency; confidence measures rule strength
- Lift > 1 indicates positive association, Lift < 1 indicates negative association
- Apriori algorithm uses anti-monotone property for candidate pruning
- FP-Growth builds an FP-tree and is faster than Apriori (only 2 scans vs multiple)
- Frequent itemsets are required before generating association rules
- Strong rules satisfy both minimum support and minimum confidence
- Closed and maximal frequent itemsets provide compressed representations

## Common Mistakes to Avoid

- Confusing support of an itemset with confidence of a rule - support requires both items, confidence is conditional
- Forgetting that X and Y in rule X → Y must be disjoint itemsets
- Applying minimum support threshold to rules instead of itemsets
- Incorrectly interpreting lift values - many students confuse positive and negative associations
- Not understanding that Apriori generates candidate itemsets while FP-Growth directly mines the tree

## Revision Tips

1. Practice calculating support and confidence from raw transaction data - this is the most common question type
2. Memorize the Apriori algorithm steps and understand why candidate pruning works
3. Create a comparison table between Apriori and FP-Growth covering scans, candidate generation, and complexity
4. Solve at least 2-3 full examples of rule generation from frequent itemsets
5. Remember: Lift = 1 means independence, > 1 means positive association, < 1 means negative association