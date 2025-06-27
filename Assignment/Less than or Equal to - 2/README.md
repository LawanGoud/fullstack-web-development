## 🧩 Problem Name:

**Less than or Equal to - 2**

---

## 📝 Task:

Read two numbers `A` and `B`, and:

1. Check if `A <= B`
2. Check if `B <= A`
3. Print both results in the specified format

---

## 💡 Concepts Used:

- `input()` for user input
- `int()` for number conversion
- Relational operator `<=`
- `print()` for formatted output

---

## 🧠 Step-by-Step:

### Step 1: Read the two numbers

```python
A = int(input())
B = int(input())
```

### Step 2: Perform the comparisons

```python
a_le_b = A <= B
b_le_a = B <= A
```

### Step 3: Print the results in the given format

```python
print("A <= B is", a_le_b)
print("B <= A is", b_le_a)
```

---

## ✅ Complete Code:

```python
# Step 1: Read input
A = int(input())
B = int(input())

# Step 2: Perform comparisons
a_le_b = A <= B
b_le_a = B <= A

# Step 3: Print the results
print("A <= B is", a_le_b)
print("B <= A is", b_le_a)
```

---

## 🧪 Sample Input:

```
5
3
```

## 🎯 Output:

```
A <= B is False
B <= A is True
```
