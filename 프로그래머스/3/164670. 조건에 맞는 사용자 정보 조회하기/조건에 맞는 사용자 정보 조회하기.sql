-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ', STREET_ADDRESS1,' ', STREET_ADDRESS2) as "전체주소", CONCAT(substr(TLNO,1,3), '-', substr(TLNO,4,4), '-', substr(TLNO,8, 4)) as "전화번호"
FROM USED_GOODS_USER u JOIN (
    SELECT count(writer_id), writer_id
    FROM USED_GOODS_BOARD
    GROUP BY writer_id
    Having count(writer_id) >= 3
) b ON u.user_id = b.writer_id

ORDER BY USER_ID DESC