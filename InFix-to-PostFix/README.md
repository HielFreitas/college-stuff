# Infix to postfix expression convertion in Python
Simple implementation of fix to postfix expression converter algorithm in Python for my Computer Architecture class.

## infixToPostfix(infix)
This function takes the infix expression as a string and it returns the postfix also as a string.

## Example
```
from InfixToPostfix import * 

infix = 'A+B*C+(D+E)*F'
print("Infix: ", infix)
print("Postfix: ", infixToPostfix(infix))
```
