## 🧩 **Problem Name:**

**Check One Greater**

---

## 📝 **Task:**

Write a program that:

- Reads two numbers **A** and **B**.
- Checks if **B is greater than A by exactly one**.
- Prints `True` if the condition is satisfied, otherwise `False`.

---

## 💡 **Concepts Used:**

- `input()` to take user input
- `int()` to convert string input to integers
- Relational and arithmetic comparison: `B == A + 1`
- `print()` to display the result

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read two numbers from the user

```python
A = int(input())
B = int(input())
```

This reads two inputs and converts them from strings to integers.

---

### ✅ Step 2: Check if B is exactly one more than A

```python
result = (B == A + 1)
```

This checks if `B` is **equal to A plus 1**, which means **B is one greater than A**.

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read input numbers
A = int(input())
B = int(input())

# Step 2: Check if B is greater than A by 1
result = (B == A + 1)

# Step 3: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
2
3
```

## 🎯 Sample Output:

```
True
```
