## 🧩 **Problem Name:**

**Area and Perimeter of Square**

---

## 📝 **Task:**

Write a program that:

- Takes the **side** of a square as input.
- Calculates the **area** and **perimeter** of the square.
- Prints the results in the specified format.

---

## 📐 **Formulas Used:**

- **Area of square** = side × side
- **Perimeter of square** = 4 × side

---

## 💡 **Concepts Used:**

- ✅ `input()` to take input
- ✅ `int()` to convert input to an integer
- ✅ Arithmetic operations: `*` and multiplication
- ✅ `print()` to display results

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read input

```python
side = input()
```

This reads the side length of the square as a string.

---

### ✅ Step 2: Convert input to integer

```python
side = int(side)
```

We convert it to `int` to perform math operations.

---

### ✅ Step 3: Calculate area

```python
area = side * side
```

---

### ✅ Step 4: Calculate perimeter

```python
perimeter = 4 * side
```

---

### ✅ Step 5: Print output in the required format

```python
print("Area of the square is:", area)
print("Perimeter of the square is:", perimeter)
```

---

## ✅ Full Code:

```python
# Step 1: Take input
side = input()

# Step 2: Convert to integer
side = int(side)

# Step 3: Calculate area
area = side * side

# Step 4: Calculate perimeter
perimeter = 4 * side

# Step 5: Print results
print("Area of the square is:", area)
print("Perimeter of the square is:", perimeter)
```

---

## 🧪 Sample Input:

```
3
```

## 🎯 Sample Output:

```
Area of the square is: 9
Perimeter of the square is: 12
```
