-- Task 15: Count number of records per score and sort descending by number
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;

