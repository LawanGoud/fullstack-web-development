## 🧩 **Problem Name:**

**Divisible by 10 or 5**

---

## 🎯 **Goal:**

Write a program that:

* ✅ Reads a number `N`
* ✅ Checks:

  * If `N` is divisible by `10` → Print `"Divisible by 10"`
  * Else if `N` is divisible by `5` → Print `"Divisible by 5"`
  * Else → Print `"Not Divisible by 10 or 5"`

---

## 🧠 **Concepts Used:**

* Input/output
* Integer division and remainder (`%`)
* Nested conditionals

---

## ✅ **Code:**

```python
N = int(input())

if N % 10 == 0:
    print("Divisible by 10")
else:
    if N % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not Divisible by 10 or 5")
```

---

## 🧪 **Sample Input:**

```
15
```

## 🧾 **Sample Output:**

```
Divisible by 5
```

---

