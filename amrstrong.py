# Program to check if a 3-digit number is an Armstrong Number
# Example: 153 -> (1^3 + 5^3 + 3^3) = 153 (True)


number_str = input()  # Taking input as string to access individual digits
digit_1 = int(number_str[0])
digit_2 = int(number_str[1])
digit_3 = int(number_str[2])

original_number = int(number_str)

# Checking the Armstrong condition
if (digit_1**3 + digit_2**3 + digit_3**3) == original_number:
    print("True")
else:
    print("False")