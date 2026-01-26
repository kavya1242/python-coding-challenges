# Program to convert total days into Years, Weeks, and Days

n = int(input())

# Calculate Years
years = n // 365 
remaining_days_after_years = n % 365

# Calculate Weeks from the remaining days
weeks = remaining_days_after_years // 7

# Calculate final remaining Days
days = remaining_days_after_years % 7

print(years,"year")
print(weeks,"weeks")
print(days,"days")