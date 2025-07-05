n = input()

number = int(n)

digit1 = int(n[0])
digit2 = int(n[1])

if number % digit1 == 0 and number % digit2 == 0:
    print(number * 2)
else:
    print(number)