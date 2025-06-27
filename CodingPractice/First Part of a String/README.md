## 🧩 Problem Name

**First Part of a String**

---

## 📌 Task

Write a program that:

- Reads a **string** where:

  - The **first part** contains only **digits**.
  - The **last character** is a **single letter**.

- Prints the **first part** (the number part) of the string.

---

## 🧠 Concept Explanation

We're told that the input string format is:

- Numbers first.
- Then exactly one letter at the end.

For example:

- `"10y"` → first part: `"10"`
- `"1a"` → first part: `"1"`

To extract this:

- We can slice the string from the **start up to the second-last character**.

Use slicing like:

```python
digits = code[:-1]
```

This gives everything except the last character.

---

## ✅ Step-by-Step Code

### Step 1: Read the input string

```python
code = input()
```

### Step 2: Slice all characters except the last one

```python
digits = code[:-1]
```

### Step 3: Print the digit part

```python
print(digits)
```

---

## ✅ Final Code

```python
code = input()
print(code[:-1])
```

---

## 🧪 Sample Input

```
10y
```

## 🎯 Sample Output

```
10
```
