## 🧩 **Problem Name:**

**Compare First Digit & Last Digit**

---

## 📝 **Task:**

Write a program that:

- Reads two **three-digit numbers**, `A` and `B`
- Checks whether the **first digit of A** is **less than** the **last digit of B**
- Prints the result as `True` or `False`

---

## 💡 **Concepts Used:**

- `input()` to read input
- Type conversion between `int` and `str`
- String indexing to access specific digits
- `print()` for output
- `>` and `<` relational operators

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read input values

We read both numbers as **strings** to easily access their digits by index:

```python
A = input()
B = input()
```

---

### ✅ Step 2: Extract the required digits

- First digit of A is at index `0`
- Last digit of B is at index `2` (since it's a 3-digit number)

```python
first_digit_A = int(A[0])
last_digit_B = int(B[2])
```

We convert the digits to `int` so we can compare them.

---

### ✅ Step 3: Compare the digits

```python
result = first_digit_A < last_digit_B
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read inputs as strings
A = input()
B = input()

# Step 2: Extract digits
first_digit_A = int(A[0])
last_digit_B = int(B[2])

# Step 3: Compare the digits
result = first_digit_A < last_digit_B

# Step 4: Print result
print(result)
```

---

## 🧪 Sample Input:

```
123
378
```

### ➕ Explanation:

- First digit of `123` is `1`
- Last digit of `378` is `8`
- `1 < 8` → ✅

---

## 🎯 Sample Output:

```
True
```
