## 🧩 **Problem Name:**

**Between 9 and 21**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three numbers: `A`, `B`, and `C`
✅ Checks if **any one** of the numbers is between **9 and 21** (inclusive)
✅ If true, print `"True"`
✅ Otherwise, print `"False"`

---

## 🧠 **Concepts Used:**

* Input and output
* Integer conversion
* Comparison operators (`>=`, `<=`)
* Logical operator (`or`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the numbers

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check if any number is between 9 and 21

```python
if (A >= 9 and A <= 21) or (B >= 9 and B <= 21) or (C >= 9 and C <= 21):
    print("True")
else:
    print("False")
```

---

## 🧪 Sample Input:

```
2  
4  
16
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
# Read first number
A = int(input())

# Read second number
B = int(input())

# Read third number
C = int(input())

# Check if any of the numbers is between 9 and 21
if (A >= 9 and A <= 21) or (B >= 9 and B <= 21) or (C >= 9 and C <= 21):
    # If yes, print True
    print("True")
else:
    # If not, print False
    print("False")
```

---

