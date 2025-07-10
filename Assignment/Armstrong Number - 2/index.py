# Read the number
N = int(input())

# Convert number to string to access digits
num_str = str(N)

# Calculate sum of 4th powers of each digit
sum_of_powers = int(num_str[0])**4 + int(num_str[1])**4 + int(num_str[2])**4 + int(num_str[3])**4

# Check if it's an Armstrong number
if sum_of_powers == N:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
