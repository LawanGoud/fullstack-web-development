
## 🧩 **Problem Name:**

**Relation b/w Numbers**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two numbers `X` and `Y`
✅ Checks the relation between `X` and `Y`
✅ Prints `"X < Y"` if `X` is less than `Y`
✅ Otherwise, prints `"X >= Y"`

---

## 🧠 **Concepts Used:**

* Conditional statements (`if-else`)
* Comparison operators (`<`, `>=`)
* Input/output handling

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
X = int(input())
Y = int(input())
```

---

### ✅ Step 2: Compare X and Y

```python
if X < Y:
    print("X < Y")
else:
    print("X >= Y")
```

---

## 🧪 Sample Input:

```
2
5
```

### 🧾 Sample Output:

```
X < Y
```

---

## ✅ Full Code:

```python
# Read two numbers from user
X = int(input())
Y = int(input())

# Check if X is less than Y
if X < Y:
    # If X is less, print the relation
    print("X < Y")
else:
    # Otherwise, print X >= Y
    print("X >= Y")
```

---

