-- 코드를 입력하세요
SELECT DISTINCT(h.CAR_ID) FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h JOIN CAR_RENTAL_COMPANY_CAR c ON h.CAR_ID = c.CAR_ID WHERE CAR_TYPE = '세단' AND START_DATE LIKE '2022-10%' ORDER BY CAR_ID DESC