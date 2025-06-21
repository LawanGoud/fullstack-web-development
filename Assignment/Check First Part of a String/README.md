### ✅ **Problem Summary**

You are given two strings:

- `S1`: A full string
- `S2`: A possible prefix

👉 You need to check if `S1` **starts with** `S2`.
You may only use **string slicing**, not unlearned concepts like `startswith()`.

---

### 🧠 **Step-by-step Explanation**

#### Step 1: Take input

```python
S1 = input()
S2 = input()
```

#### Step 2: Get the first part of `S1` with the same length as `S2`

```python
first_part = S1[:len(S2)]
```

#### Step 3: Compare and print the result

```python
print(first_part == S2)
```

---

### 🧾 Full Code:

```python
S1 = input()
S2 = input()

# Extract the first part of S1 with the same length as S2
first_part = S1[:len(S2)]

# Check if they are equal
print(first_part == S2)
```

---

### 🧪 Sample Input:

```
rainbow
rain
```

### 🎯 Sample Output:

```
True
```
