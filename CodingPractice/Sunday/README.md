## 🧩 **Problem Name:**

**Sunday**

---

## 📝 **Task:**

Write a program that:

- Reads a **day number** (1 to 7)
- Checks if the day is **Sunday**
- Prints `True` if it is Sunday, otherwise `False`

---

## 💡 **Assumption:**

- In many calendars, **Sunday is represented by 7**

So:

```
1 → Monday
2 → Tuesday
...
7 → Sunday
```

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read input as integer

```python
day = int(input())
```

This reads a number (e.g., `7`) and converts it from string to integer.

---

### ✅ Step 2: Check if the number is equal to 7

```python
result = day == 7
```

This uses the equality operator `==` to check if the entered number is 7 (Sunday).

---

### ✅ Step 3: Print the result

```python
print(result)
```

---

## ✅ Full Code:

```python
# Step 1: Read the day number
day = int(input())

# Step 2: Check if it's Sunday (i.e., day number is 7)
result = day == 7

# Step 3: Print the result
print(result)
```

---

## 🧪 Sample Input:

```
7
```

## 🎯 Sample Output:

```
True
```

If the input was `5`, the output would be `False`.
