# Database Transactions

## Overview

Transactions ensure atomicity of database operations, guaranteeing that either all operations succeed or none apply. Understanding transaction management is critical for data consistency in Android applications.

## Key Points

- **beginTransaction()**: Starts transaction block
- **setTransactionSuccessful()**: Marks transaction for commit
- **endTransaction()**: Commits if successful, rolls back otherwise
- **Atomicity**: All or nothing principle for grouped operations
- **Performance**: Batch operations in transactions are significantly faster
- **Thread Safety**: Transactions should occur on same thread

## Important Concepts

- Default behavior: transaction rolls back if setTransactionSuccessful() not called
- Nested transactions not supported
- Transactions improve performance for bulk inserts/updates
- Use try-finally to ensure endTransaction() called
- Transactions lock database until completion

## Notes

- Always use transactions for multiple related operations
- Call setTransactionSuccessful() only if all operations succeed
- Use try-finally pattern to guarantee endTransaction()
- Batch inserts 100x faster with transactions than individual commits
