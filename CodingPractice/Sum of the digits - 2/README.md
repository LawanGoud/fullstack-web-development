## 🧩 **Problem Name:**

**Sum of The Digits - 2**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a number `num` between `0` and `10000`
- ✅ Calculates the **sum of its digits**
- ✅ Prints the result

---

## 🧠 **Concepts Used:**

- Input/output
- Arithmetic operators (`//` and `%`)
- Conditional logic (No loops used)

---

## ✅ **Code with Comments:**

```python
# Read the number from the user
number = int(input())

# Initialize sum to 0
digit_sum = 0

# Extract and add each digit from right to left using % and //
if number >= 10000:
    digit_sum += number // 10000
    number = number % 10000

if number >= 1000:
    digit_sum += number // 1000
    number = number % 1000

if number >= 100:
    digit_sum += number // 100
    number = number % 100

if number >= 10:
    digit_sum += number // 10
    number = number % 10

# Add the last digit
digit_sum += number

# Print the sum of digits
print(digit_sum)
```

---

## 🧪 **Sample Input:**

```
25
```

## 🧾 **Sample Output:**

```
7
```

---
