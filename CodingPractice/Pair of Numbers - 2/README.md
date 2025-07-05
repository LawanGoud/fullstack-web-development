## 🧩 **Problem Name:**

**Pair of Numbers - 2**

---

## 🎯 **Goal:**

✅ Read two numbers `A` and `B`
✅ Check:

* A **and** B are divisible by 3
* A **or** B is divisible by 12
  ✅ If **both** conditions are true → print `"Pair"`
  ✅ Otherwise → print `"Not a Pair"`

---

## 🧠 **Concepts Used:**

* Modulus operator `%`
* Logical operators `and`, `or`
* Input and output

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

# Check A and B divisible by 3
div_by_3 = A % 3 == 0 and B % 3 == 0

# Check A or B divisible by 12
div_by_12 = A % 12 == 0 or B % 12 == 0

# Final check
if div_by_3 and div_by_12:
    print("Pair")
else:
    print("Not a Pair")
```

---

## 🧪 Sample Input:

```
15  
240
```

### 🧾 Sample Output:

```
Pair
```

---
