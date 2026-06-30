-- 코드를 작성해주세요
SELECT count(*) as "FISH_COUNT", max(i.length) as "MAX_LENGTH", a.FISH_TYPE
FROM (
    SELECT FISH_TYPE, AVG(
    case
        when length <= 10 OR length is null then 10
        else length
    end
    ) as "avg_length"
    FROM FISH_INFO 
    GROUP BY FISH_TYPE
    HAVING avg_length >= 33
) a JOIN FISH_INFO i ON i.FISH_TYPE = a.FISH_TYPE

GROUP BY a.FISH_TYPE
ORDER BY a.FISH_TYPE