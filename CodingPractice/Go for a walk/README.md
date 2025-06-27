
## 🧩 **Problem Name:**

**Go for a walk**

---

## 🎯 **Goal:**

Write a program that:
✅ Reads an integer representing **temperature**
✅ Checks if the temperature is **between 15 and 40 (inclusive)**

* If yes → Print `"Can go for a walk"`
* Otherwise → Print `"Cannot go for a walk"`

---

## 🧠 **Concepts Used:**

* Conditional statements (`if-else`)
* Logical operators (`and`)
* Comparison operators (`>=`, `<=`)

---

## 🪜 **Step-by-Step Solution**

### ✅ Step 1: Read the temperature

```python
temperature = int(input())
```

---

### ✅ Step 2: Check if it is between 15 and 40

```python
if temperature >= 15 and temperature <= 40:
    print("Can go for a walk")
else:
    print("Cannot go for a walk")
```

---

## 🧪 Sample Input:

```
26
```

### 🧾 Sample Output:

```
Can go for a walk
```

---

## ✅ Full Code:

```python
# Read the temperature value
temperature = int(input())

# Check if temperature is between 15 and 40 (inclusive)
if temperature >= 15 and temperature <= 40:
    # If yes, print message for going out
    print("Can go for a walk")
else:
    # If not in the range, print message for not going out
    print("Cannot go for a walk")
```

---

