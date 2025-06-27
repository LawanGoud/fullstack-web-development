## 🧩 **Problem Name:**

**Basic Arithmetic**

---

## 📝 **Task:**

Write a program that:

- Takes **two integer inputs**, `A` and `B`.
- Prints the result of the following operations **in order**:

  1. Addition (`A + B`)
  2. Subtraction (`A - B`)
  3. Multiplication (`A * B`)

---

## 💡 **Concepts Used:**

- ✅ `input()` to read data
- ✅ `int()` for type conversion
- ✅ Basic arithmetic operators (`+`, `-`, `*`)
- ✅ `print()` to display output

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read two inputs from the user

```python
A = input()
B = input()
```

- The `input()` function reads data as strings.

---

### ✅ Step 2: Convert inputs to integers

```python
A = int(A)
B = int(B)
```

- Converts `A` and `B` from string to integer.

---

### ✅ Step 3: Perform the operations

```python
add = A + B          # Addition
sub = A - B          # Subtraction
mul = A * B          # Multiplication
```

---

### ✅ Step 4: Print each result on a new line

```python
print(add)
print(sub)
print(mul)
```

---

## ✅ Full Code:

```python
# Step 1: Read inputs
A = input()
B = input()

# Step 2: Convert to integers
A = int(A)
B = int(B)

# Step 3: Perform operations
add = A + B
sub = A - B
mul = A * B

# Step 4: Print the results
print(add)
print(sub)
print(mul)
```

---

## 🧪 Sample Input:

```
4
3
```

## 🎯 Sample Output:

```
7
1
12
```
