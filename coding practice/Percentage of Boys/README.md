## 🧩 **Problem Name**

**Percentage of Boys**

---

## 📌 **Task**

Write a Python program that:

- Reads the percentage of girls in a class
- Calculates the percentage of boys
- Prints the result

**Note:** The total percentage of boys and girls together is always **100%**.

---

## 🧠 **Step-by-Step Explanation**

---

### ✅ Step 1: Read Input – Percentage of Girls

Use the `input()` function and convert the input to a number using `int()` since percentage is typically an integer.

```python
girls_percentage = input()
girls_percentage = int(girls_percentage)
```

📌 Example:
If the user enters `30`, that means 30% are girls.

---

### ✅ Step 2: Calculate Boys Percentage

Since the total is 100%, subtract the percentage of girls from 100.

```python
boys_percentage = 100 - girls_percentage
```

📌 Example:
If `girls_percentage` is `30`,
Then `boys_percentage = 100 - 30 = 70`

---

### ✅ Step 3: Print the Result

Print the value of `boys_percentage`.

```python
print(boys_percentage)
```

---

## 🧪 **Example**

**Input:**

```
30
```

**Output:**

```
70
```

---

## ✅ **Final Code**

```python
# Step 1: Read the percentage of girls
girls_percentage = input()
girls_percentage = int(girls_percentage)

# Step 2: Calculate boys percentage
boys_percentage = 100 - girls_percentage

# Step 3: Print the result
print(boys_percentage)
```
