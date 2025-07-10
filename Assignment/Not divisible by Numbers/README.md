
## 🧩 **Problem Name:**

**Not divisible by Numbers**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Check if `N` is **not divisible** by all of these numbers: **2, 3, 5, 7**
✅ Print `True` if **not divisible** by any of them
✅ Otherwise, print `False`

---

## 🧠 **Concepts Used:**

* Remainder operator `%`
* Logical operator `and`
* Conditional statements (`if-else`)

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Check if N is not divisible by 2, 3, 5, and 7
if N % 2 != 0 and N % 3 != 0 and N % 5 != 0 and N % 7 != 0:
    print(True)
else:
    print(False)
```

---

## 🧪 Sample Input:

```
5633
```

### 🧾 Sample Output:

```
True
```

---

