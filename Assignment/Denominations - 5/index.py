A = int(input())  # Read the amount

# Calculate number of 2000 rupee notes
n2000 = A // 2000
A = A % 2000  # Update the remaining amount

# Calculate number of 500 rupee notes
n500 = A // 500
A = A % 500

# Calculate number of 200 rupee notes
n200 = A // 200
A = A % 200

# Calculate number of 50 rupee notes
n50 = A // 50
A = A % 50

# Calculate number of 20 rupee notes
n20 = A // 20
A = A % 20

# Calculate number of 5 rupee coins/notes
n5 = A // 5
A = A % 5

# Calculate number of 2 rupee coins
n2 = A // 2
A = A % 2

# The remaining amount is in 1 rupee coins
n1 = A

# Print all values in one line
print("2000 :", n2000, "500 :", n500, "200 :", n200, "50 :", n50, "20 :", n20, "5 :", n5, "2 :", n2, "1 :", n1)
