## 🧩 **Problem Name:**

**Special Eleven**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a number `N`
✅ Checks if the remainder when `N` is divided by 11 is **0 or 1**
✅ If so, print `"Special Eleven"`
✅ Otherwise, print `"Normal Number"`

---

## 🧠 **Concepts Used:**

* Modulus operator (`%`)
* Comparison operators (`==`)
* Logical operator (`or`)
* Input and output

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the number

```python
N = int(input())
```

---

### ✅ Step 2: Check if N % 11 is 0 or 1

```python
if N % 11 == 0 or N % 11 == 1:
    print("Special Eleven")
else:
    print("Normal Number")
```

---

## 🧪 Sample Input:

```
22
```

### 🧾 Sample Output:

```
Special Eleven
```

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Check if remainder is 0 or 1 when N is divided by 11
if N % 11 == 0 or N % 11 == 1:
    # If condition is true, print Special Eleven
    print("Special Eleven")
else:
    # Otherwise, print Normal Number
    print("Normal Number")
```

---

