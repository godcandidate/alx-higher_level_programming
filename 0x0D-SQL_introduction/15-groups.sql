-- lists the number of records with the same score
-- from `second_table` of the database `hbtn_0c_0`

SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
