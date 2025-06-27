## 🧩 **Problem Name**

**Area of a Rectangle**

---

## 📌 **Task**

Write a Python program that:

- Takes two inputs: **Length** and **Breadth** of a rectangle,
- Calculates the **Area** using the formula:

  $$
  \text{Area} = \text{Length} \times \text{Breadth}
  $$

- Prints the result.

---

## 🧠 **Step-by-Step Explanation**

---

### ✅ Step 1: Take Input for Length

Use the `input()` function to get the **Length** of the rectangle.
Since `input()` returns a string, convert it to an integer using `int()`.

```python
length = input()       # Example input: "3"
length = int(length)   # Converted to integer: 3
```

---

### ✅ Step 2: Take Input for Breadth

Get the **Breadth** of the rectangle in the same way.

```python
breadth = input()         # Example input: "4"
breadth = int(breadth)    # Converted to integer: 4
```

---

### ✅ Step 3: Calculate the Area

Multiply `length` and `breadth` to get the area.

```python
area = length * breadth   # 3 * 4 = 12
```

---

### ✅ Step 4: Print the Area

Use the `print()` function to display the result.

```python
print(area)    # Output: 12
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
12
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

# Step 3: Calculate Area
area = length * breadth

# Step 4: Print the result
print(area)
```

---
