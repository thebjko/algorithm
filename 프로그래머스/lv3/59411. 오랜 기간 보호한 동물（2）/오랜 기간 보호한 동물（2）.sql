-- 코드를 입력하세요
# SELECT ANIMAL_ID, NAME
# FROM (
#     SELECT L.ANIMAL_ID, R.DATETIME-L.DATETIME DATETIME, L.NAME
#     FROM ANIMAL_INS L
#     INNER JOIN ANIMAL_OUTS R
#     ON L.ANIMAL_ID = R.ANIMAL_ID
# ) sub_tb
# ORDER BY DATETIME DESC
# LIMIT 2;

SELECT L.ANIMAL_ID, L.NAME
FROM ANIMAL_INS L
INNER JOIN ANIMAL_OUTS R
    ON L.ANIMAL_ID = R.ANIMAL_ID
ORDER BY R.DATETIME-L.DATETIME DESC
LIMIT 2;