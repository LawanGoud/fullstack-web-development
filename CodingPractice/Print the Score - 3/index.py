distance_km = int(input())

total_score = 0

bonus = 30

if distance_km <= 20:
    total_score = distance_km * 2

elif distance_km <= 60:
    score_20 = 20 * 2
    
    extra_km = distance_km - 20
    score_extra = extra_km * 4 
    total_score = score_20 + score_extra

else:
    score_20 = 20 * 2 

    score_40 = 40 * 4 

    extra_km = distance_km - 60 
    score_extra = extra_km * 6 
    total_score = score_20 + score_40 + score_extra

total_score += bonus

print(total_score)