## 🧩 **Problem Name:**

**Between 25 and 75**

---

## 🎯 **Goal:**

Write a program that:

✅ Reads a number
✅ Checks if the number is **greater than 25** **and** **less than 75**
✅ Prints `True` if it is in that range, otherwise `False`

---

## 🧠 **Concepts Used:**

- Comparison operators: `>`, `<`
- Logical AND: `and`
- Integer input

---

## 🪜 **Step-by-Step Explanation**

### ✅ Step 1: Read the number

```python
number = int(input())
```

---

### ✅ Step 2: Check the range condition

```python
result = number > 25 and number < 75
```

This checks whether the number is **strictly between** 25 and 75.

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
35
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
number = int(input())
result = number > 25 and number < 75
print(result)
```

---
