SELECT SUM(Sales) AS Total_Sales
FROM superstore;

SELECT SUM(Profit) AS Total_Profit
FROM superstore;

SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

SELECT Region, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region;

SELECT [Product Name], SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY [Product Name]
ORDER BY Total_Sales DESC
LIMIT 10;