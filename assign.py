#!/bin/python3
import os
import sys

from typing import Dict, Optional, Tuple


# Complete the max_result_expression function below.
# You may add any imports you require from the standard library.
# Feel free to define your own helper functions, classes etc as you see fit.


def max_result_expression(expression: str, variables: Dict[str, Tuple[int, int]]) -> Optional[int]:
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].
          
    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """
    expr = expression.split(" ")
    infix = prefixToInfix(expr)
    
    

def prefixToInfix(expression:list) -> Optional [int]:
    if len(expression) == 0:
        return ""
    
    return prefixToInfix(expression[1:-1]) + expression[0] + expression[-1]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    exp = str(input())
    variables = eval(input())
    res = max_result_expression(exp, variables)

    f.write(str(res) + "\n")

    f.close()
