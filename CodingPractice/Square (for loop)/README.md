🧩 **Problem Name:**  
Square (For Loop)

❓ **Goal:**  
✅ Read a number `N`  
✅ Print a square of size `N` using stars (`*`), where each row and column has `N` stars  
✅ Each star should be followed by a space  
✅ Use only basic concepts: `input()`, `int()`, `for` loop, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- String multiplication
- `print()`

✅ **Code with Explanation:**

```python
# Read the size of the square (N)
N = int(input())

# For each row from 1 to N
for i in range(N):
    # Print a row with N stars, each followed by a space
    print("* " * N)
```

### Explanation:

- `N = int(input())`: Reads the size of the square from the user.
- The `for` loop runs `N` times (once for each row).
- In each iteration, `print("* " * N)` prints `N` stars, each followed by a space, forming one row of the square.

🧪 **Sample Input:**

```
4
```

🧾 **Sample Output:**

```
* * * *
* * * *
* * * *
* * * *
```
