# 🌀 Python Loops - `while` Loop

---

## 🧠 What is a Loop?

In Python, loops allow us to **execute a block of code multiple times**.

---

## 🔁 `while` Loop

The `while` loop runs **as long as a given condition is `True`**.

### 📌 Syntax:

```python
# Initialization
while condition:
    # Block of Code
    # Updation
```

---

## 📊 Flow of `while` Loop:

```text
Initialization
      ↓
while termination_condition:
      ↓
   Block of Code
      ↓
   Updation
      ↺ (Back to condition check)
```

---

## 🧪 Example:

```python
a = int(input())       # Initialization
counter = 0            # Counter initialized

while counter < 3:     # Termination condition
    a = a + 1          # Update value of 'a'
    print(a)           # Output
    counter = counter + 1  # Update counter
```

### ✅ Sample Input:

```
4
```

### ✅ Sample Output:

```
5
6
7
```

---

## ⚠️ Possible Mistakes:

### ❌ 1. Missing Initialization

```python
a = int(input())
while counter < 3:
    a = a + 1
    print(a)
    counter = counter + 1
```

🧯 **Error**: `NameError: name 'counter' is not defined`
📌 **Fix**: Initialize `counter = 0` before the loop.

---

### ❌ 2. Incorrect Termination Condition

```python
a = int(input())
counter = 0
condition = (counter < 3)

while condition:
    a = a + 1
    print(a)
    counter = counter + 1
```

🧯 **Issue**: Infinite loop
📌 **Why**: `condition` is set only once and never updated.

---

### ❌ 3. Not Updating the Counter

```python
a = int(input())
counter = 0

while counter < 3:
    a = a + 1
    print(a)
# missing: counter = counter + 1
```

🧯 **Issue**: Infinite loop
📌 **Fix**: Always update the loop variable inside the loop.

---
