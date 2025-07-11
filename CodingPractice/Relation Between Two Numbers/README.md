## 🧩 **Problem Name:**

**Relation Between Two Numbers**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads two numbers: `A` and `B`
- ✅ Compares `A` and `B` using **relational operators**
- ✅ Prints the correct relation:

  - `"A == B"` if both are equal
  - `"A > B"` if A is greater
  - `"A < B"` if A is less

---

## 🧠 **Concepts Used:**

- Input/Output
- Relational operators: `==`, `>`, `<`
- Conditional statements (`if`, `elif`, `else`)

---

## ✅ **Code with Comments:**

```python
# Read first number
num1 = int(input())  # Example: 3

# Read second number
num2 = int(input())  # Example: 4

# Check if num1 is equal to num2
if num1 == num2:
    print("A == B")

# Check if num1 is greater than num2
elif num1 > num2:
    print("A > B")

# If both conditions above are false, num1 is less than num2
else:
    print("A < B")
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
