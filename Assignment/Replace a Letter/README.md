## 🧩 **Problem Name:**

**Replace a Letter**

---

## 📝 **Task:**

Write a program that:

- Reads a **word `W`**
- Reads an **index `I`**
- Reads a **character `C`**

Replace the character at index `I` of `W` with the new character `C` and print the updated word.

---

## 💡 **Concepts Used:**

- ✅ String indexing
- ✅ String slicing
- ✅ String concatenation
- ⚠️ Strings are **immutable** in Python, so we can't change them directly — we create a new string.

---

## 🧠 **Step-by-Step Explanation:**

### Step 1: Take inputs

```python
W = input()     # The word
I = int(input())  # The index (convert to int)
C = input()     # The new character
```

---

### Step 2: Replace character at index `I`

To do this, we:

- Take the **part before** index `I`: `W[:I]`
- Add the **new character**: `C`
- Add the **part after** index `I`: `W[I+1:]`

```python
new_word = W[:I] + C + W[I+1:]
```

---

### Step 3: Print the updated word

```python
print(new_word)
```

---

## ✅ Full Code:

```python
# Step 1: Read inputs
W = input()
I = int(input())
C = input()

# Step 2: Replace the character at index I
new_word = W[:I] + C + W[I+1:]

# Step 3: Print the result
print(new_word)
```

---

## 🧪 Sample Input:

```
Prime
3
z
```

## 🎯 Sample Output:

```
Prize
```
