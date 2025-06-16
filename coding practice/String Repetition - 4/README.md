## 🧩 Problem Name

**String Repetition - 4**

---

## 📌 Task

Write a program that:

- Reads a **string** and an **integer N**.
- Prints the **string repeated N times**, with **spaces** in between.

---

## 🧠 Concept Explanation

To solve this problem using what we’ve learned so far:

- Use `input()` to take user inputs.
- Use `int()` to convert string input to integer.
- Use string concatenation `+` to combine the word with a space.
- Use `*` to repeat the string.

> We will **not** use `.strip()` or `.join()` because those are not yet introduced.

---

## ✅ Step-by-Step Code

### Step 1: Read inputs

```python
word = input()
N = int(input())
```

### Step 2: Repeat the word N times with a space after each

```python
output = (word + " ") * N
```

### Step 3: Print the result

```python
print(output)
```

---

## ✅ Final Code

```python
word = input()
N = int(input())
output = (word + " ") * N
print(output)
```

---

## 🧪 Sample Input

```
messages
3
```

## 🎯 Sample Output

```
messages messages messages
```

---

> ✅ Note: There's an **extra space** at the end. That’s okay for now, because we haven’t learned how to remove it using `.strip()` yet.
