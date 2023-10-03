count = input("How many numbers you would like to summerize?")

number = 0

for i in range(int(count)):
        number = number + int(input(f"Enter number {i+1}: "))

print(f"The sum is equal to: {number}")