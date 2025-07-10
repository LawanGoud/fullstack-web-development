## 🧩 **Problem Name:**

**Armstrong Number**

---

## 🎯 **Goal:**

✅ Read a **three-digit number** `N`
✅ Check if `N` is an **Armstrong Number**

An **Armstrong number** is a number where the **sum of the cubes of its digits** equals the number itself.

For example:

* `153 → 1³ + 5³ + 3³ = 153` → Armstrong
* `370 → 3³ + 7³ + 0³ = 370` → Armstrong
* `123 → 1³ + 2³ + 3³ = 36` → Not Armstrong

---

## 🧠 **Concepts Used:**

* String indexing to extract digits
* Type conversion (`str()` and `int()`)
* Exponentiation (`**`)
* Conditional check (`if...else`)

---

## ✅ Full Code:

```python
# Read the number
N = input()

# Convert each digit to integer and find the cube
a = int(N[0]) ** 3
b = int(N[1]) ** 3
c = int(N[2]) ** 3

# Find the sum of the cubes
armstrong_sum = a + b + c

# Convert N to integer for comparison
number = int(N)

# Check and print result
if armstrong_sum == number:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
```

---

## 🧪 Sample Input:

```
153
```

### 🧾 Sample Output:

```
Armstrong Number
```

---
