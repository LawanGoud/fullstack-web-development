
## 🧩 **Problem Name:**

**Pair of Numbers**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers `A` and `B`
✅ Checks if:

* Both `A` and `B` are less than or equal to `1000`
  **OR**
* `B` is greater than `500`

✅ If the condition is true, print `"Pair"`
✅ Otherwise, print `"Not a pair"`

---

## 🧠 **Concepts Used:**

* Comparison operators (`<=`, `>`)
* Logical operators (`and`, `or`)
* Conditional statements (`if-else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input values

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check the condition

```python
if A <= 1000 and B <= 1000 or B > 500:
    print("Pair")
else:
    print("Not a pair")
```

---

## 🧪 Sample Input:

```
300
200
```

### 🧾 Sample Output:

```
Pair
```

---

## ✅ Full Code:

```python
# Read the first number
A = int(input())

# Read the second number
B = int(input())

# Check if both A and B are less than or equal to 1000, or B is greater than 500
if A <= 1000 and B <= 1000 or B > 500:
    # If the condition is satisfied, print "Pair"
    print("Pair")
else:
    # If the condition is not satisfied, print "Not a pair"
    print("Not a pair")
```

---

