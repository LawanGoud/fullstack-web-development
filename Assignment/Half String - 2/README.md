## 🧩 **Problem Name:**

**Half String - 2**

---

## 📝 **Task:**

Write a program that:

- Reads a **string** from the user.
- Prints the **second half** of the string.

---

## 💡 **Concepts Used:**

- ✅ String indexing
- ✅ String slicing
- ✅ Integer division with `//`

---

## 🧠 **Step-by-Step Explanation:**

### Step 1: Take input from user

```python
text = input()
```

This reads a string and stores it in the variable `text`.

---

### Step 2: Find the half index

```python
half_index = len(text) // 2
```

- `len(text)` gives the total number of characters.
- `//` is **integer division**, so it gives the index for the **second half**.

---

### Step 3: Slice the string from half index to end

```python
second_half = text[half_index:]
```

This gives the part of the string from `half_index` to the end.

---

### Step 4: Print the result

```python
print(second_half)
```

---

## ✅ Full Code:

```python
# Step 1: Read input
text = input()

# Step 2: Calculate half index
half_index = len(text) // 2

# Step 3: Slice second half
second_half = text[half_index:]

# Step 4: Print the second half
print(second_half)
```

---

## 🧪 Sample Input:

```
Football
```

## 🎯 Sample Output:

```
ball
```
