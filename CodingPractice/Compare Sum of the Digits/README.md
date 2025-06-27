## 🧩 **Problem Name:**

**Compare Sum of the Digits**

---

## 📝 **Task:**

Write a program that:

- Takes a **two-digit number** `N` as input.
- Finds the **sum of its digits**.
- Checks if the **sum is greater than 7**.
- Prints `True` if it is, otherwise `False`.

---

## 💡 **Concepts Used:**

- `input()` to read user input.
- String indexing to access individual digits.
- `int()` to convert characters to integers.
- Relational operator `>` to compare.
- `print()` to display the result.

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the number as a string

```python
n = input()
```

### ✅ Step 2: Use string indexing to extract the digits

Since it's a **two-digit number**, we can do:

```python
digit1 = int(n[0])  # first digit
digit2 = int(n[1])  # second digit
```

### ✅ Step 3: Add the digits

```python
sum_digits = digit1 + digit2
```

### ✅ Step 4: Compare the sum with 7

```python
result = sum_digits > 7
```

### ✅ Step 5: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read the two-digit number as string
n = input()

# Step 2: Extract digits and convert to integers
digit1 = int(n[0])
digit2 = int(n[1])

# Step 3: Calculate the sum of digits
sum_digits = digit1 + digit2

# Step 4: Check if the sum is greater than 7
result = sum_digits > 7

# Step 5: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
45
```

## 🎯 Sample Output:

```
True
```
