## 🧩 **Problem Name:**

**Compare Last Three Characters**

---

## 📝 **Task:**

Write a program that:

- Reads **two words** as input.
- Checks whether the **last three characters** of both words are the **same**.
- Prints `True` or `False`.

---

## 💡 **Concepts Used:**

- `input()` to read input
- String slicing
- Comparison using `==`
- `print()` to display the result

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the input strings

```python
word1 = input()
word2 = input()
```

This will store the two words entered by the user.

---

### ✅ Step 2: Get the last 3 characters

We can use **negative indexing** or **slicing** to get the last three characters from each word.

```python
last3_word1 = word1[-3:]
last3_word2 = word2[-3:]
```

Example:
If `word1 = "apple"` and `word2 = "pimple"`

- `last3_word1 = "ple"`
- `last3_word2 = "ple"`

---

### ✅ Step 3: Compare the two substrings

```python
result = last3_word1 == last3_word2
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read two words
word1 = input()
word2 = input()

# Step 2: Slice to get last 3 characters
last3_word1 = word1[-3:]
last3_word2 = word2[-3:]

# Step 3: Compare
result = last3_word1 == last3_word2

# Step 4: Print result
print(result)
```

---

## 🧪 Sample Input:

```
apple
pimple
```

## 🎯 Sample Output:

```
True
```
