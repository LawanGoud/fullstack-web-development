
## 🧩 **Problem Name:**

**Print the Score**

---

## 🎯 **Goal:**

✅ Read a number `D` (distance in km)
✅ Calculate the **score** based on these rules:

* If `D <= 10`, score = `D`
* If `D > 10`, score = `10 + (D - 10) * 3`

🖨️ Print the **score**

---

## 🧠 **Concepts Used:**

* `input()` and `int()` to read numbers
* `if`, `else` statements
* Basic arithmetic operators (`+`, `-`, `*`)

---

## ✅ Full Code:

```python
# Read the distance
D = int(input())

# Check the condition and calculate the score
if D <= 10:
    print(D)
else:
    print(10 + (D - 10) * 3)
```

---

## 🧪 Sample Input:

```
3
```

### 🧾 Sample Output:

```
3
```

---

Let me know if you’d like me to explain the logic in even more steps!
