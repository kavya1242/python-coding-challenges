# Program to break down an amount into denominations (500, 50, 10, 1)

amount = int(input())

# Calculating 500 rupee notes
notes_500 = amount // 500
remaining_after_500 = amount % 500

# Calculating 50 rupee notes
notes_50 = remaining_after_500 // 50
remaining_after_50 = remaining_after_500 % 50

# Calculating 10 rupee notes
notes_10 = remaining_after_50 // 10
remaining_after_10 = remaining_after_50 % 10

# Calculating 1 rupee notes
notes_1 = remaining_after_10 // 1

print(f"500: {notes_500} 50: {notes_50} 10: {notes_10} 1: {notes_1}")