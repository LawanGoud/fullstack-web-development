## 🧩 **Problem Name:**

**Print the Score - 3**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `D` → Distance in kilometers
- ✅ Calculates total score using:

  - First 20 km → `2 points per km`
  - Next 40 km (21-60) → `4 points per km`
  - Beyond 60 km → `6 points per km`

- ✅ Adds a bonus of **30** to the final score
- ✅ Prints the total score

---

## 🧠 **Concepts Used:**

- Input/output
- Conditional statements
- Arithmetic operations
- Cumulative scoring logic

---

## ✅ **Code with Comments:**

```python
# Read the distance in kilometers
distance_km = int(input())

# Initialize score
total_score = 0

# Bonus for all cases
bonus = 30

# Case 1: Distance up to 20 km
if distance_km <= 20:
    total_score = distance_km * 2

# Case 2: Distance between 21 and 60 km
elif distance_km <= 60:
    # First 20 km → 2 points per km
    score_20 = 20 * 2
    # Remaining km (above 20 up to D) → 4 points per km
    extra_km = distance_km - 20
    score_extra = extra_km * 4
    total_score = score_20 + score_extra

# Case 3: Distance above 60 km
else:
    # First 20 km → 2 points
    score_20 = 20 * 2
    # Next 40 km → 4 points
    score_40 = 40 * 4
    # Remaining km (above 60) → 6 points
    extra_km = distance_km - 60
    score_extra = extra_km * 6
    total_score = score_20 + score_40 + score_extra

# Add bonus
total_score += bonus

# Print the total score
print(total_score)
```

---

## 🧪 **Sample Input:**

```
125
```

## 🧾 **Sample Output:**

```
620
```

---
