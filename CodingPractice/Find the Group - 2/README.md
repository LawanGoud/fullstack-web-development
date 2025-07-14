## 🧩 **Problem Name:**

**Find the Group (Alternating Pattern)**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `N` (between 1 and 30)
- ✅ Finds which **group** it belongs to:

  - Group 1 → 1, 7, 13, 19, 25
  - Group 2 → 2, 8, 14, 20, 26
  - Group 3 → 3, 9, 15, 21, 27
  - Group 4 → 4, 10, 16, 22, 28
  - Group 5 → 5, 11, 17, 23, 29
  - Group 6 → 6, 12, 18, 24, 30

---

## 🧠 **Concepts Used:**

- Input/output
- Modulo operator `%`
- Handling zero case with condition

---

## ✅ **Code:**

```python
N = int(input())  # Read the number

# Find the group number using modulo
group = N % 6

# If remainder is 0, it belongs to Group 6
if group == 0:
    group = 6

print("Group", group)
```

---

## 🧪 **Sample Input:**

```
29
```

## 🧾 **Sample Output:**

```
Group 5
```

---
