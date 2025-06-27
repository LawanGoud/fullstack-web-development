## 🧩 **Problem Name**

**Part of a String - 2**

---

## 📌 **Task**

Write a program that:

- Reads a **word**
- Reads two integers **X** and **Y**
- Prints the part of the word **from index X up to index Y**

---

## 🧠 **Concept Explanation**

We use **string slicing** in Python to extract a substring using:

```python
word[X:Y]
```

- This returns all characters from index `X` to index `Y - 1`
- The **end index `Y` is not included**
- Indexing starts at `0`

---

### ✅ Example

```python
word = "Growing"
print(word[3:6])  # Outputs: "win"
```

But in your example, you expected `wing` as output.
So to **include the character at index Y**, we need to use:

```python
word[X:Y+1]
```

---

## ✅ Step-by-Step Code

### Step 1: Read the word

```python
word = input()
```

### Step 2: Read the two indices and convert to integers

```python
X = int(input())
Y = int(input())
```

### Step 3: Slice the word from X to Y (inclusive)

```python
part = word[X:Y+1]
```

### Step 4: Print the result

```python
print(part)
```

---

## ✅ Final Code

```python
word = input()
X = int(input())
Y = int(input())
print(word[X:Y+1])
```

---

## 🧪 Sample Input

```
Growing
3
6
```

## 🎯 Sample Output

```
wing
```
