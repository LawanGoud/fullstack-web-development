## 🧩 **Problem Name:**

**Even or Odd**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a number `N`
✅ Checks if `N` is divisible by `2`
✅ If divisible, print `"Even"`
✅ Otherwise, print `"Odd"`

---

## 🧠 **Concepts Used:**

* Modulus operator (`%`)
* Conditional statements (`if`, `else`)
* Input and output

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number

```python
N = int(input())
```

---

### ✅ Step 2: Check if divisible by 2

```python
if N % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 🧪 Sample Input:

```
4
```

### 🧾 Sample Output:

```
Even
```

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Check if the number is divisible by 2
if N % 2 == 0:
    # If divisible, print Even
    print("Even")
else:
    # If not divisible, print Odd
    print("Odd")
```

