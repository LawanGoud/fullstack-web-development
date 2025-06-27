salary = int(input())
years = int(input())

if years > 5:
    bonus = salary * 5 / 100 
    print(bonus)
else:
    print("No Bonus")