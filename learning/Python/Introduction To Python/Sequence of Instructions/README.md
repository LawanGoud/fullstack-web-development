# 🧾 Sequence of Instructions in Python

## 📌 Program

A **program** is a **sequence of instructions** given to a computer to perform a specific task.

---

## 🔤 Defining a Variable

A variable is **created** when you assign a value to it **for the first time**.

### ✅ Example:

```python
age = 10
```

---

## 🖨️ Printing the Value in a Variable

### ✅ Example 1: Correct Way

```python
age = 10
print(age)
```

**Output:**

```
10
```

### ❌ Example 2: Using Quotes

```python
age = 10
print("age")
```

**Output:**

```
age
```

> 💡 **Note:**
> If the variable name is inside **quotes**, it will be treated as a string — not a variable.
> To print the **value**, do **not use quotes**.

---

## 🔃 Order of Instructions

Python executes code **line-by-line**, from top to bottom.

### ❌ Incorrect Example:

```python
print(age)
age = 10
```

**Output:**

```
NameError: name 'age' is not defined
```

> ⚠️ `age` must be defined **before** it is used.

---

## ⚠️ Spacing in Python

Python does **not allow random spaces** at the beginning of a line (except in blocks like loops or functions).

### ❌ Incorrect:

```python
a = 10 * 5
b = 5 * 0.5
 b = a + b  # ❌ This line has a space at the beginning
```

**Output:**

```
IndentationError: unexpected indent
```

---

## 🔁 Variable Assignment

Variables can be **reassigned** — their values can change.

### ✅ Example:

```python
a = 1
print(a)  # Output: 1

a = 2
print(a)  # Output: 2
```

---

## 🧪 More Examples of Variable Assignment

### Example 1:

```python
a = 2
print(a)      # Output: 2

a = a + 1
print(a)      # Output: 3
```

### Example 2:

```python
a = 1
b = 2
a = b + 1
print(a)      # Output: 3
print(b)      # Output: 2
```

---

## 📘 Expression

An **expression** is a valid combination of:

- **values**
- **variables**
- **operators**

### ✅ Examples:

```python
a * b
a + 2
5 * 2 + 3 * 4
```

---

## 🔢 BODMAS Rule in Python

Python follows **BODMAS** for evaluating expressions:

**B** - Brackets
**O** - Orders (exponents, powers)
**D** - Division
**M** - Multiplication
**A** - Addition
**S** - Subtraction

---

### 🧠 Step-by-Step Example:

```python
(5 * 2) + (3 * 4)
# = 10 + 12
# = 22
```

---

## 🧮 Code Examples Using BODMAS

```python
print(10 / 2 + 3)      # Output: 8.0
print(10 / (2 + 3))    # Output: 2.0
```

---
