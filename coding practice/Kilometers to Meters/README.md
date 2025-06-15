## 🧩 **Problem Name**

**Kilometers to Meters**

---

## 📌 **Task**

Write a program that:

- Takes a distance in kilometers as input
- Converts it to meters
- Prints the result

📌 **Note:**
1 Kilometer = 1000 Meters

---

## 🧠 **Step-by-Step Explanation**

---

### ✅ Step 1: Read the Input

We need to read the number of kilometers from the user using `input()` and convert it to `float`, since the distance can be a decimal number.

```python
km = input()
km = float(km)
```

📌 Example:

```
Input: 1.2
```

Now `km = 1.2`

---

### ✅ Step 2: Convert to Meters

Multiply the kilometers by `1000` to get meters.

```python
meters = km * 1000
```

So, `1.2 * 1000 = 1200`

---

### ✅ Step 3: Print the Result

Use `print()` to show the number of meters.

```python
print(int(meters))
```

We use `int()` here because the result should be a whole number (e.g., 1200), not a decimal like 1200.0.

---

## ✅ **Final Code**

```python
km = input()
km = float(km)

meters = km * 1000

print(int(meters))
```

---

## 🧪 **Sample Input**

```
1.2
```

## 🎯 **Sample Output**

```
1200
```
