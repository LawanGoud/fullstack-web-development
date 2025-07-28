🧩 **Problem Name:**  
Solid Rectangle (For Loop)

❓ **Goal:**  
✅ Read two integers: M (number of rows) and N (number of columns)  
✅ Print a solid rectangle of M rows and N columns, with a single asterisk (`*`) followed by a space in each cell

🧠 **Concepts Used:**

- `input()`
- `int()`
- Nested `for` loops
- `print()` with optional `end` parameter

✅ **Code with Explanation:**

```python
# Read the number of rows (M)
M = int(input())
# Read the number of columns (N)
N = int(input())

# For each row
for i in range(M):
    for j in range(N):
        print("*", end=" ")
    print()  # Newline after each row
```

🧪 **Sample Input:**

```
2
3
```

🧾 **Sample Output:**

```
* * *
* * *
```
