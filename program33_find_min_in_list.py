# Program 33: Find minimum element in a list

numbers = [12, 45, 7, 89, 23]

min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

print("Minimum value:", min_value)
