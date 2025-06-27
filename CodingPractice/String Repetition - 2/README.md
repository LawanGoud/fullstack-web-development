## 🧩 **Problem Name**

**String Repetition - 2**

---

## 📌 **Task**

Write a program that:

- Takes a **word** as input
- Takes an **integer N** as input
- Prints the **word repeated N times** in a single line (without spaces)

---

## 🧠 **Concept Explanation**

In Python:

- Strings can be repeated using the `*` operator
  Example:

  ```python
  print("Hi" * 3)  # Output: HiHiHi
  ```

So, repeating a string `N` times means:

```python
result = word * N
```

---

## ✅ **Step-by-Step Code Explanation**

### ✅ Step 1: Read the inputs

```python
word = input()         # Example: "Maths"
N = int(input())       # Example: 2
```

---

### ✅ Step 2: Repeat the word N times

```python
result = word * N
```

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## ✅ Final Code

```python
word = input()
N = int(input())

print(word * N)
```

---

## 🧪 Sample Input

```
Maths
2
```

## 🎯 Sample Output

```
MathsMaths
```
