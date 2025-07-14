## 🧩 **Problem Name:**

**Denominations**

---

## 🎯 **Goal:**

✅ Read the total amount
✅ Find and print the **minimum number of currency notes** required using:

```
1000, 500, 100, 50, 20, 5, 1
```

---

## 🧠 **Concepts Used:**

- Input/output
- Integer division `//`
- Modulus operator `%`
- Step-by-step calculation

---

## ✅ **Code (With Comments):**

```python
# Read the amount
amount = int(input())

# Calculate number of 1000 notes
note_1000 = amount // 1000
amount = amount % 1000  # Remaining amount

# Calculate number of 500 notes
note_500 = amount // 500
amount = amount % 500

# Calculate number of 100 notes
note_100 = amount // 100
amount = amount % 100

# Calculate number of 50 notes
note_50 = amount // 50
amount = amount % 50

# Calculate number of 20 notes
note_20 = amount // 20
amount = amount % 20

# Calculate number of 5 notes
note_5 = amount // 5
amount = amount % 5

# Remaining is the number of 1 rupee notes
note_1 = amount

# Print the result
print("1000:", note_1000)
print("500:", note_500)
print("100 :", note_100)
print("50 :", note_50)
print("20 :", note_20)
print("5 :", note_5)
print("1 :", note_1)
```

---

## 🧪 **Sample Input:**

```
8593
```

## 🧾 **Sample Output:**

```
1000: 8
500: 1
100 : 0
50 : 1
20 : 2
5 : 0
1 : 3
```

---
