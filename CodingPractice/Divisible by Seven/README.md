## 🧩 **Problem Name:**

**Divisible by Seven**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a number `N`
✅ Checks if `N` is divisible by `7`
✅ If yes, print `"Divisible by Seven"`
✅ Otherwise, print `"Not Divisible by Seven"`

---

## 🧠 **Concepts Used:**

* Modulus operator `%`
* Conditional statements `if-else`
* Input and output

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number

```python
N = int(input())
```

---

### ✅ Step 2: Check if divisible by 7

```python
if N % 7 == 0:
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")
```

---

## 🧪 Sample Input:

```
35
```

### 🧾 Sample Output:

```
Divisible by Seven
```

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Check if the number is divisible by 7
if N % 7 == 0:
    # If divisible, print this
    print("Divisible by Seven")
else:
    # If not divisible, print this
    print("Not Divisible by Seven")
```

---

