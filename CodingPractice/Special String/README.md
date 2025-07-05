## 🧩 **Problem Name:**

**Special String**

---

## 🎯 **Goal:**

✅ Read a string `S`
✅ Check:

* First 3 letters of `S` = `"NXT"`
* Rest part is a number divisible by 2 or 7
  ✅ If both are true → print `"Special String"`
  ✅ Else → print `"Not a Special String"`

---

## 🧠 **Concepts Used:**

* String slicing (`[:3]` and `[3:]`)
* Type casting (`int()`)
* Modulus operator `%`
* Logical operators `and`, `or`

---

## ✅ Full Code:

```python
S = input()

# Check first 3 letters are 'NXT'
starts_with_nxt = S[:3] == "NXT"

# Convert the rest to number
number = int(S[3:])

# Check if number is divisible by 2 or 7
divisible = number % 2 == 0 or number % 7 == 0

# Final check using both conditions
if starts_with_nxt and divisible:
    print("Special String")
else:
    print("Not a Special String")
```

---

## 🧪 Sample Input:

```
NXT1234
```

### 🧾 Sample Output:

```
Special String
```

---

