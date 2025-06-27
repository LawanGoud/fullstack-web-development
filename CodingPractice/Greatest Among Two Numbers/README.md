## 🧩 **Problem Name:**

**Greatest among two numbers**

---

## 📝 **Task:**

Write a program that:

- Takes **two numbers** as input
- Checks if the **first number is greater** than the second
- Prints the result: `True` or `False`

---

## 💡 **Concepts Used:**

- `input()` to take user input
- `int()` to convert input to integer
- Relational operator `>` for comparison
- `print()` to show the result

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the first number

```python
a = input()
```

### ✅ Step 2: Read the second number

```python
b = input()
```

### ✅ Step 3: Convert both inputs to integers

```python
a = int(a)
b = int(b)
```

### ✅ Step 4: Compare if first number is greater than second

```python
result = a > b
```

### ✅ Step 5: Print the result (`True` or `False`)

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read the first number
a = input()

# Step 2: Read the second number
b = input()

# Step 3: Convert inputs to integers
a = int(a)
b = int(b)

# Step 4: Check if first number is greater than second
result = a > b

# Step 5: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
6
4
```

## 🎯 Sample Output:

```
True
```
