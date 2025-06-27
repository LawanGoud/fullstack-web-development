## 🧩 **Problem Name:**

**Skip the Fourth Character**

---

## 📝 **Task:**

Write a program that:

- Takes a **word** as input
- Removes the **4th character** (i.e., character at index `3`)
- Prints the resulting word

---

## 🔍 **Logic:**

When you need to **remove a character at a specific position**, you can:

- Take everything **before** that character (`word[:index]`)
- Take everything **after** that character (`word[index+1:]`)
- Then **combine** them using `+`

For this task, we want to skip the **4th character**, which is at **index 3**.
So, we split the word into:

- `word[:3]` → First 3 characters
- `word[4:]` → From the 5th character onward

We then combine both parts:

```python
new_word = word[:3] + word[4:]
```

---

## 💡 **Concepts Used:**

- ✅ `input()` for user input
- ✅ **String indexing** (starts at 0)
- ✅ **Slicing** to extract parts of the string
- ✅ **Concatenation** to combine two string parts

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the input word

```python
word = input()
```

---

### ✅ Step 2: Split into two parts

```python
part1 = word[:3]    # Characters before index 3 (0,1,2)
part2 = word[4:]    # Characters after index 3 (starting from index 4)
```

---

### ✅ Step 3: Combine parts and store in a new variable

```python
new_word = part1 + part2
```

---

### ✅ Step 4: Print the result

```python
print(new_word)
```

---

## ✅ Full Code with Comments:

```python
# Step 1: Read the input word from the user
word = input()

# Step 2: Get the first part (before index 3)
part1 = word[:3]

# Step 3: Get the second part (after index 3)
part2 = word[4:]

# Step 4: Combine both parts to skip the 4th character
new_word = part1 + part2

# Step 5: Print the new word
print(new_word)
```

---

## 🧪 Sample Input:

```
Equality
```

## 🎯 Sample Output:

```
Equlity
```
