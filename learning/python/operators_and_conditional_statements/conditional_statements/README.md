## 🧩 **Concept: Conditional Statements in Python**

---

### 🧠 **1. Block of Code**

A **block of code** is a group of statements that are intended to run together.
In Python, blocks are defined by **indentation** (spaces at the beginning of lines).

---

### 🎯 **2. Condition**

A **condition** is an expression that evaluates to either `True` or `False`.

✅ **Examples of conditions:**

```python
2 < 3         # True
a == b        # Depends on values of a and b
True          # Always True
```

---

### 🔎 **3. Conditional Statement**

A **conditional statement** uses a condition to decide **whether or not** to run a block of code.

✅ **Example:**

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

> `if x > 5:` is a **conditional statement**

---

### 🧱 **4. Conditional Block**

The code that is **indented** under an `if` is called a **conditional block**.
It only runs if the condition is `True`.

✅ **Example:**

```python
age = 20
if age >= 18:
    print("You can vote")
    print("You're an adult")
```

Both `print()` statements above run **only if** `age >= 18`.

---

### 🧾 **5. Indentation**

Indentation is the **space** at the beginning of a line. Python uses it to define blocks.

🔴 **Wrong (inconsistent indentation):**

```python
if True:
    print("Line 1")
        print("Line 2")   # ❌ This will cause an error
```

✅ **Correct:**

```python
if True:
    print("Line 1")
    print("Line 2")
```

---

### 🔄 **6. If-Else Syntax**

Use `if-else` to run **one block if the condition is True**, and another if it’s False.

✅ **Example:**

```python
a = int(input())
if a > 0:
    print("Positive")
else:
    print("Not Positive")
print("End")
```

---

### ⚠️ **7. Possible Mistakes in If-Else**

🛑 **Mistake 1: `else` without `if`**

```python
else:
    print("This will give an error")  # ❌ No if above
```

**Error:**

```
SyntaxError: invalid syntax
```

🛑 **Mistake 2: Code between `if` block and `else`**

```python
a = 10
if a > 0:
    print("Positive")
print("Some line")   # ❌ Code between if and else
else:
    print("Not Positive")
```

**Error:**

```
SyntaxError: invalid syntax
```

✅ **Correct Way:**

```python
a = 10
if a > 0:
    print("Positive")
else:
    print("Not Positive")
```

🛑 **Mistake 3: Uneven indentation in blocks**

```python
if True:
    print("Yes")
      print("No")  # ❌ Too many spaces
```

**Error:**

```
IndentationError: unexpected indent
```

---
