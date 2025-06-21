### ✅ **Problem: Positive Number**

**Goal:**
Read two numbers `A` and `B`, and check if **at least one** of them is a **positive number**.

---

### 🧠 **Concept Used**

Use the **logical `or` operator**:

```python
A > 0 or B > 0
```

This will return `True` if **either** `A` or `B` is greater than `0`.

---

### 🪜 **Steps**

1. Read integer input `A`
2. Read integer input `B`
3. Use logical condition `A > 0 or B > 0`
4. Print the result

---

### 🧾 **Code**

```python
# Step 1: Read input values
A = int(input())
B = int(input())

# Step 2: Check if at least one number is positive
result = A > 0 or B > 0

# Step 3: Print the result
print(result)
```

---

### 🔍 **Sample Input**

```
4
-6
```

### 🎯 **Sample Output**

```
True
```
