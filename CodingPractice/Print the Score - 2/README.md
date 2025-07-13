## 🧩 **Problem Name:**

**Print the Score - 2**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `D` → Distance in kilometers

- ✅ Calculates score based on:

  - For first 50 km → `3 points per km`
  - For distance above 50 km → `5 points per km`

- ✅ Prints the total score.

---

## 🧠 **Concepts Used:**

- Input/output
- Conditional statements
- Basic arithmetic

---

## ✅ **Code with Comments:**

```python
# Read the distance in kilometers
distance_km = int(input())

# Check if distance is less than or equal to 50
if distance_km <= 50:
    # If within first 50 km, score is 3 points per km
    total_score = distance_km * 3
else:
    # First 50 km → 3 points per km = 50 * 3
    score_first_50 = 50 * 3

    # Remaining km → 5 points per km
    extra_km = distance_km - 50
    score_extra = extra_km * 5

    # Total score is sum of both
    total_score = score_first_50 + score_extra

# Print the final score
print(total_score)
```

---

## 🧪 **Sample Input:**

```
75
```

## 🧾 **Sample Output:**

```
275
```

---
