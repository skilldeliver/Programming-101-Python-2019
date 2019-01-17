# Intervals

You are presented with a bunch of lines with integers on each line:

```
-181
-414
441
889
-547
-313
622
679
782
-640
```

The integers can be positive and negative.

## The task

In a language of your choice, implement a program, that reads those lines from the standard input (stdin), and outputs all consecutive intervals of the numbers, in ascending order.

For example, for the input:

```
-181
-414
441
889
-547
-313
622
679
782
-640
```

The output should be:

```
[-640, -640] with consecutive count of 1
[-547, -547] with consecutive count of 1
[-414, -414] with consecutive count of 1
[-313, -313] with consecutive count of 1
[-181, -181] with consecutive count of 1
[441, 441] with consecutive count of 1
[622, 622] with consecutive count of 1
[679, 679] with consecutive count of 1
[782, 782] with consecutive count of 1
[889, 889] with consecutive count of 1
```

Another example, for the input:

```
123
567
124
568
-100
-99
```

The output should be:

```
[-100, -99] with consecutive count of 2
[123, 124] with consecutive count of 2
[567, 568] with consecutive count of 2
```

**The output should end with a newline.**

## The tests

Alongside the task, add tests, that proove your solution is correct. This is entirely up to you.

