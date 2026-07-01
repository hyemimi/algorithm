-- 코드를 입력하세요
# spayed
# intact: 중성화 x / neutered: 중성화 o
# spayed: 중성화 o / intact: 중성화 x
# in: 중성화 x / out: 중성화 o


SELECT i.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME
FROM ANIMAL_INS i JOIN ANIMAL_OUTS o 
ON i.ANIMAL_ID = o.ANIMAL_ID
where i.SEX_UPON_INTAKE like 'Intact%' and (o.SEX_UPON_OUTCOME like 'Spayed%' or o.SEX_UPON_OUTCOME like 'Neutered%')
ORDER BY i.Animal_id

