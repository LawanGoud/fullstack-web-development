## 🧩 **Problem Name:**

**Triangles - Type Based on Sides**

---

## 🎯 **Goal:**

✅ Read three side lengths: `a`, `b`, `c`
✅ Print:

- `"Equilateral"` → if all three sides are equal
- `"Isosceles"` → if any two sides are equal
- `"Scalene"` → if all sides are different

---

## 🧠 **Concepts Used:**

- Input/output
- Conditional statements
- Equality and comparison operators

---

## ✅ **Code (With Comments):**

```python
# Read the three side lengths of the triangle
side_a = int(input())
side_b = int(input())
side_c = int(input())

# Check and print the type of triangle
if side_a == side_b and side_b == side_c:
    # All three sides are equal
    print("Equilateral")
elif side_a == side_b or side_b == side_c or side_a == side_c:
    # Any two sides are equal
    print("Isosceles")
else:
    # All three sides are different
    print("Scalene")
```

---

## 🧪 **Sample Input 1:**

```
4
4
4
```

## 🧾 **Sample Output 1:**

```
Equilateral
```

---

## 🧪 **Sample Input 2:**

```
5
5
3
```

## 🧾 **Sample Output 2:**

```
Isosceles
```

---

## 🧪 **Sample Input 3:**

```
6
5
4
```

## 🧾 **Sample Output 3:**

```
Scalene
```

---
