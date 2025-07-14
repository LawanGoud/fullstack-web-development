A = int(input())  # Read the amount

hundreds = A // 100        # Number of 100 rupee notes
A = A % 100                # Remaining amount after 100s

fifties = A // 50          # Number of 50 rupee notes
A = A % 50                 # Remaining amount after 50s

twenties = A // 20         # Number of 20 rupee notes
A = A % 20                 # Remaining amount after 20s

tens = A // 10             # Number of 10 rupee notes
A = A % 10                 # Remaining amount after 10s

print("100 Notes:", hundreds)
print("50 Notes:", fifties)
print("20 Notes:", twenties)
print("10 Notes:", tens)
