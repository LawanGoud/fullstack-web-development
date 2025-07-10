## 🧩 **Problem Name:**

**Number or Remainder**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Check if one of these conditions is true:

* `N` is divisible by **5** and **7**
* OR `N` is less than **7**

✅ If true, **print `N`**
✅ Otherwise, **print**:

* Remainder when `N` is divided by 5
* Remainder when `N` is divided by 7
  (on separate lines)

---

## 🧠 **Concepts Used:**

* Remainder operator `%`
* Comparison and logical operators (`and`, `or`)
* Conditional statements

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Check the conditions
if (N % 5 == 0 and N % 7 == 0) or N < 7:
    print(N)
else:
    print(N % 5)
    print(N % 7)
```

---

## 🧪 Sample Input:

```
9
```

### 🧾 Sample Output:

```
4
2
```

---

