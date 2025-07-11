## 🧩 **Problem Name:**

**Course Fee**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads the marks `M` of a student
- ✅ Checks and prints the discount based on the following rules:

  - If `M >= 90`, print `"Discount is 200"`
  - Else if `M >= 50`, print `"Discount is 100"`
  - Else, print `"No Discount"`

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators (`>=`)
- Nested `if` statements (no `elif` yet)

---

## ✅ **Code with Comments and Explanation:**

```python
# Read marks from the user and store in a variable
student_marks = int(input())  # Example: 93

# Check if marks are greater than or equal to 90
if student_marks >= 90:
    print("Discount is 200")
else:
    # If not, check if marks are greater than or equal to 50
    if student_marks >= 50:
        print("Discount is 100")
    else:
        # If marks are below 50, no discount
        print("No Discount")
```

---

## 🧪 **Sample Input:**

```
93
```

## 🧾 **Sample Output:**

```
Discount is 200
```

---
