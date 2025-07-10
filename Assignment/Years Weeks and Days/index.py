# Read the number of days
N = int(input())

# Calculate years
years = N // 365

# Remaining days after years
remaining_days = N % 365

# Calculate weeks from remaining days
weeks = remaining_days // 7

# Remaining days after weeks
days = remaining_days % 7

# Print the result
print(years)
print(weeks)
print(days)
