# 📘 More Arithmetic Operators in Python

This document explains how to use **Modulus**, **Exponent**, and how to find the **Square** and **Square Root** using arithmetic operators in Python.

---

## 🔢 Modulus Operator `%`

The **modulus operator** gives the **remainder** of a division.

### 🧮 Syntax:

```python
a % b
````

### ✅ Examples:

```python
print(6 % 3)   # Output: 0
print(7 % 4)   # Output: 3
```

---

## ⚡ Exponent Operator `**`

The **exponent operator** is used to raise a number to the power of another number.

### 🧮 Syntax:

```python
a ** b
```

### ✅ Example:

```python
print(2 ** 4)   # Output: 16
```

---

## 🔲 Square of a Number

To find the **square** of a number, raise it to the power of 2.

### ✅ Example:

```python
print(5 ** 2)   # Output: 25
```

---

## 🧮 Square Root of a Number

To find the **square root**, raise the number to the power of `0.5`.

### ✅ Example:

```python
print(16 ** 0.5)   # Output: 4.0
```

---

### ✅ Summary Table

| Operation   | Operator | Example     | Output |
| ----------- | -------- | ----------- | ------ |
| Modulus     | `%`      | `7 % 4`     | `3`    |
| Exponent    | `**`     | `2 ** 4`    | `16`   |
| Square      | `** 2`   | `5 ** 2`    | `25`   |
| Square Root | `** 0.5` | `16 ** 0.5` | `4.0`  |

---



---


## 📘 **Conditional Statements – Nested, Elif & Else**

---

### ✅ **1. Nested Conditional Statements**

A **conditional block inside another conditional block** is called a **nested conditional**.

#### 🧩 **Syntax:**

```python
if condition1:
    if condition2:
        # Block 2
        # Executed only if both condition1 and condition2 are True
```

#### 🧪 **Example:**

```python
matches_won = int(input())
goals = int(input())

if matches_won > 8:
    if goals > 20:
        print("Hurray")
    print("Winner")
```

📝 If `matches_won > 8` and `goals > 20`, it prints:

```
Hurray  
Winner
```

---

### ✅ **2. Nested Conditions in `else` Block**

You can also write `if` conditions **inside `else` blocks**.

#### 🧩 **Syntax:**

```python
if condition1:
    # Block 1
else:
    if condition2:
        # Block 2
    else:
        # Block 3
```

#### 🧪 **Example:**

```python
a = 2
b = 3
c = 1

if (a > b) and (a > c):
    print(a)
else:
    if (b > c):
        print(b)
    else:
        print(c)
```

✅ Output will be `3`, as `b` is the greatest.

---

### ✅ **3. `elif` Statement**

Use `elif` to check **multiple conditions** after an `if`.

#### 🧩 **Syntax:**

```python
if condition1:
    # Block 1
elif condition2:
    # Block 2
elif condition3:
    # Block 3
else:
    # Final Block (Optional)
```

---

### ✅ **4. Multiple `elif` Blocks**

You can write **many `elif`** blocks between `if` and `else`.

🔍 **Only the first true condition** will be executed, others will be skipped.

#### 🧪 **Example:**

```python
number = 5

if number % 10 == 0:
    print("Divisible by 10")
elif number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
```

✅ Output:

```
Divisible by 5
```

---

### ⚠️ **Mistake to Avoid**

❌ Don't write `elif` **after** `else`.
`else` must always come **last**.

---

