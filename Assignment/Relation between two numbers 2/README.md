## 🧩 **Problem Name:**

**Relation Between Two Numbers - 2**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads two numbers `num1` and `num2`
- ✅ Compares the values and prints the appropriate relation:

  - `"A == B"` if they are equal
  - `"A > B"` if the first number is greater
  - `"A < B"` if the second number is greater

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators: `==`, `<`, `>`
- Conditional statements: `if`, `elif`, `else`

---

## ✅ **Code with Comments:**

```python
# Read first number
num1 = int(input())

# Read second number
num2 = int(input())

# Compare and print the relationship
if num1 == num2:
    print("A == B")  # Both numbers are equal
elif num1 > num2:
    print("A > B")   # First number is greater
else:
    print("A < B")   # Second number is greater
```

---

## 🧪 **Sample Input:**

```
3
4
```

## 🧾 **Sample Output:**

```
A < B
```

---
