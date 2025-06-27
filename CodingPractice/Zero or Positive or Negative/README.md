
## 🧩 **Problem Name:**

**Zero or Positive or Negative**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer number
✅ Checks and prints:

* `"Zero"` if the number is 0
* `"Positive"` if the number is greater than 0
* `"Negative"` if the number is less than 0

---

## 🧠 **Concepts Used:**

* Input reading with `input()`
* Type conversion using `int()`
* Conditional statements (`if`, `elif`, `else`)
* Comparison operators (`==`, `>`, `<`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input number

```python
num = int(input())
```

---

### ✅ Step 2: Use if-elif-else to check and print the result

```python
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")
```

---

## 🧪 Sample Input:

```
-12
```

### 🧾 Sample Output:

```
Negative
```

---

## ✅ Full Code:

```python
# Read the input number
num = int(input())

# Check if the number is zero
if num == 0:
    print("Zero")
# Check if the number is positive
elif num > 0:
    print("Positive")
# Otherwise, it must be negative
else:
    print("Negative")
```

---

