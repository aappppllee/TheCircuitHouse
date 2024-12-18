SELECT Brand_Name, COUNT(*) AS SKU_Count
FROM ProductInfo
GROUP BY Brand_Name;