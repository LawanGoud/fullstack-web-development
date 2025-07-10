## 🧩 **Problem Name:**

**Armstrong Number - 2**

---

## 🎯 **Goal:**

✅ Read a **four-digit number** `N`
✅ Check if `N` is an **Armstrong Number**

An **Armstrong number** is a number in which the **sum of each digit raised to the power 4** is **equal to the number itself** (because it's a four-digit number).

✅ If it is, print: `"Armstrong Number"`
✅ Otherwise, print: `"Not an Armstrong Number"`

---

## 🧠 **Concepts Used:**

* Input and output
* Integer to string conversion
* Exponentiation (`**`)
* Conditional `if-else`

---

## ✅ Full Code:

```python
# Read the number
N = int(input())

# Convert number to string to access digits
num_str = str(N)

# Calculate sum of 4th powers of each digit
sum_of_powers = int(num_str[0])**4 + int(num_str[1])**4 + int(num_str[2])**4 + int(num_str[3])**4

# Check if it's an Armstrong number
if sum_of_powers == N:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
```

---

## 🧪 Sample Input:

```
1634
```

### 🧾 Sample Output:

```
Armstrong Number
```

---

