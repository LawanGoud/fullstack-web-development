
## 🧩 **Problem Name:**

**Increment the number**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer `N`
✅ If `N > 10`, prints `N + 5`
✅ Otherwise, prints `N + 1`

---

## 🧠 **Concepts Used:**

* Input reading using `input()`
* Type conversion using `int()`
* Conditional statements (`if`, `else`)
* Basic arithmetic operations (`+`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input number

```python
N = int(input())
```

---

### ✅ Step 2: Use `if` to check `N > 10`, otherwise use `else`

```python
if N > 10:
    print(N + 5)
else:
    print(N + 1)
```

---

## 🧪 Sample Input:

```
3
```

### 🧾 Sample Output:

```
4
```

---

## ✅ Full Code:

```python
# Read an integer input from the user
N = int(input())

# Check if N is greater than 10
if N > 10:
    # If N > 10, add 5 and print the result
    print(N + 5)
else:
    # Otherwise, add 1 and print the result
    print(N + 1)
```

---

