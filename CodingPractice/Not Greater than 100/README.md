### ✅ **Problem: Not Greater than 100**

**Goal:**
Check if the **sum** of two numbers `A` and `B` is **not greater than 100**.

---

### 🧠 **Concept Used**

We need to check:

```python
(A + B) <= 100
```

---

### 🪜 **Steps**

1. Read integer input `A`
2. Read integer input `B`
3. Compute the sum of `A + B`
4. Check if the sum is **less than or equal to 100**
5. Print the result

---

### 🧾 **Code**

```python
# Step 1: Read inputs
A = int(input())
B = int(input())

# Step 2: Check if sum is not greater than 100
result = (A + B) <= 100

# Step 3: Print result
print(result)
```

---

### 🔍 **Sample Input**

```
30
20
```

### 🎯 **Sample Output**

```
True
```
