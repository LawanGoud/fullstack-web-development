## 🧩 **Problem Name:**

**Profit or Loss**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads two numbers: `cost_price` (CP) and `selling_price` (SP)
- ✅ Compares SP with CP and prints:

  - `"Profit"` if SP > CP
  - `"Loss"` if SP < CP
  - `"No Profit - No Loss"` if SP == CP

---

## 🧠 **Concepts Used:**

- Input/output
- Type conversion (`int` or `float`)
- Comparison operators (`>`, `<`, `==`)
- Conditional statements (`if`, `elif`, `else`)

---

## ✅ **Code with Comments:**

```python
# Read the cost price and selling price
cost_price = int(input())      # Example: 143
selling_price = int(input())   # Example: 155

# Compare selling price with cost price
if selling_price > cost_price:
    print("Profit")  # Earned more than spent
elif selling_price < cost_price:
    print("Loss")    # Sold for less than spent
else:
    print("No Profit - No Loss")  # Sold at same price
```

---

## 🧪 **Sample Input:**

```
143
155
```

## 🧾 **Sample Output:**

```
Profit
```

---
