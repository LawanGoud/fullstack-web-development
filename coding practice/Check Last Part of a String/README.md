## 🧩 **Problem Name:**

**Check Last Part of a String**

---

## 📝 **Task:**

Write a program that:

- Reads two words `A` and `B`
- Checks if `B` is the last part of `A`
- Prints `True` or `False`

---

## 💡 **Concepts Used:**

- `input()` to read user input
- String slicing
- `==` (equality) operator

---

## ✅ Step-by-Step Solution:

### 📌 Step 1: Read input

```python
A = input()
B = input()
```

### 📌 Step 2: Find the length of word B

```python
len_B = len(B)
```

This helps us know how many characters we need to check at the end of word A.

### 📌 Step 3: Slice the end of word A

```python
last_part_of_A = A[-len_B:]
```

This takes the last `len_B` characters from A.
For example:

- A = "Blackhole"
- B = "hole"
- A\[-4:] → "hole"

### 📌 Step 4: Compare with B

```python
result = last_part_of_A == B
```

### 📌 Step 5: Print the result

```python
print(result)
```

---

## ✅ Full Code (No advanced methods):

```python
# Step 1: Read input
A = input()
B = input()

# Step 2: Get the length of B
len_B = len(B)

# Step 3: Extract the last part of A with the same length as B
last_part_of_A = A[-len_B:]

# Step 4: Compare and print the result
print(last_part_of_A == B)
```

---

## 🧪 Sample Input:

```
Blackhole
hole
```

## 🎯 Sample Output:

```
True
```
