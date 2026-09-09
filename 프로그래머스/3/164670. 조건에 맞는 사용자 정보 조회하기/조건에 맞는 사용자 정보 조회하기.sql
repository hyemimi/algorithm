-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, 
concat(u.CITY, " ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) AS "전체주소", 
concat(substr(u.TLNO,1,3), '-', substr(u.TLNO, 4, 4), '-', substr(u.TLNO, 8,4)) AS "전화번호"
FROM (SELECT WRITER_ID, count(*) as "cnt" FROM USED_GOODS_BOARD GROUP BY WRITER_ID HAVING cnt >= 3) c JOIN USED_GOODS_USER u
ON c.WRITER_ID = u.USER_ID
ORDER BY u.USER_ID DESC