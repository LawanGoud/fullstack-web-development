
## 🧩 **Problem Name:**

**Bonus Salary**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an employee's `salary` and `years of service`
✅ If `years of service` > 5, print `"Bonus: "` followed by 5% of the salary
✅ Otherwise, print `"No Bonus"`

---

## 🧠 **Concepts Used:**

* Input and type conversion
* Arithmetic operations (percentage calculation)
* Conditional statements (`if`, `else`)
* `print()` function

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read `salary` and `years_of_service`

```python
salary = int(input())
years = int(input())
```

---

### ✅ Step 2: Use condition to check if service is more than 5 years

---

## 🧪 Sample Input:

```
250000  
3
```

### 🧾 Sample Output:

```
No Bonus
```

---

## ✅ Full Code:

```python
# Read the salary
salary = int(input())

# Read the number of years of service
years = int(input())

# Check if the years of service is more than 5
if years > 5:
    # Calculate 5% bonus
    bonus = salary * 5 / 100
    # Print the bonus amount
    print("Bonus:", bonus)
else:
    # Print No Bonus if service is 5 years or less
    print("No Bonus")
```

---

