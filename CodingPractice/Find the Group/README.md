## 🧩 **Problem Name:**

**Find the Group**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `N` (between 1 and 10)
- ✅ Prints:

  - `"Group A"` if the number is **odd**
  - `"Group B"` if the number is **even**

---

## 🧠 **Concepts Used:**

- Input/output
- Arithmetic operator: Modulus `%`
- Conditional statements (`if-else`)

> 💡 **Tip:**
> The modulus operator `%` gives the remainder after division.
> If `N % 2 == 0` → even number.
> If `N % 2 == 1` → odd number.

---

## ✅ **Code:**

```python
N = int(input())  # Read a number between 1 to 10

# Check if the number is odd or even
if N % 2 == 1:
    print("Group A")  # Odd numbers are in Group A
else:
    print("Group B")  # Even numbers are in Group B
```

---

## 🧪 **Sample Input:**

```
6
```

## 🧾 **Sample Output:**

```
Group B
```

---
