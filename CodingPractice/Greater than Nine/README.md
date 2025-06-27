### ✅ **Problem: Greater than Nine**

**Goal:**
Read two numbers `A` and `B`, and check if **both** are greater than `9`.

---

### 🧠 **Concept Used**

Use the **logical `and` operator**:

```python
A > 9 and B > 9
```

This returns `True` only when **both** `A` and `B` are greater than `9`.

---

### 🪜 **Steps**

1. Read `A` using `int(input())`
2. Read `B` using `int(input())`
3. Check: `A > 9 and B > 9`
4. Print the result

---

### 🧾 **Code**

```python
# Step 1: Read input values
A = int(input())
B = int(input())

# Step 2: Check if both A and B are greater than 9
result = A > 9 and B > 9

# Step 3: Print the result
print(result)
```

---

### 🔍 **Sample Input**

```
11
20
```

### 🎯 **Sample Output**

```
True
```
