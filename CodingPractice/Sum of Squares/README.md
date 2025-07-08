## 🧩 **Problem Name:**

**Sum of Squares**

---

## 🎯 **Goal:**

✅ Read two numbers `A` and `B`
✅ Calculate `A² + B²` using the exponent operator
✅ If the sum is **greater than or equal to 60**, print `"Greater than or Equal to 60"`
✅ Otherwise, print `"Less than 60"`

---

## 🧠 **Concepts Used:**

* Input and type conversion (`int`)
* Exponentiation operator `**`
* Conditional statements (`if` / `else`)

---

## ✅ Full Code:

```python
# Read the first number
A = int(input())

# Read the second number
B = int(input())

# Calculate the sum of the squares
sum_of_squares = A**2 + B**2

# Check if the sum is greater than or equal to 60
if sum_of_squares >= 60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")
```

---

## 🧪 Sample Input:

```
10  
2
```

### 🧾 Sample Output:

```
Greater than or Equal to 60
```

---

