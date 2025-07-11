## 🧩 **Problem Name:**

**Weight**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads the weight `W` of a box in kilograms
✅ Checks:

* If `W >= 100` → Print `"Box is Heavier"`
* Else if `W >= 30` → Print `"Box is Heavy"`
  ✅ Use **nested conditionals**

---

## 🧠 **Concepts Used:**

* Input and output
* Comparison operators (`>=`)
* Conditional statements (`if`, `else`)
* **Nested conditional blocks**

---

## 🪜 **Step-by-Step Solution:**

### ✅ Step 1: Read the weight

```python
W = int(input())
```

---

### ✅ Step 2: Check conditions using nested `if`

```python
if W >= 100:
    print("Box is Heavier")
else:
    if W >= 30:
        print("Box is Heavy")
```

---

## 🧪 **Sample Input:**

```
60
```

### 🧾 **Sample Output:**

```
Box is Heavy
```

---

