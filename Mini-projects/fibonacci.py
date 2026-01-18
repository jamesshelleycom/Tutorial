a = 0
b = 1

while True:
    try:
        n = int(input("How many Fibonacci numbers should we generate? "))
        break
    except ValueError:
        print("Please enter a valid intege to continue")

for i in range(n):
    print(a)
    a, b = b, a + b