## 🧩 **Problem Name:**

**Allowed to Exam**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads two strings `H` (Hall ticket) and `I` (Identification card)
✅ Checks:

* If `H` is equal to `"Y"` → Print `"Allowed to Exam - Has Hall ticket"`
* Else if `I` is equal to `"Y"` → Print `"Allowed to Exam - Has Identification Card"`
  ✅ Use **nested conditionals**

---

## 🧠 **Concepts Used:**

* Input and output
* String comparison
* Conditional statements (`if`, `else`)
* **Nested conditional blocks**

---

## 🪜 **Step-by-Step Solution:**

### ✅ Step 1: Read inputs

```python
H = input()
I = input()
```

---

### ✅ Step 2: Check conditions using nested `if`

```python
if H == "Y":
    print("Allowed to Exam - Has Hall ticket")
else:
    if I == "Y":
        print("Allowed to Exam - Has Identification Card")
```

---

## 🧪 **Sample Input:**

```
Y  
N
```

### 🧾 **Sample Output:**

```
Allowed to Exam - Has Hall ticket
```

---