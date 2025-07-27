## 🧩 **Problem Name:**

**Print Length Times**

---

## 🎯 **Goal:**

✅ Read a word (string)
✅ Find its length (N)
✅ Print the **first character** of the string **N times**, one per line

---

## 🧠 **Concepts Used:**

- Input/output
- String indexing (`word[0]`)
- String length (`len()`)
- `while` loop

---

## ✅ **Code with Explanation:**

```python
# Read the input string
word = input()

# Get the length of the string
length = len(word)

# Get the first character of the string
first_character = word[0]

# Set a counter variable
count = 0

# Loop from 0 to length
while count < length:
    print(first_character)  # Print the first character
    count = count + 1       # Move to the next count
```

---

## 🧪 **Sample Input:**

```
Cool
```

## 🧾 **Sample Output:**

```
C
C
C
C
```

---
