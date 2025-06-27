age = int(input())
guardian_status = input()

result = (12 <= age <= 60) or (guardian_status == 'yes')
print(result)