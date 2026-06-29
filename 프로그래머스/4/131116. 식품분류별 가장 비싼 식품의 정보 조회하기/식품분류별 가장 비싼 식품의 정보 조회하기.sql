-- 코드를 입력하세요
SELECT a.CATEGORY, a.MAX_PRICE, p.PRODUCT_NAME
FROM (SELECT CATEGORY, max(PRICE) as "MAX_PRICE" FROM FOOD_PRODUCT
      GROUP BY CATEGORY
       HAVING CATEGORY IN ('과자', '국', '김치', '식용유') )
      a JOIN FOOD_PRODUCT p 
ON a.category = p.category and a.MAX_PRICE = p.price
ORDER BY MAX_PRICE DESC
