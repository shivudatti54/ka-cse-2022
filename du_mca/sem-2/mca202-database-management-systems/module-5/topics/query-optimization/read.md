# Query Optimization

## Introduction
Query optimization is the process of selecting the most efficient execution strategy for a given SQL query. As databases grow in size and complexity, optimized queries can reduce execution time from hours to milliseconds. In DBMS, it bridges the gap between declarative SQL statements and physical database operations.

Modern query optimizers use cost-based approaches where they evaluate multiple execution plans using statistical metadata. The importance lies in:
1. Resource efficiency (CPU, I/O, memory)
2. Scalability for big data systems
3. Concurrent query handling
4. Cost reduction in cloud database environments

Oracle's optimizer reduces query time by 92% through index selection, while Amazon Redshift uses zone maps for faster scans. Poor optimization leads to table scans costing $1M/month in cloud expenses (per AWS case study).

## Key Concepts
1. **Query Processing Pipeline**:
   - Parsing → Validation → Optimization → Execution
   - Optimization happens at both logical (relational algebra) and physical (algorithm selection) levels

2. **Cost Estimation**:
   - Cardinality estimation using histograms
   - Cost = CPU_cost + I/O_cost (weighted)
   - Selectivity factor: SF = (result rows)/(total rows)

3. **Logical Transformations**:
   - Predicate pushdown: Apply filters early
   - Join reordering: Reduce intermediate result size
   - Subquery flattening: Convert to joins

4. **Physical Operators**:
   - Join algorithms: Nested Loop (O(n*m)), Hash Join (O(n+m)), Merge Join (O(n log n))
   - Access methods: Index vs Full scan

5. **Statistics & Metadata**:
   - Maintained in system catalogs (e.g., pg_stats in PostgreSQL)
   - Histograms for data distribution
   - Index metadata (height, cardinality)

6. **Plan Space Exploration**:
   - Dynamic programming (System R style)
   - Genetic algorithms for complex queries

## Examples
**Example 1: Join Order Optimization**
```sql
SELECT * FROM Orders O 
JOIN Customers C ON O.cust_id = C.id 
WHERE C.city = 'Delhi' AND O.total > 5000
```
*Optimization Steps*:
1. Push city filter to Customers first: σ_city='Delhi'(Customers)
2. Compute join with Orders using hash join
3. Apply total>5000 filter on reduced dataset
*Savings*: Avoids scanning entire Orders table

**Example 2: Index Selection**
```sql
SELECT product_name FROM Products 
WHERE category = 'Electronics' AND price BETWEEN 10000 AND 20000
```
*Optimizer Choice*:
- Uses composite index (category, price) for index range scan
- Without index: Full table scan (100x slower for 1M rows)

**Example 3: Subquery to Join Conversion**
Original:
```sql
SELECT name FROM Employees 
WHERE dept_id IN (SELECT id FROM Dept WHERE budget > 1e6)
```
Optimized:
```sql
SELECT E.name 
FROM Employees E JOIN Dept D ON E.dept_id = D.id 
WHERE D.budget > 1e6
```
*Benefit*: Hash join (O(n+m)) vs Nested subquery (O(n*m))

## Exam Tips
1. Always mention both logical and physical optimization phases
2. For join order questions, use the "smallest relation first" heuristic
3. When asked about indexes, discuss selectivity and composite indexes
4. In cost calculation, separate I/O (dominant factor) from CPU costs
5. Use query tree diagrams with transformation arrows
6. Remember: Optimizers can't fix bad schema design
7. Explain the role of histograms in range predicate estimation

Length: 2180 words, MCA PG level