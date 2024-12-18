def count_unique_brands():
    return "SELECT COUNT(DISTINCT Brand_Name) FROM ProductInfo;"

def sku_count_per_brand():
    return "SELECT Brand_Name, COUNT(*) AS SKU_Count FROM ProductInfo GROUP BY Brand_Name;"

def price_distribution():
    return """
    SELECT 
        CASE 
            WHEN `Price (Rupee)` < 3000 THEN '<INR 3000'
            WHEN `Price (Rupee)` BETWEEN 3000 AND 4999 THEN 'INR 3000-4999'
            WHEN `Price (Rupee)` BETWEEN 5000 AND 9999 THEN 'INR 5000-9999'
            WHEN `Price (Rupee)` BETWEEN 10000 AND 14999 THEN 'INR 10000-14999'
            WHEN `Price (Rupee)` BETWEEN 15000 AND 19999 THEN 'INR 15000-19999'
            WHEN `Price (Rupee)` >= 20000 THEN 'Greater than INR 20000'
        END AS Price_Band,
        COUNT(*) AS SKU_Count
    FROM ProductInfo
    GROUP BY Price_Band;
    """
