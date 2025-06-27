## 🧩 **Problem Name:**

**Part of a String - 3**

---

## 📝 **Task:**

Write a program that:

- Reads a string `A`.
- Excludes the **first two** and **last two** characters from the string.
- Prints the **middle part** only.

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the input

```python
A = input()
```

---

### ✅ Step 2: Exclude the first 2 and last 2 characters

We use **string slicing** here:

```python
result = A[2:-2]
```

- `A[2:]` → starts from index 2 to the end.
- `A[2:-2]` → starts from index 2 and stops **before** the last two characters.

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read input
A = input()

# Step 2: Slice to exclude first 2 and last 2 characters
result = A[2:-2]

# Step 3: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
##Soft##
```

## 🎯 Sample Output:

```
Soft
```
