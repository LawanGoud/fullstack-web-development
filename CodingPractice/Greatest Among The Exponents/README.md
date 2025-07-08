

## 🧩 **Problem Name:**

**Greatest Among The Exponents**

---

## 🎯 **Goal:**

✅ Read two numbers `A` and `B`
✅ Calculate `A ** B` and `B ** A`
✅ Print the greater value between the two

---

## 🧠 **Concepts Used:**

* Input and type conversion (`int`)
* Exponentiation operator `**`
* Conditional statements (`if` / `else`)

---

## ✅ Full Code:

```python
# Read the first number
A = int(input())

# Read the second number
B = int(input())

# Calculate A power B and B power A
power1 = A ** B
power2 = B ** A

# Print the greatest among the two powers
if power1 > power2:
    print(power1)
else:
    print(power2)
```

---

## 🧪 Sample Input:

```
2  
3
```

### 🧾 Sample Output:

```
9
```

---

