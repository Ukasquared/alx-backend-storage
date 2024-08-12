-- script that ranks country origins of bands, ordered by the number of (non-unique) fans
ALTER TABLE metal_bands
CHANGE COLUMN fans nb_fans INT;

SELECT origin, SUM(nb_fans) AS Total
FROM metal_bands
GROUP BY origin
ORDER BY Total DESC;