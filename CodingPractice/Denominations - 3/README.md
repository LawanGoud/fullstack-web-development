## 🧩 **Problem Name:**

**Denominations - 3**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads an amount `A`
- ✅ Calculates the **minimum number** of:

  - ₹500 notes
  - ₹50 notes
  - ₹10 notes
  - ₹1 coins

- ✅ Prints the count of each denomination in **one line**

---

## 🧠 **Concepts Used:**

- Input/output
- Integer division (`//`)
- Modulo/remainder (`%`)
- Step-by-step breakdown of amount using denominations

---

## ✅ **Code:**

```python
A = int(input())  # Read the amount

notes_500 = A // 500
remaining = A % 500

notes_50 = remaining // 50
remaining = remaining % 50

notes_10 = remaining // 10
remaining = remaining % 10

notes_1 = remaining

print("500:", notes_500, "50:", notes_50, "10:", notes_10, "1:", notes_1)
```

---

## 🧪 **Sample Input:**

```
1543
```

## 🧾 **Sample Output:**

```
500: 3 50: 0 10: 4 1: 3
```

---
