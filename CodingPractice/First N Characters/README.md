## 🧩 **Problem Name**

**First N Characters**

---

## 📌 **Task**

Write a program that:

- Reads a **word**
- Reads an **integer N**
- Prints the **first N characters** of the word

---

## 🧠 **Concept Explanation**

We use **string slicing** in Python:

```python
word[:N]
```

This will return characters **from index 0 up to (but not including) index N** — meaning the first **N characters**.

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

### Step 3: Slice the first N characters

```python
result = word[:N]
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
print(word[:N])
```

---

## 🧪 Sample Input

```
Superman
5
```

## 🎯 Sample Output

```
Super
```
