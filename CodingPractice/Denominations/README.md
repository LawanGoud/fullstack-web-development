## 🧩 **Problem Name:**

**Denominations**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads an amount `A`
- ✅ Calculates the **minimum number** of:

  - ₹5 notes
  - ₹1 coins

- ✅ Prints the count of ₹5 and ₹1 notes separately.

---

## 🧠 **Concepts Used:**

- Input/output
- Integer division (`//`)
- Remainder (`%`)
- Arithmetic operations

---

## ✅ **Code:**

```python
A = int(input())  # Read the total amount

notes_5 = A // 5       # Find how many ₹5 notes
remaining = A % 5      # Remaining amount after using ₹5 notes
notes_1 = remaining    # All remaining is covered by ₹1 notes

print("5 :", notes_5)
print("1:", notes_1)
```

---

## 🧪 **Sample Input:**

```
16
```

## 🧾 **Sample Output:**

```
5 : 3
1: 1
```

---
