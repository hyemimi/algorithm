SELECT distinct c.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR c JOIN (
    SELECT CAR_ID, 
    max(
    case when month(START_DATE) = 10 then 1
    ELSE 0
    end 
    ) as "October"
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    GROUP BY CAR_ID
) h
ON c.CAR_ID = h.CAR_ID 
WHERE  c.CAR_TYPE='세단' and h.October = 1
ORDER BY c.CAR_ID DESC