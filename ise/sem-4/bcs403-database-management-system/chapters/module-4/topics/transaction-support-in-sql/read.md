sql
-- Transaction begins implicitly
UPDATE Accounts SET balance = balance - 1000 WHERE account_id = 101; -- Debit
UPDATE Accounts SET balance = balance + 1000 WHERE account_id = 202; -- Credit

-- Check for errors in your application code here...
-- If no errors, save changes permanently.
COMMIT;

-- If an error occurred (e.g., insufficient funds, system crash), revert changes.
-- ROLLBACK;