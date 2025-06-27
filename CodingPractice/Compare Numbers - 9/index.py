n = input()

a = int(n[0])
b = int(n[1])
c = int(n[2])

all_gt_7 = (a > 7) and (b > 7) and (c > 7)

product_check = (a * b <= 30) and (b * c <= 30) and (a * c <= 30)

result = all_gt_7 or product_check 

print(result)
