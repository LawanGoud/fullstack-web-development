## 🧩 **Problem Name:**

**Compare Digits**

---

## 📝 **Task:**

Write a program that:

- Reads a **two-digit number** `N`.
- Checks:

  1. If `N > 25`
  2. If the **first digit** is greater than the **second digit**

- Print both results, each on a new line.

---

## 💡 **Concepts Used:**

- `input()` to read input
- Type conversion (`int()` and `str()`)
- String indexing to get individual digits
- Comparison using `>` operator

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the number

```python
N = input()
```

We'll read the number as a **string** so we can access digits using indexing.

---

### ✅ Step 2: Check if number > 25

We need to convert the string input to an integer to compare with 25.

```python
is_greater_than_25 = int(N) > 25
```

---

### ✅ Step 3: Compare the first and second digits

Since `N` is a string, we can get individual digits using indexing.

```python
first_digit = int(N[0])
second_digit = int(N[1])
is_first_greater = first_digit > second_digit
```

---

### ✅ Step 4: Print the results

```python
print(is_greater_than_25)
print(is_first_greater)
```

---

## ✅ Full Code:

```python
# Step 1: Read the two-digit number as a string
N = input()

# Step 2: Check if N is greater than 25
is_greater_than_25 = int(N) > 25

# Step 3: Extract digits and compare
first_digit = int(N[0])
second_digit = int(N[1])
is_first_greater = first_digit > second_digit

# Step 4: Print the results
print(is_greater_than_25)
print(is_first_greater)
```

---

## 🧪 Sample Input:

```
28
```

## 🎯 Sample Output:

```
True
False
```

Because:

- 28 > 25 → ✅
- 2 > 8 → ❌

---
