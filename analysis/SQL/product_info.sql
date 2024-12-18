USE productdatabase;
SELECT DISTINCT Brand_Name, `Price (Rupee)`, Rating, Rating_Count, Review_Count, Sponsored
FROM productinfo;

SELECT * from productinfo;

SELECT COUNT(*) AS total_rows
FROM (
    SELECT DISTINCT Brand_Name, `Price (Rupee)`, Rating, Rating_Count, Review_Count, Sponsored
    FROM productinfo
) AS distinct_rows;

