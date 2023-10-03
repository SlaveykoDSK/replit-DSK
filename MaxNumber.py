numbers = input("How many numbers you would like to compare: ")

max_number = int()

for i in range(int(numbers)):
    n = int(input(f"Write number {i+1}: "))
    if n > max_number:
        max_number = n

print(f"The number max number is equal to: {max_number}")

