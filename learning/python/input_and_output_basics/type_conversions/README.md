# 🧵 Python: String Slicing, Data Types & Type Conversion

## 📘 String Slicing

**Slicing** means extracting a specific part of a string using its **index values**.

### 🔹 Syntax

```python
variable[start_index:end_index]
```

- Starts from `start_index`
- Ends just **before** `end_index` (it is **not included** in the result)

---

### ✅ Example

```python
message = "Hi Ravi"
part = message[3:7]
print(part)
```

**Output:**

```
Ravi
```

- Index 3 = R
- Index 4 = a
- Index 5 = v
- Index 6 = i
- Index 7 is not included

---

### 🔚 Slicing to the End

If you leave out `end_index`, it slices till the **end of the string**.

```python
message = "Hi Ravi"
part = message[3:]
print(part)
```

**Output:**

```
Ravi
```

---

### 🔙 Slicing from the Start

If you leave out `start_index`, it starts from the **beginning** (index 0).

```python
message = "Hi Ravi"
part = message[:2]
print(part)
```

**Output:**

```
Hi
```

---

## 🧪 Checking Data Type

In Python, every value has a **data type** such as:

- `int` – integer numbers (e.g., 5, 100)
- `float` – decimal numbers (e.g., 3.14, -2.0)
- `str` – strings (e.g., "Hello", "123")

Use the `type()` function to check a value’s data type.

```python
print(type(10))      # <class 'int'>
print(type(4.2))     # <class 'float'>
print(type("Hi"))    # <class 'str'>
```

---

## 🔁 Type Conversion (Type Casting)

**Type Conversion** is converting one data type into another.

Examples:

- String to Integer
- Integer to String
- Float to Integer, etc.

---

### 🔢 Converting String to Integer

Use `int()` to convert a string that contains a **valid number** into an integer.

```python
a = "5"
a = int(a)
print(type(a))   # <class 'int'>
print(a)         # 5
```

> This works only if the string is a valid whole number (like `"5"`).

---

### ⚠️ Invalid Integer Conversion Examples

```python
a = "Five"
a = int(a)       # ❌ Error! "Five" is not a number

a = "5.0"
a = int(a)       # ❌ Error! This is a float string, not an integer
```

---

## ➕ Adding Two Numbers from User Input

`input()` reads user input as a **string** by default. To perform mathematical operations, convert them to integers using `int()`.

```python
a = input()      # Example input: 10
a = int(a)

b = input()      # Example input: 5
b = int(b)

result = a + b
print(result)
```

**Output:**

```
15
```

---

## 🔡 Converting Integer to String

Use `str()` to convert an integer to a string — useful when combining with other strings (concatenation).

```python
a = input()      # 10
a = int(a)

b = input()      # 5
b = int(b)

result = a + b
print("Sum: " + str(result))
```

**Output:**

```
Sum: 15
```

> If you don’t use `str()`, trying to add a string to a number will cause an error.

---

## ✅ Summary

| Operation    | Example                       | Description                     |
| ------------ | ----------------------------- | ------------------------------- |
| Slicing      | `s[2:5]`                      | Extracts from index 2 to 4      |
| Type Check   | `type(x)`                     | Returns the data type           |
| String → Int | `int("5")`                    | Converts string to integer      |
| Int → String | `str(10)`                     | Converts integer to string      |
| User Input   | `input()`                     | Takes input as a string         |
| Input + Math | `int(input()) + int(input())` | Add two numbers entered by user |

---
