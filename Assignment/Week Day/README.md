🧩 **Problem Name:**

**Week Day (Using `elif`)**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `D` representing a day of the week (1 to 7)
- ✅ Prints:

  - `"Week Start"` if `D` is 1 or 2 (Monday or Tuesday)
  - `"Midweek"` if `D` is 3, 4, or 5 (Wednesday to Friday)
  - `"Weekend"` if `D` is 6 or 7 (Saturday or Sunday)

---

## 🧠 **Concepts Used:**

- Input/output
- `if`, `elif`, `else`
- Logical operator `or`

---

## ✅ **Code (Using `elif`):**

```python
D = int(input())  # Read the day number

if D == 1 or D == 2:
    print("Week Start")
elif D == 3 or D == 4 or D == 5:
    print("Midweek")
else:
    print("Weekend")
```

---

## 🧪 **Sample Input:**

```
6
```

## 🧾 **Sample Output:**

```
Weekend
```

---

### ✅ When to Use `elif`:

- When you have **multiple exclusive** conditions (only one of them can be true).
- It helps you avoid too many `nested if` blocks and keeps your code more **readable**.
