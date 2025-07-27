n = int(input())

product = 1
count = 1
while count <= n:
    num = int(input())
    product *= num
    count += 1
print(product)