# Reverse Polish Notation

Reverse polish notation, or RPN, is one of the three commonly used calculation notations. The other two are polish notation and infix notation.

The latter, infix notation, is the one most commonly used across the world and is probably the form of notation that is most familiar to readers. Infix notation is the standard taught in schools, with the operator placed "in" the formula. For example, to show the calculation 6 plus 3, infix notation is written as 6 + 3.

In contrast, the polish and reverse polish notations place the operator on either side of the numbers. Polish notation would note the above calculation as + 10 5. Reverse polish notation is simply the opposite of that, with the operator appearing after the numbers. The infix notation formula of 6 + 3 is noted as 6 3 + in RPN.

Our task today is to calculate an RPN expression and use the TDD approach to do it.

An RPN expression is one of the following:
* a number `x`, in which case the value of the expression is that of `x`
* a sequence of form `e1 e2 op`, where `e1` and `e2` are RPN expressions and `op`

## Signature
```python
def rpn_calc(expression):
    pass
```

## Test Examples
## Test examples
```python
>>> rpn_calc('20 4 /')
5
>>> rpn_calc('4 2 + 3 -')
3
>>> rpn_calc('3 5 8 * 7 + *')
141
>>> rpn_calc('9 SQRT')
3
```
