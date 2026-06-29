-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', b.board_id, '/', f.file_id, f.file_name, f.file_ext) as "FILE_PATH"
FROM (SELECT * FROM USED_GOODS_BOARD ORDER BY VIEWS DESC limit 1) b JOIN USED_GOODS_FILE f ON b.BOARD_ID = f.BOARD_ID
ORDER BY f.file_id DESC
              