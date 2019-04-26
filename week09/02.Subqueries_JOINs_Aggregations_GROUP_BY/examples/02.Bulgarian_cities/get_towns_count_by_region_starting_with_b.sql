SELECT regions.name, regions.code, COUNT(*) as 'Towns count'
	FROM towns
	INNER JOIN regions
		ON towns.region_code == regions.code
	WHERE towns.type == 'с.'
	GROUP BY regions.code
		 HAVING regions.name LIKE 'Б%';

/*
Стъпки:

1. Правим INNER JOIN за да вземем всички ГРАДОВЕ заедно с техните области
    ```
    SELECT regions.name, regions1.code, towns.name
        FROM towns
        INNER JOIN regions
            ON towns.region_code == regions.code
        WHERE towns.type == 'с.'
    ```

2. Групираме градовете на база на уникалните стойност на колоната `regions.code` (GROUP BY regions.code)

3. Добавяме агрегацията `COUNT` в `SELECT` клаузата и махаме `towns.name`.
  - искаме уникален ред за всяка група (от GROUP BY) и агрегация върху нея. Тоест можем да SELECT-нем агрегация върху стойностите + всяка колона, която Е УНИКАЛНА ЗА ГРУПАТА (в случая полетата на `regions` са уникални, полетата на `towns` - не)

4. Добавяме условието че името на региона трябва да започва с `Б` - `HAVING regions.name LIKE 'Б%'`
*/
