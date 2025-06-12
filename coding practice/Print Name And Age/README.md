### 👤 Print Name and Age

**Task:**  
Write a Python program that:

- Reads a person's **name** and **age**
- Prints the output in the following format:

```

{name} is {age} years old

```

---

### ✅ Python Code:

```python
name = input()
age = input()
print(name + " is " + age + " years old")
```

---

### 🧠 Explanation:

1. `input()` is used twice — once to read the name and once to read the age.
2. We use string concatenation (`+`) to combine the values with the message.
3. The final message is printed in the desired format.

---

### 🧪 Example:

**Input:**

```
Anita
23
```

**Output:**

```
Anita is 23 years old
```

---

> 💡 Since `input()` always returns a string, there's no need to convert `age` before concatenation.
