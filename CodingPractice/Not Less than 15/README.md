## 🧩 **Problem Name:**

**Not Less than 15**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two integers `A` and `B`
✅ Checks if **any** of the numbers is **not less than 15** (i.e., **greater than or equal to 15**)
✅ Prints `True` if at least one of them is `>= 15`, otherwise `False`

---

## 🧠 **Concepts Used:**

- Comparison operators (`>=`)
- Logical operator (`or`)
- `input()` to read values
- `int()` for type conversion

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input values

```python
A = int(input())
B = int(input())
```

---

### ✅ Step 2: Check the condition

```python
result = A >= 15 or B >= 15
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
921
6
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
A = int(input())
B = int(input())

result = A >= 15 or B >= 15
print(result)
```
