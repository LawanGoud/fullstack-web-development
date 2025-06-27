## 🧩 **Problem Name:**

**Valid Triangle**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads three angles of a triangle: `A`, `B`, and `C`
✅ Checks if the sum of the three angles is exactly **180**
✅ If so, print `"It's a Triangle"`
✅ Otherwise, print `"It's not a Triangle"`

---

## 🧠 **Concepts Used:**

* Input and integer conversion
* Arithmetic operation (addition)
* Conditional statement (`if`-`else`)
* Comparison operator (`==`)
* Output with `print()`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the angles

```python
A = int(input())
B = int(input())
C = int(input())
```

---

### ✅ Step 2: Check if the sum of angles is 180

```python
if A + B + C == 180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
```

---

## 🧪 Sample Input:

```
80  
90  
100
```

### 🧾 Sample Output:

```
It's not a Triangle
```

---

## ✅ Full Code:

```python
# Read the first angle
A = int(input())

# Read the second angle
B = int(input())

# Read the third angle
C = int(input())

# Check if the sum of the three angles is equal to 180
if A + B + C == 180:
    # If yes, it's a valid triangle
    print("It's a Triangle")
else:
    # If not, it's not a valid triangle
    print("It's not a Triangle")
```

---

