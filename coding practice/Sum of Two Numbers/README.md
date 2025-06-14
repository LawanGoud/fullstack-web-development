## 🧩 **Problem Name**

**Sum of Two Numbers**

---

## 📌 **Task**

Write a Python program that reads two integer inputs (A and B), adds them, and prints the result.

---

## 🧠 **Step-by-Step Explanation**

### ✅ Step 1: Read the First Input

We use the `input()` function to take input from the user.
Since `input()` gives a **string**, we must convert it to an integer using `int()`.

```python
A = input()       # Read first number as string
A = int(A)        # Convert string to integer
```

---

### ✅ Step 2: Read the Second Input

Similarly, we read the second number and convert it to an integer.

```python
B = input()       # Read second number as string
B = int(B)        # Convert string to integer
```

---

### ✅ Step 3: Add the Numbers

Now, we add both numbers and store the result in a variable.

```python
result = A + B
```

---

### ✅ Step 4: Print the Result

We display the final result using the `print()` function.

```python
print(result)
```

---

## 🧪 **Example**

**Input:**

```
2
3
```

**Output:**

```
5
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

# Step 3: Add the numbers
result = A + B

# Step 4: Print the result
print(result)
```

---
