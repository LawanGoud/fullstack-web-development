## 🧩 **Problem Name:**

**Validate Password**

---

## 📝 **Task:**

Write a program that:

- Takes a string input representing a **password**.
- Checks if the **length of the password** is **greater than 7**.
- Prints `True` if the condition is met, otherwise prints `False`.

---

## 💡 **Concepts Used:**

- `input()` to read user input.
- `len()` to get the number of characters in the string.
- Relational operator `>` to check if length > 7.
- `print()` to display the result.

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the password from input

```python
password = input()
```

### ✅ Step 2: Check the length of the password

```python
is_valid = len(password) > 7
```

### ✅ Step 3: Print the result

```python
print(is_valid)
```

---

## ✅ Full Code:

```python
# Step 1: Read the password
password = input()

# Step 2: Check if the password length is greater than 7
is_valid = len(password) > 7

# Step 3: Print the result
print(is_valid)
```

---

## 🧪 Sample Input:

```
passwd
```

## 🎯 Sample Output:

```
False
```

### Why?

Because `"passwd"` has **6 characters**, which is **not greater than 7**.

---
