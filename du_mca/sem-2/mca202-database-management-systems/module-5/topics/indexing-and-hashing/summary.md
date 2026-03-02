# Indexing and Hashing - Summary

## Key Definitions and Concepts

- **Index**: An auxiliary data structure that provides efficient access paths to database records based on search key values
- **Search Key**: One or more attributes used to locate records in an index
- **B+ Tree**: A balanced tree structure where all data pointers are stored in leaf nodes, with leaf nodes linked sequentially
- **B Tree**: A balanced tree structure where data pointers can be stored in both internal and leaf nodes
- **Hash Index**: Uses a hash function to compute bucket addresses for direct O(1) average-case access
- **Clustering Index**: Determines the physical storage order of data tuples in the relation
- **Secondary Index**: Any index that is not a clustering index; provides alternative access paths

## Important Formulas and Theorems

- **B+ Tree Order m Properties**: Maximum m-1 keys per node, minimum ⌈m/2⌉ keys (except root), all leaves at same level
- **Hash Function**: h(key) = key mod n (basic static hashing), where n is number of buckets
- **Time Complexity**: B+ tree search/insert/delete = O(logₘ n); Hash index search = O(1) average case
- **Index Selectivity**: Fraction of records satisfying a predicate = (records returned / total records)

## Key Points

- Indexes trade space for time—require additional storage but dramatically reduce query execution time
- Only one clustering index per table (determines physical order), but multiple secondary indexes allowed
- B+ trees are preferred over B trees in databases due to higher fan-out and efficient range queries
- Leaf nodes in B+ trees are linked, enabling efficient ordered traversal and range queries
- Hash indexes excel at point queries (O(1) average) but fail for range queries
- Dynamic hashing (extendible/linear) overcomes overflow problems of static hashing
- Composite index on (A, B) can only efficiently support queries filtering on A or (A, B), not B alone
- Index maintenance during INSERT/UPDATE/DELETE adds overhead—balance read optimization with write costs

## Common Mistakes to Avoid

1. **Confusing B and B+ trees**: Remember B+ trees have all data in leaves, B trees have data in both internal and leaf nodes
2. **Thinking multiple clustering indexes possible**: Physical data can only be ordered one way—only one clustering index per table
3. **Ignoring index maintenance costs**: Over-indexing degrades DML performance; each index must be updated on every insert/delete/update
4. **Assuming hash indexes help with range queries**: Hash function destroys ordering; range scans require full index/table scan

## Revision Tips

1. **Draw B+ trees**: Practice constructing and searching B+ trees with small order values to internalize the structure
2. **Remember the leftmost prefix rule**: For composite indexes (A, B, C), only queries on A, (A,B), or (A,B,C) can use the index efficiently
3. **Compare and contrast**: Create a table comparing B+ trees, B trees, hash indexes, and their suitability for different query types
4. **Focus on properties**: For B+ trees, remember the minimum/maximum keys per node, balance property, and leaf node linking
5. **Real-world perspective**: Consider why commercial databases (Oracle, SQL Server, PostgreSQL) predominantly use B+ trees for default indexing