## 🧩 **Problem Name:**

**Print the Value**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a string `S`
- ✅ The **last character** of `S` tells us what multiplier to use:

  - `'T'` → Multiply number by `10`
  - `'H'` → Multiply number by `100`
  - `'K'` → Multiply number by `1000`

- ✅ The **remaining part** of the string (except the last character) is the number
- ✅ Print the result after multiplying

---

## 🧠 **Concepts Used:**

- Input/output
- String slicing and indexing
- Type conversion (string to int)
- Conditional statements

---

## ✅ **Code with Comments:**

```python
# Read the input string
input_string = input()

# Get the last character to decide the multiplier
unit = input_string[-1]

# Get the numeric part by removing the last character
number_part = input_string[:-1]

# Convert number part to integer
numeric_value = int(number_part)

# Decide multiplier based on unit character
if unit == "T":
    result = numeric_value * 10
elif unit == "H":
    result = numeric_value * 100
elif unit == "K":
    result = numeric_value * 1000
else:
    result = numeric_value  # If no valid unit is given

# Print the final result
print(result)
```

---

## 🧪 **Sample Input:**

```
34T
```

## 🧾 **Sample Output:**

```
340
```

---
