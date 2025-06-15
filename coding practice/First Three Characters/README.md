## 🧩 **Problem Name**

**First Three Characters**

---

## 📌 **Task**

Write a program that:

- Takes a single line of input (a word)
- Prints the **first three characters** of that input

---

## 🧠 **Concept Explanation**

In Python, you can extract a **portion of a string** using **string slicing**:

```python
word[start_index:end_index]
```

- This includes characters from `start_index` **up to but not including** `end_index`.
- To get the first three characters, you slice from index `0` to `3`:

  ```python
  word[:3]
  ```

---

## ✅ **Step-by-Step Code Explanation**

### ✅ Step 1: Read the input

```python
word = input()   # Example: "Four"
```

---

### ✅ Step 2: Slice the first 3 characters

```python
first_three = word[:3]  # 'Fou'
```

---

### ✅ Step 3: Print the result

```python
print(first_three)
```

---

## ✅ Final Code

```python
word = input()
print(word[:3])
```

---

## 🧪 Sample Input

```
Four
```

## 🎯 Sample Output

```
Fou
```
