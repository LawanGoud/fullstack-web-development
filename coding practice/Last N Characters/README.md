## 🧩 **Problem Name**

**Last N Characters**

---

## 📌 **Task**

Write a program that:

- Reads a **word**
- Reads an **integer N**
- Prints the **last N characters** of the word

---

## 🧠 **Concept Explanation**

To get the **last N characters** of a string in Python, we can use **negative indexing with slicing**:

```python
word[-N:]
```

This means:
Start from the **N-th character from the end**, and go till the **end** of the string.

---

## ✅ Step-by-Step Code

### Step 1: Read the word

```python
word = input()
```

### Step 2: Read the number N

```python
N = int(input())
```

### Step 3: Slice the last N characters

```python
result = word[-N:]
```

### Step 4: Print the result

```python
print(result)
```

---

## ✅ Final Code

```python
word = input()
N = int(input())
print(word[-N:])
```

---

## 🧪 Sample Input

```
Forgive
4
```

## 🎯 Sample Output

```
give
```
