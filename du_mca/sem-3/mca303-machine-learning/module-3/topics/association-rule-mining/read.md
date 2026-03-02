# Association Rule Mining

## Introduction
Association Rule Mining (ARM) is a fundamental technique in machine learning for discovering interesting relationships between variables in large databases. Originally developed for market basket analysis to identify product combinations frequently purchased together, it now powers recommendation systems, healthcare analytics, and fraud detection systems.

The importance of ARM lies in its ability to uncover hidden patterns that are not immediately apparent. For DU MCA students, mastering ARM is crucial for building intelligent systems in e-commerce (Amazon's "Frequently Bought Together"), content recommendation (Netflix/Spotify suggestions), and bioinformatics (gene co-occurrence patterns).

Key challenges include handling high-dimensional data, managing computational complexity, and avoiding spurious correlations. The Apriori algorithm (1994) remains foundational, while modern variations like FP-Growth address scalability issues in big data environments.

## Key Concepts
1. **Itemset**: Collection of one or more items (e.g., {milk, bread})
2. **Support**: Probability that transaction contains X ∪ Y  
   `supp(X ⇒ Y) = P(X ∪ Y)`
3. **Confidence**: Conditional probability of Y given X  
   `conf(X ⇒ Y) = P(Y|X) = supp(X ∪ Y)/supp(X)`
4. **Lift**: Measure of interestingness beyond random chance  
   `lift(X ⇒ Y) = supp(X ∪ Y)/(supp(X) × supp(Y))`
5. **Apriori Principle**: If itemset is frequent, all subsets are frequent
6. **FP-Growth**: Uses frequent-pattern tree with divide-and-conquer approach
7. **Anti-Monotonicity**: Support of superset ≤ support of subset

**Algorithms Comparison**:
- Apriori: Breadth-first search, multiple database scans
- FP-Growth: Depth-first search, compressed data structure
- Eclat: Vertical data format, uses set intersections

## Examples

**Example 1: Basic Rule Calculation**
Transactions:
1. {Bread, Milk}
2. {Bread, Diaper, Beer, Eggs}
3. {Milk, Diaper, Beer, Cola}
4. {Bread, Milk, Diaper, Beer}
5. {Bread, Milk, Diaper, Cola}

Find confidence and lift for rule {Milk, Diaper} ⇒ {Beer}

Solution:
- Support({Milk, Diaper, Beer}) = 2/5 = 0.4
- Support({Milk, Diaper}) = 3/5 = 0.6
- Confidence = 0.4/0.6 ≈ 0.667
- Support({Beer}) = 3/5 = 0.6
- Lift = 0.4/(0.6×0.6) ≈ 1.11

**Example 2: Apriori Algorithm**
Min Support = 0.4, Min Confidence = 0.6

Step 1: Find frequent 1-itemsets
Bread(4), Milk(4), Diaper(4), Beer(3) [Cola(2) discarded]

Step 2: Generate 2-itemset candidates:
{Bread,Milk}(3), {Bread,Diaper}(3), {Milk,Diaper}(3), {Diaper,Beer}(3)

Step 3: Prune using min support:
All above itemsets have support 0.6 (3/5)

Step 4: Generate rules:
{Bread} ⇒ {Milk} (conf=3/4=0.75)
{Milk} ⇒ {Bread} (conf=3/4=0.75)
{Diaper} ⇒ {Beer} (conf=3/4=0.75)

## Exam Tips
1. Always mention anti-monotonicity property in Apriori questions
2. For lift interpretation: >1 = positive correlation, <1 = negative
3. FP-Growth's advantage: No candidate generation, uses FP-tree
4. When asked to "find interesting rules", calculate lift not just confidence
5. Remember time complexity: Apriori O(2^D) vs FP-Growth O(D×N)
6. Real-world case: Mention Walmart's beer-diaper discovery
7. Handling large datasets: Use hash trees (Apriori) or partitioning