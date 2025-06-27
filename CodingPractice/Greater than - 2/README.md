## 🧩 **Problem Name:**

**Greater than - 2**

---

## 📝 **Task:**

Write a program that:

- Reads two numbers: `A` and `B`
- Checks if `A` is **greater than** `B`
- Prints the result in the format:

  ```
  A > B is True
  ```

  or

  ```
  A > B is False
  ```

---

## 💡 **Concepts Used:**

- `input()` to take user input
- `int()` to convert string input to integers
- `>` relational operator to compare values
- `print()` with formatted output

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read two numbers from the user

```python
A = int(input())
B = int(input())
```

This reads two inputs and converts them into integers.

---

### ✅ Step 2: Compare if A is greater than B

```python
result = A > B
```

---

### ✅ Step 3: Print the result with message

```python
print("A > B is", result)
```

---

## ✅ Full Code:

```python
# Step 1: Read inputs
A = int(input())
B = int(input())

# Step 2: Compare A > B
result = A > B

# Step 3: Print result in required format
print("A > B is", result)
```

---

## 🧪 Sample Input:

```
8
5
```

## 🎯 Sample Output:

```
A > B is True
```
