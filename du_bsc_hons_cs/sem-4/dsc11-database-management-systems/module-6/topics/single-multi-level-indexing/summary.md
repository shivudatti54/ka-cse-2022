# Single and Multi-Level Indexing - Summary

## Key Definitions and Concepts

- **Index**: An auxiliary data structure that provides fast access to database records based on search key values
- **Search Key**: An attribute or set of attributes on which an index is built
- **Primary Index**: Built on primary key; data file is physically sorted; sparse index
- **Clustering Index**: Built on non-key attribute with logical ordering; groups similar records together
- **Secondary Index**: Built on any non-key attribute; always dense; allows multiple per table
- **Dense Index**: Index entry exists for every record in the data file
- **Sparse Index**: Index entry exists only for some records (typically block addresses)
- **B-Tree**: Balanced tree with data stored in both internal and leaf nodes
- **B+ Tree**: Enhanced B-tree where all data is stored only in leaf nodes; leaf nodes are linked

## Important Formulas and Theorems

- **B-Tree of order m**: Maximum children = m, minimum children = ⌈m/2⌉ (except root)
- **B+ Tree of order m**: Maximum keys in leaf = m, minimum = ⌈m/2⌉, internal nodes have max m-1 keys
- **Search Complexity**: O(logₘn) where m = tree order, n = number of records
- **Single-level index search**: O(log₂b) where b = number of index blocks
- **Disk I/O for B+ tree**: Height of tree = number of levels (typically 2-4 for millions of records)

## Key Points

- Indexes dramatically reduce query time from O(n) to O(log n) but increase storage overhead and slow down data modification operations
- Primary indexes require sorted data files and are sparse; secondary indexes are always dense
- B+ trees are the dominant index structure in modern RDBMS due to efficient range queries and balanced performance
- In B+ trees, all actual data pointers are in leaf nodes; internal nodes only contain search keys
- The linked list structure of B+ tree leaves enables efficient range queries (e.g., BETWEEN, >, <)
- Multi-level indexing solves the problem of indexes too large to fit in memory
- Index selectivity (percentage of records returned) determines index usefulness—highly selective indexes provide greater benefit

## Common Mistakes to Avoid

- Confusing B-tree and B+ tree: Remember B-trees store data in all nodes, B+ trees only in leaves
- Thinking all indexes improve performance: Too many indexes hurt INSERT/UPDATE performance
- Believing primary indexes can have duplicate values: Primary keys must be unique
- Overlooking that secondary indexes always point to primary key, requiring additional lookup (index clustering factor)

## Revision Tips

- Practice constructing B+ trees with different orders and insertion sequences
- Memorize the differences between index types with a comparison table
- For exam questions, always calculate disk I/O counts when analyzing query performance
- Understand the relationship between index order, tree height, and search performance
- Review how database systems like MySQL and PostgreSQL implement indexes using B+ trees