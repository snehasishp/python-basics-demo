num = int(input("Enter the number:"))

if num > 0:
    print(f"The number {num} is positive")
    if (num % 2 == 0):
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")
elif num == 0:
    print(f"The number {num} is zero")
else:
    print(f"The number {num} is negative")

# print("Infinity symbol (Unicode): \u221E")