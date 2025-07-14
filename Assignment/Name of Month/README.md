## 🧩 **Problem Name:**

**Name of Month**

---

## 🎯 **Goal:**

✅ Read a number between 1 and 12
✅ Print the name of the corresponding month
✅ If the number is not in this range, print `"Invalid Month Number"`

---

## 🧠 **Concepts Used:**

- Input/output
- Integer comparison
- Conditional statements (`if`, `elif`, `else`)

---

## ✅ **Code (With Comments & Explanation):**

```python
# Read the month number from user
month_number = int(input())

# Check and print the corresponding month name
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    # If the number is not between 1 and 12, it's invalid
    print("Invalid Month Number")
```

---

## 🧪 **Sample Input 1:**

```
4
```

## 🧾 **Sample Output 1:**

```
April
```

---

## 🧪 **Sample Input 2:**

```
13
```

## 🧾 **Sample Output 2:**

```
Invalid Month Number
```

---
