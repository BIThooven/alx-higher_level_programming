-- listing all records of a table where name is not empty
SELECT score, name FROM second_table
WHERE NOT name = ""
ORDER BY score DESC;
