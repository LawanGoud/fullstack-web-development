distance = int(input())

score = 0

if distance <= 50:
    score = distance * 3
elif distance <= 100:
    score = (50 * 3) + ((distance - 50) * 5)
elif distance <= 200:
    score = (50 * 3) + (50 * 5) + ((distance - 100) * 6)
else:
    score = (50 * 3) + (50 * 5) + (100 * 6) + ((distance - 200) * 100)

score += 100
print(score)