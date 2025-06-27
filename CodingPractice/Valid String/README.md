
## 🧩 **Problem Name:**

**Valid String**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **string** `S`
✅ Checks if:

* The **length of S is between 2 and 7** (inclusive), **OR**
* The **first character of S is not equal to `'a'`**

🔹 If any one condition is **True**, print:

```
Valid String
```

🔹 Otherwise, print:

```
Not a Valid String
```

---

## 🧠 **Concepts Used:**

* `len()` function for string length
* String indexing (`S[0]`)
* Logical operators (`or`)
* Conditional statements (`if-else`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the string

```python
S = input()
```

---

### ✅ Step 2: Apply conditions

```python
2 <= len(S) <= 7 or S[0] != 'a'
```

---

### ✅ Step 3: Print result using `if-else`

---

## 🧪 Sample Input:

```
apple
```

### 🧾 Sample Output:

```
Valid String
```

---

## ✅ Full Code:

```python
# Read the input string
S = input()

# Check if the length is between 2 and 7 or first character is not 'a'
if 2 <= len(S) <= 7 or S[0] != 'a':
    # If any condition is true, it's a valid string
    print("Valid String")
else:
    # Otherwise, it's not valid
    print("Not a Valid String")
```

---

