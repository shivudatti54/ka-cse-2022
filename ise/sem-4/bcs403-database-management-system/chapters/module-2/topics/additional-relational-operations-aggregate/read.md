sql
SELECT SUM(Amount) AS TotalSales,
COUNT(OrderID) AS TotalOrders
FROM Sales;
