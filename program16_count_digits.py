# Program 16: Count number of digits in a number

num = int(input("Enter a number: "))
count = 0

if num == 0:
    count = 1
else:
    while num != 0:
        num = num // 10
        count += 1

print("Total digits:", count)
