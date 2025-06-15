## 🧩 **Problem Name**

**Part of a String**

---

## 📌 **Task**

Write a program that:

- Reads a **word**
- Reads an **index** (an integer)
- Prints the **part of the word starting from the given index to the end**

---

## 🧠 **Concept Explanation**

We use **string slicing** in Python to extract part of a string.

```python
word[start_index:]
```

- This will return all characters from `start_index` to the **end of the string**.
- Indexing starts at `0`.

For example:

```python
word = "Unhappy"
print(word[2:])  # Outputs: "happy"
```

---

## ✅ **Step-by-Step Code Explanation**

### ✅ Step 1: Read the word

```python
word = input()
```

### ✅ Step 2: Read the index as an integer

```python
index = int(input())
```

### ✅ Step 3: Slice from index to end

```python
part = word[index:]
```

### ✅ Step 4: Print the result

```python
print(part)
```

---

## ✅ Final Code

```python
word = input()
index = int(input())
print(word[index:])
```

---

## 🧪 Sample Input

```
Unhappy
2
```

## 🎯 Sample Output

```
happy
```
