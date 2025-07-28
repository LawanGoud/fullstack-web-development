🧩 **Problem Name:**  
Print from M to N (For Loop)

❓ **Goal:**  
✅ Read two integers, `M` and `N`  
✅ Print each integer from `M` to `N` (inclusive), one per line  
✅ Use only basic concepts: `input()`, `int()`, `for` loop, and `print()`

🧠 **Concepts Used:**

- `input()`
- `int()`
- `for` loop
- `print()`

✅ **Code with Explanation:**

```python
# Read the starting number M
M = int(input())

# Read the ending number N
N = int(input())

# Print each number from M to N, one per line
for i in range(M, N + 1):
    print(i)
```

### Explanation:

- `M = int(input())`: Reads the first number from the user (start value).
- `N = int(input())`: Reads the second number from the user (end value).
- `for i in range(M, N + 1)`: The loop variable `i` starts at `M` and continues up to `N` (inclusive).
- Inside the loop, `print(i)` prints each value on a new line.

🧪 **Sample Input:**

```
2
6
```

🧾 **Sample Output:**

```
2
3
4
5
6
```
