### ✅ **Problem: Negative Numbers**

**Goal:**
Read two numbers `A` and `B`, and check if **both** are negative numbers.

---

### 🧠 **Concept Used**

Use the **logical `and` operator**:

```python
A < 0 and B < 0
```

This returns `True` only when **both** `A` and `B` are less than `0`.

---

### 🪜 **Steps**

1. Read integer input `A`
2. Read integer input `B`
3. Check whether both are negative using:
   `A < 0 and B < 0`
4. Print the result

---

### 🧾 **Code**

```python
# Step 1: Read input values
A = int(input())
B = int(input())

# Step 2: Check if both A and B are negative
result = A < 0 and B < 0

# Step 3: Print the result
print(result)
```

---

### 🔍 **Sample Input**

```
-3
-9
```

### 🎯 **Sample Output**

```
True
```
