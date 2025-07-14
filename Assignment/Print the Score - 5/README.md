## 🧩 **Problem Name:**

**Print the Score - 5**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a distance `D` in kilometers.
- ✅ Calculates the score based on the slabs:

  - `0 - 50 km` → 3 points per km
  - `51 - 100 km` → 5 points per km
  - `101 - 200 km` → 6 points per km
  - `> 200 km` → 10 points per km

- ✅ Adds a **bonus score of 100**
- ✅ Prints the total score

---

## 🧠 **Concepts Used:**

- Input/output
- Integer comparison
- Nested `if` statements
- Arithmetic operations
- Accumulative scoring

---

## ✅ **Code:**

```python
D = int(input())  # Read the distance in km
score = 0         # Initial score

if D <= 50:
    score = D * 3
elif D <= 100:
    score = (50 * 3) + ((D - 50) * 5)
elif D <= 200:
    score = (50 * 3) + (50 * 5) + ((D - 100) * 6)
else:
    score = (50 * 3) + (50 * 5) + (100 * 6) + ((D - 200) * 10)

score += 100  # Add bonus
print(score)
```

---

## 🧪 **Sample Input:**

```
120
```

## 🧾 **Sample Output:**

```
620
```

---
