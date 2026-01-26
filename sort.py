# Program to remove duplicates from an input list and sort it
# Demonstrates: String splitting, Sets for uniqueness, and List Sorting


# Input: 10 20 10 30 20
# Output: [10, 20, 30]

input_data = input().split()

# Using a set to automatically remove duplicate values
unique_values = set(input_data)

integer_list = []
for item in unique_values:
    integer_list.append(int(item))

# Sorting the final list for a clean output
print(sorted(integer_list))