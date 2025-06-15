## 🧩 **Problem Name**

**Sum of Two Numbers - 2**

---

## 📌 **Task**

Write a program that:

- Reads two numbers (can be decimal numbers)
- Adds the two numbers
- Prints the result in the format:
  `Sum: <sum>`

---

## 🧠 **Step-by-Step Explanation**

---

### ✅ Step 1: Read Inputs

Use the `input()` function to read two numbers. Since they are decimal numbers, we convert them to `float`.

```python
a = input()
a = float(a)

b = input()
b = float(b)
```

📌 Example Input:

```
3.0
4.0
```

Now:

- `a = 3.0`
- `b = 4.0`

---

### ✅ Step 2: Add the Numbers

Add the two float values:

```python
result = a + b
```

Now `result = 7.0`

---

### ✅ Step 3: Print the Output in Given Format

Use string concatenation to format the output correctly.

```python
print("Sum: " + str(result))
```

This will print:

```
Sum: 7.0
```

---

## ✅ **Final Code**

```python
a = input()
a = float(a)

b = input()
b = float(b)

result = a + b

print("Sum: " + str(result))
```

---

## 🧪 **Sample Input**

```
3.0
4.0
```

## 🎯 **Sample Output**

```
Sum: 7.0
```
