## 🧩 **Problem Name:**

**Years, Weeks & Days**

---

## 🎯 **Goal:**

✅ Read number of days `N`
✅ Convert `N` days into:

* Years (`Y`) → `1 year = 365 days`
* Weeks (`W`) → `1 week = 7 days`
* Days (`D`) → Remaining days after converting to years and weeks

✅ Print years, weeks, and days **each on a new line**

---

## 🧠 **Concepts Used:**

* Integer division (`//`)
* Modulus (`%`)
* Input and output

---

## ✅ Full Code:

```python
# Read the number of days
N = int(input())

# Calculate years
years = N // 365

# Remaining days after years
remaining_days = N % 365

# Calculate weeks from remaining days
weeks = remaining_days // 7

# Remaining days after weeks
days = remaining_days % 7

# Print the result
print(years)
print(weeks)
print(days)
```

---

## 🧪 Sample Input:

```
1329
```

### 🧾 Sample Output:

```
3  
33  
3
```

---
