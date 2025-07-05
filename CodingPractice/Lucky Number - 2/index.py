n = input()

number = int(n)
digit1 = int(n[0])
digit2 = int(n[1])

if number % 9 == 0 or  digit1 == 9 or digit2 == 9:
    print("Lucky Number")
else:
    print("Unlucky Number")