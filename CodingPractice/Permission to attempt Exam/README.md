## 🧩 **Problem Name:**

**Permission to Attempt Exam**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads attendance percentage `A` (with `%` at the end, like `"80%"`)
- ✅ Reads medical report status `M` (`"Y"` or `"N"`)
- ✅ Checks if:

  - Attendance is **greater than or equal to 75**
  - OR Medical report status is `"Y"`

- ✅ Prints:

  - `"Allowed to write exam"` if **either** condition is satisfied
  - `"Cannot write exam"` otherwise

---

## 🧠 **Concepts Used:**

- String manipulation (`strip`, `int`, slicing)
- Conditional statements (`if-else`)
- Logical OR (`or`)

---

## ✅ **Code with Comments:**

```python
# Read attendance percentage as string input (e.g. "80%")
attendance_input = input()

# Read medical report status ("Y" or "N")
has_medical_report = input()

# Remove the '%' from the end and convert to integer
attendance_value = int(attendance_input[:-1])

# Check the conditions
if attendance_value >= 75 or has_medical_report == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
```

---

## 🧪 **Sample Input:**

```
80%
Y
```

## 🧾 **Sample Output:**

```
Allowed to write exam
```

---
