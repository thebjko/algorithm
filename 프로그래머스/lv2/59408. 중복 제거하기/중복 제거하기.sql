# SELECT COUNT(NAME) `COUNT`
# FROM(
#     SELECT DISTINCT NAME
#     FROM ANIMAL_INS
#     WHERE NAME IS NOT NULL
# ) SUB_TB;

SELECT COUNT(distinct(NAME)) AS 'COUNT'
FROM ANIMAL_INS
WHERE NAME IS NOT NULL