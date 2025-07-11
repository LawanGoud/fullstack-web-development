## 🧩 **Problem Name:**

**Rankers**

---

## 🎯 **Goal:**

* Read the rank `R` of a student
* Check the following:

  * If `R <= 3`:
    👉 Print `"One of Top 3"`
  * Else:
    👉 If `R <= 10`:
    👉 Print `"Not Top 3 but One of Top 10"`

---

## ✅ **Code with Nested If:**

```python
# Read the rank
R = int(input())

# Check if rank is in top 3
if R <= 3:
    print("One of Top 3")
else:
    # Nested check for top 10
    if R <= 10:
        print("Not Top 3 but One of Top 10")
```

---

## 🧪 **Sample Input:**

```
7
```

## 🧾 **Sample Output:**

```
Not Top 3 but One of Top 10
```

---

