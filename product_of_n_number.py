# Program to calculate the product of 'N' user-provided numbers


# Get the total number of inputs to expect
total_numbers = int(input())

result_product = 1
processed_count = 0

# Loop until we have processed all 'N' numbers
while processed_count < total_numbers:
    current_value = int(input())
    result_product = result_product * current_value
    processed_count += 1

print(result_product)