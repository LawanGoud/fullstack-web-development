## 🧩 **Problem Name**

**Perimeter of Rectangle**

---

## 📌 **Task**

Write a Python program that:

- Takes two inputs: **Length** and **Breadth** of a rectangle
- Calculates the **Perimeter** using the formula:

  $$
  \text{Perimeter} = 2 \times (\text{Length} + \text{Breadth})
  $$

- Prints the result.

---

## 🧠 **Step-by-Step Explanation**

---

### ✅ Step 1: Take Input for Length

Use `input()` to read the Length of the rectangle. Convert the input string to an integer using `int()`.

```python
length = input()        # Example: "3"
length = int(length)    # Converted to integer: 3
```

---

### ✅ Step 2: Take Input for Breadth

Read the Breadth and convert it to an integer.

```python
breadth = input()         # Example: "4"
breadth = int(breadth)    # Converted to integer: 4
```

---

### ✅ Step 3: Calculate the Perimeter

Use the given formula:

$$
\text{Perimeter} = 2 \times (\text{Length} + \text{Breadth})
$$

```python
perimeter = 2 * (length + breadth)    # 2 * (3 + 4) = 14
```

---

### ✅ Step 4: Print the Result

Print the final perimeter.

```python
print(perimeter)     # Output: 14
```

---

## 🧪 **Example**

**Input:**

```
3
4
```

**Output:**

```
14
```

---

## ✅ **Final Code**

```python
# Step 1: Read and convert Length
length = input()
length = int(length)

# Step 2: Read and convert Breadth
breadth = input()
breadth = int(breadth)

# Step 3: Calculate Perimeter
perimeter = 2 * (length + breadth)

# Step 4: Print the result
print(perimeter)
```

---
