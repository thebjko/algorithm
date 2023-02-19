# https://stackoverflow.com/questions/4740612/query-to-convert-from-datetime-to-date-mysql
# SELECT ANIMAL_ID, NAME, CAST(DATETIME AS DATE) '날짜'
# FROM ANIMAL_INS;

# SELECT ANIMAL_ID, NAME, DATE(DATETIME) '날짜'
# FROM ANIMAL_INS;

SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d')
FROM ANIMAL_INS;