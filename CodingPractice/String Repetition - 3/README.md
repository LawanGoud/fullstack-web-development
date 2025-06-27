## 🧩 Problem Name

**String Repetition - 3**

---

## 📌 Task

Write a program that:

- Reads a **word** and a **number (N)**.
- Prints the **last three characters** of the word **N times** in a single line (no spaces).

---

## 🧠 Concept Explanation

To solve the problem:

1. Extract the **last 3 characters** using slicing:

   ```python
   word[-3:]
   ```

2. Repeat the result **N times**:

   ```python
   repeated = last_three * N
   ```

---

## ✅ Step-by-Step Code

### Step 1: Read inputs

```python
word = input()
N = int(input())
```

### Step 2: Slice last 3 characters

```python
last_three = word[-3:]
```

### Step 3: Repeat and print

```python
print(last_three * N)
```

---

## ✅ Final Code

```python
word = input()
N = int(input())
last_three = word[-3:]
print(last_three * N)
```

---

## 🧪 Sample Input

```
Transport
2
```

## 🎯 Sample Output

```
ortort
```
