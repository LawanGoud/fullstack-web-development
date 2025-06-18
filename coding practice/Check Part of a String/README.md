## 🧩 **Problem Name:**

**Check Part of a String**

---

## 📝 **Task:**

Write a program that:

- Reads two words `A` and `B`
- Reads an index `I`
- Checks if **word B starts at index I in word A**
- Prints `True` or `False`

---

## 💡 **Concepts Used:**

- `input()` to read values
- Type conversion with `int()`
- String slicing `A[I:I+len(B)]`
- Comparison using `==`

---

## 🧠 Step-by-Step Explanation:

### ✅ Step 1: Read inputs

```python
A = input()  # First word
B = input()  # Second word
I = int(input())  # Index (converted to integer)
```

---

### ✅ Step 2: Use slicing to get the part of A that starts at index I and is the same length as B

```python
part_from_A = A[I:I+len(B)]
```

For example:

- A = "Repeat"
- B = "pea"
- I = 2
- A\[2:5] → "pea" ✅

---

### ✅ Step 3: Compare the sliced part with B

```python
result = part_from_A == B
```

---

### ✅ Step 4: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read inputs
A = input()
B = input()
I = int(input())

# Step 2: Slice A from index I to I+len(B)
part_from_A = A[I:I+len(B)]

# Step 3: Compare and print the result
print(part_from_A == B)
```

---

## 🧪 Sample Input:

```
Repeat
pea
2
```

## 🎯 Sample Output:

```
True
```
