🧩 **Problem Name:**  
Sum of N Inputs (For Loop)

❓ **Goal:**  
✅ Read a number N  
✅ Then read N numbers (one per line)  
✅ Print the sum of the N numbers

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- Sum accumulation with a variable
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Initialize sum variable
total = 0

# For N times, read a number and add to total
for i in range(N):
    num = int(input())
    total = total + num

# Print the final sum
print(total)
```

🧪 **Sample Input:**

```
3
8
11
25
```

🧾 **Sample Output:**

```
44
```
