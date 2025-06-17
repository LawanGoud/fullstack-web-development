## 🧩 **Problem Name:**

**Negative Number**

---

## 📝 **Task:**

Write a program that:

- Reads a number from the user
- Checks whether the number is **negative** (i.e., less than zero)
- Prints `True` if it is negative, else `False`

---

## 💡 **Concepts Used:**

- `input()` to take input
- `int()` to convert string input to integer
- Relational operator `<`
- `print()` to display result

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read input from the user

```python
number = input()
```

- This takes input as a string.

---

### ✅ Step 2: Convert it to integer

```python
number = int(number)
```

- Now we can compare it numerically.

---

### ✅ Step 3: Check if the number is less than 0

```python
result = number < 0
```

- If it's less than 0, the result will be `True`, otherwise `False`.

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read the input
number = input()

# Step 2: Convert the input to integer
number = int(number)

# Step 3: Check if number is negative
result = number < 0

# Step 4: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
-25
```

## 🎯 Sample Output:

```
True
```
