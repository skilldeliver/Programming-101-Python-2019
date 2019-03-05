# Are two words anagrams?
Create a function, that reads two words from the standard input and output and returns if the two of them are anagrams.
For anagrams, check here - https://en.wikipedia.org/wiki/Anagram

For example, `listen` and `silent` are anagrams.
**Consider lowering the case of the two words since the case does not matter. `SILENT` and `listen` are also anagrams.**

## Signature:
```python
def anagrams():
    pass
```


## Expected output
* `ANAGRAMS` if the words are anagrams of each other
* `NOT ANAGRAMS` if the two words are not anagrams of each other


## Test Examples

Input:

```
TOP_CODER COTO_PRODE
```

Output:

```
NOT ANAGRAMS
```

---

Input:

```
boro kilata
```

Output:

```
NOT ANAGRAMS
```

Also, should not make songs together.

---

Input:

```
BRADE BEARD
```

Output:

```
ANAGRAMS
```
