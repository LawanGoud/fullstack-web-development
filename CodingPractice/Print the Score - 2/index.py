distance_km = int(input())

if distance_km <= 50:
    total_score = distance_km * 3 
else:
    score_first_50 = 50 * 3 

    extra_km = distance_km - 50 
    score_extra = extra_km * 5 

    total_score = score_first_50 + score_extra

print(total_score)