🧩 **Problem Name:**  
Sum of Numbers from M to N (For Loop)

❓ **Goal:**  
✅ Read two integers, `M` and `N`  
✅ Print the sum of all numbers from `M` to `N` (including both `M` and `N`)  
✅ Use only basic concepts: `input()`, `int()`, `for` loop, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- Addition using a variable
- `print()`

✅ **Code with Explanation:**

```python
# Read the starting number M
M = int(input())

# Read the ending number N
N = int(input())

# Initialize a variable to store the sum
total = 0

# Add all numbers from M to N (inclusive) to total
for i in range(M, N + 1):
    total = total + i

# Print the final sum
print(total)
```

### Explanation:

- `M = int(input())`: Reads the first integer from the user as the start of the range.
- `N = int(input())`: Reads the second integer as the end of the range.
- `total = 0`: Initializes a variable to store the running sum.
- `for i in range(M, N + 1)`: Loops from `M` to `N` (including `N`), adding each number to `total`.
- After the loop, `print(total)` outputs the computed sum.

🧪 **Sample Input:**

```
2
6
```

🧾 **Sample Output:**

```
20
```

🧪 **Sample Input:**

```
10
20
```

🧾 **Sample Output:**

```
165
```
