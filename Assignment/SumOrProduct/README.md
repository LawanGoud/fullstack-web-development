## 🧩 **Problem Name:**

**Sum or Product**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if the sum of `A` and `B` is **less than 10**
✅ If so, print the **sum**
✅ Otherwise, print the **product**

---

## 🧠 **Concepts Used:**

* Integer input using `int(input())`
* Arithmetic operations: sum (`+`) and product (`*`)
* Conditional statement (`if-else`)
* Comparison operator (`<`)
* Output using `print()`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read inputs

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check condition and print result

```python
if A + B < 10:
    print(A + B)
else:
    print(A * B)
```

---

## 🧪 Sample Input:

```
1  
2
```

### 🧾 Sample Output:

```
3
```

---

## ✅ Full Code:

```python
# Read the first number
A = int(input())

# Read the second number
B = int(input())

# Check if the sum of A and B is less than 10
if A + B < 10:
    # If the sum is less than 10, print the sum
    print(A + B)
else:
    # Otherwise, print the product of A and B
    print(A * B)
```

---

