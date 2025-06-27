## 🧩 **Problem Name:**

**Shape**

---

## 📝 **Task:**

Write a program that:

- Takes a number `N` as input.
- Prints **three lines**.
- Each line contains **`N` plus symbols (`+`)**.
- Each plus symbol should be followed by a **space**.

---

## 💡 **Concepts Used:**

- ✅ `input()` to read data from the user
- ✅ `int()` to convert string input to integer
- ✅ String repetition (`"* " * n`) to create repeated patterns
- ✅ `print()` to display output

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Read the input and convert it

```python
n = input()
n = int(n)
```

This reads the number as a string and converts it to an integer.

---

### ✅ Step 2: Prepare a line of N plus symbols

```python
line = "+ " * n
```

- If `n = 4`, then `line = "+ + + + "`

---

### ✅ Step 3: Print the line 3 times

```python
print(line)
print(line)
print(line)
```

---

## ✅ Full Code:

```python
# Step 1: Read input and convert to integer
n = input()
n = int(n)

# Step 2: Create one line with N plus symbols
line = "+ " * n

# Step 3: Print that line 3 times
print(line)
print(line)
print(line)
```

---

## 🧪 Sample Input:

```
4
```

## 🎯 Sample Output:

```
+ + + +
+ + + +
+ + + +
```
