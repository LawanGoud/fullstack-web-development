month_number = int(input())

if month_number == 11 or month_number == 12 or month_number == 1:
    print("Winter")
elif month_number == 4 or month_number ==  5 or month_number == 6:
    print("Summer")
elif month_number == 7 or month_number == 8:
    print("Rainy")
elif month_number == 9 or month_number == 10:
    print("Autumn")
else:
    print("Invalid month")