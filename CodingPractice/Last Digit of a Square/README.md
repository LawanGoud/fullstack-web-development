## 🧩 **Problem Name:**

**Last Digit of a Square**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Get the **last digit** of `N` (without `%`)
✅ Get the **last digit** of `N²` (without `%`)
✅ If both are equal, print `"Equal"`
✅ Otherwise, print `"Not Equal"`

---

## 🧠 **Concepts Used:**

* Type conversion (`str()`)
* Indexing (accessing last character using `[-1]`)
* Conditional statements

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Convert N to string and get last digit
last_digit = str(N)[-1]

# Square the number
square = N ** 2

# Convert square to string and get last digit
square_last_digit = str(square)[-1]

# Compare and print result
if last_digit == square_last_digit:
    print("Equal")
else:
    print("Not Equal")
```

---

## 🧪 Sample Input:

```
15
```

### 🧾 Sample Output:

```
Equal
```

---

