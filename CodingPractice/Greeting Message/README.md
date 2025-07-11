## 🧩 **Problem Name:**

**Greeting Message**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads the current time in 24-hour format (`hour`)
- ✅ Prints a greeting based on the time:

| Time Range                     | Greeting       |
| ------------------------------ | -------------- |
| 4 ≤ hour < 12                  | Good Morning   |
| 12 ≤ hour < 16                 | Good Afternoon |
| 16 ≤ hour < 20                 | Good Evening   |
| 20 ≤ hour < 24 or 0 ≤ hour < 4 | Good Night     |

---

## 🧠 **Concepts Used:**

- Input/output
- Comparison operators
- `if`, `elif`, `else` statements
- Logical OR (`or`) operator

---

## ✅ **Code with Comments and Explanation:**

```python
# Read the current time as an integer (0 to 23)
current_hour = int(input())  # Example: 9

# Check if time is between 4 and 12 (exclusive of 12)
if current_hour >= 4 and current_hour < 12:
    print("Good Morning")

# Check if time is between 12 and 16 (exclusive of 16)
elif current_hour >= 12 and current_hour < 16:
    print("Good Afternoon")

# Check if time is between 16 and 20 (exclusive of 20)
elif current_hour >= 16 and current_hour < 20:
    print("Good Evening")

# For any other time, it's Good Night
else:
    print("Good Night")
```

---

## 🧪 **Sample Input:**

```
9
```

## 🧾 **Sample Output:**

```
Good Morning
```

---
