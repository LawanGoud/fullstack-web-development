## 🧩 **Problem Name**

**Division of Two Numbers**

---

## 📌 **Task**

Write a Python program that:

- Reads two numbers, A and B (from user input),
- Divides A by B (A ÷ B),
- Prints the result.

---

## 🧠 **Step-by-Step Explanation**

### ✅ Step 1: Read the First Input

Use the `input()` function to get the first number (A) from the user. Since `input()` gives a string, convert it to an integer using `int()`.

```python
A = input()     # Example: "15"
A = int(A)      # Converted to 15
```

---

### ✅ Step 2: Read the Second Input

Similarly, get the second number (B) and convert it to an integer.

```python
B = input()     # Example: "3"
B = int(B)      # Converted to 3
```

---

### ✅ Step 3: Divide A by B

Use the `/` operator for division. This returns a float result in Python.

```python
result = A / B  # 15 / 3 = 5.0
```

---

### ✅ Step 4: Print the Result

Use the `print()` function to display the result.

```python
print(result)   # Output: 5.0
```

---

## 🧪 **Example**

**Input:**

```
15
3
```

**Output:**

```
5.0
```

---

## ✅ **Final Code**

```python
# Step 1: Read and convert first number
A = input()
A = int(A)

# Step 2: Read and convert second number
B = input()
B = int(B)

# Step 3: Perform division
result = A / B

# Step 4: Print the result
print(result)
```

---
