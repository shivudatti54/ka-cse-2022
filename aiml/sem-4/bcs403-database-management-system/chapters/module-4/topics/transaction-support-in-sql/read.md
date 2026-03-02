sql
-- Start the transaction
BEGIN TRANSACTION;

-- 1. Deduct amount from Account_A
UPDATE Accounts
SET Balance = Balance - 1000
WHERE Account_Number = 'Account_A';

-- 2. Add amount to Account_B
UPDATE Accounts
SET Balance = Balance + 1000
WHERE Account_Number = 'Account_B';

-- Check for errors (this is pseudo-logic, often done in application code)
-- IF @@ERROR <> 0  -- If an error occurred in any statement
-- BEGIN
--     ROLLBACK TRANSACTION; -- Undo both changes
--     PRINT 'Transaction Failed. Rolling back.';
-- END
-- ELSE
-- BEGIN
--     COMMIT TRANSACTION; -- Save both changes permanently
--     PRINT 'Transaction Committed Successfully.';
-- END

-- For this example, we assume no errors and commit.
COMMIT TRANSACTION;