# Task

Your task for today is to make your mixins from [week05]() to work with nested objects.

## Example:
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

## Notes

* `from_json()` should also work for nested objects
* Xmlable should work as well
* Think of objects equality!
* Don't forget to write tests!
