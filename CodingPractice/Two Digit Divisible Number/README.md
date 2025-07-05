## 🧩 **Problem Name:**

**2 Digit Divisible Number**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **two-digit number** `N`
✅ Checks if `N` is divisible by **both its digits**
✅ If so, print **double of N** (`N * 2`)
✅ Otherwise, print `N`

---

## 🧠 **Concepts Used:**

* Input and output
* Integer conversion
* Indexing a string
* Type casting
* Modulus operator `%`
* Logical operator `and`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read input

```python
N = input()
```

---

### ✅ Step 2: Convert to integer and extract digits

```python
number = int(N)
digit1 = int(N[0])  # First digit
digit2 = int(N[1])  # Second digit
```

---

### ✅ Step 3: Check if divisible by both digits

```python
if digit1 != 0 and digit2 != 0 and number % digit1 == 0 and number % digit2 == 0:
    print(number * 2)
else:
    print(number)
```

---

## 🧪 Sample Input:

```
15
```

### 🧾 Sample Output:

```
30
```

---

## ✅ Full Code:

```python
# Read a two-digit number as string
N = input()

# Convert string to integer
number = int(N)

# Get the first and second digits
digit1 = int(N[0])
digit2 = int(N[1])

# Check if both digits are not zero and N is divisible by both digits
if digit1 != 0 and digit2 != 0 and number % digit1 == 0 and number % digit2 == 0:
    # Print double of N
    print(number * 2)
else:
    # Print original number
    print(number)
```

---

