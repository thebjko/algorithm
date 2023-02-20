SELECT CAR_ID, CAR_TYPE, ROUND(DAILY_FEE*30*(1-DISCOUNT_RATE/100)) FEE
FROM CAR_RENTAL_COMPANY_CAR
NATURAL JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
NATURAL JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN
WHERE CAR_TYPE IN ('세단', 'SUV') AND DURATION_TYPE LIKE '30%'
    AND CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE DATE_FORMAT(START_DATE, '%Y-%m') <= '2022-11' AND DATE_FORMAT(END_DATE, '%Y-%m') >= '2022-11'
    )
GROUP BY CAR_ID
HAVING FEE >= 500000 AND FEE < 2000000
ORDER BY 3 DESC, 2, 1 DESC;