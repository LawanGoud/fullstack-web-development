a = int(input())
b = int(input())

power1 = a ** b 
power2 = b ** a 

if power1 > power2:
    print(power1)
else:
    print(power2)