x = int(input())

n = int(input())

product = 1
count = 1

while count <= n:
    number = x + count
    product *= number
    count += 1

print(product)