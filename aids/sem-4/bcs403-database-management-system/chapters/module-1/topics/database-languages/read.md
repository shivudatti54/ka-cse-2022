sql
BEGIN TRANSACTION;
UPDATE Accounts SET Balance = Balance - 5000 WHERE Acc_No = 'A1'; -- Debit
UPDATE Accounts SET Balance = Balance + 5000 WHERE Acc_No = 'A2'; -- Credit
COMMIT; -- If both updates succeed, make changes permanent. If one fails, use ROLLBACK.