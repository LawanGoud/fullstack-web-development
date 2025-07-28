🧩 **Problem Name:**  
Rectangle (For Loop)

❓ **Goal:**  
✅ Read two numbers, `M` (number of rows) and `N` (number of columns)  
✅ Print a rectangle of stars: `M` rows and `N` columns, each star followed by a space, one row per line  
✅ Use only basic concepts: `input()`, `int()`, `for` loop, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- String multiplication
- `print()`

✅ **Code with Explanation:**

```python
# Read the number of rows (M)
M = int(input())

# Read the number of columns (N)
N = int(input())

# For each row from 1 to M
for i in range(M):
    # Print a row with N stars, each followed by a space
    print("* " * N)
```

### Explanation:

- `M = int(input())`: Reads the total number of rows for the rectangle.
- `N = int(input())`: Reads the total number of columns for the rectangle.
- The `for` loop repeats `M` times, once for each row.
- In every iteration, `print("* " * N)` prints `N` stars (each with a space after), making up one row of the rectangle.

🧪 **Sample Input:**

```
4
5
```

🧾 **Sample Output:**

```
* * * * *
* * * * *
* * * * *
* * * * *
```
