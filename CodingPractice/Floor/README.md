## 🧩 **Problem Name:**

**Floor**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **Room Number** in the format `"R<number>"` (e.g., `R1`, `R35`)
✅ Extracts the **numeric part** of the Room Number
✅ Checks if that number is **less than 30**

🔹 If it is less than 30, print:

```
Ground Floor
```

🔹 Otherwise, print:

```
Not Ground Floor
```

---

## 🧠 **Concepts Used:**

* String slicing
* Type conversion from string to integer
* Conditional statement (`if`, `else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the Room Number as input

```python
room = input()
```

---

### ✅ Step 2: Extract the number part using slicing

```python
number = int(room[1:])
```

---

### ✅ Step 3: Check if the number is less than 30

```python
if number < 30:
    print("Ground Floor")
else:
    print("Not Ground Floor")
```

---

## 🧪 Sample Input:

```
R1
```

### 🧾 Sample Output:

```
Ground Floor
```

---

## ✅ Full Code:

```python
# Read the Room Number input (e.g., "R35")
room = input()

# Extract the numeric part from the Room Number using slicing (skip the first character 'R')
number = int(room[1:])

# Check if the number is less than 30
if number < 30:
    # If it is, print Ground Floor
    print("Ground Floor")
else:
    # Otherwise, print Not Ground Floor
    print("Not Ground Floor")
```

---
