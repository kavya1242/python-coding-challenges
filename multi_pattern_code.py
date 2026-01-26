# Multi-Pattern Generator Tool (Butterfly, Diamond, Pyramid)
# This is an independent project created to demonstrate complex nested logic 
# and user-interactive CLI tools.
# Author: Kavya (Dr. AIT, ECE)

print("Choose pattern among: BUTTERFLY, HALLOW BUTTERFLY, DIAMOND, PYRAMID")
pattern = input("Type the pattern in capital words: ")
n = int(input("Enter the size (number >= 2): "))

space = " "

if pattern == "BUTTERFLY":
    symbol ="🤍"
    for i in range(1, n + 1):
        print(symbol * i + space * (4 * (n - i)) + symbol * i)
    for i in range(1, n):
        print(symbol * (n - i) + space * (4 * i) + symbol * (n - i))

elif pattern == "DIAMOND":
    symbol = "🤍"
    for i in range(1, n + 1):
        print(space * (n - i) + symbol * i)
    for i in range(1, n):
        print(space * i + symbol * (n - i))

elif pattern == "HALLOW BUTTERFLY":
    symbol = "* "
    # Top edge
    print(symbol + space * (4 * (n - 1)) + symbol)
    # Upper half
    for i in range(1, n):
        side_space = space * int(((i * 4) - 4) // 2)
        mid_space = space * (4 * ((n - 1) - i))
        print(symbol + side_space + symbol + mid_space + symbol + side_space + symbol)
    # Lower half
    for i in range(1, n):
        side_space = space * (2 * ((n - 1) - i))
        mid_space = space * ((i * 4) - 4)
        print(symbol + side_space + symbol + mid_space + symbol + side_space + symbol)
    # Bottom edge
    print(symbol + space * (4 * (n - 1)) + symbol)

elif pattern == "PYRAMID":
    symbol = "🤍"
    for i in range(1, n + 1):
        row = space * 2 * (n - i) + symbol * (2 * i - 1)
        print(row)
else:
    print("Invalid pattern. Please try again.")