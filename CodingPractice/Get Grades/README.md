## 🧩 **Problem Name:**

**Get Grades**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads the student's marks
- ✅ Prints the grade based on the score:

  - `"A"` if marks > 85
  - `"B"` if marks > 70 and ≤ 85
  - `"C"` if marks ≥ 60 and ≤ 70
  - `"F"` if marks < 60

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators (`>`, `<`, `>=`, `<=`)
- `if`, `elif`, `else` conditional blocks

---

## ✅ **Code with Comments and Explanation:**

```python
# Read the marks from the user
student_marks = float(input())  # Example: 70.5

# Check if marks are greater than 85 → Grade A
if student_marks > 85:
    print("A")

# Check if marks are greater than 70 and less than or equal to 85 → Grade B
elif student_marks > 70 and student_marks <= 85:
    print("B")

# Check if marks are between 60 and 70 inclusive → Grade C
elif student_marks >= 60 and student_marks <= 70:
    print("C")

# If none of the above, marks must be less than 60 → Grade F
else:
    print("F")
```

---

## 🧪 **Sample Input:**

```
70.5
```

## 🧾 **Sample Output:**

```
B
```

---
