## 🧩 **Topic:** Relational Operators

---

## 📝 **What Are Relational Operators?**

Relational operators **compare values** and return a result in the form of **`True` or `False`**.

These operators are commonly used in **conditions, comparisons, and decision-making** in Python.

---

## 🔗 **List of Relational Operators**

| Operator | Description              | Example    | Result  |
| -------- | ------------------------ | ---------- | ------- |
| `>`      | Greater than             | `5 > 3`    | `True`  |
| `<`      | Less than                | `2 < 1`    | `False` |
| `==`     | Equal to                 | `4 == 4`   | `True`  |
| `!=`     | Not equal to             | `6 != 5`   | `True`  |
| `>=`     | Greater than or equal to | `10 >= 10` | `True`  |
| `<=`     | Less than or equal to    | `3 <= 4`   | `True`  |

---

## 💡 **Examples**

### 🔹 Comparing Numbers

```python
print(2 <= 3)      # True
print(2.53 >= 2.55)  # False
```

### 🔹 Comparing Integer and Float

```python
print(12 == 12.0)    # True (same value)
print(12 == 12.1)    # False
```

### 🔹 Comparing Strings

```python
print("ABC" == "ABC")     # True
print("CBA" != "ABC")     # True
print("ABC" == "abc")     # False (case-sensitive)
```

> **Note:** Python is case-sensitive: `"Hello"` ≠ `"hello"`

---

## ⚠️ **Common Mistakes**

### ❌ Mistake 1: Using `=` instead of `==`

```python
print(3 = 3)  # ❌ Invalid
```

🔸 Error: `SyntaxError: expression cannot contain assignment, perhaps you meant "=="?`

✔️ Correct:

```python
print(3 == 3)
```

---

### ❌ Mistake 2: Adding space between operators like `< =`

```python
print(2 < = 3)  # ❌ Invalid
```

🔸 Error: `SyntaxError`

✔️ Correct:

```python
print(2 <= 3)
```

---

## 🔍 **Comparing Different Types**

### Strings and Booleans

```python
print(True == "True")   # False
print(123 == "123")     # False
print(1.1 == "1.1")     # False
```

In these cases, Python **does not automatically convert** between types for comparisons.

---

## ✅ Summary

- Relational operators return **boolean values** (`True` or `False`)
- Always use `==` for **comparison**, not `=`
- No space is allowed between symbols like `<=`, `>=`
- Be aware of **data types** and **case sensitivity** when comparing values

---
