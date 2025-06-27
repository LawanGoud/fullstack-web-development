## 🧩 **Problem Name:**

**Valid Number**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **three-digit number** `N`
✅ Checks if:

* At least **one digit is not equal to 5**
* The number is **between 300 and 700** (inclusive)
  ✅ If both conditions are true, print `"Valid Number"`
  ✅ Otherwise, print `"Not a Valid Number"`

---

## 🧠 **Concepts Used:**

* Input and output
* Type conversion
* String indexing
* Logical operators (`or`, `and`)
* Comparison operators

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number as a string and convert it to integer

```python
n = input()
number = int(n)
```

---

### ✅ Step 2: Check the two conditions:

1. Any digit is not equal to 5
2. The number is between 300 and 700

```python
if (n[0] != '5' or n[1] != '5' or n[2] != '5') and number >= 300 and number <= 700:
    print("Valid Number")
else:
    print("Not a Valid Number")
```

---

## 🧪 Sample Input:

```
653
```

### 🧾 Sample Output:

```
Valid Number
```

---

## ✅ Full Code:

```python
# Read the number as a string
n = input()

# Convert the number to integer for range check
number = int(n)

# Check if any digit is not '5' and number is between 300 and 700
if (n[0] != '5' or n[1] != '5' or n[2] != '5') and number >= 300 and number <= 700:
    # If both conditions are true, it's a valid number
    print("Valid Number")
else:
    # Otherwise, it's not a valid number
    print("Not a Valid Number")
```

---
