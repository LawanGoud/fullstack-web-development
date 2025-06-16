Absolutely! Let's walk through the solution **step-by-step**.

---

## 🧩 **Problem Name:**

**Percentage - 2**

---

## 📝 **Task:**

Write a program that:

- Takes a number **N** as input.
- Calculates **X**, which is 30% of **N**.
- Calculates **Y**, the remaining part of **N** (i.e., 70% of **N**).
- Prints **Y**.

---

## 💡 **Concepts Used:**

- ✅ `input()` to read input
- ✅ `float()` for decimal calculation
- ✅ Percentage formula:

  $$
  \text{value} = \left( \frac{\text{percentage}}{100} \right) \times \text{N}
  $$

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read input

```python
N = input()
```

This reads the input as a string.

---

### ✅ Step 2: Convert to float

```python
N = float(N)
```

This converts `N` to a float to support decimal values like 35.0.

---

### ✅ Step 3: Calculate 30% of N

```python
X = (30 / 100) * N
```

---

### ✅ Step 4: Calculate Y (remaining part of N)

```python
Y = N - X
```

You could also directly use 70%:

```python
# Y = (70 / 100) * N  # This also works
```

---

### ✅ Step 5: Print Y

```python
print(Y)
```

---

## ✅ Full Code:

```python
# Step 1: Read the input
N = input()

# Step 2: Convert to float
N = float(N)

# Step 3: Calculate 30% of N
X = (30 / 100) * N

# Step 4: Calculate the remaining (Y)
Y = N - X

# Step 5: Print Y
print(Y)
```

---

## 🧪 Sample Input:

```
50
```

## 🎯 Sample Output:

```
35.0
```
