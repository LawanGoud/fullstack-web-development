## 🧩 **Problem Name:**

**Smallest Among 3 Numbers**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads three numbers `A`, `B`, and `C`
- ✅ Finds the smallest number among them
- ✅ Prints the smallest value

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators (`<`)
- Nested `if` statements
- No built-in `min()` function used (manual comparison for learning)

---

## ✅ **Code with Comments:**

```python
# Read three numbers
num1 = int(input())  # First number
num2 = int(input())  # Second number
num3 = int(input())  # Third number

# Check which number is the smallest using nested conditions
if num1 < num2:
    if num1 < num3:
        print(num1)  # num1 is smaller than both num2 and num3
    else:
        print(num3)  # num3 is smaller than num1 and num2
else:
    if num2 < num3:
        print(num2)  # num2 is smaller than both
    else:
        print(num3)  # num3 is smallest
```

---

## 🧪 **Sample Input:**

```
6
5
4
```

## 🧾 **Sample Output:**

```
4
```

---
