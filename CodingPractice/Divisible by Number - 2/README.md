## 🧩 **Problem Name:**

**Divisible by Number - 2**

---

## 🎯 **Goal:**

✅ Read a number `number`
✅ Find the **triple** of the number (3 × number)
✅ Check if the triple is **divisible by 6**

➡️ If **divisible by 6**, print the triple
➡️ Otherwise, print the original number

---

## 🧠 **Concepts Used:**

* Multiplication (`*`)
* Division check using remainder (`%`)
* Conditional statements

---

## ✅ Full Code:

```python
# Read the input number
number = int(input())

# Calculate the triple of the number
triple_of_number = 3 * number

# Check if the triple is divisible by 6
if triple_of_number % 6 == 0:
    print(triple_of_number)
else:
    print(number)
```

---

## 🧪 Sample Input:

```
6
```

### 🧾 Sample Output:

```
18
```

---
