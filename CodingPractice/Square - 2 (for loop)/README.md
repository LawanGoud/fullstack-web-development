🧩 **Problem Name:**  
Square of Numbers (For Loop)

❓ **Goal:**  
✅ Read a number `M`  
✅ Print a square of size `M` using numbers, where each row contains the row number (starting from 1) repeated `M` times.  
✅ Each row and column should use numbers (not stars).  
✅ Use only `input()`, `int()`, `for` loop, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- String multiplication
- `print()`

✅ **Code with Explanation:**

```python
# Read the size of the square (M)
M = int(input())

# For each row from 1 to M
for i in range(1, M + 1):
    # Print the row number i, M times, as a string
    print(str(i) * M)
```

### Explanation:

- `M = int(input())`: Reads the size of the square from the user.
- The `for` loop runs from 1 to `M` (each for a new row).
- In each loop, `print(str(i) * M)` prints the row number `i`, repeated `M` times, making one line of the square.

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
1111
2222
3333
4444
```
