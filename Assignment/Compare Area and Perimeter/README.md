## 🧩 Problem Name

**Compare Area and Perimeter**

---

## 📝 Task

Write a program that:

1. Reads the **length** and **breadth** of a rectangle.
2. Calculates the **area**:

   $$
   \text{Area} = \text{length} \times \text{breadth}
   $$

3. Calculates the **perimeter**:

   $$
   \text{Perimeter} = 2 \times (\text{length} + \text{breadth})
   $$

4. Checks whether the **area is less than or equal to the perimeter**.
5. Prints `True` if it is, else prints `False`.

---

## 💡 Concepts Used

- `input()` to read numbers.
- `int()` (or `float()`) to convert the inputs to numbers.
- Basic arithmetic (`*`, `+`) to compute area and perimeter.
- Comparison operator `<=`.
- `print()` to display the result.

---

## 🧠 Step‑by‑Step Explanation

### 1️⃣ Read the inputs

```python
length = int(input())
breadth = int(input())
```

_(Use `float()` instead of `int()` if you expect decimals.)_

### 2️⃣ Compute the area

```python
area = length * breadth
```

### 3️⃣ Compute the perimeter

```python
perimeter = 2 * (length + breadth)
```

### 4️⃣ Compare area and perimeter

```python
result = area <= perimeter
```

### 5️⃣ Print the comparison result

```python
print(result)
```

---

## ✅ Complete Code

```python
# Read length and breadth
length = int(input())
breadth = int(input())

# Calculate area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Check if area is less than or equal to perimeter
result = area <= perimeter

# Print the result
print(result)
```

---

### 🧪 Example

**Input**

```
4
3
```

**Calculations**

- Area = 4 × 3 = 12
- Perimeter = 2 × (4 + 3) = 14
- 12 ≤ 14 → `True`

**Output**

```
True
```
