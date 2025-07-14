total_days = int(input())

year = total_days // 365 

total_days = total_days % 365 

weeks = total_days // 7

total_days = total_days % 7

days = total_days % 7

print(year, "years", weeks, "weeks", days, "days")