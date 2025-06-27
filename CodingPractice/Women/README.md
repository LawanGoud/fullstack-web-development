## 🧩 **Problem Name:**

**Women**

---

## 🎯 **Goal:**

Write a program that:

✅ Reads **three strings**: `A`, `B`, and `C`
✅ Checks if **any one** of them is equal to `"woman"`
✅ Prints `True` if at least one is `"woman"`, otherwise `False`

---

## 🧠 **Concepts Used:**

- String comparison (`==`)
- Logical operator (`or`)
- `input()` for taking input

---

## 🪜 **Step-by-Step Explanation**

### ✅ Step 1: Read the inputs

```python
A = input()
B = input()
C = input()
```

---

### ✅ Step 2: Check if any of the three is `"woman"`

```python
result = A == "woman" or B == "woman" or C == "woman"
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## 🧪 Sample Input:

```
man
woman
man
```

### 🧾 Sample Output:

```
True
```

---

## ✅ Full Code:

```python
A = input()
B = input()
C = input()

result = A == "woman" or B == "woman" or C == "woman"
print(result)
```

---
