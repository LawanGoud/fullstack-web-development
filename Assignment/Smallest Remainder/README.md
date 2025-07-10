## 🧩 **Problem Name:**

**Smallest Remainder**

---

## 🎯 **Goal:**

✅ Read two numbers `first_number` and `second_number`
✅ Find:

* `remainder1` = first\_number % second\_number
* `remainder2` = second\_number % first\_number
  ✅ Print the **smallest** among the two remainders

---

## 🧠 **Concepts Used:**

* Remainder operator `%`
* Conditional statements (`if-else`)

---

## ✅ Full Code:

```python
# Read the first number
first_number = int(input())

# Read the second number
second_number = int(input())

# Calculate remainders
remainder1 = first_number % second_number
remainder2 = second_number % first_number

# Compare and print the smallest remainder
if remainder1 < remainder2:
    print(remainder1)
else:
    print(remainder2)
```

---

## 🧪 Sample Input:

```
3  
7
```

### 🧾 Sample Output:

```
1
```

---

