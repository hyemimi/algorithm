-- 코드를 입력하세요
SELECT year(s.SALES_DATE) as "YEAR", month(s.SALES_DATE) as "MONTH", i.gender, count(distinct s.user_id) as "USERS"
FROM USER_INFO i JOIN ONLINE_SALE s ON i.user_id = s.user_id and i.gender is not null
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER