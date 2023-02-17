-- 코드를 입력하세요
SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_OUTS
    WHERE SEX_UPON_OUTCOME LIKE 'INTACT%' 
) AND SEX_UPON_INTAKE LIKE 'INTACT%'  
ORDER BY ANIMAL_ID;


# SELECT ANIMAL_ID
# FROM ANIMAL_OUTS
# WHERE SEX_UPON_OUTCOME LIKE 'INTACT%' 