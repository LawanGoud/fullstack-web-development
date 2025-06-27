# 📘 Inputs and Outputs Basics (Strings)

## 🔗 String Concatenation

**Concatenation** means **joining strings together** using the `+` operator.

### ✅ Example:

```python
a = "Hello" + " " + "World"
print(a)
```

**Output:**

```
Hello World
```

---

## ❌ Concatenation Errors

You can **only concatenate strings** — not strings with numbers directly.

### ❌ Incorrect:

```python
a = "*" + 10
print(a)
```

**Output:**

```
TypeError: can only concatenate str (not "int") to str
```

> 💡 To fix this, convert the number to a string: `"*"+str(10)`

---

## 🔁 String Repetition

Use `*` to **repeat a string** multiple times.

### ✅ Example 1:

```python
a = "*" * 10
print(a)
```

**Output:**

```
**********
```

### ✅ Example 2:

```python
s = "Python"
s = ("* " * 3) + s + (" *" * 3)
print(s)
```

**Output:**

```
* * * Python * * *
```

---

## 📏 Length of a String

Use `len()` to find the **number of characters** in a string.

### ✅ Example:

```python
username = input()  # Input: Ravi
length = len(username)
print(length)
```

**Output:**

```
4
```

---

## 📥 Taking Input from the User

The `input()` function is used to **read user input**.
It always returns the input as a **string**.

### ✅ Example 1:

```python
username = input()  # Input: Ajay
print(username)
```

**Output:**

```
Ajay
```

### ✅ Example 2:

```python
username = input()  # Ravi
age = input()       # 10
print(username + " is " + age + " years old")
```

**Output:**

```
Ravi is 10 years old
```

> 💡 **Note:** Even if the user enters a number, `input()` treats it as a **string**.

---

## 🔢 String Indexing

You can **access individual characters** in a string using **indexing** (starting from 0).

### ✅ Example:

```python
username = "Ravi"
first_letter = username[0]
print(first_letter)
```

**Output:**

```
R
```

---

## ⚠️ IndexError

If you try to access a character at an index that doesn't exist, you'll get an error.

### ❌ Example:

```python
username = "Ravi"
print(username[4])
```

**Output:**

```
IndexError: string index out of range
```

> The string `"Ravi"` has indices 0, 1, 2, and 3 — so index 4 is out of range.

---
