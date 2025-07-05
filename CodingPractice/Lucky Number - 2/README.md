## 🧩 **Problem Name:**

**Lucky Number - 2**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads a **two-digit number** `N`
✅ Checks if **any** of these conditions is true:

* `N` is divisible by 9
* **Any digit** of `N` is 9
  ✅ If so, print `"Lucky Number"`
  ✅ Otherwise, print `"Unlucky Number"`

---

## 🧠 **Concepts Used:**

* Input and output
* Modulus operator `%`
* Indexing strings
* Type casting
* Logical operator `or`

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the input

```python
N = input()
```

---

### ✅ Step 2: Convert to integer and extract digits

```python
number = int(N)
digit1 = int(N[0])
digit2 = int(N[1])
```

---

### ✅ Step 3: Check the conditions

```python
if number % 9 == 0 or digit1 == 9 or digit2 == 9:
    print("Lucky Number")
else:
    print("Unlucky Number")
```

---

## 🧪 Sample Input:

```
18
```

### 🧾 Sample Output:

```
Lucky Number
```

---

## ✅ Full Code:

```python
# Read a two-digit number as string
N = input()

# Convert the number to integer
number = int(N)

# Extract first and second digits
digit1 = int(N[0])
digit2 = int(N[1])

# Check if N is divisible by 9 or one of the digits is 9
if number % 9 == 0 or digit1 == 9 or digit2 == 9:
    print("Lucky Number")
else:
    print("Unlucky Number")
```

---

