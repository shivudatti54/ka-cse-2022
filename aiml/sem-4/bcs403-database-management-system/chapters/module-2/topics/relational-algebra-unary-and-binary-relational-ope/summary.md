# Relational Algebra

### Unary Relational Operations

- Projection: $\sigma_{A_i} R$ - selects columns A_i from relation R
- Selection: $\pi_{A_i} R$ - selects rows where A_i is true from relation R
- Union: $R \cup S$ - combines two relations R and S
- Difference: $R \setminus S$ - removes rows in S from relation R
- Intersect: $R \cap S$ - keeps rows in both relations R and S
- Complement: $\overline{R}$ - all possible rows not in relation R

### Binary Relational Operations

- Cartesian Product: $R \times S$ - combines each row of R with each row of S
- Join: $R \bowtie S$ - combines rows of R with rows of S based on a common attribute
- Division: $R \div S$ - returns rows in R for each row in S

### Additional Relational Operations

- Aggregate: $\sigma_{A_i = f(R)} R$ - selects rows where A_i equals a function f of R
- Grouping: $G(R, A_i)$ - partitions relation R by attribute A_i
- Sorting: $\sigma_{A_i = f(R)} R$ - sorts relation R by attribute A_i
- Subquery: $(R \bowtie S).f(R)$ - uses the result of another query R as an attribute

### Theorems and Formulas

- De Morgan's Law: $(R \cup S)^c = R^c \cap S^c$
- Distributive Law: $(R \cap (S \cup T)) = (R \cap S) \cup (R \cap T)$

### Examples of Queries

- Find all employees with salary greater than 50000: $\sigma_{salary > 50000} E$
- Find all customers who have ordered more than one product: $\sigma_{count(\text{order}) > 1} C \bowtie O$
- Find all products with the lowest price: $\sigma_{price = (\text{min}(price))} P$
