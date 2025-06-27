n = input()

number = int(n)


if (n[0] != '5' or n[1] != '5' or n[2] != '5') and number >= 300 and number <= 700:
    print("Valid Number")
else:
    print("Not a Valid Number")