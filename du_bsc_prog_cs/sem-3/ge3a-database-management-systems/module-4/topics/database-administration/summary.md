# Database Administration - Summary

## Key Definitions and Concepts

- **Database Administrator (DBA)**: The professional responsible for installing, configuring, maintaining, securing, and optimizing database management systems
- **ACID Properties**: Atomicity (all-or-nothing), Consistency (valid state), Isolation (concurrent control), Durability (permanent results)
- **Role-Based Access Control (RBAC)**: Grouping privileges into roles for simplified user management
- **Principle of Least Privilege**: Users should have only minimum privileges necessary for their job
- **Recovery Point Objective (RPO)**: Maximum acceptable data loss measured in time
- **Recovery Time Objective (RTO)**: Maximum acceptable downtime

## Important Formulas and Theorems

- **Backup Strategy Formula**: RPO determines backup frequency; more frequent backups = smaller RPO
- **Isolation Level Anomalies**: READ UNCOMMITTED → dirty/non-repeatable/phantom reads; READ COMMITTED → non-repeatable/phantom reads; REPEATABLE READ → phantom reads; SERIALIZABLE → none
- **Index Selectivity**: High cardinality columns benefit most from B-tree indexes; low cardinality columns may use bitmap indexes

## Key Points

- DBAs balance three competing priorities: performance, security, and availability
- Four main types of backups: Full, Incremental, Differential, and Transaction Log
- Security implementation involves Authentication, Authorization, Auditing, and Encryption
- Query optimization uses EXPLAIN plans to identify bottlenecks
- Proper indexing can improve query performance by 90% or more
- Lock escalation and deadlock prevention are critical for concurrency management
- Data dictionary contains metadata essential for database administration

## Common Mistakes to Avoid

- Granting excessive privileges (not following least privilege principle)
- Neglecting to test backup and recovery procedures regularly
- Creating too many indexes (impacts INSERT/UPDATE performance)
- Ignoring transaction log management (leads to disk space issues)
- Not monitoring database performance proactively

## Revision Tips

1. Practice writing SQL commands for user creation, privilege granting, and basic administration tasks
2. Memorize the differences between backup types and when each is appropriate
3. Review isolation level characteristics and the anomalies each prevents
4. Understand the relationship between normalization and performance optimization
5. Prepare flowchart for backup and recovery decision-making processes