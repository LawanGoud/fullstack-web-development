## 🧩 **Problem Name:**

**Leap Year**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a year `Y`
- ✅ Checks if the year is a **leap year** using these rules:

| Condition for Leap Year                         |
| ----------------------------------------------- |
| Divisible by `400`                              |
| Divisible by `4` **and not divisible** by `100` |

- ✅ Prints `True` if any of the above conditions are satisfied, otherwise prints `False`

---

## 🧠 **Concepts Used:**

- Input/output
- Logical operators: `and`, `or`, `not`
- Modulus operator `%` to check divisibility
- Boolean expressions

---

## ✅ **Code with Comments and Explanation:**

```python
# Read the input year
year = int(input())  # Example: 2016

# Check if year is divisible by 400
is_divisible_by_400 = (year % 400 == 0)

# Check if year is divisible by 4 and not divisible by 100
is_divisible_by_4_not_100 = (year % 4 == 0) and (year % 100 != 0)

# A year is a leap year if it satisfies either condition
if is_divisible_by_400 or is_divisible_by_4_not_100:
    print(True)
else:
    print(False)
```

---

## 🧪 **Sample Input and Output:**

**Input:**

```
2016
```

**Output:**

```
True
```

---
