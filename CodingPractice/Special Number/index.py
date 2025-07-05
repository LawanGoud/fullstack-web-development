n = input()

first = int(n[0])
second = int(n[1])

num = int(n)

if (first + second == 7) or (first == 7 or second == 7) or (num % 7 == 0):
    print("Special Number")
else:
    print("Normal Number")