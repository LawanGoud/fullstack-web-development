## 🧩 **Problem Name:**

**Polygon Name by Number of Sides**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `N` (number of sides)
- ✅ Prints the name of the polygon:

| Sides (`N`) | Polygon Name  |
| ----------- | ------------- |
| `< 3`       | Not Polygon   |
| `3`         | Triangle      |
| `4`         | Quadrilateral |
| `5`         | Pentagon      |
| `> 5`       | Big Polygon   |

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison and equality operators
- `if`, `elif`, `else` statements

---

## ✅ **Code with Comments and Explanation:**

```python
# Read the number of sides from input
sides = int(input())  # Example: 4

# Check if it's less than 3 → Not a polygon
if sides < 3:
    print("Not Polygon")

# Check if it has exactly 3 sides
elif sides == 3:
    print("Triangle")

# Check if it has exactly 4 sides
elif sides == 4:
    print("Quadrilateral")

# Check if it has exactly 5 sides
elif sides == 5:
    print("Pentagon")

# If more than 5 sides
else:
    print("Big Polygon")
```

---

## 🧪 **Sample Inputs and Outputs:**

**Input:**

```
3
```

**Output:**

```
Triangle
```

**Input:**

```
7
```

**Output:**

```
Big Polygon
```

---
