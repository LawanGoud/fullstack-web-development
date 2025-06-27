## 🧩 Problem Name

**Half String**

---

## 📌 Task

Write a program that:

- Reads a word as input.
- Prints the **first half** of the word.

---

## 🧠 Concept Explanation

To extract the **first half** of a string:

- We need the **length** of the string.
- Use integer division (`//`) to find half the length.
- Use **string slicing** to get the first half.

### For example:

Input: `"Amazon"`
Length = 6
Half = 6 // 2 = 3
Output = `"Amazon"[0:3]` → `'Ama'`

---

## ✅ Step-by-Step Code

### Step 1: Read input string

```python
word = input()
```

### Step 2: Find half length

```python
half_length = len(word) // 2
```

### Step 3: Slice and print the first half

```python
print(word[:half_length])
```

---

## ✅ Final Code

```python
word = input()
half_length = len(word) // 2
print(word[:half_length])
```

---

## 🧪 Sample Input

```
Amazon
```

## 🎯 Sample Output

```
Ama
```
