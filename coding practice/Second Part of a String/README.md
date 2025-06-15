## 🧩 Problem Name

**Second Part of a String**

---

## 📌 Task

Write a program that:

- Reads a **string** where:

  - The first **2 characters** are letters.
  - The rest of the string consists of **digits**.

- Prints the **second part** (the digit part) of the string.

---

## 🧠 Concept Explanation

We are told:

- First 2 characters are **letters**.
- The rest of the string contains **only digits**.

We can use **string slicing** to extract the part from **index 2 to the end** of the string:

```python
digits = code[2:]
```

---

## ✅ Step-by-Step Code

### Step 1: Read the input string

```python
code = input()
```

### Step 2: Extract from index 2 to the end

```python
digits = code[2:]
```

### Step 3: Print the digits part

```python
print(digits)
```

---

## ✅ Final Code

```python
code = input()
print(code[2:])
```

---

## 🧪 Sample Input

```
OF63
```

## 🎯 Sample Output

```
63
```

---
