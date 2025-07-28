m = int(input("Enter the starting number (M): "))
n = int(input("Enter the ending number (N): "))

total = 0

for i in range(m, n + 1):
    total += i

print("The sum of numbers from", m, "to", n, "is:", total)