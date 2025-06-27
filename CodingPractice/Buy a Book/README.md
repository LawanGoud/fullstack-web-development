## 🧩 **Problem Name:**

**Buy a Book**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads the **size `S`** (string) and **page count `C`** (integer) of a book
✅ Checks if:

* `S` is equal to `"large"`
* OR `C` is greater than or equal to `300`

✅ If either condition is true, print `"Buy a Book"`
✅ Otherwise, print `"Do Not Buy a Book"`

---

## 🧠 **Concepts Used:**

* String comparison (`==`)
* Numeric comparison (`>=`)
* Logical operator (`or`)
* Conditional statements (`if-else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the inputs

```python
S = input()
C = int(input())
```

---

### ✅ Step 2: Check the conditions

```python
if S == "large" or C >= 300:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")
```

---

## 🧪 Sample Input:

```
large
80
```

### 🧾 Sample Output:

```
Buy a Book
```

---

## ✅ Full Code:

```python
# Read the size of the book as a string
S = input()

# Read the page count of the book as an integer
C = int(input())

# Check if the size is "large" or page count is 300 or more
if S == "large" or C >= 300:
    # If condition is true, print this message
    print("Buy a Book")
else:
    # If neither condition is met, print this message
    print("Do Not Buy a Book")
```

---

