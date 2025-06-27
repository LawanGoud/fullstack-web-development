## 🧩 **Problem Name**

**Subtraction of Two Numbers**

---

## 📌 **Task**

Write a Python program that:

- Reads two **decimal numbers** (float values) `A` and `B`
- Subtracts `B` from `A` (i.e., performs `A - B`)
- Prints the result

---

## 🧠 **Step-by-Step Explanation**

---

### ✅ Step 1: Read Input `A`

Use the `input()` function and convert the input to a `float`, because the input is a decimal number.

```python
A = input()
A = float(A)     # Example: A = 15.55
```

---

### ✅ Step 2: Read Input `B`

```python
B = input()
B = float(B)     # Example: B = 6.23
```

---

### ✅ Step 3: Perform Subtraction

```python
result = A - B   # result = 15.55 - 6.23 = 9.32
```

---

### ✅ Step 4: Print the Result

```python
print(result)    # Output: 9.32
```

---

## 🧪 **Example**

**Input:**

```
15.55
6.23
```

**Output:**

```
9.32
```

---

## ✅ **Final Code**

```python
# Step 1: Read and convert A
A = input()
A = float(A)

# Step 2: Read and convert B
B = input()
B = float(B)

# Step 3: Subtract B from A
result = A - B

# Step 4: Print the result
print(result)
```

---
