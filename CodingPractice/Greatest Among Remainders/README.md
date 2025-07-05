## 🧩 **Problem Name:**

**Greatest Remainder (Divide by 4 and 5)**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a number `N`
✅ Finds:

* Remainder when `N` is divided by `4`
* Remainder when `N` is divided by `5`
  ✅ Prints the **greater** of the two remainders

---

## 🧠 **Concepts Used:**

* Modulus operator (`%`)
* Comparison using `if-else`
* Input and output

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number

```python
N = int(input())
```

---

### ✅ Step 2: Find remainders

```python
r1 = N % 4  
r2 = N % 5
```

---

### ✅ Step 3: Compare remainders and print the greater

```python
if r1 > r2:
    print(r1)
else:
    print(r2)
```

---

## 🧪 Sample Input:

```
12
```

### 🧾 Sample Output:

```
2
```

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Find remainder when N is divided by 4
r1 = N % 4

# Find remainder when N is divided by 5
r2 = N % 5

# Compare and print the greater remainder
if r1 > r2:
    print(r1)
else:
    print(r2)
```

---
