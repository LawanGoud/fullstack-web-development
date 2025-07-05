## 🧩 **Problem Name:**

**Lucky Number - 3**

---

## 🎯 **Goal:**

✅ Read a number `N`
✅ Check divisibility in this order of priority:

1. Divisible by 6 → highest priority
2. Divisible by 3
3. Divisible by 2
   ✅ Print `"Number is divisible by X"` where X is the luckiest number that divides it
   ✅ If not divisible by any, print:
   `Number is not divisible by 2, 3 or 6`

---

## 🧠 **Concepts Used:**

* Modulus operator `%`
* Logical operators
* Simple if-elif-else structure

---

## ✅ Full Code:

```python
N = int(input())

if N % 6 == 0:
    print("Number is divisible by 6")
elif N % 3 == 0:
    print("Number is divisible by 3")
elif N % 2 == 0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")
```

---

## 🧪 Sample Input:

```
126
```

### 🧾 Sample Output:

```
Number is divisible by 6
```

---

