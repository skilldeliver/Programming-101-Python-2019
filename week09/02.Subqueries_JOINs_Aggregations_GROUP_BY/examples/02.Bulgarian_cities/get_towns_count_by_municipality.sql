SELECT municipalities.name, municipalities.code, COUNT(*) as 'Towns count'
	FROM towns
	INNER JOIN municipalities
		ON towns.municipality_code == municipalities.code
	GROUP BY municipalities.code;
    
/*
Стъпки:

1. Правим INNER JOIN за да вземем всички градове и села заедно с техните общини
    ```
    SELECT municipalities.name, municipalities.code, towns.name
        FROM towns
        INNER JOIN municipalities
            ON towns.municipality_code == municipalities.code
    ```

2. Групираме градоевете на база на уникалните стойност на колоната `municipaties.code` (GROUP BY municipaties.code)

3. Добавяме агрегацията `COUNT` в `SELECT` клаузата и махаме `towns.name`.
  - искаме уникален ред за всяка група (от GROUP BY) и агрегация върху нея. Тоест можем да SELECT-нем агрегация върху стойностите + всяка колона, която Е УНИКАЛНА ЗА ГРУПАТА (в случая полетата на `municipality` са уникални, полетата на `towns` - не)
*/
