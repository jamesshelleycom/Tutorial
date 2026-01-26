import math

def factorial_recursive(n) :
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_function(condition):
    function_result = math.factorial(condition)
    recursive_result = factorial_recursive(condition)
    return function_result, recursive_result

base_condition = 10

func_result, recur_result = factorial_function(base_condition)

print(f"Function result for", base_condition, "is", func_result)

print(f"Recursive result for", base_condition, "is", recur_result)
