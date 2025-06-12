### 🔁 Reverse the Digits

**Task:**  
Write a Python program that:

- Reads a **two-digit number** as input
- Prints the digits in **reverse order**

---

### ✅ Python Code:

```python
number = input()
first_digit = number[0]
second_digit = number[1]
print(second_digit + first_digit)
```

---

### 🧠 Explanation:

- `input()` reads the number as a **string**.
- `number[0]` is the **first digit**.
- `number[1]` is the **second digit**.
- We **swap** the order using string concatenation (`+`) and print the result.

---

### 🧪 Example:

**Input:**

```
42
```

**Output:**

```
24
```

---

> ✅ This approach uses only basic indexing and string joining — no slicing or complex methods.
