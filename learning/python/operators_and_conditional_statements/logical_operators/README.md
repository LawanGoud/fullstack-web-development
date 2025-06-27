## 🔍 **Logical Operators in Python**

Logical operators allow you to combine **Boolean expressions**. They always return either `True` or `False`.

### ✅ Available Operators:

| Operator | Meaning                          | Example         | Result  |
| -------- | -------------------------------- | --------------- | ------- |
| `and`    | True **only if both** are True   | `True and True` | `True`  |
| `or`     | True **if at least one** is True | `True or False` | `True`  |
| `not`    | **Negates** the boolean value    | `not True`      | `False` |

---

### 🧠 **Logical AND (`and`)**

Returns `True` **only if both** sides are `True`.

```python
print(True and True)       # True
print(True and False)      # False
print((2 < 3) and (1 < 2))  # True, because both are True
```

**Step-by-step:**

```
(2 < 3) and (1 < 2)
True and True
=> True
```

---

### 🧠 **Logical OR (`or`)**

Returns `True` **if at least one** of the expressions is `True`.

```python
print(False or False)      # False
print(True or False)       # True
print((2 < 3) or (2 < 1))   # True
```

**Step-by-step:**

```
(2 < 3) or (2 < 1)
True or False
=> True
```

---

### 🧠 **Logical NOT (`not`)**

Returns the **opposite** of a Boolean value.

```python
print(not False)        # True
print(not True)         # False
print(not (2 < 3))      # False
```

**Step-by-step:**

```
not (2 < 3)
not True
=> False
```

---

### 🧾 **Summary**

| Expression           | Result |
| -------------------- | ------ |
| `True and False`     | False  |
| `True or False`      | True   |
| `not True`           | False  |
| `not(False or True)` | False  |

---
