Sure! Here's a clear and complete explanation along with the code:

---

## 🧩 **Problem Name:**

**Simple Triangle - 4**

---

## 📝 **Task:**

Write a program that prints a triangle pattern using the **plus (`+`)** symbol.

### 🔸 Output Format:

```
+
++
+++
```

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Understand the pattern

- The triangle has **3 rows**.
- Row 1: 1 plus → `+`
- Row 2: 2 pluses → `++`
- Row 3: 3 pluses → `+++`

So, for each row `i` from 1 to 3, we print `+` repeated `i` times.

---

### ✅ Step 2: Use a loop to build the pattern

We can use a loop to print each line with increasing number of plus symbols.

---

## ✅ Full Python Code:

```python
# Print row 1
print("+")

# Print row 2
print("++")

# Print row 3
print("+++")
```

🟢 This version is fixed for 3 lines.

---

### 🔄 Optional: Using a loop (advanced / future)

If you're familiar with loops later, this could be done like:

```python
for i in range(1, 4):
    print("+" * i)
```

But since you're not using loops yet, the manual print statements are perfect.

---

## ✅ Sample Output:

```
+
++
+++
```
