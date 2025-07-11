units = int(input())

amount = 0 

if units <= 50:
    amount = units * 2 

elif units <= 150:
    amount = 50 * 2 + (units - 50) * 3

elif units <= 250:
    amount = 50 * 2 + 100 * 3 + (units - 150) * 5

else:
    amount = 50 * 2 + 100 * 3 + 100 * 5 + (units - 250) * 8

surcharge = amount * 0.20
total_bill = amount + surcharge

print(total_bill)