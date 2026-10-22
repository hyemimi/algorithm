-- 코드를 작성해주세요
SELECT ID, 
case 
    when SIZE_OF_COLONY > 1000 then "HIGH"
    when 100 < SIZE_OF_COLONY and SIZE_OF_COLONY <= 1000 then 'MEDIUM'
    else "LOW"
end
as "SIZE"
FROM ECOLI_DATA
ORDER BY ID