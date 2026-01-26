
def fibonacci_recursive(num) :

    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return fibonacci_recursive(num - 1) + fibonacci_recursive(num - 2)

while True:
    try:
        n = int(input("How many Fibonacci numbers should we generate? "))
        break
    except ValueError:
        print("Please enter a valid integer to continue")

print("Fibonacci is:", fibonacci_recursive(n))
