# Hangman game

## How to play the game?

One player thinks of a word or phrase and the other tries to guess what it is one letter at a time.
The first player draws a number of dashes equivalent to the number of letters in the word. If the guessing player suggests a letter that occurs in the word, the other player fills in the blanks with that letter in the right places. If the word does not contain the suggested letter, the other player draws one element of a hangman’s gallows. As the game progresses, a segment of the gallows and of a victim is added for every suggested letter not in the word. The number of incorrect guesses before the game ends is up to the players, but completing a character in a noose provides a minimum of ten wrong answers until the game ends.

## Objective

Guess the word/phrase before your man gets hung!

## Signature
```python
def hangman(clue_word):
    pass
```

## Test examples
```python
python3 hangman.py Inception
Welcome to Hangman! Let's play!
_ _ _ _ _ _ _ _ _

Guess a letter: n

_ n _ _ _ _ _ _ n

Guess a letter: o

_ n _ _ _ _ _ o n

Guess a letter: p

_ n _ _ p _ _ o n

Guess a letter: k

Incorrect!

Guess a letter:

...
Guess a letter:

I n c e p t i o n

Congratulations!

```

If the player cannot guess the word in ten tries, the game ends and the user should receive this final message!

```
You lost!
 _________
|    |    |
|  \ O /  |
|    |    |
|    |    |
|   / \   |
```
