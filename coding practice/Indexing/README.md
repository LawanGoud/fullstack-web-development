## 🧩 **Problem Name**

**Indexing**

---

## 📌 **Task**

Write a program that:

- Takes a **word** `W` as input
- Takes an **integer** `N` as input
- Prints the **character at index N** in the word

---

## 🧠 **Concept Explanation**

In Python:

- Strings are indexed starting from `0`
- So for the word `"Chocolate"`, the characters are indexed like this:

```
Index:   0 1 2 3 4 5 6 7 8
Word :   C h o c o l a t e
```

If `N = 2`, the character at index 2 is `'o'`.

---

## ✅ **Step-by-Step Code Explanation**

### ✅ Step 1: Read the word and the index

```python
word = input()    # Example: "Chocolate"
index = int(input())  # Example: 2
```

---

### ✅ Step 2: Print the character at the given index

```python
print(word[index])
```

---

## ✅ Final Code

```python
word = input()
index = int(input())

print(word[index])
```

---

## 🧪 Sample Input

```
Chocolate
2
```

## 🎯 Sample Output

```
o
```
