## 🧩 **Problem Name:**

**Days Conversion**

---

## 🎯 **Goal:**

Write a program that:

✅ Reads a number `N` (total days)
✅ Converts it into:

- Years (1 year = 365 days)
- Weeks (1 week = 7 days)
- Remaining Days

---

## 🧠 **Concepts Used:**

- Input/output
- Integer division (`//`)
- Modulus (`%`)
- Step-by-step breakdown

---

## ✅ **Code:**

```python
# Read total number of days
N = int(input())

# Calculate number of years
Y = N // 365

# Remaining days after years
remaining_days = N % 365

# Calculate number of weeks
W = remaining_days // 7

# Remaining days after weeks
D = remaining_days % 7

# Print the result
print(Y, "years", W, "weeks", D, "days")
```

---

## 🧪 **Sample Input:**

```
1329
```

## 🧾 **Sample Output:**

```
3 years 33 weeks 3 days
```

---
