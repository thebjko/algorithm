-- 코드를 입력하세요
SELECT CAR_TYPE, COUNT(CAR_TYPE) CARS
FROM (
    SELECT CAR_TYPE, OPTIONS
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE OPTIONS LIKE '%통풍%' OR OPTIONS LIKE '%열선%' OR OPTIONS LIKE '%가죽%'
) sub_tb
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;
