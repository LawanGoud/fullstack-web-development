## 🧩 **Problem Name:**

**Denominations - 5 (One-line Output with Comments)**

---

## 🎯 **Goal:**

- ✅ Read amount `A`
- ✅ Calculate minimum number of notes for:
  `2000`, `500`, `200`, `50`, `20`, `5`, `2`, `1`
- ✅ Print output in a **single line**
- ✅ Add clear **comments and explanation**

---

## 🧠 **Concepts Used:**

- Integer division (`//`) – to get how many notes
- Modulus (`%`) – to find the remaining amount
- `print(..., end=" ")` – for single-line output
- Step-by-step breakdown using basic operators

---

## ✅ **Code:**

```python
A = int(input())  # Read the amount

# Calculate number of 2000 rupee notes
n2000 = A // 2000
A = A % 2000  # Update the remaining amount

# Calculate number of 500 rupee notes
n500 = A // 500
A = A % 500

# Calculate number of 200 rupee notes
n200 = A // 200
A = A % 200

# Calculate number of 50 rupee notes
n50 = A // 50
A = A % 50

# Calculate number of 20 rupee notes
n20 = A // 20
A = A % 20

# Calculate number of 5 rupee coins/notes
n5 = A // 5
A = A % 5

# Calculate number of 2 rupee coins
n2 = A // 2
A = A % 2

# The remaining amount is in 1 rupee coins
n1 = A

# Print all values in one line
print("2000 :", n2000, "500 :", n500, "200 :", n200, "50 :", n50, "20 :", n20, "5 :", n5, "2 :", n2, "1 :", n1)
```

---

## 🧪 **Sample Input:**

```
2257
```

## 🧾 **Sample Output:**

```
2000 : 1 500 : 0 200 : 1 50 : 1 20 : 0 5 : 1 2 : 1 1 : 0
```

---
