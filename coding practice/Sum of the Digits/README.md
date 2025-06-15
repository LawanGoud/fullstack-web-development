## 🧩 **Problem Name**

**Sum of the sum_of_digits**

---

## 📌 **Task**

Write a program that:

- Reads a **three-digit number** (as a string)
- Calculates the **sum of its digits** using string indexing
- Prints the result

---

## 🧠 **Concept Explanation**

When you read input using `input()`, it's a **string** by default.
You can access each digit using **indexing** like this:

```python
number = "326"
number[0] → '3'
number[1] → '2'
number[2] → '6'
```

But these are strings, so we must **convert each character to an integer** using `int()` before summing.

---

## ✅ **Step-by-Step Code Explanation**

### ✅ Step 1: Read the input

```python
number = input()  # number is a string like "326"
```

---

### ✅ Step 2: Access each character and convert to integer

```python
a = int(number[0])  # First digit
b = int(number[1])  # Second digit
c = int(number[2])  # Third digit
```

---

### ✅ Step 3: Add the digits

```python
sum_of_digits = a + b + c
```

---

### ✅ Step 4: Print the result

```python
print(sum_of_digits)
```

---

## ✅ Final Code

```python
number = input()

a = int(number[0])
b = int(number[1])
c = int(number[2])

sum_of_digits = a + b + c

print(sum_of_digits)
```

---

## 🧪 Sample Input

```
326
```

## 🎯 Sample Output

```
11
```

---

## 🧩 **Problem Name**

**Sum of the sum_of_digits**

---

## 📌 **Task**

Write a program that:

- Reads a **three-digit number**
- Calculates the **sum of its digits**
- Prints the result

---

## 🧠 **Concept Explanation**

For example, if the input is:

```
326
```

We want to calculate:

```
3 + 2 + 6 = 11
```

---

## ✅ **Step-by-Step Code Explanation**

---

### ✅ Step 1: Read Input

Read the number as input and convert it to an integer:

```python
number = input()
number = int(number)
```

---

### ✅ Step 2: Extract Digits

We can extract each digit using division and modulo operations:

```python
hundreds = number // 100         # Gets the hundreds digit
tens = (number // 10) % 10       # Gets the tens digit
ones = number % 10               # Gets the units digit
```

---

### ✅ Step 3: Add the Digits

```python
sum_of_digits = hundreds + tens + ones
```

---

### ✅ Step 4: Print the Result

```python
print(sum_of_digits)
```

---

## ✅ **Final Code**

```python
number = input()
number = int(number)

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

sum_of_digits = hundreds + tens + ones

print(sum_of_digits)
```

---

## 🧪 **Sample Input**

```
326
```

## 🎯 **Sample Output**

```
11
```
