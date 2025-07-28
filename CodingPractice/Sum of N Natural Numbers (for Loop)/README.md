🧩 **Problem Name:**  
Sum of N Natural Numbers (For Loop)

❓ **Goal:**  
✅ Read a number N  
✅ Print the sum of natural numbers from 1 to N

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- `range()`
- Sum accumulation with a variable
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Initialize sum variable
total = 0

# Add each natural number from 1 to N
for i in range(1, N + 1):
    total = total + i

# Print the resulting sum
print(total)
```

🧪 **Sample Input:**

```
6
```

🧾 **Sample Output:**

```
21
```
