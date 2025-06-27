Here’s the solution for the given problem, explained step by step:

---

## 🧩 **Problem Name:**

**Entrance**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer `A` (age)
✅ Reads a string `S` (guardian status: `"yes"` or `"no"`)
✅ Checks if:

- Age is between 12 and 60 (inclusive), **or**
- Guardian status is `"yes"`
  ✅ Prints `True` or `False`

---

## 🧠 **Concepts Used:**

- Comparison operators (`>=`, `<=`)
- Logical operator (`or`)
- `input()` to read input
- Type conversion with `int()`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input values

```python
A = int(input())     # Age
S = input()          # Guardian status
```

---

### ✅ Step 2: Check conditions

```python
result = (12 <= A <= 60) or (S == "yes")
```

---

### ✅ Step 3: Print result

```python
print(result)
```

---

## 🧪 Sample Input:

```
15
no
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
A = int(input())  # Read age
S = input()       # Read guardian status

# Check if age is between 12 and 60 or guardian is 'yes'
result = (12 <= A <= 60) or (S == "yes")

# Print the result
print(result)
```
