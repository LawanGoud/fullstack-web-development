## 🧩 **Problem Name:**

**Maximum Number of Handshakes**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads an integer `N` (number of students)
- ✅ Calculates the total number of handshakes if **each student shakes hands with every other student exactly once**
- ✅ Prints the total number of handshakes

---

## 🧠 **Concepts Used:**

- Input/output
- Arithmetic
- Formula for combinations (manually applied):

  - Handshakes = `N * (N - 1) / 2`

---

## ✅ **Code:**

```python
# Read the number of students
students = int(input())

# Calculate number of handshakes using the formula N * (N - 1) / 2
# Since we're doing integer division, we use //
handshakes = (students * (students - 1)) // 2

# Print the result
print(handshakes)
```

---

## 🧪 **Sample Input:**

```
5
```

## 🧾 **Sample Output:**

```
10
```

---
