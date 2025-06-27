
## 🧩 **Problem Name:**

**Zero or Positive**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer number
✅ Checks if the number is:

* Equal to 0 → print `"Zero"`
* Greater than 0 → print `"Positive"`

---

## 🧠 **Concepts Used:**

* Input reading with `input()`
* Type conversion with `int()`
* Comparison operators (`==`, `>`)
* Conditional statements (`if`, `elif`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input

```python
num = int(input())
```

---

### ✅ Step 2: Use conditional statements

```python
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
```

---

## 🧪 Sample Input:

```
56
```

### 🧾 Sample Output:

```
Positive
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
```

---

