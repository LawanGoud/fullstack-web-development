
## 🧩 **Problem Name:**

**Vote Eligibility**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads the **age** of a person
✅ Checks if the age is **greater than or equal to 18**
✅ Prints `"Eligible"` if true
✅ Otherwise, prints `"Not Eligible"`

---

## 🧠 **Concepts Used:**

* Conditional statements (`if-else`)
* Integer comparison (`>=`)
* Input/output handling

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input value

```python
age = int(input())
```

---

### ✅ Step 2: Check if age is greater than or equal to 18

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## 🧪 Sample Input:

```
15
```

### 🧾 Sample Output:

```
Not Eligible
```

---

## ✅ Full Code:

```python
# Read the age from user
age = int(input())

# Check if age is greater than or equal to 18
if age >= 18:
    # If true, print "Eligible"
    print("Eligible")
else:
    # If false, print "Not Eligible"
    print("Not Eligible")
```

---

