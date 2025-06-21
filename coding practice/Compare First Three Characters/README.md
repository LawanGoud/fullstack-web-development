## 🧩 **Problem Name:**

**Compare First Three Characters**

---

## 📝 **Task:**

Write a program that:

- Takes two words as input.
- Checks whether the **first three characters** of both words are the same.
- Prints `True` or `False`.

---

## 💡 **Concepts Used:**

- `input()` to read strings.
- String slicing (`word[:3]`).
- Comparison using `==`.

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the two input words

```python
word1 = input()
word2 = input()
```

This takes two words from the user and stores them.

---

### ✅ Step 2: Get the first 3 characters of each word

```python
part1 = word1[:3]
part2 = word2[:3]
```

This slices each word from index `0` to `2` (inclusive), which gives us the **first 3 characters**.

---

### ✅ Step 3: Compare the two parts

```python
result = part1 == part2
```

This checks if the first three characters are the same.

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read two input words
word1 = input()
word2 = input()

# Step 2: Slice first 3 characters from each
part1 = word1[:3]
part2 = word2[:3]

# Step 3: Compare and print result
print(part1 == part2)
```

---

## 🧪 Sample Input:

```
Apple
Application
```

## 🎯 Sample Output:

```
True
```

✅ Because both start with `"App"`.

---
