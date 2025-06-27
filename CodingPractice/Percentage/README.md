## 🧩 **Problem Name**

**Percentage**

---

## 📌 **Task**

Write a program that:

- Takes a percentage `P` as input
- Calculates `P%` of the number `200`
- Prints the result

---

## 🧠 **Concept Explanation**

To calculate a percentage **P** of any number **N**, use this formula:

```
value = (P / 100) * N
```

In this case:

- `P` = percentage input from user
- `N` = 200
- We need to compute `value = (P / 100) * 200`

---

## ✅ **Step-by-Step Code Explanation**

---

### ✅ Step 1: Read the Input

Read percentage `P` using `input()`. Since it may be a decimal, convert it to `float`.

```python
P = input()
P = float(P)
```

---

### ✅ Step 2: Perform the Calculation

```python
value = (P / 100) * 200
```

Example:
If P = 50
Then: `value = (50 / 100) * 200 = 100.0`

---

### ✅ Step 3: Print the Result

```python
print(value)
```

---

## ✅ **Final Code**

```python
P = input()
P = float(P)

value = (P / 100) * 200

print(value)
```

---

## 🧪 **Sample Input**

```
50
```

## 🎯 **Sample Output**

```
100.0
```
