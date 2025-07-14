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

---

## 🧠 **What’s the problem?**

You have `N` students in a class.
Each student has to **shake hands with every other student exactly once**.

---

## 🤝 **What’s happening during handshakes?**

Let’s take an example:

### 👉 If there are 3 students:

- Student 1 shakes hands with Student 2 and Student 3 → **2 handshakes**
- Student 2 has already shaken with 1, now shakes with 3 → **1 handshake**
- Student 3 already shook hands with both → **0 new handshakes**

**Total = 2 + 1 = 3 handshakes**

---

## 🔢 **So what's the pattern?**

We’re actually doing a combination:
For **N** students, we want to choose any **2 students** to do a handshake.

### ✨ Formula:

```
Total Handshakes = N × (N - 1) ÷ 2
```

Why?

- `N` students
- Each student shakes hands with `(N - 1)` others
- But this counts each handshake **twice** (A with B and B with A), so we divide by `2`

---

## ✅ Example for N = 5:

```
Total handshakes = 5 × (5 - 1) ÷ 2
                 = 5 × 4 ÷ 2
                 = 20 ÷ 2
                 = 10
```

So there are **10 handshakes**.

---

## 🧾 Final Code (with comments):

```python
# Read number of students
students = int(input())

# Use formula: N * (N - 1) // 2
handshakes = (students * (students - 1)) // 2  # Integer division to avoid decimal

# Print total handshakes
print(handshakes)
```

---
