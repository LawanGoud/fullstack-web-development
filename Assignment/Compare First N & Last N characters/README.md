## 🧩 Problem Name:

**Compare First N & Last N Characters**

---

## 📝 Task:

- Read a string and a number `N`
- Check if the **first N characters** and the **last N characters** of the string are **not the same**
- Print the result: `True` or `False`

---

## 💡 Concepts Used:

- `input()` for reading input
- String slicing (`[:N]`, `[-N:]`)
- `!=` for comparison
- `print()` for displaying output

---

## 🧠 Step-by-Step:

### Step 1: Read the inputs

```python
text = input()       # Read the string
n = int(input())     # Read the integer N
```

### Step 2: Slice first and last N characters

```python
first_part = text[:n]
last_part = text[-n:]
```

### Step 3: Compare them

```python
result = first_part != last_part
```

### Step 4: Print the result

```python
print(result)
```

---

## ✅ Complete Code:

```python
text = input()
n = int(input())

first_part = text[:n]
last_part = text[-n:]

print(first_part != last_part)
```

---

## 🧪 Sample Input:

```
toronto
2
```

## 🎯 Output:

```
False
```

Because:

- First 2 characters: `"to"`
- Last 2 characters: `"to"`
- So they **are** the same → `not the same` is `False`
