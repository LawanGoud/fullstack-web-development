## 🧩 **Problem Name**

**Remainder**

---

## 📌 **Task**

Write a program that:

- Reads two numbers: the **dividend** and the **divisor**
- Calculates the **remainder** using the formula
- Prints the remainder

---

## 🧠 **Concept Explanation**

We are given:

- **Dividend** → the number to be divided (e.g., 7)
- **Divisor** → the number by which division is done (e.g., 2)

To calculate the **remainder**, we use the formula:

```
remainder = dividend - (divisor * quotient)
```

Where `quotient` is the **integer division** result of:

```
quotient = dividend // divisor
```

---

## ✅ **Step-by-Step Code Explanation**

---

### ✅ Step 1: Read Inputs

We'll read both numbers and convert them to integers.

```python
dividend = input()
dividend = int(dividend)

divisor = input()
divisor = int(divisor)
```

---

### ✅ Step 2: Calculate Quotient

```python
quotient = dividend // divisor
```

This uses integer division (`//`) to get the whole number part of the division.

---

### ✅ Step 3: Calculate Remainder

```python
remainder = dividend - (divisor * quotient)
```

---

### ✅ Step 4: Print the Result

```python
print(remainder)
```

---

## ✅ **Final Code**

```python
dividend = input()
dividend = int(dividend)

divisor = input()
divisor = int(divisor)

quotient = dividend // divisor
remainder = dividend - (divisor * quotient)

print(remainder)
```

---

## 🧪 **Sample Input**

```
7
2
```

## 🎯 **Sample Output**

```
1
```
