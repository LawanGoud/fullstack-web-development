## 🧩 **Problem Name:**

**Weather Condition**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads a temperature `T`
- ✅ Checks `T` and displays a weather condition message based on the temperature range

---

## 🧠 **Concepts Used:**

- Input/output
- Floating-point numbers
- Comparison operators (`<`, `<=`)
- `if`, `elif`, `else` conditional statements

---

## ✅ **Code with Comments:**

```python
# Read temperature as float input
temperature = float(input())

# Check temperature range and print message
if temperature < 0:
    print("Freezing weather")  # If temperature is less than 0
elif temperature < 10:
    print("Very Cold weather")  # 0 <= T < 10
elif temperature < 20:
    print("Cold Weather")  # 10 <= T < 20
elif temperature < 30:
    print("Normal")  # 20 <= T < 30
elif temperature < 40:
    print("Hot")  # 30 <= T < 40
else:
    print("Very Hot")  # T >= 40
```

---

## 🧪 **Sample Input:**

```
-50.0
```

## 🧾 **Sample Output:**

```
Freezing weather
```

---
