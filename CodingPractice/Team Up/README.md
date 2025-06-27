
## 🧩 **Problem Name:**

**Team Up**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads the scores `A` and `B` of two players
✅ Checks if:

* **One** of the scores is **greater than 300**, and
* The **sum** of the scores is **less than 500**

✅ If the condition is true, print `"Can team up"`
✅ Otherwise, print `"Cannot team up"`

---

## 🧠 **Concepts Used:**

* Comparison operators (`>`, `<`)
* Logical operators (`and`, `or`)
* Conditional statements (`if-else`)
* Arithmetic addition

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the scores

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check the conditions

```python
if (A > 300 or B > 300) and (A + B < 500):
    print("Can team up")
else:
    print("Cannot team up")
```

---

## 🧪 Sample Input:

```
350
134
```

### 🧾 Sample Output:

```
Can team up
```

---

## ✅ Full Code:

```python
# Read the score of player A
A = int(input())

# Read the score of player B
B = int(input())

# Check if one of the scores is greater than 300 and the total is less than 500
if (A > 300 or B > 300) and (A + B < 500):
    # If condition is true, they can team up
    print("Can team up")
else:
    # If condition is false, they cannot team up
    print("Cannot team up")
```

---

