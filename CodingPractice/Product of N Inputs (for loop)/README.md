🧩 **Problem Name:**  
Product of N Inputs (For Loop)

❓ **Goal:**  
✅ Read a number N  
✅ Then read N numbers (one per line)  
✅ Print the product of the N numbers

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- Multiplication accumulation with a variable
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Initialize product variable
product = 1

# Multiply each input number to the product
for i in range(N):
    num = int(input())
    product = product * num

# Print the final product
print(product)
```

🧪 **Sample Input:**

```
3
2
3
7
```

🧾 **Sample Output:**

```
42
```
