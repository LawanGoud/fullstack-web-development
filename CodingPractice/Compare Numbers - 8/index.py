n = input()

digit1 = int(n[0])
digit2 = int(n[1])
digit3 = int(n[2])

is_one =( n[0] == '1') or (n[1] == "1") or (n[2] == '1')

sum_less = (digit1 + digit2 + digit3) < 12

last_is_five = n[2] == '5'

result = is_one and sum_less and last_is_five 

print(result)
