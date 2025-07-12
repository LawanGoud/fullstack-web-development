## 🧩 **Problem Name:**

**Get Season**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `month_number` (1 to 12)
- ✅ Maps the month to a season:

  - **Winter** → November (11), December (12), January (1)
  - **Summer** → April (4), May (5), June (6)
  - **Rainy** → July (7), August (8)
  - **Autumn** → September (9), October (10)

---

## 🧠 **Concepts Used:**

- Input/output
- Integer comparison
- `if` / `elif` / `else` statements
- Logical `or` operator

---

## ✅ **Code with Comments:**

```python
# Read the month number
month_number = int(input())  # Example: 1

# Check the season based on month number
if month_number == 11 or month_number == 12 or month_number == 1:
    print("Winter")
elif month_number == 4 or month_number == 5 or month_number == 6:
    print("Summer")
elif month_number == 7 or month_number == 8:
    print("Rainy")
elif month_number == 9 or month_number == 10:
    print("Autumn")
else:
    print("Invalid month")  # If the month number is not between 1 and 12
```

---

## 🧪 **Sample Input:**

```
1
```

## 🧾 **Sample Output:**

```
Winter
```

---
