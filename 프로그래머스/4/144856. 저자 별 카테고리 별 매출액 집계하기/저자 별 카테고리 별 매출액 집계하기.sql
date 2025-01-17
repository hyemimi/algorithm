-- 코드를 입력하세요
SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(S.SALES * B.PRICE) AS TOTAL_SALES
FROM (BOOK B JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID) JOIN AUTHOR A ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE S.SALES_DATE like '%2022-01%'
GROUP BY B.AUTHOR_ID, B.CATEGORY
ORDER BY AUTHOR_ID,CATEGORY DESC