## 🧩 **Problem Name:**

**Star Repetition - 5**

---

## 📝 **Task:**

Write a program that:

- Reads two words: `W1` and `W2`.
- `W1` starts with `W2` as its prefix.
- Replace the **first part** (equal to length of `W2`) in `W1` with stars (`*`).
- Print the modified version of `W1`.

---

## 💡 **Concepts Used:**

- ✅ `input()` to read input
- ✅ `len()` to find length
- ✅ String slicing and repetition (`*`)
- ✅ String concatenation

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Take two inputs

```python
W1 = input()
W2 = input()
```

---

### ✅ Step 2: Get the length of W2

```python
L = len(W2)
```

---

### ✅ Step 3: Replace the first `L` characters of W1 with `*`

```python
first_part = "*" * L        # Repeat * for each character in W2
second_part = W1[L:]        # Get the remaining part from W1
```

---

### ✅ Step 4: Combine both parts and print

```python
print(first_part + second_part)
```

---

## ✅ Full Code:

```python
# Step 1: Read both inputs
W1 = input()
W2 = input()

# Step 2: Get the length of W2
L = len(W2)

# Step 3: Create new string with stars and the remaining part of W1
first_part = "*" * L
second_part = W1[L:]

# Step 4: Print the result
print(first_part + second_part)
```

---

## 🧪 Sample Input:

```
Subway
Sub
```

## 🎯 Sample Output:

```
***way
```
