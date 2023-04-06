-- 코드를 입력하세요
SELECT * FROM (SELECT CAR_ID, CAR_TYPE, (CASE WHEN CAR_TYPE = '세단' THEN ROUND(DAILY_FEE * 30 * 0.92) ELSE ROUND(DAILY_FEE * 30 * 0.95) END) AS FEE FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_TYPE IN ('세단', 'SUV') ) AS A 
WHERE FEE >= 500000 AND FEE < 2000000 AND (CAR_ID) IN (SELECT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING (DATE_FORMAT(MAX(START_DATE),'%Y-%m-%d') > '2022-11-30' OR DATE_FORMAT(MAX(END_DATE),'%Y-%m-%d') < '2022-11-01'))
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC