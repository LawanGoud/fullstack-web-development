## 🧩 **Problem Name:**

**Greater than or Equal to**

---

## 📝 **Task:**

Write a program that:

- Reads **two numbers**: A and B
- Checks if **A is greater than or equal to B**
- Prints the result in the format:

  ```
  A >= B is True
  ```

---

## 💡 **Concepts Used:**

- `input()` to read input
- `float()` to handle decimal values
- `>=` relational operator
- `print()` with string formatting

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read input for A

```python
A = float(input())
```

We use `float` because the input can have decimals (e.g., 4.3)

---

### ✅ Step 2: Read input for B

```python
B = float(input())
```

---

### ✅ Step 3: Compare A and B using `>=`

```python
result = A >= B
```

---

### ✅ Step 4: Print the result in the required format

```python
print("A >= B is", result)
```

---

## ✅ Full Code:

```python
# Step 1: Read first number
A = float(input())

# Step 2: Read second number
B = float(input())

# Step 3: Check if A is greater than or equal to B
result = A >= B

# Step 4: Print the result in the specified format
print("A >= B is", result)
```

---

## 🧪 Sample Input:

```
4.3
3.2
```

## 🎯 Sample Output:

```
A >= B is True
```
