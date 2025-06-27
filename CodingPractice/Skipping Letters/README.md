## 🧩 **Problem Name:**

**Skipping Letters**

---

## 📝 **Task:**

You're given:

- A **word** (string input)
- An **index** (integer input)

Write a program to print the word **without the character at the given index**.

---

## 🔍 **Logic:**

To skip (remove) a character at a specific index from a string:

1. Get all characters **before** the index using slicing: `word[:index]`
2. Get all characters **after** the index using slicing: `word[index+1:]`
3. **Concatenate** both parts

---

## 💡 **Concepts Used:**

- ✅ String slicing (`word[:index]`, `word[index+1:]`)
- ✅ Input reading and type conversion (`input()`, `int()`)
- ✅ String concatenation (`+`)

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the input word

```python
word = input()
```

### ✅ Step 2: Read the index value (and convert to integer)

```python
index = int(input())
```

### ✅ Step 3: Slice the string to skip the character at the given index

```python
part1 = word[:index]      # All characters before the given index
part2 = word[index+1:]    # All characters after the given index
```

### ✅ Step 4: Combine both parts

```python
new_word = part1 + part2
```

### ✅ Step 5: Print the result

```python
print(new_word)
```

---

## ✅ Full Python Code with Comments:

```python
# Step 1: Read the word from the user
word = input()

# Step 2: Read the index of the character to be removed
index = int(input())

# Step 3: Slice the word to skip the character at the given index
part1 = word[:index]     # From start to one before the index
part2 = word[index+1:]   # From one after the index to end

# Step 4: Combine the two parts
new_word = part1 + part2

# Step 5: Print the new word
print(new_word)
```

---

## 🧪 Sample Input:

```
Combine
4
```

## 🎯 Sample Output:

```
Combne
```

✅ The character at index 4 (`'n'`) is skipped.
