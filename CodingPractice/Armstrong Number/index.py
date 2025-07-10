# Read the number

n = input()

# converrt each digit to integer and find the cube

a = int(n[0]) ** 3
b = int(n[1]) ** 3
c = int(n[2]) ** 3

# Find the sum of the cubes
armstrong_num = a + b + c

# convert n to integer for comparison
number = int(n)

# Check and print result 
if armstrong_num == number:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")