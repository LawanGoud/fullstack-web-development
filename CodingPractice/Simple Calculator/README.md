## 🧩 **Problem Name:**

**Simple Calculator**

---

## 🎯 **Goal:**

Write a program that:

- ✅ Reads an **operator `O`** (one of `+`, `-`, `*`, `/`, `%`)
- ✅ Reads two integers `A` and `B`
- ✅ Performs the corresponding arithmetic operation
- ✅ Prints the **result**

---

## 🧠 **Concepts Used:**

- Input/output
- Arithmetic operators (`+`, `-`, `*`, `/`, `%`)
- Conditional statements

---

## ✅ **Code with Comments:**

```python
# Read the operator as a string
operator = input()

# Read two integer values
first_number = int(input())
second_number = int(input())

# Check and apply the corresponding operation
if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    # Ensure no division by zero
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("Cannot divide by zero")
elif operator == "%":
    # Ensure no division by zero for modulus
    if second_number != 0:
        print(first_number % second_number)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
```

---

## 🧪 **Sample Input:**

```
+
3
5
```

## 🧾 **Sample Output:**

```
8
```

---
