### 🔢 First & Last Digits

**Task:**  
Write a Python program that:

- Reads a **4-digit number** as input
- Prints the **first** and **last** digit of the number

---

### ✅ Python Code:

```python
number = input()
print(number[0], number[-1])
```

---

### 🧠 Explanation:

- `input()` reads the number as a string.
- `number[0]` gives the **first digit**.
- `number[-1]` gives the **last digit**.
- `print(..., ...)` prints them with a space in between.

---

### 🧪 Example:

**Input:**

```
5389
```

**Output:**

```
5 9
```

---

> 💡 Using string indexing allows easy access to specific digit positions.
