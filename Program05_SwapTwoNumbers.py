# Program05_SwapTwoNumbers.py
# This program swaps two numbers without using a temporary variable

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

# Swapping
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
