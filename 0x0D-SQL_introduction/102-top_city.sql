-- a scripts that displays the top 3 of cities temperature during july and august ordered by temperature(descending)
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- Filters for July (7) and August (8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

