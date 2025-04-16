a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

# Display before swapping
print(f"\nBefore swapping:\na = {a}, b = {b}, c = {c}")

# Swapping using a temporary variable
temp = a
a = b
b = c
c = temp

# Display after swapping
print(f"\nAfter swapping:\na = {a}, b = {b}, c = {c}")