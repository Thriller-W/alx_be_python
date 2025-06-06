## user input
number = int(input("Enter a number to see its multiplication table: "))

## Solution for Multiplication table
for i in range (1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
