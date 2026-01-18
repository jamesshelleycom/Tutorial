while True:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid integer")

result = 1 

for i in range(1, n + 1):
    result = result * i

print(result)
