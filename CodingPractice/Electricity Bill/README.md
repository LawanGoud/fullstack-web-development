## 🧩 **Problem Name:**

**Electricity Bill**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads number of units consumed
- ✅ Applies the **per-unit charge based on slabs**:

  - 0–50 units → ₹2/unit
  - 51–150 units → ₹3/unit
  - 151–250 units → ₹5/unit
  - Above 250 units → ₹8/unit

- ✅ Adds **20% surcharge** on the total bill
- ✅ Prints the **final bill amount**

---

## 🧠 **Concepts Used:**

- Input/output
- Conditional (`if`, `elif`, `else`)
- Arithmetic operators
- Percentage calculation
- No nested conditionals (clear step-by-step logic)

---

## ✅ **Code with Comments:**

```python
# Read units consumed
units = int(input())  # Example: 50

# Initialize total amount
amount = 0

# Calculate bill based on slab
if units <= 50:
    amount = units * 2

elif units <= 150:
    # First 50 units → ₹2/unit, next (units - 50) → ₹3/unit
    amount = 50 * 2 + (units - 50) * 3

elif units <= 250:
    # First 50 → ₹2/unit, next 100 → ₹3/unit, rest → ₹5/unit
    amount = 50 * 2 + 100 * 3 + (units - 150) * 5

else:
    # First 50 → ₹2, next 100 → ₹3, next 100 → ₹5, rest → ₹8/unit
    amount = 50 * 2 + 100 * 3 + 100 * 5 + (units - 250) * 8

# Add 20% surcharge to the total amount
surcharge = amount * 0.20
total_bill = amount + surcharge

# Print final bill amount
print(total_bill)
```

---

## 🧪 **Sample Input:**

```
50
```

## 🧾 **Sample Output:**

```
120.0
```

---
