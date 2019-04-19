## Tasks

Every dictionary in the following tasks can have another dictionary as value or a iterable of dictionaries.

### Task 1

Implement `deep_find(data, key)` which finds the given `key` in the `data` and returns it's value.

**NOTE:** Add 2 solutions - one using DFS and one with BFS.

### Task 2

Implement `deep_find_all(data, key)` which finds the given `key` in the `data` and returns array of the found values.

**NOTE:** Add 2 solutions - one using DFS and one with BFS.

### Task 3

Implement `deep_update(data, key, val)` which updates every occurance of the given `key` in the `data` with `val`.

### Task 4

Implement `deep_apply(func, data)` which applies the given `func` to all **keys** from the given `data`.

### Task 5

Implement `deep_compare(obj1, obj2)` where obj1 and obj2 can be `dict` or `iterable` and compares the given objects.

### Task 6

Implement `schema_validator(schema: List, data: Dict)` which should assert that the given `data` keys are as the given `schema`.
**Notes**
* `data` is valid only if the given keys from the `schema` are found in the `data`.
* If the `schema` has more or less keys, `data` is invalid.
* If there is a missmatch in the `schema` and the `data` keys, `data` is invalid.
* `schema_validator` should work for N levels of nesting.

Example `schema`:

```
schema = [
    'key1',
    'key2',
    [
        'key3',
        ['inner_key1', 'inner_key2']
    ]
]
```

Valid `data`:

```
data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    }
}
```

Invalid `data`:

```
data = {
    'key1': 'val1',
    'key2': 'val2',
    'key3': {
        'inner_key1': 'val1',
        'inner_key2': 'val2'
    },
    'key4': 'not expected'
}
```

### Extra Task

Your task for today is to make your mixins from [week05]() to work with nested objects.

#### Example:
Let's say you have `class Human` and each human has some skills (`class Skill`). If you initialize your object like this:
```python
    marto = Human(
        name='Marto',
        age=20,
        is_student=True,
        job=None,
        skills=[
            Skill('X', level=100),
            Skill('Y', level=10),
        ]
    )
```

Calling `marto.to_json()` should look like this:
```json
{
    "type": "Human",
    "dict": {
        "name": "Marto",
        "age": 20,
        "is_student": true,
        "job": null,
        "skills": [
            {
                "type": "Skill",
                "dict": {
                    "name": "X",
                    "level": 100
                }
            },
            {
                "type": "Skill",
                "dict": {
                    "name": "Y",
                    "level": 10
                }
            }
        ]
    }
}
```

#### Notes

* `from_json()` should also work for nested objects
* Xmlable should work as well
* Think of objects equality!
* Don't forget to write tests!
