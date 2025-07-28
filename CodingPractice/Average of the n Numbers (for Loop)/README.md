🧩 **Problem Name:**  
Average of N Numbers (For Loop)

❓ **Goal:**  
✅ Read a number N  
✅ Print the average of numbers from 1 to N

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- Sum accumulation with a variable
- Division for average
- `print()`

✅ **Code with Explanation:**

```python
# Read the number N
N = int(input())

# Initialize sum variable
total = 0

# Add each number from 1 to N to total
for i in range(1, N + 1):
    total = total + i

# Calculate the average
average = total / N

# Print the resulting average
print(average)
```

🧪 **Sample Input:**

```
8
```

🧾 **Sample Output:**

```
4.5
```
