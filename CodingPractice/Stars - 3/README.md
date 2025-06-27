## 🧩 **Problem Name:**

**Stars - 3**

---

## 📝 **Task:**

Write a program that:

- Takes an integer input `N`
- Prints **3 lines**
- Each line should have **N stars (`*`)** with **a space after each star**

---

## 💡 **Concepts Used:**

- `input()` to take input
- `int()` for type conversion
- String multiplication to repeat `"* "` N times
- `print()` to print multiple lines

---

## 🧠 **Step-by-Step Explanation:**

### ✅ Step 1: Take Input

```python
n = input()
```

🔸 `n` is a string by default. To do math or repetition, convert to an integer.

```python
n = int(n)
```

---

### ✅ Step 2: Create a line of N stars

To get N stars with a space after each, we use:

```python
line = "* " * n
```

🟢 Example:
If `n = 4`, then
`line = "* * * * "`

---

### ✅ Step 3: Print that line 3 times

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

# Step 2: Create a line with N stars
line = "* " * n

# Step 3: Print the line 3 times
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
* * * *
* * * *
* * * *
```
