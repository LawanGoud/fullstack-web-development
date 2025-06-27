## 🧩 **Problem Name:**

**Top 10 Rankers**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a student’s rank `R`
✅ If `R` is less than 10, print `"HONOR STUDENT"`
✅ Otherwise, print `"NORMAL STUDENT"`

---

## 🧠 **Concepts Used:**

* Integer input using `int(input())`
* Conditional statement (`if-else`)
* Comparison operator (`<`)
* Output using `print()`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input rank

```python
R = int(input())
```

---

### ✅ Step 2: Check if rank is less than 10

```python
if R < 10:
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")
```

---

## 🧪 Sample Input:

```
7
```

### 🧾 Sample Output:

```
HONOR STUDENT
```

---

## ✅ Full Code:

```python
# Read the rank of the student
R = int(input())

# Check if the rank is less than 10
if R < 10:
    # If yes, print HONOR STUDENT
    print("HONOR STUDENT")
else:
    # Otherwise, print NORMAL STUDENT
    print("NORMAL STUDENT")
```

---

