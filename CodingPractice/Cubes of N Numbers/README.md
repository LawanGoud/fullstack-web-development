## 🧩 **Problem Name:**

**Cubes of N Numbers**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Print the **cube** of numbers from 1 to `N`
✅ One cube per line

---

## 🧠 **Concepts Used:**

- Input/output
- While loop
- Arithmetic operations (`*`)

---

## 🧮 **Note:**

Cube of a number `X` is `X * X * X`

---

## ✅ **Code:**

```python
# Read the number N
limit = int(input())

# Initialize the number to 1
number = 1

# Loop to print the cube of numbers from 1 to N
while number <= limit:
    cube = number * number * number  # Calculate cube
    print(cube)                      # Print the cube
    number = number + 1              # Move to next number
```

---

## 🧪 **Sample Input:**

```
4
```

## 🧾 **Sample Output:**

```
1
8
27
64
```

---
