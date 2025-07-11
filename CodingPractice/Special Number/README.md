Thanks for letting me know! Since you're still learning the **basics**, I’ll explain this **without advanced methods** like `//` or `%` used in a confusing way.

We’ll solve it **step-by-step** and in your **beginner format**, without using any concepts you haven’t learned yet.

---

## 🧩 **Problem Name:**

**Special Number**

---

## 🎯 **Goal:**

✅ Read a **two-digit number** `N`
✅ Check if **any** of the following is true:

- The **sum of its digits is 7**
- **One of the digits is 7**
- The number is **divisible by 7**

👉 If **any** condition is true → print `"Special Number"`
👉 Otherwise → print `"Normal Number"`

---

## 🧠 **Concepts Used:**

- `input()` and `int()` for reading numbers
- Convert number to string to get digits easily
- Use `int()` to convert each digit back to number
- `or` operator for checking multiple conditions

---

## ✅ Full Code (No advanced math):

```python
# Read the number as input
N = input()

# First digit (tens place)
first = int(N[0])

# Second digit (ones place)
second = int(N[1])

# Convert full number to integer
num = int(N)

# Check all three conditions
if (first + second == 7) or (first == 7 or second == 7) or (num % 7 == 0):
    print("Special Number")
else:
    print("Normal Number")
```

---

## 🧪 Sample Input:

```
67
```

### 🧾 Sample Output:

```
Special Number
```

---
