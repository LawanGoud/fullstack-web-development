## 🧩 **Problem Name:**

**Greatest Among Three Numbers - 2**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads three numbers `A`, `B`, and `C`
- ✅ Checks which number is the greatest among the three
- ✅ Prints the greatest number

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators (`>`)
- Nested `if` statements (no `elif` yet)

---

## ✅ **Code (with different variable names):**

```python
first_value = int(input())
second_value = int(input())
third_value = int(input())

if first_value > second_value:
    if first_value > third_value:
        print(first_value)
    else:
        print(third_value)
else:
    if second_value > third_value:
        print(second_value)
    else:
        print(third_value)
```

---

## 🧪 **Sample Input:**

```
10
15
20
```

## 🧾 **Sample Output:**

```
20
```

---
