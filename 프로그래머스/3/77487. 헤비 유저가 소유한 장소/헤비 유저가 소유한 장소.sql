-- 코드를 입력하세요
# 헤비유저 -> ID를 그룹화하여 카운팅한 갯수를 컬럼으로 사용함. 단, 2 이상이어야 함.
# 아이디 순으로 조회
SELECT P.ID, P.NAME, P.HOST_ID
FROM (SELECT HOST_ID, count(*) as "cnt" FROM PLACES GROUP BY HOST_ID HAVING cnt >= 2) a JOIN PLACES P
ON a.HOST_ID = P.HOST_ID
ORDER BY P.ID
