# Program 32: Find maximum element in a list

numbers = [12, 45, 7, 89, 23]

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("Maximum value:", max_value)


