# Read the distance as an integer
distance_km = int(input())

# Initialize total score
total_score = 0

# Fixed bonus
bonus = 50

# Case 1: Distance up to 40 km
if distance_km <= 40:
    total_score = distance_km * 2

# Case 2: Distance between 41 and 60 km
elif distance_km <= 60:
    score_40 = 40 * 2
    extra_km = distance_km - 40
    score_extra = extra_km * 4
    total_score = score_40 + score_extra

# Case 3: Distance between 61 and 120 km
elif distance_km <= 120:
    score_40 = 40 * 2
    score_20 = 20 * 4
    extra_km = distance_km - 60
    score_extra = extra_km * 6
    total_score = score_40 + score_20 + score_extra

# Case 4: Distance above 120 km
else:
    score_40 = 40 * 2
    score_20 = 20 * 4
    score_60 = 60 * 6
    extra_km = distance_km - 120
    score_extra = extra_km * 8
    total_score = score_40 + score_20 + score_60 + score_extra

# Add bonus to total score
total_score += bonus

# Print the final score
print(total_score)
