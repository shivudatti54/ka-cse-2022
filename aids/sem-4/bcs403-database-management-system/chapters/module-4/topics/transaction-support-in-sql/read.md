sql
-- Begin the transaction (implicitly by the first DML statement in many DBMS)
UPDATE Accounts SET balance = balance - 1000 WHERE account_id = 'A';
UPDATE Accounts SET balance = balance + 1000 WHERE account_id = 'B';

-- Check for errors programmatically (e.g., in application code)
-- If no errors are found, permanently save the changes.
COMMIT;

-- If an error occurred (e.g., insufficient balance, system crash), undo the changes.
-- ROLLBACK;