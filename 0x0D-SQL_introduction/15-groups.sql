-- script to group results
SELECT `score`, COUNT(*) AS number FROM second_table GROUP BY score DESC;
