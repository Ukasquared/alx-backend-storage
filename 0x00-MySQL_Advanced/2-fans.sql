-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
ALTER TABLE metal_bands
CHANGE fans nb_fans
SELECT origin, SUM(nb_fans) AS Total
FROM metal_bands
GROUP BY origin
ORDER BY Total DESC;