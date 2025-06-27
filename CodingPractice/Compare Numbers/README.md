## ✅ Problem: Compare Numbers

**Goal:**
Read two numbers `A` and `B`, then check if:

- **Both** `A > 35` and `B > 35`, **OR**
- `A > B`

---

## 🧠 Concepts Used

- **Logical Operators**:

  - `and` for combining conditions that **must both be true**
  - `or` for combining conditions where **either can be true**

---

## 🪜 Step-by-Step

### Step 1: Read two integers

```python
A = int(input())
B = int(input())
```

### Step 2: Apply the condition

```python
result = (A > 35 and B > 35) or (A > B)
```

### Step 3: Print the result

```python
print(result)
```

---

## 🔁 Full Code

```python
A = int(input())
B = int(input())

result = (A > 35 and B > 35) or (A > B)

print(result)
```

---

## 🧪 Sample Input

```
45
25
```

## 🎯 Sample Output

```
True
```
