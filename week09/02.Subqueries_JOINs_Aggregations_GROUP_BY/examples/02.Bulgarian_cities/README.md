# Bulgarian cities
---

NOTE: Има коментари в sql файловете :wink:


В базата има 3 таблици:

1. 'towns'
  - id - primary key
  - type - varchar
  - name - varchar
  - ekatte - varchar
  - postal_code - varchar
  - region_code - varchar
  - municipality_code - varchar

2. `regions`
  - id - primary key
  - name - varchar
  - code - varchar
  - ekatte - varchar

3. `municipalities`
  - id - primary key
  - name - varchar
  - code - varchar
  - ekatte - varchar


## Примери за GROUP BY + Aggregation

- `get_towns_count_by_municipality.sql` -  взима броят градовете и селата във всяка община в страната

- `get_cities_count_by_region.sql` -  взима само броят ГРАДОВЕТЕ във всяка област в страната

- `get_towns_count_by_region_starting_with_a.sql` -  взима само броят СЕЛАТА във всяка област в страната, САМО за областите, имената на които, започват с `Б`
