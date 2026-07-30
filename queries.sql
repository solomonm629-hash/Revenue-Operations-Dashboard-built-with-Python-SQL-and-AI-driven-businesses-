-- Revenue Operations SQL Queries

SELECT SUM(Revenue) AS Total_Revenue
FROM revenue_data;

SELECT AVG(Revenue) AS Average_Revenue
FROM revenue_data;

SELECT MAX(Customers) AS Total_Customers
FROM revenue_data;

SELECT AVG(Churn) AS Average_Churn
FROM revenue_data;

SELECT Month, Revenue
FROM revenue_data
ORDER BY Revenue DESC;
